from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/{url_path:path}")
async def proxy(url_path: str):
    if not url_path:
        return {"success": False, "errors": ["url path empty"]}

    response = requests.get(f'https://planner.uniud.it/{url_path}')
    if response.ok:
        return response.content

    return {"success": False, "errors": ["request failed", f"status code: {response.status_code}"]}
