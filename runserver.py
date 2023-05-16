import os
from app import APP

VERSION = '1.0.0'

if __name__ == "__main__":
    start = False
    port = 5000
    debug = os.environ.get("DEBUG", False)
    while not start and port < 5010:
        try:
            APP.run(debug=debug, port=port)
            start = True
        except OSError as e:
            print(e)
            print(f"Version:{VERSION}")
            port += 1
