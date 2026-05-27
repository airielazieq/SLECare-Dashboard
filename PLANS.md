# SLECare INNOVERSE Dashboard Implementation Plan

## Goal

Implement the exact six-module clinician-researcher dashboard defined in `SPEC.md`, using the existing data, CatBoost models, feature JSON files, and SHAP assets. Build the prototype in the requested order: cohort understanding, patient risk assessment, high-risk prioritization, timeline review, global risk drivers, and research export.

## Context

The repository already contains the required source files and assets:

- Raw cohort Excel: `data/ANONYMOUS DATA EXCEL LN RELAPSE_UKM.xlsx`, `Sheet1`, 218 rows x 75 columns.
- CKD model-ready data: `data/CB_CKD_cleaned_with_target.csv`, 174 rows x 20 columns, target `CKD`.
- Remission model-ready data: `data/CB_Remission_cleaned_with_target.csv`, 174 rows x 21 columns, target `CR_12_MTH_PRED_10`.
- CatBoost models:
  - `model/catboost_ckd_model.pkl`
  - `model/catboost_remission_model.pkl`
- Feature JSON files:
  - `model/ckd_rfe_features.json`
  - `model/remission_rfe_features.json`
- SHAP assets:
  - `assets/ckd_barplot.png`
  - `assets/remission_barplot.png`
  - `assets/Dependence Plots/*.png`

CatBoost and SHAP can load and predict locally. The implementation should still keep fallback behavior modular for prototype resilience.

## Constraints

- Modify app code only after this plan and `SPEC.md` exist.
- Do not add modules beyond:
  1. Cohort Overview
  2. Patient Risk Assessment
  3. High-Risk Patients
  4. Patient Timeline
  5. Global Risk Drivers
  6. Research Export
- Do not add a model leaderboard, treatment recommender, generic chatbot, scheduler, cost calculator, authentication system, or EMR workflow.
- Use CatBoost only for clinical-facing CKD and delayed-remission prediction.
- Use cautious decision-support wording throughout the UI.
- The LLM, if used, must only convert structured model/SHAP payloads into concise non-technical language.
- Mock-safe logic must be clearly isolated and replaceable.
- Use React, TypeScript, Vite, Tailwind CSS, Recharts, and Lucide React for the frontend.
- Use FastAPI or Flask only if backend integration is needed.
- Protect unrelated edits in the worktree.

## Done when

1. Prepare project structure and data access.
   - Inspect the existing frontend/backend structure.
   - Add or adapt only the minimal service and component files needed for the six approved modules.
   - Define shared types for cohort rows, model-ready patient rows, risk outputs, SHAP driver payloads, timeline points, and export summaries.
   - Add data-loading utilities for the raw Excel-derived cohort view and the two model-ready CSV files.
   - Keep file paths configurable and preserve the existing data, model, and asset filenames.

2. Build the six-module shell.
   - Create a professional dashboard layout with sidebar navigation.
   - Sidebar items must be exactly:
     - Cohort Overview
     - Patient Risk Assessment
     - High-Risk Patients
     - Patient Timeline
     - Global Risk Drivers
     - Research Export
   - Add a persistent clinical decision-support disclaimer using cautious wording.
   - Verify there is no route, tab, or page for model benchmarking or unrelated workflows.

3. Implement Cohort Overview first.
   - Use the available dataset to compute useful cohort statistics.
   - Show total records, model-ready sample counts, CKD distribution, delayed-remission distribution, and available demographic or clinical distributions.
   - Add Recharts visualizations for outcome burden and selected cohort characteristics.
   - Use clear empty-state messaging if a field is absent or sparse.

4. Implement Patient Risk Assessment second.
   - Support sample patient selection from model-ready rows and/or structured patient input.
   - Validate required CKD and remission feature fields using `ckd_rfe_features.json` and `remission_rfe_features.json`.
   - Run CatBoost CKD and remission predictions through an isolated service layer.
   - Return probability, risk category, target name, model input values, and prediction timestamp.
   - Generate local SHAP values where practical; otherwise use an isolated SHAP-payload-style fallback based on available features and known clinical drivers.
   - Display top risk drivers, protective factors where available, and concise clinician-friendly explanation text.
   - Ensure explanation text does not recommend treatment.

5. Implement High-Risk Patients third.
   - Reuse the same prediction service or precomputed prototype risk outputs.
   - Rank patients by CKD risk, delayed-remission risk, and combined priority.
   - Provide filters for risk category and search over patient identifiers or available display fields.
   - Show main flagging reason from SHAP payload or deterministic driver summary.
   - Keep table columns clinically useful and avoid technical metric overload.

6. Implement Patient Timeline fourth.
   - Use raw Excel timeline fields:
     - `DATE OF BIOPSY`
     - `YEAR ACTIVE LN`
     - `MONTH INTERVAL TO INDUCTION TX`
     - `CREAT BASELINE`
     - `CREAT 24 MONTH`
     - `UPCI PRE TX`
     - `UPCI 3 MTH`
     - `UPCI 6 MTH`
     - `UPCI 12 MTH`
     - `UPCI 18 MTH`
     - `UPCI 24MTH`
   - Show biopsy/LN timing, induction-treatment interval, creatinine progression, UPCI progression, and available remission/progression markers.
   - Use Recharts for longitudinal marker trends.
   - If patient-level linking is incomplete, use a clearly labelled prototype timeline derived from the selected record.

7. Implement Global Risk Drivers fifth.
   - Display `assets/ckd_barplot.png` and `assets/remission_barplot.png`.
   - Display all available dependence plots:
     - `CKD_CREAT.png`
     - `CKD_LA.png`
     - `CKD_RACE.png`
     - `Remission_CKD.png`
     - `Remission_GLOBAL.png`
     - `Remission_MONTH.png`
     - `Remission_RACE.png`
   - Add concise plain-language interpretation of cohort-level drivers.
   - Keep the page focused on explainability, not model comparison.

8. Implement Research Export sixth.
   - Generate export-ready sections for cohort summary, Table 1-style demographics/clinical summary, outcome distribution, top predictors, and SHAP findings.
   - Add copy/download actions for CSV or text summaries where feasible.
   - Clearly label prototype-generated or mock-safe text.
   - Ensure generated research-support wording does not fabricate findings beyond the available data.

9. Add integration safeguards.
   - Centralize risk category thresholds and cautious wording.
   - Keep prediction, SHAP payload creation, explanation generation, cohort analytics, and export generation in replaceable service modules.
   - Add graceful fallback messaging for missing files, model loading errors, or incomplete timeline fields.
   - Preserve all existing filenames and do not move data, model, or asset files.

10. Verify the prototype.
   - Run install/build/test commands appropriate to the existing project.
   - Start the local app and verify all six modules render.
   - Confirm the sidebar contains exactly the approved six modules.
   - Confirm CatBoost predictions or isolated fallback outputs appear for CKD and delayed remission.
   - Confirm Patient Risk Assessment displays SHAP-payload-style explanation.
   - Confirm High-Risk Patients ranks or filters patient rows.
   - Confirm Patient Timeline shows longitudinal/progression content.
   - Confirm Global Risk Drivers renders all available SHAP images.
   - Confirm Research Export produces export-ready summary content.
   - Check desktop and mobile layouts for overflow or unreadable clinical content.
   - Confirm no model leaderboard or extra module was added.
