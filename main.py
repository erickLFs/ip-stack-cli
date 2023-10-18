import sys
from request import IPStackRequest
from validator import ValidatorIP

class Main(ValidatorIP):
    def __init__(self):
        self.parse_args()
        super().__init__(self.ip)
    
    def parse_args(self):
        if len(sys.argv) < 2:
            print("Usage: python main.py <ip>")
            sys.exit(1)
        self.ip = sys.argv[1]
    
    
    def run(self):
        if self.is_valid_ip():
            ip_stack = IPStackRequest(self.ip)
            ip_stack.print_json()
        else:
            print("Invalid IP address")
            sys.exit(1)
    
    
if __name__ == '__main__':
    main = Main()
    main.run()