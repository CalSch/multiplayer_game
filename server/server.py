import socket,json,logging,threading

HOST = '127.0.0.1'
PORT = 7777         # Port to listen on (non-privileged ports are > 1023)

def send(conn: socket.socket,addr: socket._RetAddress, data: dict):
    logging.info(f"Sending packet to {str(addr)}")
    conn.send(bytes(json.dumps(data).encode('utf8')))


def playerThread(conn: socket.socket):
    logging.warning("there was a farmer who had a cow eieio.\nhe died because his didnt finish his threading function, dont be like him.")
    conn.close()

player_threads=[]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            logging.info(f"New connection to {addr}")
            thread=threading.Thread(target=playerThread, args=(conn,))
            player_threads.append(thread)
            thread.start()