---
title: "Use Case & Architecture"
weight: 10
---

# Use Case & Architecture

This workshop demonstrates Airflow 3's capabilities through building a **personalized newsletter system** that showcases modern data orchestration patterns.

## Workshop Use Case

### Automated Newsletter Generation
Create an end-to-end pipeline that:
- Retrieves motivational quotes from external APIs
- Processes and selects the best content
- Generates personalized newsletters based on user preferences
- Includes weather information for user locations
- Applies human approval workflows before delivery

### Real-World Applications
This pattern applies to:
- **Content Management**: Automated content generation and curation
- **Marketing Automation**: Personalized campaign creation
- **Data Processing**: ETL pipelines with human oversight
- **AI/ML Workflows**: Model inference with approval gates

## System Architecture

![Architecture Diagram](/static/img/etl_genai_newsletter_architecture_diagram_bedrock.png)

### Core Components

#### 1. ETL Pipeline (Asset-Oriented)
- **Raw Data Extraction**: Fetch quotes from ZenQuotes API
- **Data Transformation**: Select and format optimal content
- **Template Generation**: Create newsletter templates

#### 2. Personalization Pipeline (Task-Oriented)
- **User Data Processing**: Load individual user preferences
- **Weather Integration**: Fetch location-based weather data
- **Content Assembly**: Generate personalized newsletters

#### 3. Advanced Features
- **Human-in-the-Loop**: Manual approval workflows
- **Event-Driven Processing**: SQS-triggered execution
- **GenAI Integration**: AI-powered content personalization

### Data Flow

1. **Scheduled Extraction**: Daily quote retrieval from external API
2. **Asset-Based Triggering**: Downstream processing triggered by data availability
3. **Personalization**: User-specific content generation
4. **Approval Workflow**: Human review before final delivery
5. **Event Processing**: Real-time response to user requests (optional)

## Airflow 3 Features Demonstrated

### Assets (Data-Aware Scheduling)
- Replace traditional dataset dependencies
- Automatic DAG generation for data assets
- Improved data lineage and dependency management

### Enhanced UI
- React-based interface with improved navigation
- Better visualization of workflows and dependencies
- Enhanced debugging and monitoring capabilities

### Human-in-the-Loop Operators
- Manual intervention points in automated workflows
- Approval/rejection workflows with rich content display
- Batch processing of approval requests

### Built-in Backfills
- UI-driven historical data processing
- Progress tracking and monitoring
- Flexible reprocessing options

### DAG Versioning
- Automatic tracking of structural changes
- Visual comparison between versions
- Code history and change management

### Event-Driven Scheduling
- SQS integration for real-time triggers
- Dynamic workflow execution based on external events
- Scalable processing of user requests

## Technology Stack

### Core Platform
- **Apache Airflow 3.0**: Latest workflow orchestration features
- **Astronomer Astro**: Managed Airflow platform
- **Python**: Primary development language

### External Integrations
- **ZenQuotes API**: Motivational quote source
- **Open-Meteo API**: Weather data provider
- **Amazon SQS**: Event-driven messaging (optional)
- **Amazon Bedrock**: GenAI capabilities (optional)

### Development Tools
- **Astro IDE**: Cloud-based development environment
- **Astro CLI**: Local development and deployment
- **Git**: Version control and collaboration

## Learning Progression

### Foundation (Exercises 1-2)
- UI exploration and navigation
- Asset creation and scheduling
- Basic pipeline construction

### Intermediate (Exercises 3-4)
- Human workflow integration
- Historical data processing
- Operational management

### Advanced (Exercises 5-6)
- Change tracking and versioning
- Event-driven architectures
- AI/ML integration patterns

This architecture provides a comprehensive foundation for understanding modern data orchestration while demonstrating practical, real-world applications of Airflow 3's enhanced capabilities.