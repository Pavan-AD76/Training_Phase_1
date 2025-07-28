from fastapi import FastAPI,HTTPException

app=FastAPI()

items=[]
  
@app.get("/")
def root():
    return {"Hello":"World"}

'''
if __name__ == "__main__":
    uvicorn.run("hell0:app", host="127.0.0.1", port=8000, reload=True)
    
'''