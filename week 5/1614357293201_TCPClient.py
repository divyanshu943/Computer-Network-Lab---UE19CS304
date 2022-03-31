from socket import *
serverName = "10.1.10.29"
serverPort = 12007
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input("Input lowercase sentence:")
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print ("From Server:", modifiedSentence)
clientSocket.close()
