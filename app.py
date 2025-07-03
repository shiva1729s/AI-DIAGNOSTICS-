import streamlit as st
from PIL import Image
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Diagnostics",
    page_icon="🧬",
    layout="wide"
)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f3f4f6;
    }
    .header {
        background-color: white;
        padding: 1rem;
        margin-bottom: 2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
    <div class='header'>
        <h1 style='margin: 0;'>AI Diagnostics</h1>
        <p style='color: #666;'>Powered by Machine Learning</p>
    </div>
""", unsafe_allow_html=True)

# --- Sidebar Selection ---
analysis_type = st.sidebar.radio(
    "Select Analysis Type",
    ["Brain", "Heart", "Lungs", "Skin"]
)

# --- Layout Columns ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Upload Scan/Image")

    prompt = "Choose an image file" if analysis_type == "Skin" else "Choose a scan file"
    uploaded_file = st.file_uploader(prompt, type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"{analysis_type} Image", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Analysis Results")

    if uploaded_file:
        with st.spinner("Processing Image..."):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

        findings = {
            "Brain": [
                {"name": "Cerebral Microbleeds", "probability": 0.89, "severity": "high"},
                {"name": "White Matter Lesions", "probability": 0.45, "severity": "medium"},
                {"name": "Cortical Atrophy", "probability": 0.12, "severity": "low"},
            ],
            "Heart": [
                {"name": "Left Ventricular Hypertrophy", "probability": 0.78, "severity": "high"},
                {"name": "Coronary Calcification", "probability": 0.56, "severity": "medium"},
                {"name": "Valve Regurgitation", "probability": 0.23, "severity": "low"},
            ],
            "Lungs": [
                {"name": "Pulmonary Nodules", "probability": 0.92, "severity": "high"},
                {"name": "Pleural Effusion", "probability": 0.67, "severity": "medium"},
                {"name": "Bronchial Thickening", "probability": 0.34, "severity": "low"},
            ],
            "Skin": [
                {"name": "Melanoma", "probability": 0.82, "severity": "high"},
                {"name": "Basal Cell Carcinoma", "probability": 0.45, "severity": "high"},
                {"name": "Actinic Keratosis", "probability": 0.67, "severity": "medium"},
                {"name": "Seborrheic Keratosis", "probability": 0.78, "severity": "low"},
                {"name": "Dermatitis", "probability": 0.56, "severity": "low"},
            ]
        }

        severity_badge = {"high": "🟥", "medium": "🟨", "low": "🟩"}

        st.markdown("### Findings")
        for finding in findings[analysis_type]:
            st.markdown(f"""
                <div style='
                    background-color: #f9f9f9;
                    padding: 0.75rem;
                    border-radius: 0.5rem;
                    margin-bottom: 0.5rem;
                '>
                {severity_badge[finding["severity"]]} <strong>{finding["name"]}</strong>
                <span style='float: right;'>Probability: {finding["probability"] * 100:.1f}%</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("### Processing Information")
        a, b = st.columns(2)
        a.metric("Processing Time", "2.3s")
        b.metric("Confidence Score", "92%")

        st.markdown("### Clinical Recommendations")
        recs = {
            "Brain": ["Follow-up imaging", "Consult neurologist", "Review risk factors"],
            "Heart": ["Cardiac evaluation", "Cardiologist referral", "Lifestyle review"],
            "Lungs": ["Repeat imaging", "Pulmonary function tests", "Consult pulmonologist"],
            "Skin": ["Dermatology referral", "Dermoscopy review", "Monitor sun exposure"],
        }
        for rec in recs[analysis_type]:
            st.markdown(f"- {rec}")

    else:
        st.info("Upload a scan/image to get analysis results.")

    st.markdown("</div>", unsafe_allow_html=True)

# --- Optional Presentation ---
if st.button("View Presentation"):
    st.markdown("## AI-Powered Medical Diagnostics")
    st.image(
        "https://images.unsplash.com/photo-1584362917165-526a968579e8?auto=format&fit=crop&q=80&w=1000",
        caption="Advanced Medical Imaging"
    )

    st.markdown("""
        ### Highlights
        - Real-time Machine Learning Analysis
        - Tailored for Multi-Organ Diagnostics
        - Built with Streamlit
    """)
