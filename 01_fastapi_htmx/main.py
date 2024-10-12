from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

app = FastAPI(title="HTMX example")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/click", response_class=HTMLResponse)
def click(_: Request) -> HTMLResponse:
    return "<p>You clicked!</p>"
