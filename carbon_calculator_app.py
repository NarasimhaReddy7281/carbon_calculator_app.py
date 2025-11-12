import streamlit as st

# ----------------------------
# Carbon Footprint Calculator
# ----------------------------
class CarbonCalculator:
    def __init__(self):
        self.travel_emission = 0
        self.electricity_emission = 0
        self.diet_emission = 0

    def calculate_travel(self, km):
        self.travel_emission = km * 0.21  # 0.21 kg CO2 per km
        return self.travel_emission

    def calculate_electricity(self, units):
        self.electricity_emission = units * 0.85  # 0.85 kg CO2 per kWh
        return self.electricity_emission

    def calculate_diet(self, choice):
        if choice == "Vegetarian":
            self.diet_emission = 150
        elif choice == "Non-Vegetarian":
            self.diet_emission = 250
        elif choice == "Vegan":
            self.diet_emission = 100
        return self.diet_emission

    def total_emission(self):
        return self.travel_emission + self.electricity_emission + self.diet_emission


# ----------------------------
# Streamlit Web UI
# ----------------------------
st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌍", layout="centered")

st.title("🌿 Carbon Footprint Calculator")
st.markdown("Estimate your CO₂ emissions from travel, electricity, and diet.")

calc = CarbonCalculator()

# --- Input Section ---
st.header("🚗 Travel Emission")
km = st.number_input("Enter total kilometers travelled per week:", min_value=0.0, step=1.0)
travel_emission = calc.calculate_travel(km)

st.header("💡 Electricity Emission")
units = st.number_input("Enter monthly electricity usage (in kWh):", min_value=0.0, step=1.0)
electricity_emission = calc.calculate_electricity(units)

st.header("🍽️ Diet Emission")
diet_choice = st.selectbox("Select your diet type:", ["Vegetarian", "Non-Vegetarian", "Vegan"])
diet_emission = calc.calculate_diet(diet_choice)

# --- Calculate Button ---
if st.button("Calculate Total Carbon Footprint"):
    total = calc.total_emission()

    st.subheader("🌎 Results:")
    st.write(f"**Travel Emission:** {travel_emission:.2f} kg CO₂/week")
    st.write(f"**Electricity Emission:** {electricity_emission:.2f} kg CO₂/month")
    st.write(f"**Diet Emission:** {diet_emission:.2f} kg CO₂/year")
    st.success(f"### 🌍 Your Estimated Total Carbon Footprint: {total:.2f} kg CO₂")

    # --- Emission Level Message ---
    if total < 200:
        st.info("✅ Low impact! Keep it up!")
    elif total < 400:
        st.warning("⚠️ Moderate impact. Try reducing travel or energy use.")
    else:
        st.error("🚨 High impact! Consider more eco-friendly habits.")
