import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 23))
server_socket.listen(5)
client_socket, address = server_socket.accept()
while 1:
    #Riceviamo i dati inviati dal client.
    data = client_socket.recv(512)
    print("Ricevuto:" , data)
    #Controlliamo che il client non abbia inviato un comando di chiusura.
    if ( data == b'\xc3\xa8' ):
        client_socket.close()
        break;
    #Se non è un comando di chiusura facciamo qualcosa con i dati ricevuti.
    else:
    #FARE QUALCOSA CON I DATI.
    #Inviare i dati processati dal server.
        client_socket.send (data)
