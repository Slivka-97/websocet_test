import json
import time

import websockets
import asyncio
import aiohttp

PORT = 7890
print("Server listening on Port " + str(PORT))


async def get_data() -> tuple[float, dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://blockchain.info/ticker') as response:
            time_response = time.time()
            data = await response.json()
            return time_response, data


async def server_endpoint(websocket: websockets.WebSocketServerProtocol, path: str):
    if path == '/test':
        time_response, data = await get_data()
        while True:
            recv_msg = await websocket.recv()
            print(recv_msg)
            if time.time() - time_response > 5:
                time_response, data = await get_data()
            try:
                data_for_response = {'timestamp': time_response, 'data': data}
                json_data = json.dumps(data_for_response)
                await websocket.send(json_data)

            except websockets.ConnectionClosed as e:
                print("A client just disconnected")
    else:
        await websocket.send('Incorrect path')


async def main():
    async with websockets.serve(server_endpoint, "localhost", PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
