from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import json

app = FastAPI()


@app.get("/")
async def get():
    file_html_page = open('../client/client.html', 'r')
    html_page = file_html_page.read()
    return HTMLResponse(html_page)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    nums = 0
    while True:
        data = await websocket.receive_text()
        json_data = json.loads(data)
        nums += 1
        json_data['message_num'] = nums
        await websocket.send_text(json.dumps(json_data))
