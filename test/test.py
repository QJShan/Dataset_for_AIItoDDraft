import uvicorn
from fastapi import FastAPI,Body

app = FastAPI()


@app.post("/test")
def Chat(
        only_retrive: bool = Body(default=True),
        name: str = Body(default="hello docker",title="access private or public resources"),
):
    return {"only_retrive":only_retrive,"name":name}


if __name__ == "__main__":
    uvicorn.run(app=app,host="0.0.0.0",reload=False,port=8001)
