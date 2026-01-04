import streamlit as st
import numpy as np
import joblib

# Load model & scaler (used only for quality score if needed)
model = joblib.load("drinkable_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Water Quality Checker", layout="centered")

st.title("💧 Water Quality & Drinkability Checker")
st.markdown("Check whether water is **safe for drinking** and analyze **conductance quality**.")

st.divider()

# -----------------------------
# SAMPLE INPUTS (DEFAULT VALUES)
# -----------------------------
st.subheader("🔢 Enter Water Quality Parameters")

temp = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=60.0,
    value=28.0
)

ph = st.number_input(
    "pH Value",
    min_value=0.0,
    max_value=14.0,
    value=7.2
)

cond = st.number_input(
    "Conductivity (µmhos/cm)",
    min_value=0.0,
    value=900.0
)

bod = st.number_input(
    "BOD (mg/l)",
    min_value=0.0,
    value=2.0
)

nitrate = st.number_input(
    "Nitrate (mg/l)",
    min_value=0.0,
    value=12.0
)

coliform = st.number_input(
    "Total Coliform (MPN/100ml)",
    min_value=0,
    value=0
)

st.divider()

# -----------------------------
# CHECK BUTTON
# -----------------------------
if st.button("🔍 Check Water Quality"):

    reasons = []

    if not (6.5 <= ph <= 8.5):
        reasons.append("pH out of safe range (6.5–8.5)")

    if cond > 1500:
        reasons.append("High conductivity")

    if bod > 3:
        reasons.append("High BOD")

    if nitrate > 45:
        reasons.append("High nitrate")

    if coliform > 0:
        reasons.append("Coliform bacteria present")

    # -----------------------------
    # CONDUCTANCE QUALITY
    # -----------------------------
    if cond < 750:
        cond_quality = "Excellent 🟢"
    elif cond <= 1500:
        cond_quality = "Good 🟡"
    else:
        cond_quality = "Poor 🔴"

    st.subheader("📊 Results")

    st.write(f"**Conductance Quality:** {cond_quality}")

    if reasons:
        st.error("❌ Water is NOT DRINKABLE")
        st.write("**Reasons:**")
        for r in reasons:
            st.write(f"- {r}")
    else:
        st.success("✅ Water is DRINKABLE")

    # -----------------------------
    # OPTIONAL: ML Quality Score
    # -----------------------------
    user_input = np.array([[temp, ph, cond, bod, nitrate]])
    user_input_scaled = scaler.transform(user_input)
    quality_score = model.predict_proba(user_input_scaled)[0][1]

    st.info(f"🔬 Water Quality Score (ML): **{quality_score:.2f}**")

st.divider()
st.caption("⚠️ Drinking water safety is rule-based (WHO/BIS). ML score is for quality assessment only.")
