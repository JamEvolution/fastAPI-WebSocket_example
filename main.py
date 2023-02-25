from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
        <style>
            body {
                background-color: #1E1F2B;
                font-family: 'Roboto', sans-serif;
            }
            h1 {
                color: #FF1493;
                text-align: center;
                margin-top: 50px;
            }
            form {
                display: flex;
                justify-content: center;
                margin-top: 50px;
            }
            input[type="text"] {
                width: 300px;
                height: 40px;
                border: none;
                border-radius: 20px;
                padding: 0 20px;
                font-size: 18px;
                margin-right: 10px;
            }
            button {
                width: 100px;
                height: 40px;
                border: none;
                border-radius: 20px;
                background-color: #FF1493;
                color: #fff;
                font-size: 18px;
                cursor: pointer;
            }
            button:hover {
                background-color: #F08080;
            }
            ul {
                list-style: none;
                margin-top: 50px;
            }
            li {
                color: #fff;
                font-size: 18px;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <h1>API WebSocket Bağlantı Test Arayüzü</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")