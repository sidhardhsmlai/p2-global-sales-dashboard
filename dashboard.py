import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# --- 1. SETUP ---
st.set_page_config(page_title="Superstore Strategies", page_icon="🚀", layout="wide")

sys.path.append(os.path.abspath("src"))
import data_processing

# --- 2. DATA LOADING ---
@st.cache_data
def load_data():
    db_path = os.path.join("data", "superstore.db")
    return data_processing.get_data(db_path)

data = load_data()

# Helper to read SQL files for display
def get_sql_code(query_name):
    path = os.path.join("sql_queries", f"{query_name}.sql")
    with open(path, 'r') as f:
        return f.read()

# --- 3. UI LAYOUT ---
if data is not None:
    
    # SIDEBAR
    with st.sidebar:
        st.title("🛠️ Configuration")
        st.markdown("---")
        st.info("This dashboard is powered by a custom **Python + SQL ETL Pipeline**.")
        st.markdown("**Author:** Sidhardh Suresh")
        st.markdown("[View GitHub Repo](https://github.com/sidhardhsmlai/p2-global-sales-dashboard)")

    # MAIN TITLE
    st.title("🚀 Global Superstore: Strategic Dashboard")
    
    tab1, tab2, tab3 = st.tabs(["📈 Profitability & Growth", "🛑 Returns & Operations", "🔧 Technical Methodology"])

    # === TAB 1: EXECUTIVE OVERVIEW ===
    with tab1:
        st.markdown("### 📊 Key Performance Indicators (KPIs)")
        total_profit = data['growth']['TotalProfit'].sum()
        avg_return_rate = data['returns']['ReturnRate'].mean()
        
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric("Total Global Profit", f"${total_profit:,.0f}", "All Time")
        kpi2.metric("Avg Return Rate", f"{avg_return_rate:.2f}%", "- High Risk" if avg_return_rate > 5 else "Stable", delta_color="inverse")
        
        st.divider()
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📉 Profit Growth Trends")
            fig_growth = px.line(data['growth'].dropna(), x='OrderYear', y='YoY_Growth_Percent', color='Category', markers=True)
            fig_growth.add_hline(y=0, line_dash="dot", annotation_text="Break Even")
            st.plotly_chart(fig_growth, use_container_width=True)

        with col2:
            st.subheader("🏆 Profit Anchors (Contribution)")
            fig_contrib = px.bar(data['contribution'].sort_values('ContributionPercent', ascending=False), 
                                 x='ContributionPercent', y='SubCategory', color='Category', orientation='h')
            st.plotly_chart(fig_contrib, use_container_width=True)

    # === TAB 2: RETURNS & OPERATIONS ===
    with tab2:
        st.markdown("### 🚨 Operational Efficiency & Leaks")
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("🌍 Returns by Market")
            fig_returns = px.bar(data['returns'], x='Market', y='ReturnRate', color='ReturnRate', color_continuous_scale='Reds', text_auto='.1f')
            fig_returns.add_hline(y=5, line_dash="dash", line_color="green", annotation_text="Target (5%)")
            st.plotly_chart(fig_returns, use_container_width=True)
            st.caption("💡 **Insight:** Markets exceeding the 5% target require immediate audit.")

        with col4:
            st.subheader("👔 Manager Leaderboard")
            df_managers = data['managers'].sort_values('TotalSales', ascending=True)
            fig_managers = px.bar(df_managers, x='TotalSales', y='Manager', color='ProfitMargin_Percent', color_continuous_scale='Greens', orientation='h', text_auto='$,.0f')
            st.plotly_chart(fig_managers, use_container_width=True)
            st.caption("💡 **Insight:** Darker Green = Higher Profit Margin.")

    # === TAB 3: METHODOLOGY (The New Part) ===
    with tab3:
        st.markdown("## 🔧 Engineering Architecture")
        st.markdown("""
        This project demonstrates a full-stack data workflow, moving beyond simple CSV analysis to a production-grade ETL pipeline.
        
        **The Pipeline:**
        1.  **Extract:** Raw data loaded from Excel/CSV.
        2.  **Transform:** Cleaned in Python (Pandas) to handle missing values and correct data types.
        3.  **Load:** Stored in a persistent **SQLite Database**.
        4.  **Analysis:** Complex business questions answered via **Advanced SQL** (Window Functions, CTEs).
        """)
        
        st.divider()
        
        st.subheader("👨‍💻 SQL Code Explorer")
        st.markdown("Select a business question below to inspect the raw SQL query used to generate the data.")
        
        # Dropdown to select query
        query_option = st.selectbox(
            "Choose an Analysis Module:",
            ["Year-Over-Year Growth", "Profit Contribution", "Return Rate Analysis", "Manager Performance"]
        )
        
        # Map selection to filename
        query_map = {
            "Year-Over-Year Growth": "query_growth",
            "Profit Contribution": "query_contribution",
            "Return Rate Analysis": "query_returns",
            "Manager Performance": "query_managers"
        }
        
        # Display the code
        selected_file = query_map[query_option]
        st.code(get_sql_code(selected_file), language="sql")

else:
    st.error("❌ Critical Error: Database connection failed.")