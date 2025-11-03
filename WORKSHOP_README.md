# Airflow 3 Workshop - Workshop Studio Format

This repository has been converted to follow AWS Workshop Studio's markdown-based format and best practices.

## Workshop Structure

The workshop is now organized according to Workshop Studio standards:

```
├── contentspec.yaml          # Workshop configuration and metadata
├── content/                  # Workshop content in markdown format
│   ├── index.en.md          # Workshop homepage
│   ├── about-astro/         # Astronomer platform overview
│   ├── use-case-architecture/ # Workshop use case and architecture
│   ├── prerequisites/       # Technical requirements and knowledge
│   ├── prepare-aws-environment/ # AWS setup with sub-sections
│   │   ├── at-aws-event/    # Event-hosted scenarios
│   │   ├── launch-workshop/ # Personal AWS account setup
│   │   └── prepare-sandbox/ # Sandbox environment preparation
│   ├── modules/             # Hands-on modules
│   │   ├── module-1/        # Explore the New UI
│   │   ├── module-2/        # Use Assets
│   │   ├── module-3/        # Add Human-in-the-Loop
│   │   ├── module-4/        # Run a Backfill
│   │   ├── module-5/        # Use DAG Versioning
│   │   └── module-6/        # GenAI with Event-Driven Scheduling (Optional)
│   └── summary/             # Workshop wrap-up and next steps
├── static/                  # Static assets (images, templates)
│   ├── img/                 # Workshop images
│   └── templates/           # CloudFormation and IAM policy files
├── dags/                    # Airflow DAG files (unchanged)
├── include/                 # Supporting files (unchanged)
├── solutions/               # Exercise solutions (unchanged)
└── [other original files]   # Original project files maintained
```

## Key Features

### Workshop Studio Compliance

- **Proper front matter**: All content files include required metadata
- **Structured navigation**: Hierarchical content organization with weights
- **Workshop Studio directives**: Uses alerts, expand sections, and other WS features
- **Static assets**: Images properly organized in `/static/img/` directory
- **Content specification**: `contentspec.yaml` defines workshop metadata

### Enhanced Content Organization

- **Progressive learning**: Modules build upon each other logically
- **Clear objectives**: Each section has defined learning outcomes
- **Best practices**: Follows Workshop Studio authoring guidelines
- **Troubleshooting**: Common issues and solutions included
- **Visual aids**: Proper image integration and formatting

### Maintained Functionality

- **Original code preserved**: All DAGs, solutions, and supporting files unchanged
- **Module compatibility**: All original modules work as intended
- **Asset structure**: Images and resources properly referenced
- **Development workflow**: Original development setup still functional

## Usage Instructions

### For Workshop Studio

1. Upload this repository to Workshop Studio
2. The `contentspec.yaml` will be automatically recognized
3. Content will be built from the `content/` directory
4. Static assets will be served from the `static/` directory

### For Local Development

The original development workflow remains unchanged:

1. Follow setup instructions in `content/prepare-aws-environment/prepare-sandbox/discover-airflow-3/index.en.md`
2. Use Astro CLI and IDE as originally designed
3. Work with DAGs in the `dags/` directory
4. Reference solutions in the `solutions/` directory

## Content Guidelines

### Front Matter Requirements

All content files include:
```yaml
---
title: "Page Title"
weight: 10
---
```

### Workshop Studio Directives

The workshop uses several WS-specific features:
- `::alert[]` for important notices
- `::expand[]` for collapsible sections
- `::children` for automatic navigation
- `::code[]` for code blocks with syntax highlighting

### Image References

Images use absolute paths from the static directory:
```markdown
![Description](/static/img/image-name.png)
```

## Migration Notes

### Changes Made

1. **Added Workshop Studio structure**: Created `content/` and `static/` directories
2. **Converted README to structured content**: Broke down into logical sections
3. **Added proper front matter**: All pages include required metadata
4. **Updated image paths**: Changed to Workshop Studio static directory format
5. **Enhanced formatting**: Used Workshop Studio directives for better presentation

### Preserved Elements

1. **All original files**: DAGs, solutions, includes, and configuration files
2. **Module content**: All module instructions and code examples
3. **Image assets**: All screenshots and diagrams
4. **Development workflow**: Astro CLI and IDE setup process

## Next Steps

1. **Test in Workshop Studio**: Upload and verify the workshop builds correctly
2. **Review content**: Ensure all sections render properly
3. **Validate exercises**: Confirm all hands-on activities work as expected
4. **Gather feedback**: Collect input from workshop participants and facilitators

This conversion maintains the full functionality of the original workshop while making it compatible with AWS Workshop Studio's platform and best practices.