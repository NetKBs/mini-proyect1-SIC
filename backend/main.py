from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import analysis

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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