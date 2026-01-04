# 💧 Water Quality & Conductance Checker

A Streamlit-based web application to analyze **drinking water safety** and **conductance quality** using **WHO/BIS standards** and **Machine Learning**.

---

## 🚀 Live Demo
👉 Hosting link:- https://waterqualityandconductancecheck-dhpdkhmn8prk435wrqc26f.streamlit.app/

---

## 📌 Project Overview

This project helps users determine:
- ✅ Whether water is **safe for drinking**
- 🔬 The **conductance quality** of water (Excellent / Good / Poor)
- 📊 An **ML-based water quality score**

⚠️ **Important Note**  
Drinking water safety decisions are made using **rule-based WHO/BIS standards**, not ML alone.  
Machine Learning is used only for **quality assessment**, not final safety approval.

---

## 🧪 Parameters Used

| Parameter | Description |
|---------|------------|
| Temperature (°C) | Water temperature |
| pH | Acidity/alkalinity |
| Conductivity (µmhos/cm) | Mineral/salinity content |
| BOD (mg/l) | Organic pollution |
| Nitrate (mg/l) | Agricultural contamination |
| Total Coliform | Bacterial contamination |

---

## ✅ Drinkability Rules (WHO/BIS)

Water is considered **Drinkable** only if:

- pH is between **6.5 – 8.5**
- Conductivity ≤ **1500 µmhos/cm**
- BOD ≤ **3 mg/l**
- Nitrate ≤ **45 mg/l**
- Total Coliform = **0**

If any condition fails → ❌ **Not Drinkable**

---

## 🔬 Conductance Quality Scale

| Conductivity (µmhos/cm) | Quality |
|-------------------------|---------|
| < 750 | 🟢 Excellent |
| 750 – 1500 | 🟡 Good |
| > 1500 | 🔴 Poor |

---

## 🧠 Machine Learning Model

- Algorithm: **Random Forest Classifier**
- Purpose: **Water quality scoring**
- Trained on: Ground water quality data (West Bengal)
- Model files:
  - `drinkable_model.pkl`
  - `scaler.pkl`

---

## 🖥️ Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **Joblib**

---

## 📂 Project Structure

water-quality-app/
├── app.py
├── drinkable_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md

yaml
Copy code

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/water-quality-app.git
cd water-quality-app
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the app
bash
Copy code
streamlit run app.py
☁️ Deployment
This app is deployed using Streamlit Cloud.

Deployment requirements:

app.py in root directory

requirements.txt in root directory

Python 3.9+ recommended

🎓 Academic Use 
“Drinking water safety is governed by strict WHO/BIS rules.
Machine Learning models are probabilistic, so a hybrid approach was used where rule-based validation ensures safety and ML provides quality assessment.”

📌 Future Improvements
District-wise analysis

CSV upload for bulk testing

Interactive charts

API integration (Flask/FastAPI)

👤 Author
Ranjan Das
B.Tech CSE(AIML)
Brainware University

📜 License
This project is for educational and academic use.
