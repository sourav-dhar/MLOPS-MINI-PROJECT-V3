# MLOps Mini Project Setup Guide

A comprehensive guide for setting up a production-ready MLOps project with experiment tracking, version control, and cloud storage integration.

## Table of Contents

- [Project Initialization](#project-initialization)
- [Git Repository Setup](#git-repository-setup)
- [MLflow & DagHub Integration](#mlflow--dagshub-integration)
- [Experiment Tracking](#experiment-tracking)
- [DVC Setup with Local Remote](#dvc-setup-with-local-remote)
- [DVC Pipeline Configuration](#dvc-pipeline-configuration)
- [AWS S3 Integration](#aws-s3-integration)
- [Verification & Deployment](#verification--deployment)

---

## Project Initialization

### 1. Create Project Structure with Cookiecutter

Initialize the project using the Cookiecutter Data Science template:

```bash
cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
```

### 2. Project Cleanup

Remove unnecessary files and reorganize the models directory:

```bash
# Navigate to your project directory
cd <your-project-name>

# Reorganize models directory structure
# Move files from models/ to models/ as needed
```

### 3. Virtual Environment Setup

Create and activate a Python virtual environment:

```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# On Windows:
myenv\Scripts\activate

# On macOS/Linux:
source myenv/bin/activate
```

---

## Git Repository Setup

### 4. Initialize Git Repository

```bash
# Initialize git
git init

# Create initial commit
git add .
git commit -m "Initial project setup with cookiecutter"
```

### 5. Create Remote Repository

1. Create a new repository on GitHub
2. Add remote origin and push:

```bash
# Add remote
git remote add origin https://github.com/sourav-dhar/MLOPS-MINI-PROJECT-V3.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## MLflow & DagHub Integration

### 6. Setup DagHub for MLflow Tracking

Configure DagHub as your MLflow tracking server:

**DagHub MLflow Tracking URI:**
```
https://dagshub.com/dharsourav03/mlops-mini-project-v2.mlflow
```

### 7. Create DagHub Setup Script

Create `dagshub_setup.py`:

```python
import dagshub

dagshub.init(
    repo_owner='dharsourav03', 
    repo_name='mlops-mini-project-v2', 
    mlflow=True
)
```

### 8. Run DagHub Setup

```bash
python dagshub_setup.py
```

---

## Experiment Tracking

### 9. Experiment 1: Baseline Model

**Dataset URL:** 
```
https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv
```

Create and run your baseline experiment script with MLflow logging.

### 10. Update .gitignore

Add MLflow artifacts to `.gitignore`:

```bash
echo "mlruns/" >> .gitignore
```

### 11. Commit and Push Experiment 1

```bash
git add .
git commit -m "Add Experiment 1: Baseline model"
git push origin main
```

### 12. Experiment 2

Create and run your second experiment:

```bash
# Run experiment 2 script
python experiments/experiment_2.py

# Commit changes
git add .
git commit -m "Add Experiment 2: Model improvements"
git push origin main
```

### 13. Experiment 3

Create and run your third experiment:

```bash
# Run experiment 3 script
python experiments/experiment_3.py

# Commit changes
git add .
git commit -m "Add Experiment 3: Final model optimization"
git push origin main
```

---

## DVC Setup with Local Remote

### 14. Initialize DVC

```bash
dvc init
```

### 15. Add Local DVC Remote

Configure a local directory as DVC remote storage:

```bash
# Add local remote storage
dvc remote add -d myremote /path/to/local/storage

# Verify remote
dvc remote list
```

---

## DVC Pipeline Configuration

### 16. Create DVC Pipeline Files

Create `dvc.yaml` and `params.yaml` for your ML pipeline:

**Example `dvc.yaml`:**
```yaml
stages:
  data_preparation:
    cmd: python src/data_preparation.py
    deps:
      - src/data_preparation.py
      - data/raw
    params:
      - data_preparation
    outs:
      - data/processed

  train:
    cmd: python src/train.py
    deps:
      - src/train.py
      - data/processed
    params:
      - train
    outs:
      - models/model.pkl
```

**Example `params.yaml`:**
```yaml
data_preparation:
  test_size: 0.2
  random_state: 42

train:
  n_estimators: 100
  max_depth: 10
  learning_rate: 0.1
```

### 17. Run DVC Pipeline

```bash
# Reproduce pipeline
dvc repro

# Check status
dvc status
git status

# Commit DVC files
git add dvc.yaml dvc.lock params.yaml .gitignore
git commit -m "Add DVC pipeline configuration"

# Push data to DVC remote and code to Git
dvc push
git push origin main
```

### 18. Remove Local Remote

```bash
# List remotes
dvc remote list

# Remove local remote
dvc remote remove myremote
```

---

## AWS S3 Integration

### 19. Create S3 Bucket

1. Log in to AWS Console
2. Navigate to S3
3. Create a new bucket (e.g., `campusx-bucket`)
4. Configure appropriate permissions

### 20. Create IAM User

1. Navigate to IAM in AWS Console
2. Create a new user with programmatic access
3. Attach policy: `AmazonS3FullAccess`
4. Save Access Key ID and Secret Access Key

### 21. Install Required Packages

```bash
pip install dvc[s3] awscli
```

### 22. Configure AWS Credentials

```bash
aws configure
```

Enter your credentials when prompted:
- AWS Access Key ID
- AWS Secret Access Key
- Default region name (e.g., `us-east-1`)
- Default output format (e.g., `json`)

### 23. Add S3 Remote to DVC

```bash
# Add S3 remote
dvc remote add -d myremote s3://campusx-bucket

# Verify remote
dvc remote list
```

### 24. Run Pipeline with S3 Remote

```bash
# Reproduce pipeline
dvc repro

# Check status
dvc status
git status

# Commit changes
git add .
git commit -m "Configure S3 as DVC remote storage"

# Push to both DVC and Git
dvc push
git push origin main
```

---

## Verification & Deployment

### 25. Verify Integration

**Check MLflow Dashboard:**
```bash
# Navigate to DagHub repository
# View experiments and metrics in MLflow UI
```

**Check S3 Storage:**
1. Log in to AWS Console
2. Navigate to S3
3. Verify data and model artifacts in `campusx-bucket`

**Verify DVC Remote:**
```bash
dvc remote list
dvc status
```

---

## Project Structure

```
mlops-mini-project-v2/
├── data/
│   ├── raw/
│   ├── processed/
│   └── .gitkeep
├── models/
│   └── model.pkl
├── src/
│   ├── data_preparation.py
│   ├── train.py
│   └── evaluate.py
├── experiments/
│   ├── experiment_1.py
│   ├── experiment_2.py
│   └── experiment_3.py
├── dvc.yaml
├── params.yaml
├── dagshub_setup.py
├── requirements.txt
├── .gitignore
├── .dvc/
└── README.md
```

---

## Key Commands Reference

### Git Commands
```bash
git status                    # Check repository status
git add .                     # Stage all changes
git commit -m "message"       # Commit changes
git push origin main          # Push to remote
```

### DVC Commands
```bash
dvc init                      # Initialize DVC
dvc remote add -d name url    # Add remote storage
dvc remote list               # List remotes
dvc repro                     # Reproduce pipeline
dvc status                    # Check DVC status
dvc push                      # Push data to remote
dvc pull                      # Pull data from remote
```

### MLflow Commands
```bash
mlflow ui                     # Start MLflow UI locally
```

---

## Environment Variables

Create a `.env` file for sensitive credentials:

```bash
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
MLFLOW_TRACKING_URI=https://dagshub.com/dharsourav03/mlops-mini-project-v2.mlflow
DAGSHUB_TOKEN=your_dagshub_token
```

**Note:** Add `.env` to `.gitignore`

---

## Troubleshooting

### Common Issues

**DVC Push Fails:**
```bash
# Check remote configuration
dvc remote list

# Verify AWS credentials
aws s3 ls s3://campusx-bucket
```

**MLflow Tracking Not Working:**
```bash
# Verify DagHub connection
python dagshub_setup.py

# Check environment variables
echo $MLFLOW_TRACKING_URI
```

**Git Push Rejected:**
```bash
# Pull latest changes first
git pull origin main --rebase
git push origin main
```

---

## Best Practices

1. **Always commit DVC files with Git:**
   - `dvc.yaml`
   - `dvc.lock`
   - `.dvc` files

2. **Never commit large data files to Git:**
   - Use DVC for data versioning
   - Add data directories to `.gitignore`

3. **Keep experiments organized:**
   - Use clear naming conventions
   - Document hyperparameters in `params.yaml`
   - Log all metrics with MLflow

4. **Regular backups:**
   - Push to DVC remote frequently
   - Maintain multiple remotes for redundancy

5. **Security:**
   - Never commit AWS credentials
   - Use environment variables
   - Enable S3 bucket encryption

---

## Additional Resources

- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
- [DVC Documentation](https://dvc.org/doc)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DagHub Documentation](https://dagshub.com/docs)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)

---

## License

[Your License Here]

## Contributors

- Sourav Dhar (@dharsourav03)

---

**Last Updated:** December 2025
