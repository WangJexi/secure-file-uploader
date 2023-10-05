import boto3
import pymysql

def lambda_handler(event, context):
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    s3_client = boto3.client('s3')
    file_obj = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    file_content = file_obj['Body'].read().decode('utf-8')
    word_count = len(file_content.split())

    # Store the word count in RDS
    connection = pymysql.connect(host='your-rds-endpoint',
                                 user='your-username',
                                 password='your-password',
                                 database='your-database')
    with connection.cursor() as cursor:
        sql = "UPDATE files SET word_count=%s WHERE filename=%s"
        cursor.execute(sql, (word_count, s3_key))
    connection.commit()
    connection.close()

    return {
        'statusCode': 200,
        'body': f'Word count for {s3_key} is {word_count}'
    }
