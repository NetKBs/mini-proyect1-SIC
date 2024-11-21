import pandas as pd

dataframe_general = pd.read_csv("./dataset/gym_members_exercise_tracking.csv")

def hydratation_performance_analysys() -> dict:
  df = dataframe_general.copy()
  correlation_session_duration = df["Water_Intake (liters)"].corr(df["Session_Duration (hours)"])
  correlation_avg_bpm = df["Water_Intake (liters)"].corr(df["Avg_BPM"])
  correlation_calories_burned = df["Water_Intake (liters)"].corr(df["Calories_Burned"])

  # Crear categorías
  df["Water_Intake_Category"] = pd.cut(df["Water_Intake (liters)"], bins=[0, 1.5, 3, float('inf')], labels=["Baja 0-1.5L", "Moderada 1.5-3L", "Alta 3L+"])

  grouped_stats = df.groupby("Water_Intake_Category").agg({
      "Calories_Burned": ["mean"],
      "Avg_BPM": ["mean"],
      "Session_Duration (hours)": ["mean"]
  }).reset_index()

  # Aplanar
  grouped_stats.columns = ['_'.join(col).strip() for col in grouped_stats.columns.values]

  result = {
      "result_dataframe": grouped_stats.to_dict(orient="records"),
      "dataframe": [
          {
               "labels": ["Ingesta de Agua", "Calorías Quemadas"] ,
              "correlation": float(correlation_calories_burned * 100),
              "x": grouped_stats["Water_Intake_Category_"].to_list(),
              "y": grouped_stats["Calories_Burned_mean"].to_list(),
          },
          {
              "labels": ["Ingesta de Agua", "BPM Promedio"] ,
              "correlation": float(correlation_avg_bpm * 100),
              "x": grouped_stats["Water_Intake_Category_"].to_list(),
              "y": grouped_stats["Avg_BPM_mean"].to_list(),
          },
          {
              "labels": ["Ingesta de Agua", "Duración de la Sesión"],
              "correlation": float(correlation_session_duration * 100),
              "x": grouped_stats["Water_Intake_Category_"].to_list(),
              "y": grouped_stats["Session_Duration (hours)_mean"].to_list(),
          }
      ]
  }

  return result

def experience_workout_evolution() -> dict:
  df = dataframe_general.copy()
  correlation_calories = df["Experience_Level"].corr(df["Calories_Burned"])
  correlation_avg_bpm = df["Experience_Level"].corr(df["Avg_BPM"])
  correlation_max_bpm = df["Experience_Level"].corr(df["Max_BPM"])

  df_experience_level = df.groupby(["Experience_Level"])

  dataframe = df_experience_level.agg({
    "Calories_Burned": ["mean"],
    "Avg_BPM": ["mean"],
    "Max_BPM": ["mean"]
  }).reset_index()

  cols = ["Nivel de experiencia", "Calorias quemadas", "Frecuenca cardiaca promedio", "Frecuencia cardiaca maxima"]

  dataframe["Experience_Level"] = ["Principiante", "Intermedio", "Avanzado"]
  dataframe.columns = cols

  data_returned = {
		"result_dataframe":  dataframe.to_dict(orient="records"),
    "dataframe": [
      {
				"labels": ["Nivel de experiencia", "Calorias quemadas"],
				"correlation": float(correlation_calories * 100),
				"x": dataframe["Nivel de experiencia"].to_list(),
				"y": dataframe["Calorias quemadas"].to_list()
			},
      {
				"labels": ["Nivel de experiencia", "Frecuenca cardiaca promedio"],
				"correlation": float(correlation_avg_bpm * 100),
				"x": dataframe["Nivel de experiencia"].to_list(),
				"y": dataframe["Frecuenca cardiaca promedio"].to_list()
			},
      {
				"labels": ["Nivel de experiencia", "Frecuencia cardiaca maxima"],
				"correlation": float(correlation_max_bpm * 100),
				"x": dataframe["Nivel de experiencia"].to_list(),
				"y": dataframe["Frecuencia cardiaca maxima"].to_list()
			}
		]
	}

  return data_returned