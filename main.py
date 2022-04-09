# main.py
from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class ScoringInput(BaseModel):
    mean_radius: float
    mean_texture: float
    mean_perimeter: float
    mean_area: float
    mean_smoothness: float
    mean_compactness: float
    mean_concavity: float
    mean_concave_points: float
    mean_symmetry: float
    mean_fractal_dimension: float
    radius_error: float
    texture_error: float
    perimeter_error: float
    area_error: float
    smoothness_error: float
    compactness_error: float
    concavity_error: float
    concave_points_error: float
    symmetry_error: float
    fractal_dimension_error: float
    worst_radius: float
    worst_texture: float
    worst_perimeter: float
    worst_area: float
    worst_smoothness: float
    worst_compactness: float
    worst_concavity: float
    worst_concave_points: float
    worst_symmetry: float
    worst_fractal_dimension: float


@app.get("/")
async def root():
    return {"message": "Welcome to ML Scoring API Service. Head to /docs to know more."}

@app.post("/predict_scoring/")
async def predict_asgn_group(score: ScoringInput):
    mapping = {0:'malignant', 1:'benign'}
    score_dict = score.dict()
    model = pickle.load(open("model.pkl", 'rb'))
    prediction_label = None
    y_pred = model.predict([[v for v in score_dict.values()]])
    prediction_label = mapping[y_pred[0]]
    return {"prediction":prediction_label}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",  port=8081)    