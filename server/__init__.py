from fastapi import FastAPI
from api import include_routers

def create_app():
     _app = FastAPI(
          docs_url="/"
     )
     include_routers(_app)

     return _app

app =  create_app()
