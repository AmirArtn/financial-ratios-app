import streamlit as st
import pandas as pd

st.title("Basic Financial Ratios Calculator")

# ————————————————————————————————————————————————
# 1) Gather inputs with Streamlit widgets instead of input()
# ————————————————————————————————————————————————

st.header ("Income Statement")
revenue          = st.number_input("Net revenue",             format="%.2f")
gross_profit     = st.number_input("Gross profit",            format="%.2f")
operating_profit = st.number_input("Operating profit",        format="%.2f")
pretax_income    = st.number_input("Pretax income",           format="%.2f")
net_income       = st.number_input("Net income",              format="%.2f")
R_D              = st.number_input("R&D expenditure",         format="%.2f")
cogs             = st.number_input("Cost of goods sold",      format="%.2f")
interest_expense     = st.number_input("Interest expense",       format="%.2f")
earnings_per_share   = st.number_input("Earnings per share",     format="%.2f")

st.markdown("---")
st.header ("Balance Sheet")

current_assets    = st.number_input("Current assets",        format="%.2f")
receivable_begin    = st.number_input("Receivable begin",  format="%.2f")
receivable_end    = st.number_input("Receivable end",  format="%.2f")
total_assets      = st.number_input("Total assets",          format="%.2f")
current_liabilities  = st.number_input("Current liabilities",    format="%.2f")
total_liabilities    = st.number_input("Total liabilities",      format="%.2f")
shareholder_equity   = st.number_input("Shareholder equity",     format="%.2f")
shares_outstanding   = st.number_input("Shares outstanding",     format="%.2f")

st.markdown("---")
st.header ("Other Info")

inventory_begin   = st.number_input("Inventory begin",     format="%.2f")
inventory_end   = st.number_input("Inventory end",     format="%.2f")
market_price    = st.number_input("Market price",  format="%.2f")


# ————————————————————————————————————————————————
# 2) Compute your ratios
# ————————————————————————————————————————————————
def pct(num, base): 
    return round(num / base * 100, 2) if base else None

ratios = {
    "Net revenue margin (%)":         pct(revenue, revenue),
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
    "Debt to equity ratio":           round(total_liabilities / shareholder_equity, 3)  if shareholder_equity  else None,
    "Debt to assets ratio":           round(total_liabilities / total_assets, 3) if total_assets else None,
    "Interest coverage ratio":        round(operating_profit / interest_expense, 2) if interest_expense else None,
    "Asset turnover(%)":              pct(revenue, total_assets),
    "Inventory turnover(%)":          pct(((inventory_begin + inventory_end) / 2) , cogs),
    "Receivable turnover(%)":         pct(revenue , ((receivable_begin + receivable_end) / 2)),
    "Price to earning ratio":         round (market_price / earnings_per_share, 2) if earnings_per_share else None,
    "Revenue per share ratio":        round (revenue / shares_outstanding, 2) if shares_outstanding else None,
    "Price to book ratio":            round ((shareholder_equity / shares_outstanding) / market_price) if market_price else None,
    

}







# 1) Turn it into a DataFrame with explicit “Ratio” and “Value” columns
df = pd.DataFrame(
    list(ratios.items()),         # turns dict into [(name, value), …]
    columns=["Ratio", "Value"]
)

# 2) (Optional) Add a “Category” column for high‑level classification
categories = {
    "Net revenue margin (%)":      "Peformance",
    "Gross profit margin (%)":     "Peformance",
    "Operating profit margin (%)": "Performance",
    "Pretax margin (%)":           "Performance",
    "Net income margin (%)":       "Performance",
    "R&D margin (%)":              "Profitability",
    "COGS margin (%)":             "Efficiency",
    "Return on assets (%)":        "Performance ",
    "Return on equity (%)":        "Performance",
    "Mark‑up margin (%)":          "Pricing",
    "Current ratio":               "Liquidity",
    "Debt to equity ratio":        "Solvency",
    "Debt to assets ratio":        "Solvency",
    "Interest coverage ratio":     "Solvency", 
    "Asset turnover(%)":           "Efficiency",
    "Inventory turnover(%)":       "Efficiency",
    "Receivable turnover(%)":      "Efficiency",
    "Price to earning ratio":      "Valuation",
    "Revenue per share ratio":     "Valuation",
    "Price to book ratio":         "Valuation",
    # …add more mappings as you like…
}

