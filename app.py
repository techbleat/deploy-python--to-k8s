from fastapi import FastAPI, Depends, Form, HTTPException, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="/config/.env")

# FastAPI app
app = FastAPI()

# Environment variables for username and password
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Initialize templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Check if the entered username and password match the ones in the .env file
    if username == USERNAME and password == PASSWORD:
        response = RedirectResponse(url="/welcome", status_code=status.HTTP_302_FOUND)
        response.set_cookie(key="username", value=username)
        return response
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@app.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request):
    username = request.cookies.get("username")
    if username:
        return templates.TemplateResponse("welcome.html", {"request": request, "username": username})
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

# Run with `uvicorn app:app --reload`

