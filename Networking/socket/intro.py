'''
# Python Socket Programming:-
Syntax:-
    socket.socket (socket_family, socket_type, protocol=0)

family − AF_INET by default. Other values - AF_INET6 (eight groups of four hexadecimal digits), AF_UNIX, AF_CAN (Controller Area Network) or AF_RDS (Reliable Datagram Sockets).
socket_type − should be SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants.
protocol − number is usually zero and may be omitted.

# Server Socket Methods
bind() method − This method binds the socket to specified IP address and port number.
listen() method − This method starts server and runs into a listen loop looking for connection request from client.
accept() method − When connection request is intercepted by server, this method accepts it and identifies the client socket with its address.
'''

