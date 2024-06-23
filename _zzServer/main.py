import asyncio
import websockets

clients = set()
printers = set()


async def handler(websocket, path):
    # Register the client
    clients.add(websocket)
    try:
        async for message in websocket:
            # Assume the message format is "recipient:message"
            if ':' in message:
                recipient_name, msg = message.split(':', 1)
                if recipient_name == "SERVER":
                    if msg == "AM_PRINTER":
                        printers.add(websocket.remote_address[1])
                        await websocket.send("OK")
                    if msg == "GET_PRINTERS":
                        if len(printers) == 0:
                            await websocket.send("[]")
                        else:
                            printers_string = "','".join(str(s) for s in printers)
                            await websocket.send(f"['{printers_string}']")
                else:
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
    async with websockets.serve(handler, "localhost", 5678):
        await asyncio.Future()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
