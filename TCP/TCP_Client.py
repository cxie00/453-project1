from socket import *
import sys

serverName = "127.0.0.1"  
serverPort = 65432

def TCP_client():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    file = sys.argv[1]
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        print(f'14: {line}')
        clientSocket.send(line.encode())
        answer = clientSocket.recv(1024).decode()

        split_ans = answer.split()
        status_code = split_ans[0]
        result = split_ans[1]

        if status_code == "200":
            print(f"Result is {result}.")
        elif status_code == "620":
            print("Error 620: Invalid OC")
        elif status_code == "630":
            print("Error 630: Invalid operands")
    clientSocket.close()

TCP_client()