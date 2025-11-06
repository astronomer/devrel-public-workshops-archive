---
title: "At an AWS Event"
weight: 10
---

# At an AWS Event

If you're participating in this workshop at an AWS-hosted event, follow these instructions to access your provided AWS environment.

## Event-Provided Resources

### What's Included
- **Temporary AWS account**: Pre-configured for the workshop
- **Required permissions**: SQS and Bedrock access already enabled
- **Event Engine access**: Managed through AWS Event Engine platform
- **Time-limited access**: Account expires after the event

### Access Instructions

#### 1. Receive Event Hash
Your workshop facilitator will provide:
- **Event hash code**: Unique identifier for your session
- **Access instructions**: Specific to your event setup
- **Team assignments**: If working in groups

#### 2. Access Event Engine
1. Navigate to the provided Event Engine URL
2. Enter your event hash code
3. Follow authentication prompts
4. Access your temporary AWS Console

#### 3. Verify Permissions
Confirm you have access to:
- **Amazon SQS**: For event-driven scheduling (Exercise 4)
- **Amazon Bedrock**: For GenAI capabilities (Exercise 4)
- **IAM roles**: Pre-configured for workshop requirements

## Event-Specific Setup

### Pre-Configured Resources
Your event environment may include:
- **SQS queues**: Already created and configured
- **Bedrock model access**: Pre-approved for workshop models
- **IAM policies**: Properly scoped permissions
- **CloudFormation stacks**: Supporting infrastructure

### Environment Variables
Use these event-specific values in Exercise 4:
```bash
AIRFLOW_CONN_AWS_DEFAULT=aws://EVENT_ACCESS_KEY:EVENT_SECRET_KEY@/?region_name=EVENT_REGION
SQS_QUEUE_URL=https://sqs.EVENT_REGION.amazonaws.com/EVENT_ACCOUNT/workshop-queue
```

## Post-Event Access

### Account Cleanup
- **Automatic termination**: Event accounts expire after the session
- **No manual cleanup**: Resources automatically removed
- **Data persistence**: Workshop results not saved beyond event

### Continuing Your Learning
- **Personal AWS account**: Set up your own for continued exploration
- **Astronomer trial**: Extend your Astro platform access
- **Community resources**: Join ongoing learning communities

::alert[Event participants have everything pre-configured! Focus on learning Airflow 3 features rather than AWS setup.]{type="success"}