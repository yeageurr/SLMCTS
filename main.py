from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/home")
def home(request: Request):
  return templates.TemplateResponse(
    "home.html",
    {
      "request": request,
      "title": "Home"
    }
  )