df["Category"] = df["Ratio"].map(categories).fillna("Other")

# 3) Display it in Streamlit
st.subheader("Calculated Ratios")
st.dataframe(df)

st.title("Financial Ratios Info")

# 1) Show category explanations
with st.expander("📖 Ratio Categories Explained", expanded=False):
    st.markdown("""
    **Profitability (Higher Margins)**  
    Measures a company’s ability to generate earnings relative to its expenses and other costs.  
    - *Gross profit margin*: Gross proft / Revenue 
    - *Operating profit margin*: Operating profit / Revenue
    - *Pretax margin*: Pretax margin / Revenue            
    - *Net income margin*: Net Income ÷ Revenue
    - *Return on assets*: Net Income ÷ Total Assets
    - *Return on equity*: Net Income ÷ Shareholder Equity 
                
    **Pricing (Higher Margin)**  
    Measures a company's market power.
    - *Mark-up margin*: Gross Profit / Cost of Goods Sold

    **Liquidity (Moderate Ratio)**  
    Indicates whether the firm can meet its short‑term obligations.  
    - *Current ratio*: Current Assets ÷ Current Liabilities  

    **Solvency (Lower Ratio + High Coverage)**  
    Reflects long‑term financial stability—ability to cover all debts over time.  
    - *Debt‑to‑equity ratio*: Total Liabilities ÷ Shareholders’ Equity
    - *Debt-to-assets-ratio*: Total Liabilities / Total Assets
    - *Interest Coverage Ratio*: Operating Profit / Interest Expense

    **Efficiency (Higher Turnover Ratio)**  
    Shows how well a company uses its assets and controls its costs.  
    - *COGS margin*: COGS ÷ Revenue  
    - *Asset turnover*: Revenue ÷ Total Assets 
    - *Inventory turnover*: ((inventory begin + inventory end) / 2) / Cost of goods sold
    - *Receivable turnover*: Revenue / ((receivable begin + receivable end) / 2)         

    **Valuation (Lower Ratio = Undervalued ; Higher = Overvalued**  
    How the market prices the company relative to fundamentals.  
    - *Price to earning ratio (P/E)*: Market Price / Earning Per Share (Deluted)
    - *Revenue per share*: Net Revenue / Shares Outstanding
    - *Price to book ratio*: (shareholder_equity / shares_outstanding) / market_price
    
    
    """)

st.markdown("---")

st.subheader ("How to see competitive and durable company")
with st.expander("📖 competitive and durable Explained", expanded=False):
    st.markdown(""" Look for:
    - Long-term durable competitive advantage over competitors.
    - Consistently higher margin year to year = competitive advantage.
    - Avoiding fierce competition and a rat to the bottom. 
    - High research cost, high selling, administrative cost and high interest cost on debt that will bring a durable company down.
    - Lower company SGA expense (Selling, General & Admin) for durability ; SGA under 30%
    - Per-Share Earnings are increasing, but net earnings are decreasing - due to share buybacks.
    - Percentage of net earnings to total revenues, than their competitors.
    - High ratio of Revenue to Net Earnings.
    - Up trend Per-share earnings, as it tells us consistent earnings without an expensive process of change.
    - Avoid Wild per-share price swings because it is illusion of buying opportunity.
    - Firms that can allocate talent to their R&D more effectivily than competitive firms.
    - A history of profitable projects.

    """)

st.write("Gross Profit margin of 20%, and less = Fierce competitive industry with no market power")
st.write("Gross Profit Margin below or equal 40% = Competitive industry with market power")

# 1) Compute gross margin (or None if revenue==0)
gross_margin_pct = round((gross_profit / revenue) * 100, 2) if revenue else None

# 2) Boolean flags
is_low_margin  = gross_margin_pct is not None and gross_margin_pct <= 40
is_high_margin = gross_margin_pct is not None and gross_margin_pct >  40

# 3) Build your safe label
label = f"{gross_margin_pct:.2f}%" if gross_margin_pct is not None else "N/A"

# 4) Show it in a two-column layout
col1, col2 = st.columns([3,1])
col1.metric("Gross Profit Margin (%)", label)        # <-- only use 'label'
col2.checkbox("No Market Power (≤40%)",   value=is_low_margin,  disabled=True)
col2.checkbox("Market Power (>40%)", value=is_high_margin, disabled=True)
