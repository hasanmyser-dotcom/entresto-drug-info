"""
ENTRESTO (Sacubitril/Valsartan) - Professional Drug Information App
Pre-Pharmacode V2.0 Standard
FDA-verified | Evidence-based | Updated 2026-02-13
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="ENTRESTO (Sacubitril/Valsartan) Info",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #475569;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #f0f9ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fef2f2;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #ef4444;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #f0fdf4;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #22c55e;
        margin: 1rem 0;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 24px;
        background-color: #f1f5f9;
        border-radius: 8px 8px 0 0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
st.markdown('<h1 class="main-header">💊 ENTRESTO (Sacubitril/Valsartan)</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">✅ FDA-verified • 🔬 Evidence-based • 📅 Updated February 2026</p>', unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/heart-with-pulse.png", width=80)
    st.title("🏥 Quick Navigation")
    
    st.markdown("### 📋 Drug Information")
    st.info("**Generic Name**: Sacubitril/Valsartan\n\n**Brand Name**: ENTRESTO®\n\n**Manufacturer**: Novartis\n\n**FDA Approval**: 2015")
    
    st.markdown("### 🎯 Key Features")
    st.success("✅ Dual Mechanism (Neprilysin Inhibitor + ARB)\n\n✅ 20% Reduction in CV Death\n\n✅ 21% Reduction in HF Hospitalization")
    
    st.markdown("### ⚠️ Critical Warnings")
    st.error("🚨 36-hour washout from ACE inhibitors\n\n❌ Contraindicated with ACEi\n\n⚠️ Risk of Angioedema (0.5%)")
    
    st.markdown("---")
    st.caption("**Last Updated**: 2026-02-13\n\n**Version**: 1.0.0\n\n**Data Source**: FDA Label 2024")

# ==================== MAIN TABS ====================
tabs = st.tabs([
    "📖 Overview",
    "⚗️ Mechanism",
    "💊 Dosage",
    "⚖️ Pharmacokinetics",
    "🚫 Contraindications",
    "💊⚖️ Drug Interactions",
    "📊 Clinical Trials",
    "🧮 Dose Calculator"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.header("📖 Overview of ENTRESTO")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Indications")
        st.markdown("""
        <div class="info-box">
        <h4>👨‍⚕️ Adults:</h4>
        <ul>
            <li>Reduce risk of cardiovascular death and heart failure hospitalization</li>
            <li>Chronic heart failure with reduced ejection fraction (HFrEF)</li>
            <li>Benefits most evident when LVEF is below normal</li>
        </ul>
        
        <h4>👶 Pediatrics (≥1 year):</h4>
        <ul>
            <li>Symptomatic heart failure with systemic LV systolic dysfunction</li>
            <li>Reduces NT-proBNP and improves cardiovascular outcomes</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📦 Available Strengths")
        strengths_df = pd.DataFrame({
            "Strength (mg)": ["24/26", "49/51", "97/103"],
            "Color": ["Violet white", "Pale yellow", "Light pink"],
            "Marking": ["NVR/LZ", "NVR/L1", "NVR/L11"]
        })
        st.dataframe(strengths_df, use_container_width=True)
    
    with col2:
        st.markdown("### 🏆 Key Advantages")
        st.markdown("""
        <div class="success-box">
        <h4>✅ Superior Efficacy:</h4>
        <ul>
            <li>⬇️ 20% reduction in cardiovascular death vs. enalapril</li>
            <li>⬇️ 21% reduction in HF hospitalization</li>
            <li>⬇️ 16% reduction in all-cause mortality</li>
        </ul>
        
        <h4>✅ Safety Profile:</h4>
        <ul>
            <li>Less cough than ACE inhibitors (9% vs. 13%)</li>
            <li>Minimal CYP450 metabolism → Low drug interaction risk</li>
            <li>Well-tolerated in elderly and renal impairment</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📊 Clinical Evidence")
        st.info("""
        **PARADIGM-HF Trial** (NEJM 2014)
        - 8,442 patients with HFrEF
        - Median follow-up: 27 months
        - Primary endpoint: CV death or HF hospitalization
        - Result: HR 0.80 (95% CI 0.73-0.87, P<0.001)
        """)

# ==================== TAB 2: MECHANISM ====================
with tabs[1]:
    st.header("⚗️ Mechanism of Action")
    
    st.markdown("""
    <div class="info-box">
    <h3 style="color: #1e3a8a;">🔬 Dual Complementary Pathways</h3>
    <p>ENTRESTO combines two components that target distinct but complementary mechanisms in heart failure:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1️⃣ Sacubitril (Neprilysin Inhibitor)")
        st.markdown("""
        <div class="success-box">
        <h4>🎯 Target: Neprilysin Enzyme</h4>
        
        <h5>Mechanism:</h5>
        <ul>
            <li>Inhibits neprilysin enzyme that degrades natriuretic peptides</li>
            <li>Increases levels of ANP, BNP, and CNP</li>
            <li>Prodrug → Active metabolite LBQ657</li>
        </ul>
        
        <h5>Effects:</h5>
        <ul>
            <li>✅ Vasodilation (arterial & venous)</li>
            <li>✅ Increased sodium and water excretion</li>
            <li>✅ Reduced cardiac remodeling</li>
            <li>✅ Decreased preload and afterload</li>
            <li>✅ Improved myocardial relaxation</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 2️⃣ Valsartan (ARB)")
        st.markdown("""
        <div class="success-box">
        <h4>🎯 Target: Angiotensin II Type 1 Receptor</h4>
        
        <h5>Mechanism:</h5>
        <ul>
            <li>Blocks AT1 receptors</li>
            <li>Prevents harmful effects of RAAS activation</li>
            <li>Counteracts neprilysin's breakdown of angiotensin II</li>
        </ul>
        
        <h5>Effects:</h5>
        <ul>
            <li>✅ Vasodilation</li>
            <li>✅ Reduced aldosterone secretion</li>
            <li>✅ Decreased sodium retention</li>
            <li>✅ Lower blood pressure</li>
            <li>✅ Cardio-renal protection</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <div class="info-box">
    <h3 style="color: #1e3a8a;">🔑 Synergistic Benefit</h3>
    <p style="font-size: 1.1rem;">
    By combining neprilysin inhibition with RAAS blockade, ENTRESTO provides more comprehensive 
    neurohormonal modulation than ACE inhibitors or ARBs alone. This dual action addresses both 
    the natriuretic peptide deficiency and the RAAS overactivation that characterize heart failure.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: DOSAGE ====================
with tabs[2]:
    st.header("💊 Dosage & Administration")
    
    st.markdown("### 👨‍⚕️ Adults with Heart Failure")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        dosing_df = pd.DataFrame({
            "Phase": ["Starting Dose", "Target Dose", "Titration"],
            "Dose": ["49/51 mg twice daily", "97/103 mg twice daily", "Double every 2-4 weeks"],
            "Notes": ["For most patients", "Maintenance goal", "As tolerated"]
        })
        st.dataframe(dosing_df, use_container_width=True)
    
    with col2:
        st.metric("Daily Frequency", "2x", "Twice daily")
        st.metric("With Food?", "Optional", "No restriction")
    
    st.markdown("---")
    st.markdown("### ⚠️ Dose Adjustments for Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="warning-box">
        <h4>🔻 Start at HALF Dose (24/26 mg BID) if:</h4>
        <ul>
            <li>❌ Not currently on ACEi/ARB</li>
            <li>❌ Previously on LOW doses of ACEi/ARB</li>
            <li>🩺 Severe renal impairment (eGFR < 30 mL/min/1.73m²)</li>
            <li>🔬 Moderate hepatic impairment (Child-Pugh B)</li>
        </ul>
        <p><strong>Then titrate up every 2-4 weeks as tolerated</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
        <h4>✅ No Dose Adjustment Needed:</h4>
        <ul>
            <li>👴 Elderly (≥65 years)</li>
            <li>🩺 Mild renal impairment (eGFR 60-90)</li>
            <li>🩺 Moderate renal impairment (eGFR 30-60)</li>
            <li>🔬 Mild hepatic impairment (Child-Pugh A)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚨 CRITICAL: ACE Inhibitor Washout Period")
    
    st.markdown("""
    <div class="warning-box">
    <h3 style="color: #dc2626;">⏰ 36-HOUR WASHOUT REQUIRED</h3>
    <p style="font-size: 1.2rem; font-weight: 600;">
    When switching from an ACE inhibitor to ENTRESTO, you MUST wait at least 36 hours 
    between the last ACEi dose and the first ENTRESTO dose.
    </p>
    
    <h4>Why?</h4>
    <ul>
        <li>⚠️ Concurrent use increases risk of angioedema</li>
        <li>⚠️ Both drugs affect bradykinin metabolism</li>
        <li>⚠️ FDA BLACK BOX WARNING - contraindicated together</li>
    </ul>
    
    <h4>Example Timeline:</h4>
    <ol>
        <li>📅 Day 1, 8 AM: Last dose of enalapril</li>
        <li>⏳ Wait minimum 36 hours...</li>
        <li>📅 Day 2, 8 PM or later: First dose of ENTRESTO (49/51 mg)</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 👶 Pediatric Dosing (≥1 year)")
    
    st.info("""
    **Weight-Based Dosing:**
    - Starting: 1.6 mg/kg twice daily
    - Second step: 2.3 mg/kg twice daily
    - Final: 3.1 mg/kg twice daily
    - Titrate every 2 weeks as tolerated
    
    **Available pediatric formulations:**
    - ENTRESTO SPRINKLE capsules: 6/6 mg, 15/16 mg
    - Can open capsules and sprinkle on soft food
    """)

# ==================== TAB 4: PHARMACOKINETICS ====================
with tabs[3]:
    st.header("⚖️ Pharmacokinetics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔬 Absorption & Distribution")
        pk_absorption = pd.DataFrame({
            "Parameter": ["Bioavailability", "Tmax", "Protein Binding", "Volume of Distribution"],
            "Sacubitril": ["≥60%", "0.5 hours", "94-97%", "103 L"],
            "LBQ657 (active)": ["-", "2 hours", "94-97%", "-"],
            "Valsartan": ["Higher than other formulations", "1.5 hours", "94-97%", "75 L"]
        })
        st.dataframe(pk_absorption, use_container_width=True)
        
        st.info("""
        **💡 Important Note:**
        - Valsartan in ENTRESTO has higher bioavailability than other valsartan tablets
        - 26 mg in ENTRESTO ≈ 40 mg in other formulations
        - 51 mg in ENTRESTO ≈ 80 mg in other formulations
        - 103 mg in ENTRESTO ≈ 160 mg in other formulations
        """)
        
        st.markdown("### 💊 Metabolism")
        st.markdown("""
        <div class="success-box">
        <h4>🔑 Key Point: MINIMAL CYP450 INVOLVEMENT</h4>
        
        <p><strong>Sacubitril:</strong></p>
        <ul>
            <li>Rapidly converted to LBQ657 by <strong>esterases</strong> (NOT CYP450)</li>
            <li>LBQ657 is not significantly metabolized further</li>
        </ul>
        
        <p><strong>Valsartan:</strong></p>
        <ul>
            <li>Minimal metabolism (~20% to metabolites)</li>
            <li>NOT substrate for CYP450 enzymes</li>
        </ul>
        
        <p style="color: #16a34a; font-weight: 600; font-size: 1.1rem;">
        ✅ Result: LOW RISK of CYP450-mediated drug interactions
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🚪 Excretion")
        pk_excretion = pd.DataFrame({
            "Component": ["Sacubitril/LBQ657", "Valsartan"],
            "Urine": ["52-68%", "~13%"],
            "Feces": ["37-48%", "~86%"],
            "Half-life (T½)": ["Sacubitril: 1.4h\nLBQ657: 11.5h", "9.9h"]
        })
        st.dataframe(pk_excretion, use_container_width=True)
        
        st.markdown("### 📊 Steady State")
        st.info("""
        **Time to Steady State:** 2-3 days
        
        **Accumulation:**
        - Sacubitril & Valsartan: No significant accumulation
        - LBQ657: Accumulates 1.6-fold (expected for its longer half-life)
        """)
        
        st.markdown("### 🧬 Drug Transporters")
        st.warning("""
        **OATP1B1/OATP1B3 Inhibition:**
        - Sacubitril inhibits these hepatic uptake transporters
        - May increase exposure to drugs transported by OATP
        - However, clinical interaction studies showed NO significant effects with statins
        """)
    
    st.markdown("---")
    st.markdown("### 🎯 Clinical Implications")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h4>🔄 Food Effect</h4>
        <p style="font-size: 1.5rem; color: #22c55e;">✅</p>
        <p>No clinically significant effect</p>
        <p><small>Can take with or without food</small></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h4>💊 Drug Interactions</h4>
        <p style="font-size: 1.5rem; color: #22c55e;">LOW</p>
        <p>Minimal CYP450 involvement</p>
        <p><small>Most drugs safe to combine</small></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
        <h4>🩺 Renal Clearance</h4>
        <p style="font-size: 1.5rem; color: #f59e0b;">MODERATE</p>
        <p>52-68% renal excretion</p>
        <p><small>Dose adjust if eGFR<30</small></p>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 5: CONTRAINDICATIONS ====================
with tabs[4]:
    st.header("🚫 Contraindications & Warnings")
    
    st.markdown("### ❌ ABSOLUTE CONTRAINDICATIONS")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="warning-box">
        <h4 style="color: #dc2626;">🛑 DO NOT USE if patient has:</h4>
        
        <ol style="font-size: 1.05rem;">
            <li><strong>Hypersensitivity</strong> to sacubitril, valsartan, or any component</li>
            <li><strong>History of angioedema</strong> related to previous ACEi or ARB therapy</li>
            <li><strong>Concomitant ACE inhibitor use</strong>
                <ul>
                    <li>⚠️ MUST wait 36 hours after stopping ACEi</li>
                    <li>⚠️ Increased risk of angioedema</li>
                </ul>
            </li>
            <li><strong>Concomitant aliskiren in diabetes</strong>
                <ul>
                    <li>⚠️ Also avoid if eGFR < 60</li>
                    <li>⚠️ Risk of hypotension, hyperkalemia, renal dysfunction</li>
                </ul>
            </li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4 style="color: #dc2626;">⚠️ AVOID in:</h4>
        <ul style="font-size: 1.05rem;">
            <li>Concomitant use with other ARBs (ENTRESTO contains valsartan)</li>
            <li>Hereditary angioedema</li>
            <li>Severe hepatic impairment (Child-Pugh C)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚨 FDA BLACK BOX WARNING")
    
    st.markdown("""
    <div class="warning-box" style="border-left: 5px solid #7f1d1d;">
    <h3 style="color: #7f1d1d;">⚠️ FETAL TOXICITY</h3>
    
    <p style="font-size: 1.15rem; font-weight: 600;">
    When pregnancy is detected, discontinue ENTRESTO as soon as possible.
    </p>
    
    <h4>Risks:</h4>
    <ul>
        <li>💀 Fetal and neonatal injury and death</li>
        <li>🩺 Reduced fetal renal function → oliguria, anuria, renal failure</li>
        <li>🫁 Fetal lung hypoplasia</li>
        <li>🦴 Skeletal deformations, skull hypoplasia</li>
        <li>⬇️ Hypotension, oligohydramnios</li>
    </ul>
    
    <p style="color: #7f1d1d; font-weight: 600;">
    ❌ Pregnancy Category: D (Positive evidence of fetal risk)
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ⚠️ WARNINGS & PRECAUTIONS")
    
    warnings_data = {
        "Warning": [
            "1️⃣ Angioedema",
            "2️⃣ Hypotension",
            "3️⃣ Impaired Renal Function",
            "4️⃣ Hyperkalemia"
        ],
        "Incidence": [
            "0.5% (2.4% in Black patients)",
            "18% (vs 12% with enalapril)",
            "Cr increase >50% in ~16%",
            "K+ >5.5 mEq/L in ~12%"
        ],
        "Management": [
            "D/C immediately, supportive care, monitor airway. DO NOT rechallenge.",
            "Correct volume depletion first. Start lower dose. Monitor BP. Adjust diuretics.",
            "Monitor Cr regularly. Down-titrate if significant decrease. Careful in renal artery stenosis.",
            "Monitor K+ periodically. Reduce/interrupt dose if needed. Careful with K-sparing diuretics."
        ],
        "High Risk Groups": [
            "• History of angioedema\n• Black patients\n• ACEi-related angioedema",
            "• Volume/salt depletion\n• High-dose diuretics\n• Activated RAAS",
            "• Severe CHF\n• Renal artery stenosis\n• Pre-existing renal disease",
            "• Severe renal impairment\n• Diabetes\n• K-sparing diuretics\n• K supplements"
        ]
    }
    
    warnings_df = pd.DataFrame(warnings_data)
    st.dataframe(warnings_df, use_container_width=True, height=400)
    
    st.markdown("---")
    st.markdown("### 🤰 Pregnancy & Lactation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="warning-box">
        <h4>🤰 Pregnancy</h4>
        <ul>
            <li><strong>Category D</strong>: Positive evidence of fetal risk</li>
            <li>❌ <strong>Discontinue immediately</strong> when pregnancy detected</li>
            <li>Monitor fetus with serial ultrasound</li>
            <li>Prepare for potential oliguria, hypotension, hyperkalemia in neonate</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4>🤱 Lactation</h4>
        <ul>
            <li>Unknown if sacubitril/valsartan present in human milk</li>
            <li>Present in rat milk (animal studies)</li>
            <li>❌ <strong>Breastfeeding NOT recommended</strong> during treatment</li>
            <li>Consider risk-benefit of drug vs. breastfeeding benefits</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 6: DRUG INTERACTIONS ====================
with tabs[5]:
    st.header("💊⚖️ Drug Interactions")
    
    st.markdown("### 🔴 CONTRAINDICATED (Absolute - DO NOT USE)")
    
    contraindicated_data = {
        "Drug Class": [
            "ACE Inhibitors",
            "Aliskiren (in diabetes)"
        ],
        "Examples": [
            "Enalapril, Lisinopril, Ramipril, Perindopril, Captopril",
            "Tekturna"
        ],
        "Mechanism": [
            "Both affect bradykinin metabolism → Increased angioedema risk",
            "Dual RAAS blockade"
        ],
        "Risks": [
            "🚨 ANGIOEDEMA (can be life-threatening)",
            "⬇️ Hypotension, ⬆️ Hyperkalemia, 🩺 Renal dysfunction"
        ],
        "Action Required": [
            "⏰ 36-HOUR WASHOUT mandatory between ACEi stop and ENTRESTO start",
            "❌ Contraindicated in diabetes. Avoid if eGFR<60"
        ],
        "Evidence": [
            "FDA Label Section 4 & 7.1 | BLACK BOX WARNING",
            "FDA Label Section 4 & 7.1"
        ]
    }
    
    st.dataframe(pd.DataFrame(contraindicated_data), use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🟡 AVOID (Strong Recommendation)")
    
    avoid_data = {
        "Drug Class": ["Other ARBs"],
        "Examples": ["Losartan, Irbesartan, Candesartan, Telmisartan, Olmesartan"],
        "Reason": ["ENTRESTO already contains Valsartan (an ARB)"],
        "Risk": ["Dual ARB therapy = Increased adverse effects without added benefit"],
        "Evidence": ["FDA Label Section 7.1"]
    }
    
    st.dataframe(pd.DataFrame(avoid_data), use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🟠 MONITOR CLOSELY (Requires Monitoring)")
    
    # Create tabs for different interaction categories
    interaction_tabs = st.tabs([
        "K-Sparing Diuretics",
        "NSAIDs",
        "Lithium",
        "Potassium Supplements"
    ])
    
    with interaction_tabs[0]:
        st.markdown("""
        <div class="warning-box">
        <h4>💊 Potassium-Sparing Diuretics</h4>
        
        <p><strong>Examples:</strong></p>
        <ul>
            <li>Spironolactone (Aldactone)</li>
            <li>Eplerenone (Inspra)</li>
            <li>Triamterene</li>
            <li>Amiloride</li>
        </ul>
        
        <p><strong>Mechanism:</strong></p>
        <ul>
            <li>Both ENTRESTO and K-sparing diuretics increase serum potassium</li>
            <li>Additive hyperkalemic effect</li>
        </ul>
        
        <p><strong>Risk:</strong> ⚠️ Hyperkalemia</p>
        
        <p><strong>Management:</strong></p>
        <ul>
            <li>✅ Monitor serum potassium regularly (every 2-4 weeks initially)</li>
            <li>✅ Adjust doses based on K+ levels</li>
            <li>✅ Target K+ 4.0-5.0 mEq/L</li>
            <li>⚠️ Consider dose reduction if K+ >5.5 mEq/L</li>
        </ul>
        
        <p><strong>Evidence:</strong> FDA Label Section 7.2</p>
        </div>
        """, unsafe_allow_html=True)
    
    with interaction_tabs[1]:
        st.markdown("""
        <div class="warning-box">
        <h4>💊 NSAIDs (Including COX-2 Inhibitors)</h4>
        
        <p><strong>Examples:</strong></p>
        <ul>
            <li>Ibuprofen (Advil, Motrin)</li>
            <li>Naproxen (Aleve)</li>
            <li>Celecoxib (Celebrex)</li>
            <li>Diclofenac</li>
            <li>Indomethacin</li>
        </ul>
        
        <p><strong>Mechanism:</strong></p>
        <ul>
            <li>NSAIDs oppose vasodilation effects of ENTRESTO</li>
            <li>Reduce renal prostaglandin synthesis</li>
            <li>Decrease glomerular filtration</li>
        </ul>
        
        <p><strong>Risks:</strong></p>
        <ul>
            <li>🩺 Worsening renal function</li>
            <li>⚠️ Acute renal failure (especially in elderly, volume-depleted, compromised renal function)</li>
            <li>Usually reversible upon discontinuation</li>
        </ul>
        
        <p><strong>Management:</strong></p>
        <ul>
            <li>✅ Monitor renal function periodically (Cr, eGFR)</li>
            <li>✅ Avoid prolonged NSAID use</li>
            <li>✅ Use lowest effective NSAID dose for shortest duration</li>
            <li>💡 Consider acetaminophen (Tylenol) as alternative for pain</li>
        </ul>
        
        <p><strong>Evidence:</strong> FDA Label Section 7.3</p>
        </div>
        """, unsafe_allow_html=True)
    
    with interaction_tabs[2]:
        st.markdown("""
        <div class="warning-box">
        <h4>💊 Lithium</h4>
        
        <p><strong>Drug:</strong> Lithium Carbonate, Lithobid</p>
        
        <p><strong>Mechanism:</strong></p>
        <ul>
            <li>ARBs (valsartan) reduce renal lithium clearance</li>
            <li>Increased serum lithium levels</li>
        </ul>
        
        <p><strong>Risk:</strong> ⚠️ Lithium Toxicity</p>
        
        <p><strong>Symptoms of Lithium Toxicity:</strong></p>
        <ul>
            <li>Tremor, muscle weakness</li>
            <li>Nausea, vomiting, diarrhea</li>
            <li>Confusion, drowsiness</li>
            <li>Cardiac arrhythmias</li>
            <li>Seizures (severe cases)</li>
        </ul>
        
        <p><strong>Management:</strong></p>
        <ul>
            <li>✅ Monitor serum lithium levels regularly</li>
            <li>✅ Check levels more frequently when initiating or changing ENTRESTO dose</li>
            <li>✅ Target therapeutic lithium range: 0.6-1.2 mEq/L</li>
            <li>⚠️ Reduce lithium dose if levels elevated</li>
        </ul>
        
        <p><strong>Evidence:</strong> FDA Label Section 7.4</p>
        </div>
        """, unsafe_allow_html=True)
    
    with interaction_tabs[3]:
        st.markdown("""
        <div class="warning-box">
        <h4>💊 Potassium Supplements & Salt Substitutes</h4>
        
        <p><strong>Examples:</strong></p>
        <ul>
            <li>K-Dur, Klor-Con, Micro-K</li>
            <li>Salt substitutes containing potassium (e.g., Nu-Salt, Morton Salt Substitute)</li>
            <li>High-potassium diet</li>
        </ul>
        
        <p><strong>Mechanism:</strong></p>
        <ul>
            <li>ENTRESTO increases potassium (blocks aldosterone via RAAS)</li>
            <li>K supplements add more potassium</li>
            <li>Additive effect</li>
        </ul>
        
        <p><strong>Risk:</strong> ⚠️ Hyperkalemia</p>
        
        <p><strong>Management:</strong></p>
        <ul>
            <li>✅ Monitor serum potassium regularly</li>
            <li>✅ Avoid routine K supplementation unless clearly indicated</li>
            <li>✅ Educate patients about salt substitutes containing K+</li>
            <li>✅ Target K+ 4.0-5.0 mEq/L</li>
        </ul>
        
        <p><strong>Evidence:</strong> FDA Label Section 7.2</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ✅ NO CLINICALLY SIGNIFICANT INTERACTIONS")
    
    st.markdown("""
    <div class="success-box">
    <h4>✅ Safe to Use Without Dose Adjustment</h4>
    <p>Dedicated FDA drug interaction studies showed NO clinically meaningful interactions with:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **💊 Cardiovascular:**
        - ✅ Digoxin (Lanoxin)
        - ✅ Warfarin (Coumadin)
        - ✅ Carvedilol (Coreg)
        - ✅ Amlodipine (Norvasc)
        - ✅ Sildenafil (Viagra)
        """)
    
    with col2:
        st.markdown("""
        **💧 Diuretics:**
        - ✅ Furosemide (Lasix)
        - ✅ Hydrochlorothiazide (HCTZ)
        """)
        
        st.markdown("""
        **💊 GI/Metabolic:**
        - ✅ Omeprazole (Prilosec)
        - ✅ Metformin (Glucophage)
        """)
    
    with col3:
        st.markdown("""
        **💊 Lipid-Lowering:**
        - ✅ Atorvastatin (Lipitor)
        - ✅ Other statins
        """)
    
    st.info("**Evidence:** FDA Label Section 12.3 - Dedicated Drug Interaction Studies")
    
    st.markdown("---")
    st.markdown("### 🔬 Why So Few Interactions?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>✅ Minimal CYP450 Involvement</h4>
        <ul>
            <li>Sacubitril: Metabolized by <strong>esterases</strong> (NOT CYP450)</li>
            <li>Valsartan: Minimal metabolism (~20%)</li>
            <li><strong>Result:</strong> Low risk of CYP450-mediated interactions</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
        <h4>🔬 No CYP450 Inhibition or Induction</h4>
        <ul>
            <li>ENTRESTO does NOT inhibit CYP450 enzymes</li>
            <li>ENTRESTO does NOT induce CYP450 enzymes</li>
            <li><strong>Result:</strong> Won't affect metabolism of other drugs</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 7: CLINICAL TRIALS ====================
with tabs[6]:
    st.header("📊 Clinical Trials & Evidence")
    
    st.markdown("### 🏆 PARADIGM-HF (Landmark Trial)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h4>📋 Study Design</h4>
        <ul>
            <li><strong>Design:</strong> Randomized, double-blind, active-controlled</li>
            <li><strong>Comparator:</strong> Enalapril 10 mg twice daily</li>
            <li><strong>Population:</strong> 8,442 patients with chronic HFrEF</li>
            <li><strong>LVEF:</strong> ≤40% (later amended to ≤35%)</li>
            <li><strong>Follow-up:</strong> Median 27 months (up to 4.3 years)</li>
            <li><strong>Run-in period:</strong> Sequential enalapril (15 days) + ENTRESTO (29 days)</li>
            <li><strong>Publication:</strong> NEJM 2014</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
        <h4>🎯 Primary Endpoint</h4>
        <p style="font-size: 1.3rem; font-weight: 600; color: #16a34a;">
        Composite of CV death or HF hospitalization
        </p>
        
        <p style="font-size: 2rem; font-weight: 700; color: #16a34a; text-align: center;">
        ⬇️ 20%
        </p>
        
        <p style="text-align: center;">
        HR 0.80<br>
        (95% CI 0.73-0.87)<br>
        P < 0.001
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 Key Results")
    
    results_data = {
        "Endpoint": [
            "Primary: CV death or HF hospitalization",
            "CV death",
            "HF hospitalization",
            "All-cause mortality",
            "Sudden cardiac death"
        ],
        "ENTRESTO": ["21.8%", "13.3%", "12.8%", "17.0%", "10.0%"],
        "Enalapril": ["26.5%", "16.5%", "15.6%", "19.8%", "12.5%"],
        "Hazard Ratio": ["0.80", "0.80", "0.79", "0.84", "0.80"],
        "Risk Reduction": ["⬇️ 20%", "⬇️ 20%", "⬇️ 21%", "⬇️ 16%", "⬇️ 20%"],
        "P-value": ["<0.001", "<0.001", "<0.001", "<0.001", "<0.001"],
        "NNT (3 years)": ["21", "32", "35", "36", "40"]
    }
    
    st.dataframe(pd.DataFrame(results_data), use_container_width=True)
    
    st.success("""
    **💡 Clinical Significance:**
    - For every 21 patients treated for 3 years, 1 CV death or HF hospitalization prevented
    - For every 32 patients treated, 1 CV death prevented
    - Trial stopped early (March 2014) due to clear superiority of ENTRESTO
    """)
    
    st.markdown("---")
    st.markdown("### 👥 Subgroup Analyses")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Consistent Benefit Across Subgroups:**
        - ✅ Age (<55, 55-65, 65-75, >75 years)
        - ✅ Sex (Male, Female)
        - ✅ Race (White, Black, Asian, Other)
        - ✅ LVEF (<30%, ≥30%)
        - ✅ Diabetes (Yes, No)
        - ✅ eGFR (<60, ≥60 mL/min/1.73m²)
        - ✅ Geographic region
        """)
    
    with col2:
        st.warning("""
        **Greater Benefit in Some Groups:**
        - 📊 LVEF <median (22%): Greater absolute benefit
        - 📊 Younger patients: Larger relative risk reduction
        - 📊 No prior HF hospitalization: Better outcomes
        
        **Note:** Benefit observed across ALL subgroups
        """)
    
    st.markdown("---")
    st.markdown("### 🔬 Other Major Trials")
    
    other_trials_tabs = st.tabs(["PARAGON-HF", "PIONEER-HF", "PANORAMA-HF"])
    
    with other_trials_tabs[0]:
        st.markdown("""
        <div class="info-box">
        <h3>PARAGON-HF (HFpEF)</h3>
        
        <p><strong>Design:</strong></p>
        <ul>
            <li>4,822 patients with HF and LVEF ≥45%</li>
            <li>Comparator: Valsartan 160 mg twice daily</li>
            <li>Median follow-up: 35 months</li>
        </ul>
        
        <p><strong>Primary Endpoint:</strong> CV death or total HF hospitalizations</p>
        
        <p><strong>Results:</strong></p>
        <ul>
            <li>HR 0.87 (95% CI 0.75-1.01, P=0.06) - Did not meet statistical significance</li>
            <li>✅ Benefit in subgroups: Women (HR 0.73), LVEF <57% (HR 0.78)</li>
            <li>✅ Improved quality of life (KCCQ score)</li>
            <li>✅ Greater NT-proBNP reduction</li>
        </ul>
        
        <p><strong>Conclusion:</strong> Modest benefit in HFpEF, particularly in women and those with lower LVEF</p>
        
        <p><strong>Reference:</strong> NEJM 2019</p>
        </div>
        """, unsafe_allow_html=True)
    
    with other_trials_tabs[1]:
        st.markdown("""
        <div class="info-box">
        <h3>PIONEER-HF (Acute HF)</h3>
        
        <p><strong>Design:</strong></p>
        <ul>
            <li>881 patients hospitalized for acute decompensated HF</li>
            <li>Hemodynamically stable, initiated in-hospital</li>
            <li>Comparator: Enalapril 10 mg twice daily</li>
            <li>Follow-up: 8 weeks</li>
        </ul>
        
        <p><strong>Primary Endpoint:</strong> Time-averaged change in NT-proBNP from baseline to 4 and 8 weeks</p>
        
        <p><strong>Results:</strong></p>
        <ul>
            <li>✅ Greater NT-proBNP reduction with ENTRESTO: -46.7% vs -25.3% (P<0.001)</li>
            <li>✅ Larger reduction maintained at 8 weeks</li>
            <li>✅ Similar safety profile (hypotension, worsening renal function)</li>
            <li>✅ No signal of early harm</li>
        </ul>
        
        <p><strong>Conclusion:</strong> Safe and effective to initiate ENTRESTO in hospitalized acute HF patients</p>
        
        <p><strong>Reference:</strong> JAMA 2019</p>
        </div>
        """, unsafe_allow_html=True)
    
    with other_trials_tabs[2]:
        st.markdown("""
        <div class="info-box">
        <h3>PANORAMA-HF (Pediatric)</h3>
        
        <p><strong>Design:</strong></p>
        <ul>
            <li>375 children (1 month to <18 years) with symptomatic HF</li>
            <li>Systemic LV systolic dysfunction</li>
            <li>Comparator: Enalapril</li>
            <li>Median follow-up: 1.9 years</li>
        </ul>
        
        <p><strong>Primary Endpoint:</strong> Change in NT-proBNP at 12 weeks</p>
        
        <p><strong>Results:</strong></p>
        <ul>
            <li>✅ Greater NT-proBNP reduction with ENTRESTO: -45.6% vs -34.0%</li>
            <li>✅ Safety profile similar to adults</li>
            <li>✅ No new safety concerns in children</li>
            <li>⚠️ Limited data in infants <1 year</li>
        </ul>
        
        <p><strong>Conclusion:</strong> Efficacy and safety comparable to enalapril in children ≥1 year</p>
        
        <p><strong>Reference:</strong> Circulation 2021</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📚 Guideline Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>🇺🇸 AHA/ACC/HFSA 2022 Guidelines</h4>
        <p style="font-size: 1.3rem; font-weight: 600; color: #16a34a;">
        Class I Recommendation
        </p>
        <ul>
            <li>✅ Recommended for patients with HFrEF to reduce morbidity and mortality</li>
            <li>✅ Preferred over ACEi or ARB</li>
            <li>✅ Level of Evidence: A (High-quality evidence)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
        <h4>🇪🇺 ESC 2021 Guidelines</h4>
        <p style="font-size: 1.3rem; font-weight: 600; color: #16a34a;">
        Class I Recommendation
        </p>
        <ul>
            <li>✅ Recommended to replace ACEi to reduce risk of HF hospitalization and death</li>
            <li>✅ In ambulatory patients with HFrEF who tolerate ACEi/ARB</li>
            <li>✅ Level of Evidence: A</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 8: DOSE CALCULATOR ====================
with tabs[7]:
    st.header("🧮 ENTRESTO Dose Calculator")
    
    st.markdown("""
    <div class="info-box">
    <h3>📋 Patient Assessment Tool</h3>
    <p>Use this calculator to determine the appropriate starting dose and titration schedule for your patient.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 👤 Patient Information")
        
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=65, step=1)
        weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=75.0, step=0.5)
        
        st.markdown("### 🩺 Clinical Factors")
        
        current_acei_arb = st.selectbox(
            "Current ACEi/ARB Status",
            ["Not taking ACEi/ARB", "On LOW dose ACEi/ARB", "On MODERATE/HIGH dose ACEi/ARB"]
        )
        
        renal_function = st.selectbox(
            "Renal Function (eGFR)",
            ["Normal or Mild Impairment (≥60 mL/min/1.73m²)",
             "Moderate Impairment (30-59 mL/min/1.73m²)",
             "Severe Impairment (<30 mL/min/1.73m²)"]
        )
        
        hepatic_function = st.selectbox(
            "Hepatic Function",
            ["Normal", "Mild (Child-Pugh A)", "Moderate (Child-Pugh B)", "Severe (Child-Pugh C)"]
        )
        
        acei_stopped_hours = st.number_input(
            "Hours since last ACEi dose (if applicable)",
            min_value=0, max_value=168, value=48, step=1,
            help="Must be ≥36 hours before starting ENTRESTO"
        )
        
        calculate_btn = st.button("🧮 Calculate Recommended Dose", type="primary", use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Quick Reference")
        
        st.info("""
        **Standard Doses:**
        - 24/26 mg BID
        - 49/51 mg BID
        - 97/103 mg BID
        
        **BID = Twice Daily**
        """)
        
        st.warning("""
        **Start at HALF dose if:**
        - Not on ACEi/ARB
        - On LOW dose ACEi/ARB
        - eGFR <30
        - Child-Pugh B
        """)
    
    if calculate_btn:
        st.markdown("---")
        st.markdown("## 📋 Recommended Dosing Plan")
        
        # Determine starting dose
        start_dose = "49/51 mg"
        start_half = False
        warnings_list = []
        
        # Check for half-dose criteria
        if current_acei_arb in ["Not taking ACEi/ARB", "On LOW dose ACEi/ARB"]:
            start_dose = "24/26 mg"
            start_half = True
            warnings_list.append("⚠️ Patient not on adequate ACEi/ARB → Start at half dose")
        
        if "Severe" in renal_function:
            start_dose = "24/26 mg"
            start_half = True
            warnings_list.append("⚠️ Severe renal impairment (eGFR<30) → Start at half dose")
        
        if hepatic_function == "Moderate (Child-Pugh B)":
            start_dose = "24/26 mg"
            start_half = True
            warnings_list.append("⚠️ Moderate hepatic impairment → Start at half dose")
        
        if hepatic_function == "Severe (Child-Pugh C)":
            st.error("""
            ### 🚫 ENTRESTO NOT RECOMMENDED
            
            **Reason:** Severe hepatic impairment (Child-Pugh C)
            
            No studies have been conducted in patients with severe hepatic impairment. 
            Use of ENTRESTO is not recommended in this population.
            """)
            st.stop()
        
        # Check ACEi washout
        if current_acei_arb == "On MODERATE/HIGH dose ACEi/ARB" or acei_stopped_hours > 0:
            if acei_stopped_hours < 36:
                st.error(f"""
                ### ⚠️ INSUFFICIENT WASHOUT PERIOD
                
                **Current:** {acei_stopped_hours} hours since last ACEi dose
                **Required:** Minimum 36 hours
                **Remaining:** {36 - acei_stopped_hours} hours
                
                ❌ **DO NOT START ENTRESTO YET**
                
                **Risk:** Increased risk of angioedema if started too soon after ACEi discontinuation.
                
                **Action:** Wait at least {36 - acei_stopped_hours} more hours before initiating ENTRESTO.
                """)
                st.stop()
            else:
                st.success(f"""
                ✅ **Adequate washout period:** {acei_stopped_hours} hours (≥36 hours required)
                
                Safe to proceed with ENTRESTO initiation.
                """)
        
        # Display recommendations
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card" style="background-color: #dbeafe;">
            <h4>🎯 Starting Dose</h4>
            <p style="font-size: 2rem; font-weight: 700; color: #1e40af;">{start_dose} mg</p>
            <p>Twice daily (BID)</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            target_dose = "97/103 mg" if age >= 18 else "Weight-based"
            st.markdown(f"""
            <div class="metric-card" style="background-color: #d1fae5;">
            <h4>🎯 Target Dose</h4>
            <p style="font-size: 2rem; font-weight: 700; color: #065f46;">{target_dose}</p>
            <p>Twice daily (BID)</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card" style="background-color: #fef3c7;">
            <h4>⏱️ Titration</h4>
            <p style="font-size: 2rem; font-weight: 700; color: #92400e;">2-4 weeks</p>
            <p>Double dose each step</p>
            </div>
            """, unsafe_allow_html=True)
        
        if warnings_list:
            st.warning("**⚠️ Dose Adjustment Reasons:**\n" + "\n".join(warnings_list))
        
        # Titration schedule
        st.markdown("### 📅 Suggested Titration Schedule")
        
        if start_dose == "24/26 mg":
            titration_schedule = pd.DataFrame({
                "Week": ["Week 0 (Start)", "Week 2-4", "Week 4-8", "Week 8+"],
                "Dose": ["24/26 mg BID", "49/51 mg BID", "97/103 mg BID", "97/103 mg BID"],
                "Action": [
                    "Initiate therapy",
                    "Double dose if tolerated",
                    "Double dose if tolerated",
                    "Continue maintenance"
                ],
                "Monitor": [
                    "BP, K+, Cr at baseline",
                    "BP, symptoms, K+, Cr",
                    "BP, symptoms, K+, Cr",
                    "Regular monitoring per standard"
                ]
            })
        else:
            titration_schedule = pd.DataFrame({
                "Week": ["Week 0 (Start)", "Week 2-4", "Week 4+"],
                "Dose": ["49/51 mg BID", "97/103 mg BID", "97/103 mg BID"],
                "Action": [
                    "Initiate therapy",
                    "Double dose if tolerated",
                    "Continue maintenance"
                ],
                "Monitor": [
                    "BP, K+, Cr at baseline",
                    "BP, symptoms, K+, Cr",
                    "Regular monitoring per standard"
                ]
            })
        
        st.dataframe(titration_schedule, use_container_width=True)
        
        st.markdown("### 🔍 Monitoring Parameters")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("""
            **Before Each Dose Increase:**
            - ✅ Blood Pressure (SBP ≥100 mmHg preferred)
            - ✅ Serum Potassium (target 4.0-5.0 mEq/L)
            - ✅ Serum Creatinine / eGFR
            - ✅ Symptom assessment
            - ✅ Signs of angioedema
            """)
        
        with col2:
            st.warning("""
            **Hold or Reduce Dose if:**
            - ⚠️ SBP <90-95 mmHg (symptomatic)
            - ⚠️ Potassium >5.5 mEq/L
            - ⚠️ Cr increase >50% or eGFR decline >30%
            - ⚠️ Worsening symptoms
            - 🚨 Any signs of angioedema → STOP immediately
            """)
        
        st.success("""
        **💡 Titration Tips:**
        - Most patients tolerate full titration to 97/103 mg BID
        - Some benefit even at lower doses if target not tolerated
        - Symptomatic hypotension may improve over time - consider observation before dose reduction
        - If dose reduction needed, can retry up-titration later when stable
        """)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 2rem 0;">
    <p style="font-size: 0.9rem;">
        <strong>ENTRESTO® Drug Information System</strong><br>
        Pre-Pharmacode V2.0 Standard | Evidence-Based Medicine<br>
        Last Updated: February 13, 2026
    </p>
    <p style="font-size: 0.8rem;">
        ⚠️ <strong>Disclaimer:</strong> This application is for informational and educational purposes only. 
        It does not replace professional medical advice, diagnosis, or treatment. 
        Always consult with qualified healthcare professionals for medical decisions.
        All drug information is sourced from official FDA labels and peer-reviewed clinical trials.
    </p>
    <p style="font-size: 0.8rem;">
        📚 <strong>Data Sources:</strong> FDA Label (April 2024), PARADIGM-HF (NEJM 2014), 
        PARAGON-HF (NEJM 2019), PIONEER-HF (JAMA 2019), PANORAMA-HF (Circulation 2021)
    </p>
    <p style="font-size: 0.8rem;">
        🏥 <strong>References:</strong> American Heart Association, European Society of Cardiology, 
        National Library of Medicine, Novartis Pharmaceuticals
    </p>
</div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR FOOTER ====================
with st.sidebar:
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; font-size: 0.75rem; color: #64748b;">
        <p><strong>App Version:</strong> 1.0.0</p>
        <p><strong>Build Date:</strong> 2026-02-13</p>
        <p><strong>Framework:</strong> Streamlit</p>
        <p><strong>Standard:</strong> Pre-Pharmacode V2.0</p>
    </div>
    """, unsafe_allow_html=True)
