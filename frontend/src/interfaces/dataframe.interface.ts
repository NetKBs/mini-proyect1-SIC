export interface Hydratation {
  "Water_Intake_Category_": "Baja" | "Moderada" | "Alta",
  "Calories_Burned_mean": number,
  "Calories_Burned_std": number,
  "Avg_BPM_mean": number,
  "Avg_BPM_std": number,
  "Session_Duration (hours)_mean": number,
  "Session_Duration (hours)_std": number,
}

export interface ExperienceLevel {
  "Nivel de experiencia": "Principiante" | "intermedio" | "Avanzado",
  "Calorias quemadas": number,
  "Frecuenca cardiaca promedio": number,
  "Frecuencia cardiaca maxima": number,
}