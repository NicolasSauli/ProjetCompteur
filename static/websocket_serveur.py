import json
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketDisconnect

app = FastAPI()


ws_connections = []


counter = 0

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global counter, ws_connections

    await websocket.accept()
    ws_connections.append(websocket)

    print("Nouvelle connexion WebSocket")


    await websocket.send_text(json.dumps({"counterValue": counter}))

    try:
        while True:

            data = await websocket.receive_text()

            if data == "inc":
                counter += 1
            elif data == "dec":
                counter -= 1
            else:
                print("Action inconnue :", data)
                continue


            message = json.dumps({"counterValue": counter})
            for ws in ws_connections:
                await ws.send_text(message)

    except WebSocketDisconnect:
        print("Un client s'est déconnecté")
        ws_connections.remove(websocket)

    except Exception as e:
        print("Erreur WebSocket:", e)

