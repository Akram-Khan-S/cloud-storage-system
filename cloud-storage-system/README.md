
# Cloud-Based Storage System

This project implements a secure, scalable, and HIPAA-compliant cloud-based file storage service using AWS.

## Architecture

The `architecture/` folder contains two designs:
- **Backend-Only Architecture**: API-driven for integrations.
- **Fullstack Architecture**: Includes a lightweight frontend for file upload/download.

## Components

- **Amazon S3**: Secure file storage
- **Amazon Cognito**: Authentication
- **API Gateway + Lambda**: Serverless backend
- **DynamoDB / Aurora**: Metadata storage
- **CloudWatch, CloudTrail, GuardDuty**: Monitoring & auditing

## How to Deploy

This repo uses AWS SAM (Serverless Application Model) for backend deployment.  
To deploy:

```bash
sam build
sam deploy --guided
```
