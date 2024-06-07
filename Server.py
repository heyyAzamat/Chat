from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class ClientHandler(Thread):
    def __init__(self, client, clients):
        super().__init__()
        self._client = client
        self.clients = clients

    def run(self):
        try:
            while True:
                data = self._client.recv(1024)
                if not data:
                    break
                if data.decode("utf-8") == "byebye":
                    self.clients.remove(self._client)
                    self._client.close()
                    break
                else:
                    for client in self.clients:
                        if client != self._client:
                            client.send(data)
        except Exception as e:
            print(e)
            self.clients.remove(self._client)
            self._client.close()

def main():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("127.0.0.1", 12345))
    server.listen(512)
    clients = []

    print("Сервер запущен и ожидает подключения клиентов...")

    try:
        while True:
            curr_client, addr = server.accept()
            print(addr[0], "подключился к серверу")
            clients.append(curr_client)
            ClientHandler(curr_client, clients).start()
    except KeyboardInterrupt:
        print("Сервер остановлен.")
    finally:
        server.close()

if __name__ == "__main__":
    main()