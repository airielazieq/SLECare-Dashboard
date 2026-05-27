# SLECare INNOVERSE Dashboard Specification

## Goal

Build a clinician-researcher dashboard prototype for Lupus Nephritis decision-support and research review. The dashboard must help Prof. Dr. Syahrul Sazliyana Shaharir understand the cohort, assess CKD and delayed-remission risk, explain patient-specific risk, prioritize high-risk patients, review progression over time, and prepare research-ready summaries.

The dashboard contains exactly six modules:

1. Cohort Overview
2. Patient Risk Assessment
3. High-Risk Patients
4. Patient Timeline
5. Global Risk Drivers
6. Research Export

No model leaderboard, generic chatbot, treatment recommendation engine, appointment scheduler, cost calculator, authentication system, or EMR module will be built.

## Context

This is the SLECare INNOVERSE Dashboard prototype, built from the repository's existing data, CatBoost models, feature lists, and SHAP assets.

Available verified project inputs:

- Raw Excel source: `data/ANONYMOUS DATA EXCEL LN RELAPSE_UKM.xlsx`
  - `Sheet1` contains 218 rows and 75 columns.
  - Timeline-relevant fields include `DATE OF BIOPSY`, `YEAR ACTIVE LN`, `MONTH INTERVAL TO INDUCTION TX`, `CREAT BASELINE`, `CREAT 24 MONTH`, `UPCI PRE TX`, `UPCI 3 MTH`, `UPCI 6 MTH`, `UPCI 12 MTH`, `UPCI 18 MTH`, and `UPCI 24MTH`.
- CKD model-ready CSV: `data/CB_CKD_cleaned_with_target.csv`
  - Shape: 174 rows x 20 columns.
  - Target: `CKD`.
  - Feature JSON matches the CSV features.
- Remission model-ready CSV: `data/CB_Remission_cleaned_with_target.csv`
  - Shape: 174 rows x 21 columns.
  - Target: `CR_12_MTH_PRED_10`.
  - Feature JSON matches the CSV features.
- Clinical-facing models:
  - `model/catboost_ckd_model.pkl`
  - `model/catboost_remission_model.pkl`
  - Both CatBoost models load and predict locally.
- Feature lists:
  - `model/ckd_rfe_features.json`
  - `model/remission_rfe_features.json`
- Global SHAP assets:
  - `assets/ckd_barplot.png`
  - `assets/remission_barplot.png`
  - `assets/Dependence Plots/CKD_CREAT.png`
  - `assets/Dependence Plots/CKD_LA.png`
  - `assets/Dependence Plots/CKD_RACE.png`
  - `assets/Dependence Plots/Remission_CKD.png`
  - `assets/Dependence Plots/Remission_GLOBAL.png`
  - `assets/Dependence Plots/Remission_MONTH.png`
  - `assets/Dependence Plots/Remission_RACE.png`

Module definitions:

1. Cohort Overview
   - Show useful cohort statistics and charts from the available dataset.
   - Include patient or episode counts, CKD burden, delayed-remission burden, demographics, and key clinical distributions where available.

2. Patient Risk Assessment
   - Support sample patient selection and/or structured patient input.
   - Validate required model fields before prediction.
   - Use only CatBoost CKD and remission models for clinical-facing prediction.
   - Display CKD risk, delayed-remission risk, probability, risk category, key patient values, local explanation, and SHAP-payload-style drivers.
   - The LLM layer, if used, only converts structured model and SHAP output into concise clinical language.

3. High-Risk Patients
   - Rank or filter patients by CKD risk, delayed-remission risk, or combined priority.
   - Show risk category, key flagging reasons, and searchable/filterable patient rows.

4. Patient Timeline
   - Show longitudinal patient progression using available timeline fields.
   - Include biopsy/LN timing, induction-treatment interval, creatinine trend, UPCI trend, and remission/progression markers where available.
   - Use clearly isolated mock-safe fallback only where raw data is incomplete.

5. Global Risk Drivers
   - Display the available global SHAP bar plots and dependence plots.
   - Explain cohort-level risk drivers in plain clinical language.
   - Keep model details clinically relevant and avoid benchmarking content.

6. Research Export
   - Provide export-ready cohort summaries, Table 1-style summaries, outcome distributions, top predictors, SHAP findings, and concise research-support text.
   - Summaries must be based on available data and clearly label prototype or mock-safe content where applicable.

## Constraints

- Use cautious clinical decision-support wording only.
- Do not claim diagnosis, treatment recommendation, clinical approval, guaranteed cost reduction, autonomous decision-making, or real-world deployment readiness.
- Clinical-facing prediction uses CatBoost only:
  - `model/catboost_ckd_model.pkl`
  - `model/catboost_remission_model.pkl`
- Other models may exist for research validation but are not part of the dashboard workflow.
- Local SHAP or SHAP-payload-style explanation belongs in Patient Risk Assessment.
- Global SHAP images belong in Global Risk Drivers.
- Mock prediction or mock SHAP behavior is allowed only as an isolated, clearly replaceable fallback.
- The frontend stack is React, TypeScript, Vite, Tailwind CSS, Recharts, and Lucide React.
- Backend integration, if implemented, should use Python FastAPI or Flask for model loading, prediction, SHAP payload generation, explanation payloads, and cohort analytics.
- The user interface must be professional, clean, clinical, and not cluttered.
- Sidebar navigation must contain exactly the six approved modules.

## Done when

1. The app runs locally.
2. The sidebar contains exactly the six approved modules.
3. Cohort Overview uses the dataset for useful charts and statistics.
4. Patient Risk Assessment supports patient input or sample patient selection.
5. Patient Risk Assessment shows CKD and delayed-remission risk outputs.
6. Patient Risk Assessment includes local explanation or SHAP-payload-style explanation.
7. High-Risk Patients ranks or filters patients by risk.
8. Patient Timeline shows a longitudinal/progression view from available data or clear mock-safe fallback.
9. Global Risk Drivers displays the available SHAP images and dependence plots.
10. Research Export provides export-ready summaries or clearly labelled mock-safe export content.
11. Code is modular enough to replace mock services with real backend logic later.
12. No unnecessary model leaderboard or extra dashboard module is added.
