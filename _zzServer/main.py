import asyncio
import websockets

clients = set()


async def handler(websocket, path):
    # Register the client
    clients.add(websocket)
    try:
        async for message in websocket:
            # Assume the message format is "recipient:message"
            if ':' in message:
                recipient_name, msg = message.split(':', 1)
                # Find the recipient
                recipient = next((ws for ws in clients if ws.remote_address[1] == int(recipient_name)), None)
                if recipient:
                    await recipient.send(msg)
                else:
                    await websocket.send(f"Recipient {recipient_name} not found.")
            else:
                await websocket.send("Invalid message format. Use recipient:message.")
    except websockets.ConnectionClosed:
        print(f"Client {websocket.remote_address} disconnected")
    finally:
        # Unregister the client
        clients.remove(websocket)


async def main():
    server = await websockets.serve(handler, "localhost", 5678)
    await server.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
