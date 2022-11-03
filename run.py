from app import app
import uvicorn


if __name__ == "__main__":
    uvicorn.run("run:app",reload=True)