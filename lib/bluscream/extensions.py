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

class Utils(str):
    def getServer(self, server: str) -> Server:
        server_ = server.split("/")
        address = server_[1].split(":")
        return Server(hostname=server_[0], address=ip_address(address[0]), port=int(address[1]))
# endregion