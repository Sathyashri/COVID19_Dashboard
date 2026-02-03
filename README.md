# COVID-19 Dashboard Project

A **data visualization and analysis dashboard** built using **Streamlit** and **Plotly**, designed to explore and understand the global impact of COVID-19 through interactive charts and insights.  
The project also includes an older Dash-based version for comparison and learning.

---

## Features

- 📈 Interactive COVID-19 statistics visualization (Cases, Recoveries, Deaths)
- 🌍 Filter and analyze data by country or region
- 💡 Generate automated data insights and summaries
- 🎨 Responsive and modern dashboard UI using Streamlit
- 📊 Comparison dashboard built using Dash (`app_old.py`)

---

## Tech Stack

| Category | Technologies |
|-----------|---------------|
| **Frontend / UI** | Streamlit, Dash |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Plotly, Matplotlib |
| **Environment** | Python Virtual Environment |
| **Version Control** | Git & GitHub |

---

## Setup Instructions

### 1️ Clone the Repository
```bash
git clone https://github.com/Sathyashri/COVID19_Dashboard.git
cd COVID19_Dashboard

### 2️ Create & Activate Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

### 3️ Install Dependencies
```bash
pip install -r requirements.txt

### 4️ Run the Streamlit App
streamlit run app.py


The dashboard will open in your browser at:

http://localhost:8501

##  Data Source

Publicly available COVID-19 datasets

Data is processed and visualized for analytical and educational purposes

##  Future Enhancements

Add real-time data updates via APIs

Include vaccination and testing statistics

Deploy dashboard using Streamlit Cloud

Add trend forecasting using time-series models

Improve insights using automated analytics
