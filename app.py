import streamlit as st
import joblib

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(page_title="Urban Gardening Assistant",
                   page_icon="🌱",
                   layout="wide")

# --------------------------------------------------
# Load Trained ML Model
# --------------------------------------------------
model = joblib.load("plant_model.pkl")

# --------------------------------------------------
# Plant Knowledge Base
# --------------------------------------------------
PLANTS = [
    {
        "name":
        "Tomatoes",
        "type":
        "Vegetable",
        "sunlight":
        "Full Sun",
        "space":
        4,
        "water":
        "Medium",
        "description":
        "Well-suited for containers and balconies. Cherry varieties perform best in urban spaces."
    },
    {
        "name":
        "Lettuce",
        "type":
        "Vegetable",
        "sunlight":
        "Partial Shade",
        "space":
        1,
        "water":
        "High",
        "description":
        "Fast-growing leafy green ideal for compact containers and frequent harvests."
    },
    {
        "name":
        "Basil",
        "type":
        "Herb",
        "sunlight":
        "Full Sun",
        "space":
        1,
        "water":
        "Medium",
        "description":
        "Aromatic herb that grows well on windowsills and pairs well with tomatoes."
    },
    {
        "name":
        "Mint",
        "type":
        "Herb",
        "sunlight":
        "Partial Shade",
        "space":
        1,
        "water":
        "High",
        "description":
        "Robust grower best maintained in containers to control spreading."
    },
    {
        "name":
        "Peppers",
        "type":
        "Vegetable",
        "sunlight":
        "Full Sun",
        "space":
        2,
        "water":
        "Medium",
        "description":
        "Compact pepper varieties adapt well to pots and container gardens."
    },
    {
        "name": "Spinach",
        "type": "Vegetable",
        "sunlight": "Partial Shade",
        "space": 1,
        "water": "Medium",
        "description":
        "Cool-season crop that performs well in shallow containers."
    },
    {
        "name": "Rosemary",
        "type": "Herb",
        "sunlight": "Full Sun",
        "space": 2,
        "water": "Low",
        "description": "Drought-tolerant herb requiring minimal maintenance."
    },
    {
        "name":
        "Strawberries",
        "type":
        "Fruit",
        "sunlight":
        "Full Sun",
        "space":
        2,
        "water":
        "Medium",
        "description":
        "Excellent choice for hanging baskets and vertical planters."
    },
    {
        "name": "Marigolds",
        "type": "Flower",
        "sunlight": "Full Sun",
        "space": 1,
        "water": "Low",
        "description":
        "Natural pest deterrent and companion plant for vegetables."
    },
]

# --------------------------------------------------
# Seasonal Knowledge
# --------------------------------------------------
SEASONAL_GUIDE = {
    "Spring": {
        "months":
        "March – May",
        "plants":
        ["Tomatoes", "Peppers", "Basil", "Lettuce", "Spinach", "Strawberries"],
        "tips": [
            "Prepare soil with organic compost",
            "Gradually acclimate seedlings to outdoor conditions",
            "Monitor temperature fluctuations"
        ]
    },
    "Summer": {
        "months":
        "June – August",
        "plants":
        ["Tomatoes", "Peppers", "Basil", "Strawberries", "Marigolds"],
        "tips": [
            "Ensure consistent watering during heat",
            "Use mulch to reduce moisture loss",
            "Provide shade during peak afternoon heat"
        ]
    },
    "Fall": {
        "months":
        "September – November",
        "plants": ["Lettuce", "Spinach", "Marigolds"],
        "tips": [
            "Focus on cool-season crops", "Protect plants from early frost",
            "Clean containers to prevent disease"
        ]
    },
    "Winter": {
        "months":
        "December – February",
        "plants": ["Mint", "Rosemary"],
        "tips": [
            "Shift sensitive plants indoors", "Maintain herbs near sunlight",
            "Plan upcoming planting cycles"
        ]
    }
}


