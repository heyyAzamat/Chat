#Chat Application
This repository contains a simple chat application implemented in Python using sockets and threading. The application consists of a server (Server.py) and a client (Client.py) which allow multiple clients to connect to the server and exchange messages in real-time.

Features
Multithreaded Server: Handles multiple client connections simultaneously.
Client Nicknames: Users can set their nicknames upon connecting to the server.
Message Broadcasting: Messages sent by one client are broadcast to all other connected clients.
Graceful Disconnection: Clients can gracefully disconnect from the server by sending the "byebye" message.
Requirements
Python 3.x
Installation
Clone the repository:

sh
Копировать код
git clone https://github.com/yourusername/chat-application.git
cd chat-application
Ensure you have Python 3 installed on your system.

Usage
Running the Server
Navigate to the repository directory.

Run the server script:

sh
Копировать код
python Server.py
The server will start and listen for incoming connections on 127.0.0.1:12345.

Running the Client
Open a new terminal window.

Navigate to the repository directory.

Run the client script:

sh
Копировать код
python Client.py
Enter your nickname when prompted.

Start typing messages to send them to the chat.

Example
Start the server:

sh
Копировать код
python Server.py
Output:

Копировать код
Сервер запущен и ожидает подключения клиентов...
Start a client:

sh
Копировать код
python Client.py
Output:

markdown
Копировать код
Пожалуйста, введите свое ник: Alice
> Hello everyone!
Start another client:

sh
Копировать код
python Client.py
Output:

markdown
Копировать код
Пожалуйста, введите свое ник: Bob
> Hi Alice!
The first client will see:

makefile
Копировать код
Bob: Hi Alice!
Code Overview
Server.py
Sets up a TCP server that listens on 127.0.0.1:12345.
Accepts incoming client connections and spawns a new ClientHandler thread for each client.
ClientHandler threads manage communication with their respective clients and broadcast received messages to all other clients.
Client.py
Connects to the server at 127.0.0.1:12345.
Prompts the user to enter a nickname.
Spawns a RefreshScreenThread to listen for incoming messages from the server and print them to the console.
Reads user input and sends messages to the server.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
Contributions are welcome! Please feel free to submit a Pull Request.

For any issues or questions, please open an issue in the repository or contact the repository owner.

Happy chatting!
