from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
from datetime import datetime

app = FastAPI()

# Connection manager to handle WebSocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
        self.save_message(message)

    def save_message(self, message: str):
        with open("chat_history.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {message}\n")

manager = ConnectionManager()

@app.websocket("/ws/{user_name}/{client_id}")
async def websocket_endpoint(websocket: WebSocket, user_name: str, client_id: int):
    """
    WebSocket endpoint for client communication.
    """
    await manager.connect(websocket)
    connect_message = f"{user_name} connected."
    await manager.broadcast(connect_message)
    manager.save_message(connect_message)
    try:
        while True:
            data = await websocket.receive_text()
            message = f"{user_name}: {data}"
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        disconnect_message = f"{user_name} disconnected."
        await manager.broadcast(disconnect_message)
        manager.save_message(disconnect_message)
