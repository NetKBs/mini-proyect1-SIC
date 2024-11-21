from fastapi import FastAPI
import pandas as pd
import analysis

app = FastAPI()

@app.get("/analyze/hydration-impact") 
def get_hydration_impact():
        result = analysis.hydratation_performance_analysys()
        return result

@app.get("/analyze/experience-impact")
def get_experience_impact():
        result = analysis.experience_workout_evolution()
        return result

@app.get("/analyze/duration-impact")
def get_duration_impact():
        result = analysis.duration_of_sessions()
        return result