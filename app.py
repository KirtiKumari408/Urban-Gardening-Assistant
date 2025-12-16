import streamlit as st
import joblib

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
<<<<<<< HEAD
st.set_page_config(page_title="Urban Gardening Assistant",
                   page_icon="🌱",
                   layout="wide")
=======
st.set_page_config(
    page_title="Urban Gardening Assistant",
    page_icon="🌱",
    layout="wide"
)
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)

# --------------------------------------------------
# Load Trained ML Model
# --------------------------------------------------
model = joblib.load("plant_model.pkl")

# --------------------------------------------------
# Plant Knowledge Base
# --------------------------------------------------
PLANTS = [
    {
<<<<<<< HEAD
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
=======
        "name": "Tomatoes",
        "type": "Vegetable",
        "sunlight": "Full Sun",
        "space": 4,
        "water": "Medium",
        "description": "Well-suited for containers and balconies. Cherry varieties perform best in urban spaces."
    },
    {
        "name": "Lettuce",
        "type": "Vegetable",
        "sunlight": "Partial Shade",
        "space": 1,
        "water": "High",
        "description": "Fast-growing leafy green ideal for compact containers and frequent harvests."
    },
    {
        "name": "Basil",
        "type": "Herb",
        "sunlight": "Full Sun",
        "space": 1,
        "water": "Medium",
        "description": "Aromatic herb that grows well on windowsills and pairs well with tomatoes."
    },
    {
        "name": "Mint",
        "type": "Herb",
        "sunlight": "Partial Shade",
        "space": 1,
        "water": "High",
        "description": "Robust grower best maintained in containers to control spreading."
    },
    {
        "name": "Peppers",
        "type": "Vegetable",
        "sunlight": "Full Sun",
        "space": 2,
        "water": "Medium",
        "description": "Compact pepper varieties adapt well to pots and container gardens."
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
    },
    {
        "name": "Spinach",
        "type": "Vegetable",
        "sunlight": "Partial Shade",
        "space": 1,
        "water": "Medium",
<<<<<<< HEAD
        "description":
        "Cool-season crop that performs well in shallow containers."
=======
        "description": "Cool-season crop that performs well in shallow containers."
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
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
<<<<<<< HEAD
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
=======
        "name": "Strawberries",
        "type": "Fruit",
        "sunlight": "Full Sun",
        "space": 2,
        "water": "Medium",
        "description": "Excellent choice for hanging baskets and vertical planters."
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
    },
    {
        "name": "Marigolds",
        "type": "Flower",
        "sunlight": "Full Sun",
        "space": 1,
        "water": "Low",
<<<<<<< HEAD
        "description":
        "Natural pest deterrent and companion plant for vegetables."
    },
=======
        "description": "Natural pest deterrent and companion plant for vegetables."
    }
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
]

