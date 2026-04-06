# ⚽ European Top 5 Leagues — Historical Match Data & Championship Prediction (2015–2025)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Overview

This project conducts a complete **data analysis pipeline** — from dataset construction and cleaning to machine learning model training and probabilistic championship predictions — focusing on the **five major European football leagues** (the "Big 5"):

| League | Country | Code |
|---|---|---|
| **Premier League** | England   | `E0` |
| **La Liga** | Spain   | `SP1` |
| **Serie A** | Italy   | `I1` |
| **Bundesliga** | Germany  | `D1` |
| **Ligue 1** | France  | `F1` |

### 🎯 Objective

> *"Is it possible to estimate the probability that a team will win its championship based solely on its historical statistical performances?"*

Rather than deterministically predicting a winner, this project takes a **probabilistic approach** — estimating the probability of a title win by:

1. **Predicting total season points** using supervised regression on aggregated match-level statistics.
2. **Running Monte Carlo simulations** based on predicted points to estimate each team's probability of finishing first.

---

## 📁 Project Structure

```
European-Top-5-Leagues-2015-2025-Performances/
│
├── DATA FOR LEAGUES/                # Raw CSV files per league per season
│   ├── D1-2015-2016.csv            # Bundesliga 2015-16
│   ├── D1-2016-2017.csv
│   ├── ...
│   ├── E0-2015-2016.csv            # Premier League 2015-16
│   ├── ...
│   ├── F1-2015-2016.csv            # Ligue 1 2015-16
│   ├── ...
│   ├── I1-2015-2016.csv            # Serie A 2015-16
│   ├── ...
│   ├── SP1-2015-2016.csv           # La Liga 2015-16
│   └── ...                         # 50 CSV files total (5 leagues × 10 seasons)
│
├── FINAL DATASET/
│   ├── European Top 5 Leagues - Historical Match Data (2015-2025).csv
│   └── European Top 5 Leagues - Historical Match Data (2015-2025)-final.csv
│
├── SCRIPTS/
│   └── FUSIONNER TOUTES LES SAISONS.py   # Script to merge all season CSV files
│
├── Winners_prediction_report.ipynb        # Full analysis & ML notebook (Google Colab)
│
└── README.md                              # This file
```

---

## 📊 Dataset

### Source

