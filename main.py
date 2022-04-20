from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = [
    "https://kitsunesamaix.github.io",
    "https://uniud-timetable-app.web.app",
    "https://uniud-timetable-app.firebaseapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{url_path:path}")
async def proxy(request: Request, url_path: str):
    if not url_path:
        return {"success": False, "errors": ["url path empty"]}

    response = requests.get(f'https://planner.uniud.it/{url_path}', params=request.query_params)
    if response.ok:
        return Response(content=response.content)

    return {"success": False, "errors": ["request failed", f"status code: {response.status_code}"]}