# --------------------------------------------------
# Seasonal Knowledge
# --------------------------------------------------
SEASONAL_GUIDE = {
    "Spring": {
<<<<<<< HEAD
        "months":
        "March – May",
        "plants":
        ["Tomatoes", "Peppers", "Basil", "Lettuce", "Spinach", "Strawberries"],
=======
        "months": "March – May",
        "plants": ["Tomatoes", "Peppers", "Basil", "Lettuce", "Spinach", "Strawberries"],
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
        "tips": [
            "Prepare soil with organic compost",
            "Gradually acclimate seedlings to outdoor conditions",
            "Monitor temperature fluctuations"
        ]
    },
    "Summer": {
<<<<<<< HEAD
        "months":
        "June – August",
        "plants":
        ["Tomatoes", "Peppers", "Basil", "Strawberries", "Marigolds"],
=======
        "months": "June – August",
        "plants": ["Tomatoes", "Peppers", "Basil", "Strawberries", "Marigolds"],
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
        "tips": [
            "Ensure consistent watering during heat",
            "Use mulch to reduce moisture loss",
            "Provide shade during peak afternoon heat"
        ]
    },
    "Fall": {
<<<<<<< HEAD
        "months":
        "September – November",
        "plants": ["Lettuce", "Spinach", "Marigolds"],
        "tips": [
            "Focus on cool-season crops", "Protect plants from early frost",
=======
        "months": "September – November",
        "plants": ["Lettuce", "Spinach", "Marigolds"],
        "tips": [
            "Focus on cool-season crops",
            "Protect plants from early frost",
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
            "Clean containers to prevent disease"
        ]
    },
    "Winter": {
<<<<<<< HEAD
        "months":
        "December – February",
        "plants": ["Mint", "Rosemary"],
        "tips": [
            "Shift sensitive plants indoors", "Maintain herbs near sunlight",
=======
        "months": "December – February",
        "plants": ["Mint", "Rosemary"],
        "tips": [
            "Shift sensitive plants indoors",
            "Maintain herbs near sunlight",
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
            "Plan upcoming planting cycles"
        ]
    }
}

<<<<<<< HEAD

=======
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
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
<<<<<<< HEAD
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
=======
        - Rule-based scoring & ranking
        """)

    with col2:
        st.info("Designed for balconies, rooftops, patios, and indoor environments.")
        st.success("Combines Machine Learning with explainable scoring.")
        st.warning("Adequate sunlight improves prediction accuracy.")

# --------------------------------------------------
# Recommendation Page
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
# --------------------------------------------------
def plant_recommendation_page():
    st.title("Plant Recommendations")

    col1, col2, col3 = st.columns(3)

    with col1:
        sunlight = st.selectbox(
            "Sunlight availability",
<<<<<<< HEAD
            ["Full Sun (6+ hours)", "Partial Shade (3–6 hours)", "Low Light"])
=======
            ["Full Sun (6+ hours)", "Partial Shade (3–6 hours)", "Low Light"]
        )
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)

    with col2:
        space = st.slider("Available space (sq ft)", 1, 50, 10)

    with col3:
<<<<<<< HEAD
        water = st.selectbox("Watering frequency",
                             ["Daily", "Every 2–3 days", "Weekly"])
=======
        water = st.selectbox(
            "Watering frequency",
            ["Daily", "Every 2–3 days", "Weekly"]
        )
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)

    sunlight_encoding = {
        "Full Sun (6+ hours)": 2,
        "Partial Shade (3–6 hours)": 1,
        "Low Light": 0
    }

<<<<<<< HEAD
    water_encoding = {"Daily": 2, "Every 2–3 days": 1, "Weekly": 0}
=======
    water_encoding = {
        "Daily": 2,
        "Every 2–3 days": 1,
        "Weekly": 0
    }
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)

    if st.button("Generate Recommendations", type="primary"):
        sun_val = sunlight_encoding[sunlight]
        water_val = water_encoding[water]

        recommendations = []

        for plant in PLANTS:
<<<<<<< HEAD
            probability = model.predict_proba(
                [[sun_val, plant["space"], water_val]])[0][1]

            if probability >= 0.6:
                plant_copy = plant.copy()
                plant_copy["probability"] = probability
                recommendations.append(plant_copy)

        recommendations = sorted(recommendations,
                                 key=lambda x: x["probability"],
                                 reverse=True)
=======
            # ML Prediction
            _ = model.predict_proba([[sun_val, plant["space"], water_val]])[0][1]

            # Scoring Logic (Max = 7)
            score = 0

            if plant["sunlight"] in sunlight:
                score += 3

            if plant["space"] <= space:
                score += 2

            if plant["water"] in water:
                score += 2

            plant_result = plant.copy()
            plant_result["score"] = score
            recommendations.append(plant_result)

        recommendations = sorted(
            recommendations,
            key=lambda x: x["score"],
            reverse=True
        )
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)

        if recommendations:
            for plant in recommendations:
                st.markdown(f"### {plant['name']}")
<<<<<<< HEAD
                st.progress(int(plant["probability"] * 100))
                st.caption(
                    f"Suitability Probability: {plant['probability']:.2f}")
                st.write(plant["description"])
                st.markdown("---")
        else:
            st.warning(
                "No suitable plants found. Try adjusting input parameters.")

=======
                st.caption(f"Suitability Score: {plant['score']} / 7")
                st.write(plant["description"])
                st.markdown("---")
        else:
            st.warning("No suitable plants found. Adjust inputs and try again.")
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)

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

<<<<<<< HEAD

=======
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
# --------------------------------------------------
# Main App
# --------------------------------------------------
def main():
    st.sidebar.title("Navigation")

<<<<<<< HEAD
    page = st.sidebar.radio("Explore",
                            ["Home", "Plant Recommendation", "Seasonal Guide"])
=======
    page = st.sidebar.radio(
        "Explore",
        ["Home", "Plant Recommendation", "Seasonal Guide"]
    )
>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)

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
<<<<<<< HEAD
    st.caption(
        "Urban Gardening Assistant | Python • Streamlit • Machine Learning")
    st.caption("© 2025 Kirti Kumari")


=======
    st.caption("Urban Gardening Assistant | Python • Streamlit • Machine Learning")
    st.caption("© 2025 Kirti Kumari")

>>>>>>> 9fc1a89 (Update UI and ML-based plant scoring logic)
if __name__ == "__main__":
    main()
