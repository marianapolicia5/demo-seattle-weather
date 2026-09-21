# Smart Energy Advisor

An end-to-end data science and machine learning project for household energy forecasting, solar production estimation, and electricity tariff simulation in Portugal.

The main component of the project is the Jupyter Notebook, which covers data preparation, exploratory data analysis, feature engineering, model training, evaluation, and export of the trained machine-learning artefacts. The resulting model is then integrated into an interactive Streamlit application.

This project was developed as a Final Degree Project for the Bachelor's Degree in Computer Science and Engineering at ISMAT.

## Overview

The Smart Energy Advisor combines a machine-learning pipeline with a web application for residential energy analysis.

The project is divided into two main components:

1. **Data science and machine learning pipeline** developed in Jupyter Notebook;
2. **Interactive Streamlit application** that uses the trained model to provide forecasts and energy simulations.

The notebook is the main development and analysis component of the project. The Streamlit application provides a practical interface for using the results of the trained model.

## Machine Learning Pipeline

The complete machine-learning workflow is available in [`notebooks/notebook.ipynb`](notebooks/notebook.ipynb).

The notebook includes:

* Data loading and preparation;
* Data cleaning and processing;
* Exploratory data analysis;
* Analysis of household energy-consumption patterns;
* Feature engineering;
* Preparation of data for machine learning;
* Training of an XGBoost regression model;
* Model evaluation;
* Export of the trained model and preprocessing artefacts.

The trained artefacts are later loaded by the Streamlit application for making predictions.

## Main Model Artefacts

The following files are used by the application:

* `smart_energy_model.pkl` — trained XGBoost model;
* `scaler.pkl` — scaler used during the model pipeline;
* `df_gc_clean.pkl` — prepared dataset used by the application and analysis components.

## Streamlit Application

The trained model is integrated into a Streamlit application that provides an interactive energy-management interface.

The application includes:

* Energy-consumption forecasting;
* A 24-hour forecast view;
* Solar-production estimation;
* Energy balance analysis;
* Electricity-cost simulation;
* Comparison of Portuguese electricity tariff cycles;
* Recommendations based on energy and weather information;
* User authentication;
* Saving and viewing simulation history;
* CSV export of saved simulation data;
* Pages for dataset exploration and model analysis.

## Technologies

* **Python**
* **Jupyter Notebook**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **XGBoost**
* **Joblib**
* **Streamlit**
* **Plotly**
* **Matplotlib**
* **Seaborn**
* **Requests**
* **Supabase**
* **OpenWeatherMap API**

## Repository Structure

```text
.
├── notebooks/
│   └── notebook.ipynb          # Data analysis, preprocessing and ML pipeline
│
├── pages/
│   ├── dashboard.py            # Dataset exploration dashboard
│   ├── history.py              # Saved simulation history
│   └── AI_model.py             # Model analysis and visualisation
│
├── streamlit_app.py            # Main Streamlit application
├── utils.py                    # Model loading, predictions and recommendations
├── tariffs.py                  # Electricity tariff calculations
├── weather.py                  # Weather API integration
├── supabase_http.py            # Supabase authentication and data persistence
├── config.py                   # Configuration and environment variables
├── auth.py                     # Authentication utilities
│
├── smart_energy_model.pkl      # Trained machine-learning model
├── scaler.pkl                  # Preprocessing scaler
├── df_gc_clean.pkl             # Prepared dataset
│
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Project configuration
├── uv.lock                     # Locked dependencies
├── .gitignore
├── LICENSE
└── README.md
```

## Dataset

The project uses household energy-consumption data based on the Ausgrid Solar Home Electricity Dataset.

The data is processed in the notebook before being used for exploratory analysis and model training.

The notebook documents the main data-processing and preparation steps used throughout the project.

## External Services

The application can use the following external services:

* **OpenWeatherMap API** for weather information;
* **Supabase** for authentication and persistence of simulation history.

Some application features require the corresponding API credentials to be configured.

## Requirements

* Python 3.11 or higher;
* An OpenWeatherMap API key;
* A Supabase project and credentials for authentication and persistent history features.

The application can still run without Supabase configuration, but authentication, history, and saved scenarios may not be available.

## Installation

### Using `pip`

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Using `uv`

```bash
uv venv
source .venv/bin/activate
uv sync
```

## Configuration

API credentials should not be committed to the repository.

They can be configured using environment variables or Streamlit secrets.

### Environment Variables

```bash
export OPENWEATHER_API_KEY="your_openweather_api_key"
export SUPABASE_URL="https://your-project.supabase.co"
export SUPABASE_KEY="your_supabase_key"
```

### Streamlit Secrets

Create a `.streamlit/secrets.toml` file:

```toml
OPENWEATHER_API_KEY = "your_openweather_api_key"
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your_supabase_key"
```

The `.streamlit/secrets.toml` file should not be uploaded to GitHub.

## Running the Notebook

To explore the data analysis and machine-learning pipeline, open the notebook:

```bash
jupyter notebook notebooks/notebook.ipynb
```

Alternatively, the notebook can be opened directly through GitHub.

The notebook contains the main data-science workflow, including data preparation, exploratory analysis, model training, evaluation, and artefact generation.

## Running the Streamlit Application

Start the application from the root directory of the repository:

```bash
streamlit run streamlit_app.py
```

After starting the application, open the local address displayed in the terminal. The default address is usually:

```text
http://localhost:8501
```

## Model Integration

The Streamlit application loads the artefacts generated by the machine-learning pipeline:

```text
smart_energy_model.pkl
scaler.pkl
df_gc_clean.pkl
```

These files must remain in the project root unless the paths in the Python code are updated accordingly.

The `pages/` directory must also remain next to `streamlit_app.py` so that Streamlit can automatically detect the application pages.

## Project Highlights

This project demonstrates experience with:

* Data cleaning and preparation;
* Exploratory data analysis;
* Feature engineering;
* Supervised machine learning;
* Regression models;
* Model evaluation;
* Saving and loading trained models;
* Interactive data applications;
* API integration;
* Authentication;
* Data persistence;
* Energy-consumption analysis;
* Portuguese electricity tariff simulation.

## Academic Context

* **Project:** Final Degree Project
* **Degree:** Bachelor's Degree in Computer Science and Engineering
* **Institution:** Instituto Superior Manuel Teixeira Gomes (ISMAT)
* **Author:** Mariana Polícia

## References

* Ausgrid Solar Home Electricity Dataset (https://www.ausgrid.com.pt);
* Reference sripts for data processing: [Pierre Haessig](https://github.com/pierre-haessig/ausgrid-solar-data).
* Inspiration for the Streamlit Interface: [Streamlit Seattle Weather Demo](https://github.com/streamlit/demo-seattle-weather).
* OpenWeatherMap API;
* Streamlit;
* XGBoost;
* Scikit-learn;
* Supabase.

## License

This project includes the license available in the [`LICENSE`](LICENSE) file.