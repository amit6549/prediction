import requests
from config import API_URL

def get_last_result():
    try:
        res = requests.get(API_URL).json()
        return res.get("data", {}).get("result", "").upper()
    except:
        return None

def predict_next_color(last_result):
    # Very basic logic: alternate color (for example)
    if last_result == "RED":
        return "🟩 GREEN"
    elif last_result == "GREEN":
        return "🟥 RED"
    else:
        return "🟪 VIOLET"
