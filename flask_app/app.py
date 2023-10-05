from flask import Flask, request, render_template
import boto3
import pymysql

app = Flask(__name__)

s3_client = boto3.client('s3', region_name='your-region')

@app.route('/')
def index():
    connection = pymysql.connect(host='your-rds-endpoint',
                                 user='your-username',
                                 password='your-password',
                                 database='your-database')

    with connection.cursor() as cursor:
        cursor.execute("SELECT filename, word_count FROM files")
        files = cursor.fetchall()

    connection.close()

    # Convert results into a list of dictionaries for easier template handling
    files_list = [{"name": file[0], "word_count": file[1]} for file in files]

    return render_template('index.html', files=files_list)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    s3_client.put_object(Bucket='your-s3-bucket', Key=file.filename, Body=file.read())
    # Saving metadata (without word count, which will be updated by the Lambda function) to RDS
    connection = pymysql.connect(host='your-rds-endpoint',
                                 user='your-username',
                                 password='your-password',
                                 database='your-database')
    with connection.cursor() as cursor:
        sql = "INSERT INTO files (filename, word_count) VALUES (%s, 0)"
        cursor.execute(sql, (file.filename,))
    connection.commit()
    connection.close()

    return "File uploaded successfully!"

if __name__ == '__main__':
    app.run()
