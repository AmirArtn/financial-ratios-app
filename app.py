import streamlit as st
import pandas as pd

st.title("Basic Financial Ratios Calculator")
st.write("Warning: Save page as PDF or else you will lose your data when you exit the website.")
# ————————————————————————————————————————————————
# 1) Gather inputs with Streamlit widgets instead of input()
# ————————————————————————————————————————————————
st.text_input("Firm's name & tag:")
st.text_input("All amounts are expressed in:")

st.header ("Statements of Income")
revenue          = st.number_input("Net revenue",             format="%.2f")
cogs             = st.number_input("Cost of goods sold",      format="%.2f")
gross_profit     = st.number_input("Gross profit",            format="%.2f")
sga     = st.number_input("Selling,General & Admin",            format="%.2f")
R_D              = st.number_input("R&D expenditure",         format="%.2f")
operating_profit = st.number_input("Operating profit",        format="%.2f")
interest_expense     = st.number_input("Interest expense",       format="%.2f")
pretax_income    = st.number_input("Pretax income",           format="%.2f")
net_income       = st.number_input("Net income",              format="%.2f")
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


st.markdown("---")
st.header ("Statements of Cashflow")
st.write("Don't use negative sign, it will mess up the calulation")
net_cash_operating  = st.number_input("Net cash from operating activities",     format="%.2f")
depreciation  = st.number_input("Depreciation of property & equipment",     format="%.2f")
capital_expenditure  = st.number_input("Purchases of property and equipment",     format="%.2f")
sale_asset  = st.number_input("Sales of property and equipment",     format="%.2f")
acquisitions  = st.number_input("Acquisitions, net of cash acquired, and purchases of intangible assets",     format="%.2f")
debt_raised = st.number_input("Debt raised through financing",     format="%.2f")
debt_repaid = st.number_input("Debt repaid through financing",     format="%.2f")


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

st.subheader("Financial Ratios Info")

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

st.subheader ("Peformance & Competitive Edge Analysis")
with st.expander("📖 Competitive Edge Explained", expanded=False):
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

st.subheader("Rate of Revenue to Net Earnings")
st.write("Historical net earning of 20% or more on total revenue = Long-term competitive advantage")
income_margin_pct = round((net_income / revenue) * 100, 2) if revenue else None
is_low_income  = income_margin_pct  is not None and income_margin_pct  < 19
is_high_income = income_margin_pct  is not None and income_margin_pct  >=  20

label0 = f"{income_margin_pct:.2f}%" if income_margin_pct is not None else "N/A"

col1, col2 = st.columns([3,1])
col1.metric("Net Income Margin (%)", label0)        # <-- only use 'label'
col2.checkbox("No long-term competitive edge (<20%)",   value=is_low_income,  disabled=True)
col2.checkbox("Long-term competitive edge  (>=20%)", value=is_high_income, disabled=True)




st.subheader("Gross Margin")
st.write("Gross Profit margin of 20%, and less = Fierce competitive industry with no market power")
st.write("Gross Profit Margin below or equal 40% = Competitive industry with market power")

# 1) Compute gross margin (or None if revenue==0)
gross_margin_pct = round((gross_profit / revenue) * 100, 2) if revenue else None

# 2) Boolean flags
is_low_margin  = gross_margin_pct is not None and gross_margin_pct < 29
is_high_margin = gross_margin_pct is not None and gross_margin_pct >=  30

# 3) Build your safe label
label = f"{gross_margin_pct:.2f}%" if gross_margin_pct is not None else "N/A"

# 4) Show it in a two-column layout
col1, col2 = st.columns([3,1])
col1.metric("Gross Profit Margin (%)", label)        # <-- only use 'label'
col2.checkbox("No Market Power (≤40%)",   value=is_low_margin,  disabled=True)
col2.checkbox("Market Power (>40%)", value=is_high_margin, disabled=True)

st.subheader("Selling,General & Admin Margin")
st.write("SGA under 30% of Gross Profit = Fantastic")
st.write("SGA above 30% of Gross Profit = Overpaying managers")
SGA_margin_pct = round((sga / gross_profit) * 100, 2) if gross_profit else None

is_low_sga  = SGA_margin_pct is not None and SGA_margin_pct <= 30
is_high_sga = SGA_margin_pct is not None and SGA_margin_pct >  30

label2 = f"{SGA_margin_pct:.2f}%" if SGA_margin_pct is not None else "N/A"

col1, col2 = st.columns([3,1])
col1.metric("Selling,General & Admin Margin (%) of Gross Profit", label2)        # <-- only use 'label'
col2.checkbox("Healthy (≤30%)",   value=is_low_sga,  disabled=True)
col2.checkbox("Unhealthy (>40%)", value=is_high_sga, disabled=True)

st.subheader("Depreciation Margin")
st.write("Depreciation under 10% = Competitive Company")

depreciation_margin_pct = round((depreciation / gross_profit) * 100, 2) if gross_profit else None
is_low_depreciation  = depreciation_margin_pct is not None and depreciation_margin_pct <= 10
is_high_depreciation = depreciation_margin_pct is not None and depreciation_margin_pct >  10
label3 = f"{depreciation_margin_pct:.2f}%" if depreciation_margin_pct is not None else "N/A"

