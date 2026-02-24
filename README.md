# 🌍 Global Temperature Anomalies Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

*Analysing and forecasting global surface temperature anomalies from 1950 to 2030 using Python and machine learning.*

</div>

---

## 📖 Overview

This project analyses **global surface temperature anomalies** spanning from **1950 to 2024**, models the long-term warming trend using **linear regression**, and projects anomaly values through **2030**. The analysis demonstrates the power of simple yet effective statistical modelling applied to climate science, providing clear, data-driven insights into how much the Earth's average surface temperature has deviated from historical baselines.

> **Temperature Anomaly** — The difference between the observed temperature for a given period and a long-term average (baseline). A positive anomaly indicates warmer-than-average conditions.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **Data Simulation** | Generates realistic historical climate data (1950–2024) with a consistent warming trend and natural variability |
| 📈 **Linear Regression** | Trains a `scikit-learn` model to quantify the rate of warming per year |
| 🔮 **Future Forecasting** | Projects temperature anomalies from 2025 to 2030 |
| 🖼️ **Rich Visualisation** | Multi-layer plot with scatter data, moving averages, trend lines, and future predictions |
| 📉 **Moving Average** | 5-year rolling average to smooth short-term noise and reveal long-term trends |

---

## 🛠️ Technologies Used

- **[Python 3.8+](https://www.python.org/)** — Core programming language
- **[Pandas](https://pandas.pydata.org/)** — Data manipulation and analysis
- **[NumPy](https://numpy.org/)** — Numerical computing and array operations
- **[Matplotlib](https://matplotlib.org/)** — Base plotting library
- **[Seaborn](https://seaborn.pydata.org/)** — Statistical data visualisation
- **[Scikit-Learn](https://scikit-learn.org/)** — Machine learning (Linear Regression)

---

## 📁 Project Structure

```
Global-temperatures-Anaomolies/
├── climate analysis.py          # Main analysis and visualisation script
├── Global Temperature Anomalies # Jupyter Notebook version of the analysis
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.8+** installed. You can check with:

```bash
python --version
```

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/xainy75/Global-temperatures-Anaomolies.git
   cd Global-temperatures-Anaomolies
   ```

2. **Install the required dependencies:**

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

### Running the Analysis

```bash
python "climate analysis.py"
```

The script will:
1. Generate the simulated historical dataset
2. Train the linear regression model and print the trend summary
3. Output future temperature predictions (2025–2030)
4. Display a detailed visualisation chart

---

## 📊 Results

### Model Output

Upon running the script, you will see output similar to:

```
--- Model Summary ---
Trend: Temperatures are increasing by approximately 0.0200°C per year.

--- Future Predictions (Linear Trend) ---
   Year  Predicted_Anomaly_C
0  2025             1.248...
1  2026             1.268...
2  2027             1.288...
3  2028             1.308...
4  2029             1.328...
5  2030             1.348...

*** Predicted Temperature Anomaly for 2030: 1.35°C ***
```

### Visualisation

The generated chart contains four key layers:

- ⚫ **Gray dots** — Raw annual temperature anomaly data (1950–2024)
- 🔴 **Red line** — 5-year moving average, highlighting the underlying trend
- 🔵 **Blue dashed line** — Linear regression trend fitted to historical data
- ✖️ **Blue X markers** — Projected anomalies for 2025–2030
- 🟢 **Green dotted line** — Separator between historical data and future predictions

---

## 🌡️ Key Insight

The analysis reveals a **clear and statistically significant warming trend** from 1950 to the present day. The linear regression model estimates an increase of approximately **+0.02°C per year**, projecting a global temperature anomaly of roughly **+1.35°C by 2030** relative to the baseline period — consistent with broader scientific consensus on anthropogenic climate change.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ and 🐍 Python &nbsp;|&nbsp; Data-driven insights into our changing climate

</div>
