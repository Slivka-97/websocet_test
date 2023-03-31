import websockets
import asyncio


async def client():
    url = "ws://127.0.0.1:7890/test"
    async with websockets.connect(url) as ws:
        try:
            while True:
                await ws.send("Hello Server!")
                msg_from_server = await ws.recv()
                print(msg_from_server)
                await asyncio.sleep(1)
        except websockets.ConnectionClosed:
            print('Close connect')


asyncio.run(client())
