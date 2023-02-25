import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        while True:
            message = input("Mesajınızı girin: ")
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Gelen yanıt: {response}")

asyncio.run(send_message())