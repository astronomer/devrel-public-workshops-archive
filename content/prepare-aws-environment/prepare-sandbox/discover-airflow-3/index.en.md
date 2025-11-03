---
title: "Discover Airflow 3"
weight: 10
---

# Discover Airflow 3

Set up your Astronomer Astro environment to explore Apache Airflow 3's revolutionary new features in a managed, cloud-based platform.

## Astro Platform Setup

### Understanding Astro Architecture
- **Organization**: Your dedicated Astro account space
- **Workspaces**: Team-based project organization (e.g., per department)
- **Deployments**: Individual Airflow environments within workspaces
- **Astro IDE**: Cloud-based development environment for DAG creation

### What You'll Create
- **Free Astro trial**: Full platform access for workshop duration
- **Test deployment**: Managed Airflow 3 environment
- **Development workspace**: Cloud-based IDE for DAG development
- **Complete pipeline**: End-to-end newsletter generation system

## Step-by-Step Setup

### 1. Create Astro Account
1. Use the **workshop-specific signup link** provided by your facilitator
2. Choose **"Start a Free Astro Trial"**
3. Select **"Personal"** when asked about usage
4. Choose meaningful **Organization** and **Workspace** names
5. When prompted for template, select **"None"**
6. Click **"Create Deployment in Astro"**

::alert[Keep the Astro platform tab open - you'll return to it during setup]{type="info"}

### 2. Install Astro CLI
Download and install the Astro CLI for your operating system:

#### macOS
```bash
brew install astro
```

#### Windows
```powershell
winget install -e --id Astronomer.Astro
```

#### Linux
```bash
curl -sSL install.astronomer.io | sudo bash -s
```

### 3. Repository Setup
1. **Fork the workshop repository**: [astronomer/devrel-public-workshops](https://github.com/astronomer/devrel-public-workshops/fork)
   
   ::alert[Uncheck "Copy the main branch only" when forking]{type="warning"}

2. **Clone your fork**:
   ```bash
   git clone <your-fork-url>
   cd devrel-public-workshops
   ```

3. **Switch to workshop branch**:
   ```bash
   git checkout airflow-3-ide
   ```

### 4. Authenticate to Astro
```bash
astro login
```
- This opens your browser for authentication
- Sign in with your Astro account credentials
- Return to terminal when authentication completes

### 5. Export to Astro IDE
```bash
astro ide project export
```
- Choose **"y"** to create a new project
- Provide a **project name** when prompted
- Your Astro IDE project opens automatically in browser

### 6. Start Airflow Environment
1. In the Astro IDE, click **"Start test deployment"**
2. Wait for deployment to initialize (2-3 minutes)
3. Your managed Airflow 3 environment will be ready

### 7. Configure Deployment Settings

#### Update Worker Configuration
1. Click dropdown next to **"Sync to test"**
2. Select **"Test Deployment Details"**
3. Navigate to **Details** → **Execution** → **Edit**
4. Set **"Min # Workers"** to **0**
5. Click **"Update Deployment"**

#### Remove Environment Variable
1. Go to **Environment** tab
2. Click **"Edit Deployment Variables"**
3. Delete the **"AIRFLOW__SCHEDULER__USE_JOB_SCHEDULE"** variable
4. Save changes

### 8. Access Airflow UI
1. Return to Astro IDE
2. In dropdown next to **"Sync to Test"**, click **"Open Airflow"**
3. Your Airflow 3 environment is now ready!

## Environment Verification

### Confirm Setup Success
- [ ] Astro IDE loads without errors
- [ ] Test deployment shows "Running" status
- [ ] Airflow UI opens and displays new React interface
- [ ] No DAGs are currently visible (expected)

### Troubleshooting Common Issues

**Astro CLI Installation**
- Verify installation: `astro version`
- Check PATH configuration if command not found
- Restart terminal after installation

**Authentication Problems**
- Clear browser cache and retry `astro login`
- Try incognito/private browsing mode
- Verify email verification was completed

**Deployment Issues**
- Wait full 5 minutes for deployment startup
- Check Astro platform status page
- Contact workshop facilitator if persistent issues

## What's Next?

Your Airflow 3 sandbox environment is now ready! You have:

✅ **Managed Airflow 3 platform** with latest features  
✅ **Cloud-based development environment** for DAG creation  
✅ **Zero infrastructure management** - focus on learning  
✅ **Production-grade platform** for realistic experience  

## Platform Features Available

### Airflow 3 Capabilities
- **New React UI**: Enhanced user experience and navigation
- **Assets**: Next-generation dataset and dependency management
- **HITL Operators**: Human-in-the-loop workflow capabilities
- **Enhanced Backfills**: Built-in historical data processing
- **DAG Versioning**: Automatic change tracking and comparison

### Astro Platform Benefits
- **Auto-scaling**: Workers scale based on demand
- **Monitoring**: Built-in observability and alerting
- **Security**: Enterprise-grade security and compliance
- **CI/CD Integration**: Seamless deployment workflows

::alert[Environment ready! Proceed to the modules to start exploring Airflow 3's powerful new features.]{type="success"}