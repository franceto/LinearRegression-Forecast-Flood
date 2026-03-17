from pathlib import Path
import joblib
import pandas as pd
from groq import Groq

BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "linear_regression_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
API_KEY_PATH = BASE_DIR / "api_groq.txt"

FEATURES = [
    "MonsoonIntensity",
    "TopographyDrainage",
    "RiverManagement",
    "Deforestation",
    "Urbanization",
    "ClimateChange",
    "DamsQuality",
    "Siltation",
    "AgriculturalPractices",
    "Encroachments",
    "IneffectiveDisasterPreparedness",
    "DrainageSystems",
    "CoastalVulnerability",
    "Landslides",
    "Watersheds",
    "DeterioratingInfrastructure",
    "PopulationScore",
    "WetlandLoss",
    "InadequatePlanning",
    "PoliticalFactors",
]

def read_api_key():
    if not API_KEY_PATH.exists():
        return ""
    return API_KEY_PATH.read_text(encoding="utf-8-sig").strip()

def load_artifacts():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler

def predict_flood(model, scaler, values):
    row = pd.DataFrame([[values[f] for f in FEATURES]], columns=FEATURES)
    row_scaled = scaler.transform(row)
    pred = float(model.predict(row_scaled)[0])
    return max(0.0, min(1.0, pred))

def explain_with_groq(values, pred):
    api_key = read_api_key()
    if not api_key:
        return "Khong tim thay api_groq.txt hoac file rong."
    try:
        client = Groq(api_key=api_key)
        prompt = f"""
Bạn là trợ lý AI phân tích lũ lụt

Dữ liệu đầu vào:
{values}

FloodProbability dự đoán: {pred:.4f}

Hãy trả lời bằng tiếng việt, ngắn gọn, dễ hiểu theo 3 mục sau:
1. Mục rủi ro
2. Yếu tố đáng chú ý
3. Gợi ý giảm rủi ro
"""
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Loi Groq API: {e}"