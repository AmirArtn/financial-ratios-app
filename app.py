import streamlit as st
import pandas as pd

st.title("Basic Financial Ratios Calculator")

# ————————————————————————————————————————————————
# 1) Gather inputs with Streamlit widgets instead of input()
# ————————————————————————————————————————————————
revenue          = st.number_input("Net revenue",            min_value=0.0, format="%.2f")
gross_profit     = st.number_input("Gross profit",           min_value=0.0, format="%.2f")
operating_profit = st.number_input("Operating profit",       min_value=0.0, format="%.2f")
pretax_income    = st.number_input("Pretax income",          min_value=0.0, format="%.2f")
net_income       = st.number_input("Net income",             min_value=0.0, format="%.2f")
R_D              = st.number_input("R&D expenditure",        min_value=0.0, format="%.2f")
cogs             = st.number_input("Cost of goods sold",     min_value=0.0, format="%.2f")

st.markdown("---")

current_assets    = st.number_input("Current assets",       min_value=0.0, format="%.2f")
total_assets      = st.number_input("Total assets",         min_value=0.0, format="%.2f")
current_liabilities  = st.number_input("Current liabilities",   min_value=0.0, format="%.2f")
total_liabilities    = st.number_input("Total liabilities",     min_value=0.0, format="%.2f")
shareholder_equity   = st.number_input("Shareholder equity",    min_value=0.0, format="%.2f")
interest_expense     = st.number_input("Interest expense",      min_value=0.0, format="%.2f")
earnings_per_share   = st.number_input("Earnings per share",    min_value=0.0, format="%.2f")
shares_outstanding   = st.number_input("Shares outstanding",    min_value=0.0, format="%.2f")

# ————————————————————————————————————————————————
# 2) Compute your ratios
# ————————————————————————————————————————————————
def pct(num, base): 
    return round(num / base * 100, 2) if base else None

ratios = {
    "Gross profit margin (%)":        pct(gross_profit, revenue),
    "Operating profit margin (%)":    pct(operating_profit, revenue),
    "Pretax margin (%)":              pct(pretax_income, revenue),
    "Net income margin (%)":          pct(net_income, revenue),
    "R&D margin (%)":                 pct(R_D, revenue),
    "COGS margin (%)":                pct(cogs, revenue),
    "Return on assets (%)":           pct(net_income, total_assets),
    "Return on equity (%)":           pct(net_income, shareholder_equity),
    "Mark‑up margin (%)":             pct(gross_profit, cogs),
    "Current ratio":                  round(current_assets / current_liabilities, 2) if current_liabilities else None,
    "Debt to equity ratio": round(total_liabilities / shareholder_equity, 3),

}




# 1) Turn it into a DataFrame with explicit “Ratio” and “Value” columns
df = pd.DataFrame(
    list(ratios.items()),         # turns dict into [(name, value), …]
    columns=["Ratio", "Value"]
)

# 2) (Optional) Add a “Category” column for high‑level classification
categories = {
    "Gross profit margin (%)":     "Profitability",
    "Operating profit margin (%)": "Profitability",
    "Pretax margin (%)":           "Profitability",
    "Net income margin (%)":       "Profitability",
    "R&D margin (%)":              "Profitability",
    "COGS margin (%)":             "Efficiency",
    "Return on assets (%)":        "Performance ",
    "Return on equity (%)":        "Performance",
    "Mark‑up margin (%)":          "Pricing",
    "Current ratio":               "Liquidity",
    "Debt to equity ratio":        "Solvency",
    # …add more mappings as you like…
}

df["Category"] = df["Ratio"].map(categories).fillna("Other")

# 3) Display it in Streamlit
st.subheader("Calculated Ratios")
st.dataframe(df)

st.title("Financial Ratios Calculator")

# 1) Show category explanations
with st.expander("📖 Ratio Categories Explained", expanded=True):
    st.markdown("""
    **Profitability**  
    Measures a company’s ability to generate earnings relative to its expenses and other costs.  
    - *Gross profit margin*: (Revenue – COGS) ÷ Revenue  
    - *Net income margin*: Net Income ÷ Revenue  

    **Liquidity**  
    Indicates whether the firm can meet its short‑term obligations.  
    - *Current ratio*: Current Assets ÷ Current Liabilities  

    **Solvency**  
    Reflects long‑term financial stability—ability to cover all debts over time.  
    - *Debt‑to‑equity ratio*: Total Liabilities ÷ Shareholders’ Equity  

    **Efficiency**  
    Shows how well a company uses its assets and controls its costs.  
    - *COGS margin*: COGS ÷ Revenue  
    - *Asset turnover*: Revenue ÷ Total Assets  

    **Valuation**  
    How the market prices the company relative to fundamentals.  
    - *P/E ratio*: Share Price ÷ Earnings per Share  
    - *EV/EBITDA*: Enterprise Value ÷ EBITDA  
    """)

# … your st.number_input() calls …
# … your ratio calculations …

# 2) Display the labeled table
df = pd.DataFrame(list(ratios.items()), columns=["Ratio","Value"])
df["Category"] = df["Ratio"].map(categories)
st.subheader("Your Calculated Ratios")
st.dataframe(df)

