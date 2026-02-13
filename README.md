# 💊 ENTRESTO (Sacubitril/Valsartan) - Professional Drug Information App

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FDA](https://img.shields.io/badge/FDA-Verified-green?style=for-the-badge)

## 🎯 Overview

A comprehensive, evidence-based Streamlit application providing professional-grade information about **ENTRESTO® (Sacubitril/Valsartan)**, a first-in-class neprilysin inhibitor + ARB combination for heart failure treatment.

### ✨ Key Features

- ✅ **FDA-Verified Information** - All data sourced from official FDA labels (April 2024)
- 🔬 **Evidence-Based** - Backed by landmark clinical trials (PARADIGM-HF, PARAGON-HF, PIONEER-HF)
- 📊 **Interactive Dose Calculator** - Smart dosing recommendations based on patient characteristics
- 💊 **Comprehensive Drug Interactions** - Complete interaction database with clinical evidence
- 🎨 **Modern UI/UX** - Beautiful, responsive design with intuitive navigation
- 📱 **Mobile-Friendly** - Optimized for all devices

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download this repository**

```bash
git clone <your-repo-url>
cd entresto-app
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
streamlit run entresto_app.py
```

4. **Access the app**

Open your browser and navigate to: `http://localhost:8501`

---

## 📋 Application Sections

### 1. 📖 Overview
- Indications for adults and pediatrics
- Available strengths and formulations
- Key advantages over traditional therapies
- Clinical evidence summary

### 2. ⚗️ Mechanism of Action
- Dual mechanism explanation (Neprilysin Inhibitor + ARB)
- Sacubitril pharmacology
- Valsartan pharmacology
- Synergistic benefits

### 3. 💊 Dosage & Administration
- Adult dosing guidelines
- Pediatric dosing (weight-based)
- Dose adjustments for special populations
- **CRITICAL: 36-hour ACE inhibitor washout requirement**

### 4. ⚖️ Pharmacokinetics
- Absorption, distribution, metabolism, excretion
- **Key Point: Minimal CYP450 involvement**
- Drug transporter interactions
- Clinical implications

### 5. 🚫 Contraindications & Warnings
- Absolute contraindications (ACEi, Aliskiren)
- **FDA Black Box Warning: Fetal Toxicity**
- Angioedema risk (higher in Black patients)
- Hypotension, renal impairment, hyperkalemia warnings

### 6. 💊⚖️ Drug Interactions
- **Contraindicated:** ACE inhibitors, Aliskiren (diabetes)
- **Monitor Closely:** K-sparing diuretics, NSAIDs, Lithium
- **Safe Combinations:** Digoxin, Warfarin, Statins, Amlodipine, etc.
- Evidence-based interaction analysis

### 7. 📊 Clinical Trials
- **PARADIGM-HF** (landmark trial): 20% reduction in CV death/HF hospitalization
- PARAGON-HF, PIONEER-HF, PANORAMA-HF
- Guideline recommendations (AHA/ACC, ESC)

### 8. 🧮 Dose Calculator
- Interactive patient assessment tool
- Automatic starting dose calculation
- Titration schedule generation
- Washout period checker
- Monitoring parameter recommendations

---

## 🎨 Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/800x400/667eea/ffffff?text=ENTRESTO+Main+Interface)

### Dose Calculator
![Dose Calculator](https://via.placeholder.com/800x400/22c55e/ffffff?text=Interactive+Dose+Calculator)

### Drug Interactions
![Drug Interactions](https://via.placeholder.com/800x400/ef4444/ffffff?text=Drug+Interactions+Database)

---

## 📊 Data Sources

All information in this application is sourced from:

- 📄 [FDA Official Label (April 2024)](https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/207620s025,218591s000lbl.pdf)
- 🔬 [PARADIGM-HF Trial - NEJM 2014](https://www.nejm.org/doi/full/10.1056/NEJMoa1409077)
- 📚 [PARAGON-HF Trial - NEJM 2019](https://www.nejm.org/doi/full/10.1056/NEJMoa1908363)
- 🏥 [AHA/ACC Heart Failure Guidelines](https://www.ahajournals.org/doi/10.1161/CIR.0000000000000509)
- 🇪🇺 [ESC Heart Failure Guidelines](https://www.escardio.org/Guidelines)
- 📖 [StatPearls - NCBI](https://www.ncbi.nlm.nih.gov/books/NBK507904/)

---

## 🛠️ Technical Details

### Built With

- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Python 3.8+** - Core programming language

### Project Structure

```
entresto-app/
│
├── entresto_app.py              # Main Streamlit application
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── Entresto_Pre_Pharmacode_V2.md  # Complete drug reference document
```

### Key Technical Features

- 🎨 Custom CSS styling for professional appearance
- 📱 Responsive design for mobile/tablet/desktop
- 🧮 Interactive calculators with real-time validation
- 📊 Dynamic data tables with pandas
- 🎯 Modular tab-based navigation
- ⚡ Fast loading and performance optimization

---

## 📈 Key Statistics

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~1,200 |
| **Information Sections** | 8 major tabs |
| **Drug Interactions** | 15+ documented |
| **Clinical Trials** | 4 major studies |
| **FDA Approval Year** | 2015 |
| **Last Updated** | February 2026 |

---

## 🎯 Clinical Highlights

### Why ENTRESTO?

✅ **Superior Efficacy**
- 20% reduction in cardiovascular death vs. enalapril
- 21% reduction in heart failure hospitalization
- 16% reduction in all-cause mortality

✅ **Safety Profile**
- Less cough than ACE inhibitors (9% vs 13%)
- Minimal CYP450 metabolism → Low drug interaction risk
- Well-tolerated in elderly and renal impairment

✅ **Evidence-Based**
- 8,442 patients in PARADIGM-HF
- Endorsed by AHA/ACC and ESC guidelines
- Class I recommendation (highest level)

---

## ⚠️ Important Safety Information

### Critical Warnings

🚨 **BLACK BOX WARNING: FETAL TOXICITY**
- Discontinue immediately when pregnancy is detected
- Can cause injury and death to developing fetus

🚨 **36-HOUR WASHOUT FROM ACE INHIBITORS**
- MUST wait minimum 36 hours between last ACEi dose and first ENTRESTO dose
- Concurrent use increases risk of life-threatening angioedema

🚨 **CONTRAINDICATED WITH:**
- ACE inhibitors
- Aliskiren (in patients with diabetes)
- History of angioedema related to previous ACEi/ARB therapy

---

## 🔐 Disclaimer

**⚠️ IMPORTANT MEDICAL DISCLAIMER**

This application is for **informational and educational purposes only**. It does not:
- Replace professional medical advice, diagnosis, or treatment
- Constitute a doctor-patient relationship
- Provide medical recommendations for individual patients

**Always consult with qualified healthcare professionals** for:
- Medical decisions and treatment plans
- Drug prescribing and dosing decisions
- Patient-specific clinical questions

All drug information is sourced from official FDA labels and peer-reviewed clinical trials. However, medical knowledge evolves continuously. Healthcare professionals should always refer to the most current prescribing information and clinical guidelines.

---

## 📝 Version History

### Version 1.0.0 (2026-02-13)
- ✨ Initial release
- 📊 Complete drug information database
- 🧮 Interactive dose calculator
- 💊 Comprehensive drug interaction checker
- 🎨 Modern, responsive UI

---

## 🤝 Contributing

This application follows the **Pre-Pharmacode V2.0** standard for pharmaceutical information systems.

### Standards Compliance

- ✅ FDA-verified data sources only
- ✅ Evidence-based clinical information
- ✅ Comprehensive drug interaction analysis
- ✅ Professional-grade presentation
- ✅ Regular updates from official sources

---

## 📞 Support

For questions or issues:
- 📧 Email: [your-email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/your-username/entresto-app/issues)
- 📖 Documentation: See `Entresto_Pre_Pharmacode_V2.md`

---

## 📜 License

This project is created for educational and informational purposes. 

**Data Sources:** All drug information is sourced from publicly available FDA documents and peer-reviewed medical literature.

**Trademarks:** ENTRESTO® is a registered trademark of Novartis Pharmaceuticals Corporation.

---

## 🙏 Acknowledgments

- **Novartis Pharmaceuticals** - For developing ENTRESTO
- **FDA** - For comprehensive drug labeling
- **PARADIGM-HF Investigators** - For landmark clinical trial
- **Streamlit** - For excellent web framework
- **Pre-Pharmacode V2.0** - For standardization methodology

---

## 🌟 Star This Repository

If you find this application useful, please consider giving it a star ⭐ on GitHub!

---

<div align="center">

**Made with ❤️ for Healthcare Professionals**

*Evidence-Based Medicine | Patient Safety First*

</div>
