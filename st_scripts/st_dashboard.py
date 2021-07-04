import streamlit as st

st.set_page_config(
    page_title="DVC + Streamlit = ❤",
    initial_sidebar_state="expanded",
)

st.title("DVC + Streamlit = ❤")

class DashboardActions:
    MODEL_LIST = "See All Models"
    MODEL_INFERENCE = "Model Inference"
    MODEL_EVALUATION = "Explore Performance on the Test Set"



action = st.sidebar.selectbox(
    "What do you want to do?",
    (
        DashboardActions.MODEL_LIST,
        DashboardActions.MODEL_INFERENCE,
        DashboardActions.MODEL_EVALUATION,
    ),
)

print("Selected dashboard actions: ", action)

#if action == DashboardActions.MODEL_LIST