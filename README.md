# Secure File Uploader and Analyzer

A secure application to upload files to AWS S3 and analyze them.

## Getting Started

### Prerequisites

- AWS CLI configured with necessary permissions.
- Python 3.x
- Virtualenv

### Setting up Flask Application

1. Navigate to `flask_app` directory.
2. Set up virtual environment:
    python3 -m venv venv
    source venv/bin/activate
3. Install dependencies:
    pip install -r requirements.txt
4. Run the application:
    export FLASK_APP=app.py
    flask run


### Setting up the Lambda Function

1. Navigate to `lambda_function` directory.
2. Deploy `lambda_function.py` to AWS Lambda.
3. Ensure the function is triggered by your desired S3 bucket.

## Deployment

Instructions for deploying to AWS EC2 and Elastic Beanstalk...

## Security

Details on setting up security groups, NACLs, and other security configurations...