Raw data originates from [**Football-Data.co.uk**](https://www.football-data.co.uk/), a well-known aggregator of historical football statistics. Since no single dataset covered all 5 leagues across 10 seasons, we downloaded:

- [England (Premier League)](https://www.football-data.co.uk/englandm.php)
- [Spain (La Liga)](https://www.football-data.co.uk/spainm.php)
- [Italy (Serie A)](https://www.football-data.co.uk/italym.php)
- [Germany (Bundesliga)](https://www.football-data.co.uk/germanym.php)
- [France (Ligue 1)](https://www.football-data.co.uk/francem.php)

...and **merged them** using the [merge script](SCRIPTS/FUSIONNER%20TOUTES%20LES%20SAISONS.py).

### Key Statistics

| Attribute | Value |
|---|---|
| **Rows (matches)** | 18,013 |
| **Columns (variables)** | 154 (raw) |
| **Seasons covered** | 2015–2016 through 2024–2025 |
| **Format** | CSV |

### Key Variables

| Variable | Type | Description |
|---|---|---|
| `Div` | Categorical | League division code |
| `Season` | Categorical | Season (e.g., `2015-2016`) |
| `Date` | Date | Match date |
| `HomeTeam` | Categorical | Home team name |
| `AwayTeam` | Categorical | Away team name |
| `FTHG` | Numeric | Full-Time Home Goals |
| `FTAG` | Numeric | Full-Time Away Goals |
| `FTR` | Categorical | Full-Time Result (`H`/`D`/`A`) |
| `HS` / `AS` | Numeric | Total shots (Home / Away) |
| `HST` / `AST` | Numeric | Shots on target (Home / Away) |
| `HC` / `AC` | Numeric | Corners (Home / Away) |
| `HY` / `AY` | Numeric | Yellow cards (Home / Away) |
| `HR` / `AR` | Numeric | Red cards (Home / Away) |

> **Note:** All bookmaker odds columns were **removed** during cleaning to avoid data leakage and maintain model independence.

---

## 🔬 Methodology

The full pipeline is implemented in the [Jupyter Notebook](Winners_prediction_report.ipynb) and follows these stages:

### 1. Data Collection & Merging
- Download individual CSV files for each league/season.
- Merge all files into a single unified dataset with an added `Season` column.

### 2. Exploratory Data Analysis (EDA)
- Inspect data dimensions, types, and distributions.
- Identify missing values (primarily in bookmaker odds columns).
- Detect and handle outliers and inconsistencies.
- Visualize key patterns through correlation matrices, distribution plots, and more.

### 3. Data Cleaning & Preprocessing
- Remove irrelevant columns (bookmaker odds, redundant identifiers).
- Handle missing values in core statistics.
- Convert date formats and encode categorical variables.

### 4. Feature Engineering & Aggregation
- Aggregate **match-level** data to **team-season** level.
- Construct the **target variable**: total points per team per season (`3` for a win, `1` for a draw, `0` for a loss).
- Build features including: goals for/against, goal difference, shots, shots on target, corners, yellow and red cards — all aggregated per team per season.

### 5. Supervised Regression Modeling
- Split data chronologically (80% train / 20% test) to avoid temporal leakage.
- Train a **Linear Regression** model to predict season points from aggregated statistics.
- Evaluate using R², MAE, and other regression metrics.

### 6. Monte Carlo Championship Probability Simulation
- Use the trained model to predict points for each team.
- Add noise (based on model residuals) to simulate randomness inherent in the sport.
- Run **10,000+ simulations** per division.
- Calculate the probability of each team finishing first in its respective league.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x**
- [Google Colab](https://colab.research.google.com/) (recommended) or a local Jupyter environment.

### Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Running the Analysis

1. **Clone the repository:**
   ```bash
   git clone https://github.com/medhajita/European-Top-5-Leagues-2015-2025-Performances.git
   cd European-Top-5-Leagues-2015-2025-Performances
   ```

2. **(Optional) Merge the raw data:**
   ```bash
   cd SCRIPTS
   python "FUSIONNER TOUTES LES SAISONS.py"
   ```
   > This re-generates the merged dataset in `FINAL DATASET/`.

3. **Open the notebook:**
   Open `Winners_prediction_report.ipynb` in **Google Colab** or **Jupyter Notebook** and execute the cells sequentially.

---

## 📈 Results Highlights

- The model achieves a **high R²** on test data, indicating strong explanatory power over team season points.
- Championship probability charts are generated for each of the 5 leagues.
- Dominant teams (e.g., Bayern Munich, Paris Saint-Germain, etc.) consistently show the highest predicted title probabilities, aligning with historical outcomes.

---

## ⚠️ Limitations

1. **Structural correlation**: The high R² is partly explained by the strong mathematical relationship between goal difference and points — the model captures the scoring structure of the leagues very well, but this does not guarantee perfect predictive power for unknown future seasons.

2. **Unmeasured variables**: The model relies solely on aggregated match statistics. Factors like injuries, coaching changes, squad market value, and fixture congestion are not accounted for.

3. **Explantory, not fully predictive**: The model predicts points from *completed* season statistics, making it an explanatory model rather than a pure "pre-season" predictor.

---

## 🔮 Future Improvements

- Add **rolling averages** / recent form features.
- Include **advanced efficiency ratios** (e.g., goals per shot on target).
- Integrate **external data** (transfer market values, coaching stability).
- Experiment with **non-linear models** (Random Forest, Gradient Boosting, XGBoost).
- Build real-time prediction capabilities for ongoing seasons.

---

## 👥 Team

- **Mohamed Hajita**
- **Abdelilah Rafik**

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Football-Data.co.uk](https://www.football-data.co.uk/) for providing the raw match data.
- [scikit-learn](https://scikit-learn.org/) for the machine learning toolkit.
- [Google Colab](https://colab.research.google.com/) for the free compute environment.