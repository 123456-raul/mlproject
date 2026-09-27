# End-to-End Machine Learning Project

A complete, production-style ML pipeline — from exploratory data analysis through model training to a deployed, containerized web application with CI/CD.

## 🎯 Overview
This project takes an ML model from notebook experimentation to a fully deployed service, covering the full lifecycle: EDA, data pipelines, model training with hyperparameter tuning, a served prediction UI, containerization, and automated deployment.

## ⚙️ Pipeline
1. **EDA** (`notebook/`) — exploratory analysis and problem definition
2. **Pipeline** (`src/`) — data ingestion, transformation, and training pipeline
3. **Model Training** — trained with CatBoost (see `catboost_info/`), hyperparameter-tuned
4. **Artifacts** (`artifacts/`) — saved model and preprocessing objects
5. **Serving** (`app.py`, `templates/`) — web UI for predictions
6. **Deployment** (`application.py`, `Dockerfile`, `.ebextensions/`, `.aws/`) — containerized and deployed via Docker to Azure Container Registry, with AWS Elastic Beanstalk deployment configuration
7. **CI/CD** (`.github/workflows/`) — automated build/deploy pipeline

## 🛠️ Tech Stack
- **Language:** Python
- **Modeling:** CatBoost
- **Serving:** Flask (`app.py`/`application.py` + `templates/`)
- **Containerization:** Docker
- **Deployment:** Azure Container Registry, AWS Elastic Beanstalk
- **CI/CD:** GitHub Actions

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Docker

### Installation
\`\`\`bash
git clone https://github.com/123456-raul/mlproject.git
cd mlproject
pip install -r requirements.txt
\`\`\`

### Run Locally
\`\`\`bash
python app.py
\`\`\`

### Docker
\`\`\`bash
docker build -t testdockerrahul.azurecr.io/mltest:latest .
docker login testdockerrahul.azurecr.io
docker push testdockerrahul.azurecr.io/mltest:latest
\`\`\`

## 📁 Project Structure
\`\`\`
mlproject/
├── notebook/            # EDA and problem statement
├── src/                 # training/inference pipeline
├── artifacts/           # trained model + preprocessing objects
├── catboost_info/       # CatBoost training logs
├── templates/           # web UI templates
├── app.py               # local Flask app
├── application.py       # deployment entry point
├── Dockerfile
├── .ebextensions/       # AWS Elastic Beanstalk config
├── .aws/                # AWS config
└── .github/workflows/   # CI/CD pipeline
\`\`\`

## 📌 Future Improvements
- Add model performance metrics to README (accuracy, RMSE, etc. depending on task)
- Add a short problem statement / dataset description at the top
- Add architecture diagram showing the CI/CD → Docker → deployment flow
