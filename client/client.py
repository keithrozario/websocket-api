from websocket import create_connection
import time

ws_server = "wss://1xpovj0mt8.execute-api.ap-southeast-1.amazonaws.com/dev"

def on_pong(wsapp, message):
    print("Got a pong! Still Connected")

# create connection
ws = create_connection(ws_server, header=["Auth: 12345678"])

# test with endpoint, should return "barbarbar"
ws.send('{"action":"foo"}')
print(ws.recv())

# test with endpoint, should return "barbarbar"
ws.send('{"action":"bar"}')
ws.close()


# # ping for 15 minutes
# for i in range(1,15):
#     print(f"sent ping number {i}")
#     ws.ping()
#     time.sleep(60)  # ping every minute
# ws.close()

# # test with endpoint, should return "barbarbar"
# ws.send('{"action":"foo"}')
# print(ws.recv())

# ws.close()