# coding=utf8
# if __name__ == "": from JsMacrosAC import *  # Autocomplete, not necessary
from builtins import str
from dataclasses import dataclass
# region Server
from ipaddress import ip_address
@dataclass
class Server:
    """"""
    hostname: str
    address: ip_address
    port: int = 25565

    def __init__(self, server: str):
        server = server.split("/")
        self.hostname = server[0]
        address = server[1].split(":")
        self.address = address[0]
        if len(address) > 1: self.port = int(address[1])
# endregion

# class Utils():