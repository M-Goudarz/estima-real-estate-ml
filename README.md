# ESTIMA — Iranian Real Estate Price Prediction

### An End-to-End Machine Learning Project for Residential Property Valuation in Iran

**ESTIMA** is a machine learning project focused on estimating residential real estate prices in Iran using data-driven methods. The project aims to explore the relationship between property characteristics, location-related features, and market prices while developing a reproducible and maintainable machine learning pipeline.

Beyond building a predictive model, ESTIMA is designed as an engineering-oriented project that follows structured development practices and evolves toward a complete ML application.

---

## Overview

Real estate valuation is a complex problem influenced by multiple factors, including property size, location, building characteristics, and market conditions.

In markets with significant regional and economic variation, estimating property prices using traditional approaches can be challenging. Machine learning offers a practical way to identify patterns in historical housing data and develop predictive models that support data-driven property valuation.

ESTIMA investigates this problem using Iranian real estate data, with an initial focus on building a reliable foundation for data analysis, model development, evaluation, and deployment.

## Problem Statement

The objective of this project is to develop a machine learning system capable of estimating the price of a residential property based on its available characteristics.

Given a set of property features, the system will learn from historical housing data to predict the estimated market price of a property.

This is formulated as a **supervised regression problem**.

The project will also investigate model performance, feature importance, generalization, and the practical challenges of applying machine learning to real-world real estate data.

## Project Objectives

The primary objectives of ESTIMA are:

- Develop a structured machine learning pipeline for Iranian real estate price prediction.
- Perform exploratory data analysis to identify meaningful patterns and relationships.
- Implement robust data preprocessing and feature engineering strategies.
- Train and compare multiple regression algorithms.
- Evaluate models using appropriate regression metrics.
- Investigate the impact of property characteristics on predicted prices.
- Build a modular and maintainable Python codebase.
- Develop a deployment-ready prediction interface.
- Apply software engineering practices throughout the ML development lifecycle.

## Dataset

The project is intended to use real-world Iranian residential real estate data.

The dataset will provide information about properties and their corresponding prices. Depending on the selected data source, available features may include:

| Feature | Description |
|---|---|
| Property Area | Residential property size |
| Location | City, district, or neighborhood |
| Number of Rooms | Number of rooms in the property |
| Building Age | Age of the building |
| Property Price | Target variable for prediction |

The final dataset, its source, schema, and data limitations will be documented once the data selection and preparation process is finalized.

**Data integrity and reproducibility are important considerations.** Raw data will be kept separate from processed data, and data preparation steps will be documented as the project develops.

## Machine Learning Methodology

ESTIMA follows a structured machine learning workflow.

```text
Data Collection
      |
      v
Data Validation
      |
      v
Exploratory Data Analysis
      |
      v
Data Preprocessing
      |
      v
Feature Engineering
      |
      v
Train / Validation / Test Split
      |
      v
Model Training
      |
      v
Model Evaluation
      |
      v
Model Selection
      |
      v
Prediction Interface
```

The methodology will be refined as the dataset is explored and the project progresses.

### Model Development

The project will investigate a range of regression algorithms, starting with baseline models and progressing toward more advanced approaches.

Potential models include:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressors
- XGBoost / LightGBM, where appropriate

The final selection of models will depend on dataset characteristics, computational requirements, and empirical evaluation.

### Model Evaluation

Model performance will be evaluated using appropriate regression metrics, including:

| Metric | Purpose |
|---|---|
| MAE | Measures the average absolute prediction error |
| RMSE | Penalizes larger prediction errors more heavily |
| R² Score | Measures the proportion of target variance explained by the model |

Evaluation will be performed on held-out data to assess the model's ability to generalize to unseen properties.

No performance claims will be made until experiments have been conducted.

## Project Architecture

ESTIMA is being developed with a modular architecture to separate data processing, modeling, and application logic.

The intended architecture is:

```text
estima-real-estate-ml/
│
├── data/
│   ├── raw/              # Original datasets
│   └── processed/        # Cleaned and transformed datasets
│
├── notebooks/            # Exploratory analysis and experiments
│
├── src/
│   └── estima/           # Core machine learning package
│
├── tests/                # Automated tests
│
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

The repository structure will expand as additional components are implemented.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical computing |
| Pandas | Data manipulation and analysis |
| Matplotlib / Seaborn | Data visualization |
| Scikit-learn | Machine learning and preprocessing |
| XGBoost / LightGBM | Advanced gradient boosting, if selected |
| Jupyter Notebook | Exploratory analysis and experimentation |
| uv | Python package and environment management |
| Git & GitHub | Version control and project collaboration |
| FastAPI | Planned model serving interface |
| Docker | Planned application containerization |

The stack reflects the project's intended direction. Dependencies will be introduced as their corresponding components are implemented.

## Getting Started

### Prerequisites

- Python 3.13 or compatible version
- [uv](https://docs.astral.sh/uv/)
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/<YOUR-GITHUB-USERNAME>/estima-real-estate-ml.git
cd estima-real-estate-ml
```

Create and synchronize the project environment:

```bash
uv sync
```

Activate the virtual environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

The project is currently in its initial setup stage. Data preparation, model training, and prediction workflows will be added progressively.

## Engineering Principles

The project aims to follow these principles:

- **Reproducibility:** Keep track of dependencies and experimental configurations.
- **Modularity:** Separate responsibilities across data, modeling, and application components.
- **Maintainability:** Write clear, structured, and reusable code.
- **Data Quality:** Validate data and handle missing values, inconsistencies, and outliers carefully.
- **Evaluation Discipline:** Use appropriate validation strategies and avoid data leakage.
- **Version Control:** Track source code and configuration changes with Git.
- **Responsible Modeling:** Document assumptions, limitations, and potential sources of prediction error.

## Roadmap

ESTIMA is under active development.

- [x] Initialize repository and project structure
- [x] Configure Python project with `pyproject.toml`
- [x] Set up dependency management with uv
- [ ] Identify and finalize an Iranian real estate dataset
- [ ] Implement data validation and exploratory data analysis
- [ ] Develop data preprocessing and feature engineering pipelines
- [ ] Establish baseline regression models
- [ ] Train and compare advanced regression models
- [ ] Perform model evaluation and error analysis
- [ ] Analyze feature importance and model interpretability
- [ ] Build a reusable prediction pipeline
- [ ] Develop a FastAPI inference service
- [ ] Add automated tests
- [ ] Containerize the application with Docker
- [ ] Document model usage and deployment

## Current Status

**Stage: Initial Project Setup**

The repository structure and Python project configuration have been initialized.

The dataset selection, exploratory analysis, model development, and deployment components are planned but have not yet been implemented.

## Future Directions

Potential future extensions include:

- Location-aware property valuation
- Neighborhood-level price analysis
- Model interpretability using SHAP
- Experiment tracking
- Prediction uncertainty estimation
- API-based inference
- Containerized deployment
- Monitoring model performance and data drift

These extensions will be considered based on the quality and availability of the dataset and the results of initial experiments.

## License

The project's license will be defined as the repository matures.

---

**ESTIMA — Exploring data-driven residential property valuation in Iran.**