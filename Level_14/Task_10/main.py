from fastapi import FastAPI, HTTPException
from typing import List
import pandas as pd

app = FastAPI()

commentary_df = pd.read_csv("cricket_commentary.csv")

@app.get("/")
def read_root():
    return {"message": "Cricket Commentary API Running!"}

@app.get("/get/{match_id}")
def get_match_commentary(match_id: str):
    match_data = commentary_df[commentary_df['match_no'].str.lower() == match_id.lower()]   
    if match_data.empty:
        raise HTTPException(status_code=404, detail="Match ID not found")
    commentary_list = match_data.to_dict(orient="records")
    return {"match_id": match_id, "commentary": commentary_list}
