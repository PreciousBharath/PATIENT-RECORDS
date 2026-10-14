<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=800&size=26&duration=3500&pause=1500&color=8E54E9&center=true&vCenter=true&width=900&height=70&lines=%F0%9F%A9%BA%20Hospital%20Readmission%20Predictor" alt="Hospital Readmission Predictor"/>

<b><i>Predict patient readmission risk from records</i></b>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=36BCF7&center=true&vCenter=true&width=700&lines=%F0%9F%A9%BA%20Predict%20readmission%20risk;%F0%9F%93%8B%20Built%20on%20patient%20records;%F0%9F%A4%96%20scikit-learn%20%2B%20Flask" alt="Typing SVG" />

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn"/> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>

<img src="https://img.shields.io/github/stars/PreciousBharath/PATIENT-RECORDS?style=social" alt="stars"/> <img src="https://img.shields.io/github/forks/PreciousBharath/PATIENT-RECORDS?style=social" alt="forks"/> <img src="https://img.shields.io/github/last-commit/PreciousBharath/PATIENT-RECORDS?style=flat-square&color=blueviolet" alt="last commit"/> <img src="https://img.shields.io/github/repo-size/PreciousBharath/PATIENT-RECORDS?style=flat-square&color=success" alt="repo size"/>
</div>

---

## 🩺 About the Project

Uses **patient records** to predict the risk of **hospital readmission**. A scaled, trained scikit-learn model is served through Flask so clinicians can enter patient details and get an instant risk assessment — helping hospitals plan follow-up care.

## ✨ Key Features

- 📋 Trained on `hospital_readmission.csv`
- ⚖️ Feature scaling with `scaler.pkl`
- 🤖 Classification model (`model.pkl`) — retrain via `model.py`
- ⚡ Instant readmission **risk prediction**

## 🧠 How It Works

```mermaid
flowchart LR
R["📋 Patient Record"] --> S["⚖️ Scaler"] --> M["🤖 Classifier"] --> O{"🩺 Readmission Risk"}
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| ML | scikit-learn · Pandas · NumPy |
| Web | Flask |

## 📂 Project Structure

```text
PATIENT-RECORDS/
├── app.py
├── model.py
├── hospital_readmission.csv
├── model.pkl
└── scaler.pkl
```

## 🚀 Getting Started

```bash
git clone https://github.com/PreciousBharath/PATIENT-RECORDS.git
cd PATIENT-RECORDS
pip install flask pandas numpy scikit-learn
python app.py
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to ⭐ star the repo and open a pull request.

## 👨‍💻 Author

<div align="center">

**Bharath** — Software Developer · Project Engineer · Technical Trainer

<a href="https://github.com/PreciousBharath"><img src="https://img.shields.io/badge/GitHub-PreciousBharath-181717?style=for-the-badge&logo=github"/></a>
<a href="https://linkedin.com/in/connectbharath"><img src="https://img.shields.io/badge/LinkedIn-connectbharath-0A66C2?style=for-the-badge&logo=linkedin"/></a>

### 🍔 EAT · 😴 SLEEP · 💻 CODE · 🔁 REPEAT

⭐ **If you found this project useful, give it a star!** ⭐

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

</div>
