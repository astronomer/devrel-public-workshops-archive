---
title: "Module 4: GenAI, Event-Driven Scheduling, and Some Sci-Fi"
weight: 40
---

# Module 4: GenAI, Event-Driven Scheduling, and Some Sci-Fi

This module demonstrates a more realistic version of the newsletter pipeline using Amazon Bedrock for GenAI personalization and SQS for event-driven scheduling.

We will also spice up the newsletter by using the user's favorite sci-fi character.

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

### 1. Replace the Dag Code

1. Navigate to `dags/personalize_newsletter.py`
2. Replace the entire contents with the code from `solutions/personalize_newsletter_genai.py`

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

Restart your Airflow test deployment to load the new environment variables

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

3. The `personalize_newsletter` Dag should automatically start running
4. Monitor the Dag execution in the Airflow UI

### 7. Review Results

1. Check the Dag execution logs
2. Review your personalized newsletter in the `include/newsletters` folder
3. Notice how the GenAI integration creates more sophisticated personalization

### 8. (Bonus) Adjust the Prompt

Notice how the prompt in the code uses the user's favorite sci‑fi character? Have some fun—adjust the prompt and see how unique a newsletter you can create.

## Key Concepts

After completing this exercise, you should understand:

- How to implement event-driven scheduling with SQS
- Integration patterns for GenAI services like Bedrock
- Real-world considerations for production pipelines
- The difference between scheduled and event-driven workflows

## Next Steps

This exercise demonstrates advanced Airflow 3 patterns that you can apply to real-world scenarios. Consider how these patterns might apply to your own use cases.

::alert[Module complete! You've now experienced the full power of Airflow 3's new features.]{type="success"}
