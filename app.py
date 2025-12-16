import streamlit as st
import pandas as pd
import os

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Urban Gardening Assistant",
    page_icon="🌱",
    layout="wide"
)

# --------------------------------------------------
# Load Plant Database from CSV
# --------------------------------------------------
PLANT_CSV_PATH = "plants.csv"

if os.path.exists(PLANT_CSV_PATH):
    plant_df = pd.read_csv(PLANT_CSV_PATH)
else:
    st.error("Plant database CSV not found. Upload 'plants.csv' in the project folder.")
    plant_df = pd.DataFrame(columns=["name", "sun", "water", "space", "description"])

# --------------------------------------------------
# Home Page
# --------------------------------------------------
def home_page():
    st.title("🌱 Urban Gardening Assistant")

    st.markdown(
        """
        Urban Gardening Assistant is a smart, user-focused platform designed to help
        urban residents make informed gardening decisions.
        Users can search any plant and get guidance based on sunlight, water, and space requirements.
        """
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Purpose")
        st.write(
            """
            Support urban residents to grow plants in limited spaces such as balconies, rooftops, or indoors.
            The system suggests plants likely to thrive in the given environment.
            """
        )

    with col2:
        st.subheader("Key Features")
        st.write(
            """
            • Dynamic plant database (CSV)  
            • Search any plant → Info fetched automatically  
            • Recommendations based on sunlight, water, and space  
            • User-friendly and beginner-oriented  
            """
        )

    st.markdown("---")

    st.subheader("How It Works")
    st.write(
        """
        Users provide available space, sunlight exposure, and watering habits.
        The system evaluates plant suitability and explains why each plant is recommended.
        """
    )

# --------------------------------------------------
# Plant Recommendation Page
# --------------------------------------------------
def plant_recommendation_page():
    st.title("Plant Recommendations")

    search = st.text_input("Search plant (optional)")

    col1, col2, col3 = st.columns(3)
    with col1:
        sunlight = st.selectbox("Sunlight", ["Full Sun", "Partial Shade", "Low Light"])
    with col2:
        space = st.slider("Available space (sq ft)", 1, 50, 10)
    with col3:
        water = st.selectbox("Watering frequency", ["Low", "Medium", "High"])

    if st.button("Generate Recommendations"):
        results = []

        for _, plant in plant_df.iterrows():
            if search and search.lower() not in plant["name"].lower():
                continue

            score = 0
            reasons = []

            if plant["sun"] == sunlight:
                score += 0.4
                reasons.append("Sunlight matches your selection")
            if plant["water"] == water:
                score += 0.3
                reasons.append("Watering frequency matches your selection")
            if plant["space"] <= space:
                score += 0.3
                reasons.append("Space available is sufficient")

            if score >= 0.5:
                results.append((plant, score, reasons))

        if results:
            for plant, score, reasons in sorted(results, key=lambda x: x[1], reverse=True):
                st.markdown(
                    f"""
                    <div style='border:1px solid #ddd; border-radius:10px; padding:15px; margin-bottom:10px;'>
                        <h4>{plant['name']}</h4>
                        <p>{plant['description']}</p>
                        <b>Suitability Score:</b> {int(score*100)}%<br>
                        <b>Why recommended:</b> {', '.join(reasons)}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.warning("No matching plants found. Try adjusting inputs or search.")

# --------------------------------------------------
# Seasonal Guide Page
# --------------------------------------------------
def seasonal_guide_page():
    st.title("Seasonal Planting Guide")

    season = st.selectbox("Select season", ["Spring", "Summer", "Monsoon", "Winter"])

    if season == "Spring":
        plants = ["Tomatoes", "Basil", "Coriander", "Lettuce"]
    elif season == "Summer":
        plants = ["Chilli", "Peppers", "Mint", "Okra"]
    elif season == "Monsoon":
        plants = ["Spinach", "Coriander", "Fenugreek"]
    else:
        plants = ["Mint", "Rosemary", "Indoor Herbs"]

    for p in plants:
        st.write(f"• {p}")

# --------------------------------------------------
# Main App
# --------------------------------------------------
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Explore", ["Home", "Plant Recommendation", "Seasonal Guide"])

    st.sidebar.markdown("---")
    st.sidebar.info(
        "👩‍💻 **Developer:** Kirti Kumari|\n"
        "3rd-year Computer Science Engineering student|\n"
        "Focused on AI & ML and building practical, user-centric applications"
    )

    if page == "Home":
        home_page()
    elif page == "Plant Recommendation":
        plant_recommendation_page()
    else:
        seasonal_guide_page()

    st.markdown("---")
    st.caption("© 2025 Urban Gardening Assistant | Kirti Kumari")


if __name__ == "__main__":
    main()
