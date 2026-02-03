## COVID-19 Dashboard

An interactive COVID-19 data visualization and analysis dashboard built using Streamlit and Plotly, designed to explore and understand the global impact of COVID-19 through dynamic charts and automated insights.

The repository also includes an older Dash-based implementation for comparison and learning purposes.

## Project Overview

The COVID-19 Dashboard enables users to:

Analyze global and country-wise COVID-19 trends

Visualize cases, recoveries, and deaths interactively

Gain quick insights from real-world pandemic data

Compare modern Streamlit-based dashboards with a legacy Dash implementation

This project demonstrates skills in data analysis, visualization, and dashboard development.

## Features

Interactive visualization of COVID-19 statistics
(Confirmed Cases, Recoveries, Deaths)

Country-wise and region-wise filtering

Automated insights and summary statistics

Clean and responsive UI built with Streamlit

Legacy dashboard built using Dash (app_old.py) for comparison

Fast data handling using Pandas and NumPy

## Tech Stack

Category	Technologies
Frontend / UI	Streamlit, Dash
Data Analysis	Pandas, NumPy
Visualization	Plotly, Matplotlib
Environment	Python Virtual Environment
Version Control	Git, GitHub

## Project Structure
COVID19_Dashboard/
│
├── app.py              # Streamlit dashboard (main app)
├── app_old.py          # Dash-based legacy dashboard
├── data/               # COVID-19 dataset files
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation

## Setup Instructions

## 1️ Clone the Repository
git clone https://github.com/Sathyashri/COVID19_Dashboard.git
cd COVID19_Dashboard

## 2️ Create & Activate Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux

## 3️ Install Dependencies
pip install -r requirements.txt

## 4️ Run the Streamlit App
streamlit run app.py


The dashboard will open in your browser at:

http://localhost:8501

## Data Source

Publicly available COVID-19 datasets

Data is processed and visualized for analytical and educational purposes

## Future Enhancements

Add real-time data updates via APIs

Include vaccination and testing statistics

Deploy dashboard using Streamlit Cloud

Add trend forecasting using time-series models

Improve insights using automated analytics
