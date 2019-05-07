# -*- coding: utf-8 -*-
import struct
import socket

class utils(object):
    def recvall(sock, size):
        received_chunks = []
        buf_size = 4096
        remaining = size
        while remaining > 0:
            received = sock.recv(min(remaining, buf_size))
            if not received:
                raise Exception('unexcepted EOF')
            received_chunks.append(received)
            remaining -= len(received)
        return b''.join(received_chunks)
    
    def write_utf8(s: str, sock: socket.socket):
        encoded = s.encode(encoding='utf-8')
        sock.sendall(struct.pack('>i', len(encoded)))
        sock.sendall(encoded)
    
    def read_utf8(sock):
        len_bytes = utils.recvall(sock, 4)
        length = struct.unpack('>i', len_bytes)[0]
        encoded = utils.recvall(sock, length)
        return str(encoded, encoding='utf-8')