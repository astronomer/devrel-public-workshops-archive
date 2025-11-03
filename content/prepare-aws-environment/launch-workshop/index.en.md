---
title: "Launch Workshop in Your AWS Account"
weight: 20
---

# Launch Workshop in Your AWS Account

If you're running this workshop in your own AWS account, follow these instructions to set up the required services for Module 6.

## AWS Account Requirements

### Prerequisites
- **Active AWS account** with billing enabled
- **Administrative access** or permissions for:
  - Amazon SQS
  - Amazon Bedrock
  - IAM role and policy management
- **AWS CLI configured** (optional but recommended)

### Cost Considerations
- **SQS**: Minimal costs for message processing
- **Bedrock**: Pay-per-use for AI model inference
- **Estimated cost**: Less than $5 for workshop completion
- **Cleanup**: Remove resources after workshop to avoid ongoing charges

## Setup Instructions

### 1. Configure Amazon SQS

#### Create SQS Queue
1. Navigate to **Amazon SQS** in AWS Console
2. Click **Create queue**
3. Choose **Standard queue**
4. Name: `airflow-workshop-queue`
5. Use default settings
6. Click **Create queue**
7. **Copy the queue URL** for later use

#### Queue Configuration
```json
{
  "QueueName": "airflow-workshop-queue",
  "Attributes": {
    "VisibilityTimeoutSeconds": "300",
    "MessageRetentionPeriod": "1209600"
  }
}
```

### 2. Configure Amazon Bedrock

#### Request Model Access
1. Navigate to **Amazon Bedrock** in AWS Console
2. Go to **Model access** in left sidebar
3. Click **Request model access**
4. Select models (recommended):
   - **Claude 3 Haiku** (Anthropic)
   - **Titan Text G1 - Express** (Amazon)
5. Submit access request
6. **Wait for approval** (usually 5-10 minutes)

#### Verify Access
- Check **Model access** page shows "Access granted"
- Note the **model IDs** for configuration

### 3. Create IAM Policy

Create a policy with these permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:SendMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "arn:aws:sqs:*:*:airflow-workshop-queue"
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:ListFoundationModels"
            ],
            "Resource": "*"
        }
    ]
}
```

### 4. Create IAM User or Role

#### Option A: IAM User (Simpler)
1. Create new IAM user: `airflow-workshop-user`
2. Attach the policy created above
3. Create access keys
4. **Save credentials securely**

#### Option B: IAM Role (Recommended)
1. Create role for EC2/Lambda service
2. Attach the workshop policy
3. Configure role assumption as needed

## Environment Configuration

### AWS Credentials
Set up your credentials for Exercise 6:

```bash
# Method 1: Environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1

# Method 2: AWS CLI profile
aws configure --profile workshop
```

### Airflow Connection String
For your `.env` file in Module 6:

```bash
AIRFLOW_CONN_AWS_DEFAULT=aws://YOUR_ACCESS_KEY:YOUR_SECRET_KEY@/?region_name=us-east-1
SQS_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/YOUR_ACCOUNT_ID/airflow-workshop-queue
```

## Testing Your Setup

### Verify SQS Access
```bash
# Send test message
aws sqs send-message \
  --queue-url YOUR_QUEUE_URL \
  --message-body '{"test": "message"}'

# Receive message
aws sqs receive-message --queue-url YOUR_QUEUE_URL
```

### Verify Bedrock Access
```bash
# List available models
aws bedrock list-foundation-models --region us-east-1
```

## Troubleshooting

### Common Issues

**Permission Denied Errors**
- Verify IAM policy is correctly attached
- Check AWS credentials are properly configured
- Ensure you're using the correct region

**Bedrock Model Access**
- Confirm model access request was approved
- Try different models if one is unavailable
- Check regional availability of models

**SQS Queue Issues**
- Verify queue URL is correct
- Check queue exists in the right region
- Confirm queue permissions allow your user/role access

### Getting Help
- **AWS Documentation**: Comprehensive service guides
- **AWS Support**: For account-specific issues
- **Workshop facilitators**: For workshop-related problems

## Cleanup After Workshop

### Remove Resources
1. **Delete SQS queue**: Avoid ongoing charges
2. **Remove IAM user/role**: Clean up permissions
3. **Check Bedrock usage**: Monitor any charges
4. **CloudWatch logs**: Clean up if created

### Cost Monitoring
- Check **AWS Billing Dashboard** after workshop
- Set up **billing alerts** for future AWS usage
- Review **Cost Explorer** for detailed usage

::alert[Your AWS account is now ready for the advanced Module 6! Complete the core workshop first, then return here for GenAI integration.]{type="success"}