from socket import *

serverName = 'localhost'
serverPort = 65432

def tcp_server():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive.")
    try: 
        while True:
                connectionSocket, addr = serverSocket.accept()
                request = connectionSocket.recv(1024).decode()
                (code, answer) = check_compute(request)
                result = f'{request[:-1]} -> {code} {answer}'
                print(result)
                code_ans = f'{code} {answer}'
                connectionSocket.send(code_ans.encode())
                connectionSocket.close()
    except KeyboardInterrupt:
        connectionSocket.close()
        serverSocket.close()

def check_compute(request):
    code = isValid(request)
    if code == 200:
        answer = compute(request)
    elif code == 620 or code == 630:
        answer = -1
    return (code,answer)

def isValid(request):
    split_request = request.split()
    validOC = "+-*/"
    if split_request[0] not in validOC:
        return 620
    bool0 = isint(split_request[1])
    bool1 = isint(split_request[2])
    if not bool0 or not bool1:
        return 630
    return 200 

def compute(request):
    split_request = request.split()
    if split_request[0] == "+":
        return (int(split_request[1]) + int(split_request[2]))
    elif split_request[0] == "-":
        return (int(split_request[1]) - int(split_request[2]))
    elif split_request[0] == "*":
        return (int(split_request[1]) * int(split_request[2]))
    else:
        return (int(split_request[1]) / int(split_request[2]))

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


tcp_server()