col1, col2 = st.columns([3,1])
col1.metric("Depreciation margin (%) of Gross Profit", label3)        # <-- only use 'label'
col2.checkbox("Competitive edge (≤10%)",   value=is_low_depreciation,  disabled=True)
col2.checkbox("High depreciation cost (>40%)", value=is_high_depreciation, disabled=True)

st.subheader("Per-Share Earnings")
st.write("Shows consistency and upward trend = Competitive and durable ")

pershare_earnings = round((net_income / shares_outstanding), 2) if shares_outstanding else None

label4 = f"${pershare_earnings:.2f} per share" if pershare_earnings is not None else "N/A"

col1, col2 = st.columns([3,1])
col1.metric("Per-Share Earnings", label4) 

st.markdown("---")

st.subheader ("Valuation")
with st.expander("Undervalued or Overvalued", expanded=False):
    st.markdown(""" 
    -  A company with durable competitive advantage will use earning power to finance operation, therefore maintain high level of equity and low total liabilities.
    -  Companies without durability will show the opposite, use debt to finance operations, therefore have lower level of equity and high level of total liabilities.
    -  Durable Competitive companies have return on equity of 30% and more or there is a compound effect of return on equity as it adds up year after year.
    -  If a company shows negative equity and bad net income, it is a company heading to bankruptcy.
    -  Goodwill indicates the business is acquisitioning other business, which in turn can be profitable, but in most cases it will not be.
    -  If the company is failing and has no cash pile, that is a sinking ship no matter what management. 

    """)


st.subheader("Return on Equity Margin")
st.write("Durable Competitive companies have return on equity of 30% and more.")

equity_margin_pct = round((net_income / shareholder_equity) * 100, 2) if shareholder_equity else None

is_low_equity  = equity_margin_pct is not None and equity_margin_pct < 30
is_high_equity = equity_margin_pct is not None and equity_margin_pct >=  30

label5 = f"{equity_margin_pct:.2f}%" if equity_margin_pct is not None else "N/A"

col1, col2 = st.columns([3,1])
col1.metric("Return on Equity", label5)        # <-- only use 'label'
col2.checkbox("Nondurable (<30)",   value=is_low_equity,  disabled=True)
col2.checkbox("Durable (>=30%)", value=is_high_equity, disabled=True)

st.subheader("Basic Earning Power")
st.write("Ability to self-finance R&D and Acquiring Long-Term Assets  ")

earning_power = round((operating_profit/ total_assets), 2) if total_assets else None

is_low_earning = earning_power is not None and earning_power < 0.10
is_high_earning = earning_power is not None and earning_power >=  0.10

label6 = f"${earning_power:.2f} per dollar" if earning_power is not None else "N/A"

col1, col2 = st.columns([3,1])
col1.metric("Earning Power", label6)
col2.checkbox("No Earning Power (<$0.10)",   value=is_low_earning,  disabled=True)
col2.checkbox("Earning Power (>=$0.10)", value=is_high_earning, disabled=True)

st.subheader("Defensive Interval Ratio")
st.write("How long will the firm last with only current assets?")

# 1) Sum your annual operating expenses (SG&A + R&D)
annual_op_expense = sga + R_D   # make sure sga and R_D are annual figures

# 2) Guard against zero to avoid division-by-zero
if annual_op_expense:
    # 3) Compute daily expense
    exp_per_day = annual_op_expense / 365

    # 4) Runway in days
    runway_days = current_assets / exp_per_day

    # 5) Runway in years
    runway_years = runway_days / 365

    # 6) Format your labels
    label_days  = f"{runway_days:.0f} days"
    label_years = f"{runway_years:.2f} years"
else:
    runway_days = runway_years = None
    label_days = label_years = "N/A"

# 7) Display side by side
col1, col2 = st.columns(2)
col1.metric("Runway (days)",  label_days)
col2.metric("Runway (years)", label_years)

st.subheader("Free Cash Flow to Equity")
st.write("Amount of cash a company can pay out to its shareholders")

# 1) Compute your two numbers
#    (make sure net_cash_operating, capital_expenditure, sale_asset,
#     acquisitions, debt_raised and debt_repaid are all defined above)
fcfe_before_debt = (
    net_cash_operating
  - capital_expenditure
  + sale_asset
  - acquisitions
)

fcfe_with_debt = fcfe_before_debt + debt_raised - debt_repaid

# 2) Build safe display labels
if None in (net_cash_operating, capital_expenditure, sale_asset, acquisitions):
    label1 = "N/A"
else:
    label1 = f"${fcfe_before_debt:,.2f}"

if None in (fcfe_before_debt, debt_raised, debt_repaid):
    label2 = "N/A"
else:
    label2 = f"${fcfe_with_debt:,.2f}"

# 3) Show side-by-side metrics
col1, col2 = st.columns(2)
col1.metric("FCFE Before Debt", label1)
col2.metric("FCFE With Debt",  label2)


