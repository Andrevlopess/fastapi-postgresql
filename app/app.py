from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return 'fiz o eli e to gritando'