# --------------------------------------------------
# Home Page
# --------------------------------------------------
def home_page():
    st.title("Urban Gardening Assistant")

    st.markdown(
        "A decision-support platform that recommends suitable plants "
        "based on environmental conditions, space availability, and intelligent inference."
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ### Why Urban Gardening?
        - Grow fresh produce at home
        - Make efficient use of limited space
        - Encourage sustainable lifestyle choices

        ### System Overview
        - User-defined environmental inputs
        - ML-based suitability prediction
        - Ranked plant recommendations
        """)

    with col2:
        st.info(
            "Designed for balconies, rooftops, patios, and indoor environments."
        )
        st.success("Built with extensibility for advanced ML models.")
        st.warning("Adequate sunlight improves prediction accuracy.")


# --------------------------------------------------
# Recommendation Page (ML Inference)
# --------------------------------------------------
def plant_recommendation_page():
    st.title("Plant Recommendations")

    col1, col2, col3 = st.columns(3)

    with col1:
        sunlight = st.selectbox(
            "Sunlight availability",
            ["Full Sun (6+ hours)", "Partial Shade (3–6 hours)", "Low Light"])

    with col2:
        space = st.slider("Available space (sq ft)", 1, 50, 10)

    with col3:
        water = st.selectbox("Watering frequency",
                             ["Daily", "Every 2–3 days", "Weekly"])

    sunlight_encoding = {
        "Full Sun (6+ hours)": 2,
        "Partial Shade (3–6 hours)": 1,
        "Low Light": 0
    }

    water_encoding = {"Daily": 2, "Every 2–3 days": 1, "Weekly": 0}

    if st.button("Generate Recommendations", type="primary"):
        sun_val = sunlight_encoding[sunlight]
        water_val = water_encoding[water]

        recommendations = []

        for plant in PLANTS:
            probability = model.predict_proba(
                [[sun_val, plant["space"], water_val]])[0][1]

            if probability >= 0.6:
                plant_copy = plant.copy()
                plant_copy["probability"] = probability
                recommendations.append(plant_copy)

        recommendations = sorted(recommendations,
                                 key=lambda x: x["probability"],
                                 reverse=True)

        if recommendations:
            for plant in recommendations:
                st.markdown(f"### {plant['name']}")
                st.progress(int(plant["probability"] * 100))
                st.caption(
                    f"Suitability Probability: {plant['probability']:.2f}")
                st.write(plant["description"])
                st.markdown("---")
        else:
            st.warning(
                "No suitable plants found. Try adjusting input parameters.")


# --------------------------------------------------
# Seasonal Guide Page
# --------------------------------------------------
def seasonal_guide_page():
    st.title("Seasonal Planting Guide")

    season = st.selectbox("Select season", list(SEASONAL_GUIDE.keys()))
    data = SEASONAL_GUIDE[season]

    st.markdown(f"### {season} ({data['months']})")

    st.markdown("#### Recommended Plants")
    for plant in data["plants"]:
        st.write(f"- {plant}")

    st.markdown("#### Best Practices")
    for tip in data["tips"]:
        st.write(f"- {tip}")


# --------------------------------------------------
# Main App
# --------------------------------------------------
def main():
    st.sidebar.title("Navigation")

    page = st.sidebar.radio("Explore",
                            ["Home", "Plant Recommendation", "Seasonal Guide"])

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Developer")
    st.sidebar.info(
        "Kirti Kumari\n"
        "Pre-final year CSE undergraduate\n"
        "Passionate about AI/ML-driven systems and product-focused development"
    )

    if page == "Home":
        home_page()
    elif page == "Plant Recommendation":
        plant_recommendation_page()
    elif page == "Seasonal Guide":
        seasonal_guide_page()

    st.markdown("---")
    st.caption(
        "Urban Gardening Assistant | Python • Streamlit • Machine Learning")
    st.caption("© 2025 Kirti Kumari")


if __name__ == "__main__":
    main()
