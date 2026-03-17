import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import FEATURES, load_artifacts, predict_flood, explain_with_groq

st.set_page_config(page_title="Flood Prediction Dashboard", layout="wide")

model, scaler = load_artifacts()

st.title("Flood Prediction Dashboard")
st.subheader("Nhập các giá trị đặc trưng")

if "pred_result" not in st.session_state:
    st.session_state["pred_result"] = None
if "input_data" not in st.session_state:
    st.session_state["input_data"] = None
if "ai_text" not in st.session_state:
    st.session_state["ai_text"] = ""

values = {}
cols = st.columns(4)

for i, f in enumerate(FEATURES):
    with cols[i % 4]:
        values[f] = st.number_input(f, min_value=0, max_value=20, value=5, step=1)

if st.button("Predict"):
    st.session_state["input_data"] = values.copy()
    st.session_state["pred_result"] = predict_flood(model, scaler, values)
    st.session_state["ai_text"] = ""

if st.session_state["pred_result"] is not None and st.session_state["input_data"] is not None:
    pred = st.session_state["pred_result"]
    saved_values = st.session_state["input_data"]

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Prediction")
        st.metric("FloodProbability", f"{pred:.4f}")

        chart_df = pd.DataFrame({
            "Feature": list(saved_values.keys()),
            "Value": list(saved_values.values())
        }).sort_values("Value", ascending=False).head(8)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(chart_df["Feature"], chart_df["Value"])
        ax.invert_yaxis()
        st.pyplot(fig)

    with c2:
        st.subheader("Input Summary")
        st.dataframe(pd.DataFrame([saved_values]), use_container_width=True)

        st.subheader("AI Chat")
        if st.button("Giải thích kết quả bằng AI"):
            st.session_state["ai_text"] = explain_with_groq(saved_values, pred)

        if st.session_state["ai_text"]:
            st.write(st.session_state["ai_text"])