import pandas as pd

dataframe_general = pd.read_csv("./dataset/gym_members_exercise_tracking.csv")

def  workout_frecuency_impact() -> dict:
  df = dataframe_general.copy()
  #Correlacion
  Workout_Frequency_Fat_Percentage = df["Workout_Frequency (days/week)"].corr(df["Fat_Percentage"])
  Workout_Frequency_BMI = df["Workout_Frequency (days/week)"].corr(df["BMI"])
  #agrupacion
  grouped_stats = df.groupby("Workout_Frequency (days/week)").agg({
      "Fat_Percentage": ["mean"],
      "BMI": ["mean"]
  }).reset_index()
  #aplanando
  
  grouped_stats.columns = ['_'.join(col).strip() for col in grouped_stats.columns.values]
  #diccionario
  result = {
      "result_dataframe": grouped_stats.to_dict(orient="records"),
      "dataframe": [
          {
              "labels": ["Frecuencia de ejercicios(dias a la semana)", "Porcentaje de grasa corporal"] ,
              "correlation": float(Workout_Frequency_Fat_Percentage * 100),
              "x": grouped_stats["Workout_Frequency (days/week)_"].to_list(), 
              "y": grouped_stats["Fat_Percentage_mean"].to_list(), 
          },
          {
              "labels": ["Frecuencia de ejercicios(dias a la semana)", "Indice de masa corporal"] ,
              "correlation": float(Workout_Frequency_BMI * 100),
              "x": grouped_stats["Workout_Frequency (days/week)_"].to_list(), 
              "y": grouped_stats["BMI_mean"].to_list(), 
          }
      ]
  }
  return result

def BMI_performance_analysys() -> dict:
    df = dataframe_general.copy()
    relacion_rendimiento_calorias_quemadas = df["BMI"].corr(df["Calories_Burned"])
    relacion_rendimiento_avgBPM=df["BMI"].corr(df["Avg_BPM"])
    relacion_rendimiento_duracion=df["BMI"].corr(df["Session_Duration (hours)"])
    df["BMI_Category"] = pd.cut(df["BMI"], bins=[0, 18.5, 24.9, 29.9, float('inf')], labels=['Bajo 0-18', 'Normal 18-24', 'Sobrepeso 24-29', 'Obesidad 29+'])


    grouped_stats = df.groupby(["BMI_Category"]).agg({
                "Calories_Burned": ["mean"],
        "Avg_BPM": ["mean"],
            "Session_Duration (hours)": ["mean"]
    }).reset_index()

    grouped_stats.columns = ['_'.join(col).strip() for col in grouped_stats.columns.values]

    grouped_stats= {
        "result_dataframe":  grouped_stats.to_dict(orient="records"),
        "dataframe": [
            {
                "labels": ["Índice de masa coorporal","Calorias quemadas"],
                "correlation": float(relacion_rendimiento_calorias_quemadas * 100),
                "x": grouped_stats["BMI_Category_"].to_list(),
                "y": grouped_stats["Calories_Burned_mean"].to_list(),
            },
            {
                "labels": ["Niveles de experiencia","Frecuencia cardiaca prom"],
                "correlation": float(relacion_rendimiento_avgBPM * 100),
                "x": grouped_stats["BMI_Category_"].to_list(),
                "y": grouped_stats["Avg_BPM_mean"].to_list(),
            },
            {
                "labels": ["Niveles de experiencia","Duración de sesiones"],
                "correlation": float(relacion_rendimiento_duracion* 100),
                "x": grouped_stats["BMI_Category_"].to_list(),
                "y": grouped_stats["Session_Duration (hours)_mean"].to_list(),
            }
        ]
    }
    return grouped_stats

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

def duration_of_sessions() -> dict:
    df = dataframe_general.copy()
    correlation_calories_burned = df["Session_Duration (hours)"].corr(df["Calories_Burned"])
    correlation_water_intake = df["Session_Duration (hours)"].corr(df["Water_Intake (liters)"] )
    correlation_fat_percentage = df["Session_Duration (hours)"].corr( df["Fat_Percentage"])
    correlation_frequency = df["Session_Duration (hours)"].corr(df["Workout_Frequency (days/week)"])

    # Agrupar datos por duración de la sesión y calcular valores medios
    grouped_stats = (
        df.groupby("Session_Duration (hours)")
        .agg(
            {
                "Calories_Burned": ["mean"],
                "Water_Intake (liters)": ["mean"],
                "Workout_Frequency (days/week)": ["mean"],
                "Fat_Percentage": ["mean"],
            }
        )
        .reset_index()
    )

    # Aplanar columnas
    grouped_stats.columns = ["_".join(col).strip() for col in grouped_stats.columns.values]

    result = {
        "result_dataframe": grouped_stats.to_dict(orient="records"),
        "dataframe": [
            {
                "labels": ["Duración de la Sesión", "Calorías Quemadas"],
                "correlation": float(correlation_calories_burned * 100),
                "x": grouped_stats["Session_Duration (hours)_"].to_list(),
                "y": grouped_stats["Calories_Burned_mean"].to_list(),
            },
            {
                "labels": ["Duración de la Sesión", "Ingesta de Agua"],
                "correlation": float(correlation_water_intake * 100),
                "x": grouped_stats["Session_Duration (hours)_"].to_list(),
                "y": grouped_stats["Water_Intake (liters)_mean"].to_list(),
            },
            {
                "labels": ["Duración de la Sesión", "Porcentaje de Grasa"],
                "correlation": float(correlation_fat_percentage * 100),
                "x": grouped_stats["Session_Duration (hours)_"].to_list(),
                "y": grouped_stats["Fat_Percentage_mean"].to_list(),
            },
            {
                "labels": ["Duración de la Sesión", "Frecuencia de Entrenamiento"],
                "correlation": float(correlation_frequency * 100),
                "x": grouped_stats["Session_Duration (hours)_"].to_list(),
                "y": grouped_stats["Workout_Frequency (days/week)_mean"].to_list(),
            },
        ],
    }

    return result