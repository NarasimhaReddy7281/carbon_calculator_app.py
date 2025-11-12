🌿 Carbon Footprint Calculator
🔎 Project Overview

The Carbon Footprint Calculator is a simple, interactive web application built using Python and Streamlit.
It helps users estimate their CO₂ emissions based on their travel distance, electricity usage, and diet type.
The goal is to raise awareness about individual environmental impact and encourage eco-friendly habits.

🧠 Key Features

✅ User-friendly web interface built with Streamlit
✅ Calculates carbon emissions from:

🚗 Travel (based on distance traveled per week)

💡 Electricity usage (monthly consumption in kWh)

🍽️ Diet type (Vegetarian, Non-Vegetarian, Vegan)
✅ Provides personalized feedback:

Low, Moderate, or High Impact messages
✅ Works locally or can be deployed online using Streamlit Cloud

🧩 Technologies Used

Python 3

Streamlit (for the UI)

OOP Concepts (Class-based logic)

📁 Project Structure
carbon-footprint-calculator/
│
├── carbon_calculator_app.py     # Main Streamlit application
├── requirements.txt             # Dependencies for Streamlit
└── README.md                    # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository (or download ZIP)
git clone https://github.com/yourusername/carbon-footprint-calculator.git
cd carbon-footprint-calculator

2️⃣ Install Dependencies

Make sure you have Python installed. Then run:

pip install -r requirements.txt

3️⃣ Run the App Locally
streamlit run carbon_calculator_app.py


Then open the link shown in the terminal, usually:
👉 http://localhost:8501

🌍 Deploy on Streamlit Cloud

You can host your app online for free using Streamlit Cloud:

Push your project to GitHub (must include carbon_calculator_app.py and requirements.txt)

Go to https://share.streamlit.io

Click "New App" → Select your GitHub repo → Choose branch and main file

Click Deploy

Your live app link will be generated automatically ✅

🧾 Example Input & Output

Input Example:

Travel: 100 km/week

Electricity: 200 kWh/month

Diet: Non-Vegetarian

Output Example:

Travel Emission: 21.00 kg CO₂/week
Electricity Emission: 170.00 kg CO₂/month
Diet Emission: 250 kg CO₂/year
Total Carbon Footprint: 441.00 kg CO₂
🚨 High impact! Consider eco-friendly habits.

🖼️ Screenshot (Optional)

You can add screenshots here after running the app:

<img width="1745" height="891" alt="image" src="https://github.com/user-attachments/assets/c958c953-72fb-4740-b51a-ca0b0c306577" />


💬 Future Improvements

Save user emission data in a database (SQLite)

Add graphs or charts using matplotlib or plotly

Show tips and tricks to reduce carbon footprint

## 🧑‍💻 Author

**👨‍🎓 R.Ugra Narasimha Reddy**
**👨‍🎓 S.Nandha Kumar**
**👨‍🎓 Omkar Pranav**
