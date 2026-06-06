import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Profit Predictor",
    page_icon="💼",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
}

.main {
    background-color: #0f0f0f;
}

.stApp {
    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%);
    min-height: 100vh;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.2rem;
}

.hero-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    color: #888;
    margin-bottom: 2rem;
}

.accent { color: #00e5a0; }

.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.result-card {
    background: linear-gradient(135deg, #00e5a0 0%, #00b4d8 100%);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    margin: 1.5rem 0;
}

.result-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    color: rgba(0,0,0,0.6);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.3rem;
}

.result-value {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: #000;
    line-height: 1;
}

.stat-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    color: #ccc;
    font-size: 0.95rem;
}

.stat-value {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    color: #fff;
}

.verdict-green {
    background: rgba(0, 229, 160, 0.1);
    border: 1px solid #00e5a0;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    color: #00e5a0;
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    text-align: center;
}

.verdict-red {
    background: rgba(255, 75, 75, 0.1);
    border: 1px solid #ff4b4b;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    color: #ff4b4b;
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    text-align: center;
}

.verdict-yellow {
    background: rgba(255, 200, 0, 0.1);
    border: 1px solid #ffc800;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    color: #ffc800;
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    text-align: center;
}

.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #00e5a0;
    margin-bottom: 0.75rem;
}

div[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    color: white !important;
}

div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    color: white !important;
}

.stButton > button {
    background: linear-gradient(135deg, #00e5a0, #00b4d8) !important;
    color: #000 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    width: 100% !important;
    transition: opacity 0.2s !important;
}

.stButton > button:hover {
    opacity: 0.85 !important;
}

.remove-btn > button {
    background: rgba(255,75,75,0.15) !important;
    color: #ff4b4b !important;
    font-size: 0.8rem !important;
    padding: 0.3rem 0.8rem !important;
    border-radius: 8px !important;
    width: auto !important;
}
</style>
""", unsafe_allow_html=True)


# --- Header ---
st.markdown("""
<div style="padding: 1.5rem 0 1rem 0;">
    <div class="hero-title">Profit<br><span class="accent">Predictor</span></div>
    <div class="hero-sub">Know your numbers before you sell a single unit.</div>
</div>
""", unsafe_allow_html=True)


# --- Session State for Resources ---
if "resources" not in st.session_state:
    st.session_state.resources = [{"name": "Raw Materials", "cost": 0.0, "qty": 1.0}]


# --- STEP 1: Resources ---
st.markdown('<div class="section-label">Step 1 — Resource Costs</div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

resources_to_remove = []
for i, resource in enumerate(st.session_state.resources):
    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
    with col1:
        resource["name"] = st.text_input("Resource Name", value=resource["name"], key=f"name_{i}", label_visibility="collapsed", placeholder="e.g. Raw Materials")
    with col2:
        resource["cost"] = st.number_input("Cost ($)", value=resource["cost"], min_value=0.0, step=0.5, key=f"cost_{i}", label_visibility="collapsed")
    with col3:
        resource["qty"] = st.number_input("Qty", value=resource["qty"], min_value=0.0, step=0.5, key=f"qty_{i}", label_visibility="collapsed")
    with col4:
        st.markdown('<div class="remove-btn">', unsafe_allow_html=True)
        if st.button("✕", key=f"remove_{i}"):
            resources_to_remove.append(i)
        st.markdown('</div>', unsafe_allow_html=True)

for i in sorted(resources_to_remove, reverse=True):
    st.session_state.resources.pop(i)
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

if st.button("＋ Add Resource"):
    st.session_state.resources.append({"name": "", "cost": 0.0, "qty": 1.0})
    st.rerun()


# --- STEP 2: Selling Price & Overhead ---
st.markdown('<div class="section-label" style="margin-top:1.5rem;">Step 2 — Pricing & Sales</div>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    selling_price = st.number_input("💰 Selling Price per Unit ($)", min_value=0.0, value=25.0, step=0.5)
with col2:
    units_sold = st.number_input("📦 Expected Units to Sell", min_value=1, value=100, step=1)

fixed_overhead = st.number_input("🏢 Fixed Overhead (rent, salaries, etc.) ($)", min_value=0.0, value=500.0, step=10.0)

st.markdown('</div>', unsafe_allow_html=True)


# --- CALCULATE BUTTON ---
st.markdown("<div style='margin-top: 1rem;'>", unsafe_allow_html=True)
calculate = st.button("🚀 Calculate Profit")
st.markdown("</div>", unsafe_allow_html=True)


# --- RESULTS ---
if calculate:
    # Calculations
    variable_cost_per_unit = sum(r["cost"] * r["qty"] for r in st.session_state.resources)
    total_variable_cost = variable_cost_per_unit * units_sold
    total_cost = total_variable_cost + fixed_overhead
    total_revenue = selling_price * units_sold
    gross_profit = total_revenue - total_variable_cost
    net_profit = total_revenue - total_cost
    profit_margin = (net_profit / total_revenue * 100) if total_revenue > 0 else 0
    roi = (net_profit / total_cost * 100) if total_cost > 0 else 0
    break_even = (fixed_overhead / (selling_price - variable_cost_per_unit)
                  if selling_price > variable_cost_per_unit else float("inf"))

    # Main Result Card
    profit_color = "#00e5a0" if net_profit > 0 else ("#ff4b4b" if net_profit < 0 else "#ffc800")
    st.markdown(f"""
    <div class="result-card" style="background: linear-gradient(135deg, {profit_color} 0%, #0f0f0f 150%);">
        <div class="result-label">Net Profit</div>
        <div class="result-value" style="color: {'#000' if net_profit > 0 else '#fff'};">${net_profit:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="stat-row"><span>Total Revenue</span><span class="stat-value">${total_revenue:,.2f}</span></div>
    <div class="stat-row"><span>Total Cost</span><span class="stat-value">${total_cost:,.2f}</span></div>
    <div class="stat-row"><span>Gross Profit</span><span class="stat-value">${gross_profit:,.2f}</span></div>
    <div class="stat-row"><span>Profit Margin</span><span class="stat-value">{profit_margin:.1f}%</span></div>
    <div class="stat-row"><span>ROI</span><span class="stat-value">{roi:.1f}%</span></div>
    <div class="stat-row"><span>Variable Cost / Unit</span><span class="stat-value">${variable_cost_per_unit:,.2f}</span></div>
    <div class="stat-row" style="border:none;"><span>Break-even Units</span><span class="stat-value">{"∞" if break_even == float("inf") else f"{break_even:.0f} units"}</span></div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Verdict
    if net_profit > 0:
        st.markdown(f'<div class="verdict-green">🟢 Profitable — You make ${net_profit:,.2f} in profit!</div>', unsafe_allow_html=True)
    elif net_profit < 0:
        st.markdown(f'<div class="verdict-red">🔴 Loss — You lose ${abs(net_profit):,.2f}. Lower costs or raise price.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="verdict-yellow">🟡 Break-even — No profit, no loss.</div>', unsafe_allow_html=True)

    # Break-even note
    if break_even != float("inf"):
        if units_sold >= break_even:
            st.success(f"✅ You are {units_sold - break_even:.0f} units above break-even.")
        else:
            st.warning(f"⚠️ You need {break_even - units_sold:.0f} more units to break even.")
