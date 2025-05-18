<h1 align="center">☀️ Solar Data Discovery — Week 1 Challenge</h1>

<p align="center">
  <strong>Benin 🇧🇯 • Sierra Leone 🇸🇱 • Togo 🇹🇬</strong><br/>
  📊 Exploratory Analysis • 🌐 Dashboard • 📈 Solar Metrics • ☁️ Climate Insight
</p>

<p align="center">
  <a href="https://solar-chalenge-week1.streamlit.app"><img src="https://img.shields.io/badge/Live-Dashboard-brightgreen?style=for-the-badge&logo=streamlit" alt="Streamlit App"></a>
  <a href="https://github.com/Hailemariyam/solar-challenge-week1"><img src="https://img.shields.io/github/repo-size/Hailemariyam/solar-challenge-week1?style=for-the-badge" alt="Repo Size"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Completed-blueviolet?style=for-the-badge" alt="Project Status"></a>
</p>

---

## 🌍 Project Overview

This project analyzes solar irradiance data from **Benin**, **Sierra Leone**, and **Togo**, aiming to support solar energy planning in West Africa. It includes:

- 🔬 Data Profiling & Cleaning
- 📊 Visual & Statistical Analysis
- 📈 Country Comparison
- 🌐 Interactive Streamlit Dashboard
- 🚀 Deployment on Streamlit Cloud



## 🗃️ Project Structure

📁 dashboard
├── app
│ ├── main.py ← Streamlit UI
│ └── utils.py ← Data loading & transformation
├── data
│ └── *.csv ← Cleaned datasets
📁 notebooks ← EDA notebooks
📁 scripts ← Cleaning and processing scripts
📁 tests ← Unit tests
📄 README.md ← This file
📄 requirements.txt ← Python dependencies


---

## 📊 Key Features

✅ **Interactive Dashboard:**
Choose a country to visualize GHI, DNI, DHI, and other metrics.

✅ **Top Regions Table:**
See the top regions/stations by average GHI.

✅ **Correlation Matrix:**
Analyze how temperature, humidity, and pressure relate to solar irradiance.

✅ **Statistical Summary:**
View mean, min, max, std for each key variable.

✅ **Fully Responsive UI:**
Built with Streamlit for mobile to desktop screens.

---

## 🚀 Live App

👉 [Click here to explore the interactive dashboard](https://solar-chalenge-week1.streamlit.app)

> 💡 No installation needed. Runs in your browser.

---

## 🔍 Sample Insights

| Metric      | Benin | Sierra Leone | Togo |
|-------------|-------|--------------|------|
| **GHI**     | ☀️ Highest | Medium       | Moderate |
| **DNI**     | High  | Low          | Medium |
| **Humidity**| Low   | 🌧️ Very High | Moderate |

- Benin is best suited for solar PV (high GHI).
- Sierra Leone's high humidity may reduce panel efficiency.
- Togo shows consistent DNI—potential for CSP.

---

## 📦 Requirements

Install dependencies in a virtual environment:

```bash
pip install -r requirements.txt


## 🛠️ Run Locally

Clone the repo and run the Streamlit app locally:

```bash
streamlit run dashboard/app/main.py
