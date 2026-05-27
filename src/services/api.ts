import type { DashboardPayload, RiskResult } from "../types";

export async function loadDashboard(): Promise<DashboardPayload> {
  const response = await fetch("/api/dashboard");
  if (!response.ok) {
    throw new Error("Dashboard data service is unavailable.");
  }
  return response.json();
}

export async function predictPatient(
  patientRef: string,
  inputs: Record<string, number | string | null>,
): Promise<RiskResult> {
  const response = await fetch("/api/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ patientRef, inputs }),
  });
  if (!response.ok) {
    throw new Error("Prediction service is unavailable.");
  }
  return response.json();
}
