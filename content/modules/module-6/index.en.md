---
title: "Module 6: GenAI with Event-Driven Scheduling (Optional)"
weight: 60
---

# Module 6: GenAI with Event-Driven Scheduling (Optional)

This advanced module demonstrates a more realistic version of the newsletter pipeline using Amazon Bedrock for GenAI personalization and SQS for event-driven scheduling.

## Learning Objectives

- Implement event-driven scheduling with SQS
- Integrate GenAI capabilities using Amazon Bedrock
- Understand real-world pipeline patterns
- Configure AWS connections in Airflow

## Prerequisites

::alert[This exercise requires an AWS account with access to SQS and Amazon Bedrock]{type="warning"}

You'll need:
- AWS account with appropriate permissions
- Access to Amazon Bedrock (may require model access requests)
- SQS queue creation permissions

## Background

The previous exercises used a simplified pipeline that doesn't require external connections. This exercise shows a production-ready version that:

- **Personalizes content** using Large Language Models (LLMs)
- **Responds to events** rather than running on a schedule
- **Integrates with AWS services** for real-world functionality

This simulates an on-demand newsletter service where pipelines run as soon as users submit their preferences.

## Architecture

The enhanced pipeline includes:
- **SQS Integration**: Event-driven triggers from user requests
- **Bedrock Integration**: AI-powered content personalization
- **Real-time Processing**: Immediate response to user input

## Steps

### 1. Replace the DAG Code

1. Navigate to `dags/personalize_newsletter.py`
2. Replace the entire contents with the code from `solutions/personalize_newsletter_genai.py`

::alert[This will create a new DAG version that you can explore later!]{type="info"}

### 2. Configure Environment Variables

1. Copy the contents of `.env_example` to `.env`
2. Update the `AIRFLOW_CONN_AWS_DEFAULT` with your AWS credentials:

```bash
AIRFLOW_CONN_AWS_DEFAULT=aws://YOUR_ACCESS_KEY:YOUR_SECRET_KEY@/?region_name=us-east-1
```

::alert[IMPORTANT: Add the `.env` file to `.gitignore` to avoid pushing credentials to GitHub]{type="danger"}

### 3. Create SQS Queue

1. Log into your AWS Console
2. Navigate to **Amazon SQS**
3. Create a new queue (Standard queue is sufficient)
4. Copy the queue URL
5. Add the URL to your `.env` file:

```bash
SQS_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/123456789012/your-queue-name
```

### 4. Configure Bedrock Access

1. In AWS Console, navigate to **Amazon Bedrock**
2. Go to **Model access** in the left sidebar
3. Request access to a model (e.g., Claude or Titan models)
4. Wait for approval (this may take a few minutes)

### 5. Restart Airflow

Restart your Airflow environment to load the new environment variables:

```bash
astro dev restart
```

### 6. Test Event-Driven Scheduling

1. Navigate to your SQS queue in the AWS Console
2. Send a message with this JSON format:

```json
{
  "id": 300,
  "name": "Your Name",
  "location": "Your City",
  "motivation": "Your motivational theme",
  "favorite_sci_fi_character": "Your favorite character"
}
```

3. The `personalize_newsletter` DAG should automatically start running
4. Monitor the DAG execution in the Airflow UI

### 7. Review Results

1. Check the DAG execution logs
2. Review your personalized newsletter in the `include/newsletters` folder
3. Notice how the GenAI integration creates more sophisticated personalization

## Understanding Event-Driven Scheduling

### SQS Integration

The pipeline uses an **SQSSensor** to:
- **Poll SQS queue** for new messages
- **Trigger DAG execution** when messages arrive
- **Pass message content** to downstream tasks

### Benefits of Event-Driven Architecture

1. **Real-time response**: Immediate processing of user requests
2. **Resource efficiency**: Only runs when needed
3. **Scalability**: Handles varying load automatically
4. **Decoupling**: Separates event generation from processing

## GenAI Integration Details

### Bedrock Configuration

The pipeline uses Amazon Bedrock to:
- **Analyze user preferences** from the input message
- **Generate personalized content** based on motivational themes
- **Customize quotes** to match user interests

### Model Selection

You can modify the Bedrock model used by updating the DAG configuration. Popular options include:
- **Claude models**: Excellent for text generation and analysis
- **Titan models**: AWS-native models for various tasks
- **Jurassic models**: AI21 Labs models for text processing

## Advanced Features

### Message Processing

The enhanced pipeline:
1. **Parses SQS messages** to extract user preferences
2. **Validates input data** for required fields
3. **Enriches content** using external APIs (weather, quotes)
4. **Applies AI personalization** through Bedrock

### Error Handling

Production features include:
- **Message validation**: Ensures required fields are present
- **API retry logic**: Handles temporary service failures
- **Dead letter queues**: Manages failed message processing
- **Monitoring**: Tracks pipeline performance and errors

## Troubleshooting

### Common Issues

**Bedrock Access Denied**
- Ensure you've requested model access in the Bedrock console
- Verify your AWS credentials have Bedrock permissions

**SQS Connection Errors**
- Check your AWS credentials configuration
- Verify the SQS queue URL is correct
- Ensure your AWS account has SQS permissions

**Environment Variable Issues**
- Confirm `.env` file is properly formatted
- Restart Airflow after making changes
- Check that variables are loaded in the Airflow UI

### Performance Optimization

For production use:
- **Implement connection pooling** for AWS services
- **Use SQS batch processing** for high-volume scenarios
- **Configure appropriate timeouts** for external API calls
- **Set up monitoring and alerting** for pipeline health

## Key Concepts

After completing this exercise, you should understand:

- How to implement event-driven scheduling with SQS
- Integration patterns for GenAI services like Bedrock
- Real-world considerations for production pipelines
- The difference between scheduled and event-driven workflows

## Production Considerations

### Security
- **Credential management**: Use IAM roles instead of access keys
- **Network security**: Configure VPC endpoints for AWS services
- **Data encryption**: Ensure data is encrypted in transit and at rest

### Monitoring
- **CloudWatch integration**: Monitor AWS service usage
- **Airflow metrics**: Track DAG performance and failures
- **Cost monitoring**: Monitor AWS service costs

### Scalability
- **Auto-scaling**: Configure Airflow to scale with demand
- **Resource limits**: Set appropriate resource constraints
- **Queue management**: Implement proper SQS queue configuration

## Next Steps

This exercise demonstrates advanced Airflow 3 patterns that you can apply to real-world scenarios. Consider how these patterns might apply to your own use cases.

::alert[Advanced module complete! You've now experienced the full power of Airflow 3's new features.]{type="success"}