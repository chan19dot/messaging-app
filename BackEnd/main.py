from fastapi import FastAPI

app = FastAPI(title="Local Chat API")

@app.get("/health")
def health():
    return {"status": "ok"}


# For creating a new api follow these steps:

@app.get("/name/{name}") #name is the url ->
def getName(name:str):
    return {"msg": f"hello {name}"} # to test this copy this url localhost:8000/name/Sri
#Try changing it to localhost:8000/name/test you should see hello test
# Similarly try writing a new get endpoint returning anything.

