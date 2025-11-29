# Global Superstore: Strategic Intelligence Dashboard

### *Optimizing profitability through Advanced SQL and Python ETL Pipelines.*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/sidhardhsmlai/p2-global-sales-dashboard)

---

## 📌 Business Problem
Global Superstore, a retail giant with over 50,000 transactions, faces a **-22% profit leakage** in specific sectors despite high revenue volume. This project builds an end-to-end Business Intelligence solution to diagnose the root causes of profitability issues.

**Key Questions Answered:**
1.  **The "Discount Trap":** Which products are being over-discounted, causing valid losses?
2.  **Logistics Leaks:** Which international markets suffer from unsustainable return rates?
3.  **Performance Drivers:** Who are the top-performing regional managers based on margin efficiency?

---

## 🔧 Technical Architecture (The Engineering)
This is not just a dashboard; it is a full-stack data application demonstrating a production-grade workflow.

### 1. Extract & Transform (Python/Pandas)
* **Robust Data Cleaning:** A modular pipeline (`src/data_processing.py`) handles:
    * **Type Casting:** Converting `Postal Code` from float to string.
    * **Imputation:** Handling missing values in location data.
    * **Feature Engineering:** Creating a `Market_Group` logic to standardize "Polluted" region data (US vs. Global).
    * **Date Standardization:** Converting diverse date formats to ISO 8601 (`YYYY-MM-DD`) for SQL compatibility.

### 2. Load (SQLite)
* **Data Persistence:** Cleaned data is loaded into a persistent **SQLite Database** (`superstore.db`) to enable complex querying and prevent data redundancy.

### 3. Analyze (Advanced SQL)
* **Time-Series Analysis:** Used **Window Functions** (`LAG()`) to calculate Year-Over-Year (YoY) growth rates.
* **Contribution Analysis:** Used **Partitioning** (`SUM() OVER (PARTITION BY...)`) to calculate product profit shares without sub-queries.
* **Multi-Table Logic:** Utilized complex **`LEFT JOIN`** logic to analyze Return Rates across disjointed tables.

### 4. Visualize (Streamlit)
* **Interactive Frontend:** Built a multi-tab dashboard with **caching (`@st.cache_data`)** for high performance.
* **Dynamic Charts:** Implemented **Plotly** for interactive drill-downs and tooltips.

---

## 📂 Project Structure
```text
p2-global-sales-dashboard/
├── data/                   # Raw and Processed Data (gitignored for security)
├── notebooks/              # EDA and Prototyping (01-EDA, 02-Cleaning)
├── reports/                # Executive PDF Report & Figures
├── sql_queries/            # Raw SQL Logic Files (The "Blueprints")
├── src/                    # Modular Python Scripts (The "Engine")
│   ├── data_processing.py  # Main ETL Orchestrator
│   └── db_utils.py         # Database Connection Tools
├── tests/                  # Pytest Suite (Data Integrity Checks)
├── dashboard.py            # Streamlit Frontend Application
└── requirements.txt        # Dependency Management