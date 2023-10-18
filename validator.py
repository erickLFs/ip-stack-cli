import ipaddress
class ValidatorIP:
    """Class for Validating IP Addresses"""
    def __init__(self, ip):
        self.ip = ip

    def is_valid_ip(self):
        try:
            ipaddress.IPv4Address(self.ip)  # Intenta crear un objeto IPv4Address
            return True
        except ipaddress.AddressValueError:
            try:
                ipaddress.IPv6Address(self.ip)  # Intenta crear un objeto IPv6Address
                return True
            except ipaddress.AddressValueError:
                return False