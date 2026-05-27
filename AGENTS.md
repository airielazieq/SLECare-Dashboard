# AGENTS.md — SLECare INNOVERSE Dashboard

## Role

You are Codex working inside the SLECare INNOVERSE Dashboard repository.

Your job is to build a comprehensive clinician-researcher dashboard prototype for Lupus Nephritis risk assessment, using the existing project files, models, dataset, and SHAP assets.

This dashboard is intended for Prof. Dr. Syahrul Sazliyana Shaharir as a clinical/research tool, not as a generic ML demo.

## Core Rule

Build what is useful to the clinician-researcher user.

Do not build features just because they are technically interesting.

The system must help the user:

1. Understand the LN cohort.
2. Assess individual patient CKD and delayed-remission risk.
3. Explain why a patient is high risk.
4. Prioritize high-risk patients.
5. Review patient timeline/progression.
6. Export research-ready summaries.

## Current Project Scope

This is an INNOVERSE dashboard prototype.

The prototype may use mock-safe logic where needed, but must be structured as if it can later become a real clinical/research dashboard.

The dashboard should use the available dataset and assets for charts, tables, SHAP visuals, and demo patient records.

## Dashboard Modules

Build these modules only:

1. Cohort Overview
2. Patient Risk Assessment
3. High-Risk Patients
4. Patient Timeline
5. Global Risk Drivers
6. Research Export

Do not add unnecessary standalone modules such as:

- Model leaderboard
- General chatbot
- Cost calculator without real cost data
- Treatment recommendation engine
- Appointment scheduler
- Login/authentication unless explicitly requested
- Full hospital EMR system

## Model Deployment Rule

The clinical-facing dashboard uses CatBoost only.

Use:

- `model/catboost_ckd_model.pkl`
- `model/catboost_remission_model.pkl`

Other models, ensembles, Random Forest, SVM, and MLP are for paper/research validation only, not for the dashboard user workflow.

Do not create a model benchmarking dashboard page unless explicitly requested.

## Prediction Flow

The intended flow is:

```text
Patient input
→ validate required fields
→ CatBoost prediction
→ local SHAP explanation
→ SHAP payload
→ LLM-generated clinician-friendly explanation
→ store/display result in prototype state or database-ready structure
```

For the prototype, if real SHAP calculation is difficult, use a clearly marked mock SHAP payload builder based on available features and existing SHAP assets. Keep the code modular so real SHAP can replace the mock later.

## SHAP Rules

Use local SHAP in Module 2: Patient Risk Assessment.

Use global SHAP in Module 5: Global Risk Drivers.

Available global SHAP assets:

- `assets/ckd_barplot.png`
- `assets/remission_barplot.png`
- `assets/Dependence Plots/CKD_CREAT.png`
- `assets/Dependence Plots/CKD_LA.png`
- `assets/Dependence Plots/CKD_RACE.png`
- `assets/Dependence Plots/Remission_CKD.png`
- `assets/Dependence Plots/Remission_GLOBAL.png`
- `assets/Dependence Plots/Remission_MONTH.png`
- `assets/Dependence Plots/Remission_RACE.png`

## LLM Rule

The LLM must not make clinical predictions.

The LLM only converts structured model/SHAP output into concise, non-technical clinical language.

Correct:

> High CKD risk is mainly driven by elevated baseline creatinine, positive LA, and chronicity index.

Incorrect:

> The patient should receive treatment X.

Never provide treatment recommendations.

## Data and File Rules

Use existing files from the repository.

Current expected files:

```text
data/
- ANONYMOUS DATA EXCEL LN RELAPSE_UKM.xlsx
- optional: CB_CKD_cleaned_with_target.csv
- optional: CB_Remission_cleaned_with_target.csv

model/
- catboost_ckd_model.pkl
- catboost_remission_model.pkl
- ckd_rfe_features.json
- remission_rfe_features.json

assets/
- ckd_barplot.png
- remission_barplot.png
- Dependence Plots/*.png
```

Do not rename or move these files unless necessary.

If a file is missing, create graceful fallback/mock behavior and document it.

## Frontend Stack

Use:

- React
- TypeScript
- Vite
- Tailwind CSS
- Recharts
- Lucide React

Prioritize clean, modern, professional healthcare dashboard UI.

No childish styling.
No excessive animations.
No clutter.

## Backend Stack

Use Python FastAPI or Flask if backend is needed.

Backend responsibilities:

- load CatBoost models
- receive patient input
- return prediction output
- generate SHAP payload or mock SHAP payload
- return clinician-friendly explanation payload
- serve cohort analytics if useful

If full backend integration is too slow, build frontend with mock API services that are clearly isolated and replaceable.

## Design Principles

The dashboard must feel like something a clinician-researcher could actually use.

Prioritize:

- clarity
- trust
- clinical usefulness
- concise explanations
- patient prioritization
- research export usefulness

Avoid:

- generic ML demo feel
- dashboard bloat
- technical metrics overload
- showing model details that clinicians do not need

## Safety and Claims

This is a clinical decision-support prototype.

Always use cautious wording:

- “risk prediction”
- “decision-support”
- “may support earlier identification”
- “not a diagnostic replacement”
- “requires clinical validation before real-world deployment”

Do not claim:

- diagnosis
- treatment recommendation
- guaranteed cost reduction
- real deployment
- clinical approval
- autonomous medical decision-making

## SPEC and PLANS

After reading this file and `PROJECT_CONTEXT.md`, generate:

1. `SPEC.md`
2. `PLANS.md`

`SPEC.md` must define exactly what will be built.

`PLANS.md` must define step-by-step implementation tasks.

Do not begin major code changes until `SPEC.md` and `PLANS.md` are created.

## Done When

The dashboard prototype is done when:

1. The app runs locally.
2. The sidebar contains exactly the six approved modules.
3. Cohort Overview uses the dataset for useful charts/statistics.
4. Patient Risk Assessment supports patient input or sample patient selection.
5. Patient Risk Assessment shows CKD and delayed-remission risk outputs.
6. Patient Risk Assessment includes local explanation / SHAP-payload-style explanation.
7. High-Risk Patients ranks or filters patients by risk.
8. Patient Timeline shows longitudinal/progression view from available data or clear mock-safe fallback.
9. Global Risk Drivers displays available SHAP images and dependence plots.
10. Research Export provides export-ready summaries or mock export content.
11. Code is modular enough to replace mock services with real backend logic later.
12. No unnecessary model leaderboard page is added.
