---
title: "Prerequisites"
weight: 15
---

# Prerequisites

Before starting this workshop, please ensure you have the following prerequisites in place.

## Required Knowledge

### Technical Background
- **Basic Python programming**: Understanding of Python syntax, functions, and basic data structures
- **Command line familiarity**: Comfortable using terminal/command prompt for basic operations
- **Git basics**: Understanding of git clone, checkout, and basic version control concepts
- **Web browser navigation**: Ability to navigate web interfaces and multiple browser tabs

### Apache Airflow Concepts
- **DAGs (Directed Acyclic Graphs)**: Understanding of workflow concepts and task dependencies
- **Tasks and Operators**: Basic knowledge of how Airflow executes work
- **Scheduling**: Familiarity with cron expressions and time-based scheduling concepts

::alert[If you're new to Airflow, we recommend reviewing the [Airflow Fundamentals](https://www.astronomer.io/docs/learn/airflow-fundamentals) before starting this workshop.]{type="info"}

## Required Accounts and Access

### Astronomer Account
- **Free Astro Trial**: You'll create this during the workshop setup
- **No credit card required**: The trial provides everything needed for the workshop
- **Email access**: Ability to receive and verify email for account creation

### Development Environment
- **Modern web browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Stable internet connection**: Required for accessing cloud services and APIs
- **Local terminal access**: Command line interface for running CLI commands

## Optional Prerequisites (Exercise 6)

Exercise 6 is an advanced, optional exercise that requires additional AWS resources:

### AWS Account Requirements
- **Active AWS account** with billing enabled
- **IAM permissions** for the following services:
  - Amazon SQS (Simple Queue Service)
  - Amazon Bedrock (for GenAI capabilities)
  - Basic IAM role and policy management

### AWS Service Access
- **Amazon Bedrock model access**: May require requesting access to specific AI models
- **SQS queue creation**: Ability to create and manage SQS queues
- **AWS CLI or Console access**: For configuring services and monitoring

::alert[Exercise 6 is completely optional. You can complete the core workshop (Exercises 1-5) without any AWS account.]{type="warning"}

## Software Requirements

### Required Software
All required software will be installed during the workshop setup:

- **Astro CLI**: Will be installed following provided instructions
- **Git**: For cloning the workshop repository
- **Web browser**: For accessing Astro IDE and Airflow UI

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB available (8GB recommended)
- **Disk Space**: At least 2GB free space for the workshop files
- **Network**: Unrestricted internet access (no corporate firewall blocking)

## Pre-Workshop Checklist

Before the workshop begins, please verify:

### Account Preparation
- [ ] Email account accessible for Astronomer trial signup
- [ ] Web browser updated to latest version
- [ ] Stable internet connection confirmed

### Optional AWS Preparation (Exercise 6 only)
- [ ] AWS account credentials available
- [ ] Understanding of AWS billing (small costs may apply)
- [ ] Familiarity with AWS Console navigation

### Knowledge Verification
- [ ] Comfortable with basic Python syntax
- [ ] Can navigate command line/terminal
- [ ] Familiar with basic Airflow concepts (DAGs, tasks)
- [ ] Understanding of data pipeline concepts

## Workshop Environment

### What's Provided
- **Astro IDE**: Cloud-based development environment
- **Airflow 3 deployment**: Fully managed Airflow instance
- **Sample code**: Complete DAGs and supporting files
- **Documentation**: Step-by-step instructions and solutions

### What You'll Create
- **Personalized newsletter pipeline**: Complete ETL workflow
- **Asset-based scheduling**: Data-aware pipeline dependencies
- **Human approval workflows**: Manual intervention capabilities
- **Backfill operations**: Historical data processing
- **Version tracking**: DAG change management

## Getting Help

### During the Workshop
- **Workshop facilitators**: Available for questions and troubleshooting
- **Peer collaboration**: Work with other participants
- **Documentation**: Comprehensive step-by-step guides provided

### Resources
- **Astronomer Documentation**: [docs.astronomer.io](https://www.astronomer.io/docs/)
- **Apache Airflow Documentation**: [airflow.apache.org](https://airflow.apache.org/docs/)
- **Community Support**: [Astronomer Community](https://www.astronomer.io/community/)

## Troubleshooting Common Issues

### Browser Issues
- **Clear cache**: If experiencing loading issues
- **Disable extensions**: Some browser extensions may interfere
- **Try incognito mode**: To isolate extension-related problems

### Network Issues
- **Corporate firewalls**: May block access to cloud services
- **VPN connections**: Can sometimes cause connectivity issues
- **Mobile hotspots**: Consider as backup internet option

### Account Issues
- **Email verification**: Check spam folders for verification emails
- **Password requirements**: Ensure strong passwords for account creation
- **Multiple accounts**: Use consistent email across all services

::alert[If you encounter any issues during setup, workshop facilitators are available to help resolve them quickly.]{type="success"}

## Ready to Begin?

Once you've verified all prerequisites, you're ready to start the workshop! The next section will guide you through the complete environment setup process.

::alert[All prerequisites confirmed? Let's move on to the Setup section to begin building your Airflow 3 environment!]{type="success"}