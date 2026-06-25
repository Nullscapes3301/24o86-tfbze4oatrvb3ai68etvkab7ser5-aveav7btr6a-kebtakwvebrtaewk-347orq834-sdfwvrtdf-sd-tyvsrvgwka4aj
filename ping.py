import socket
import time

def ping(host):
    try:
        host = self.extarg1
        ip = socket.gethostbyname(host)
        print(f"Ping to {host} [{ip}]")

        start = time.time()

        s = socket.create_connection((host, 80), timeout=2)

        end = time.time()
        s.close()

        ms = (end - start) * 1000

        print(f"Awnser from {ip}: time={ms:.2f}ms")

    except socket.timeout:
        print("Timeout has finished")

    except Exception:
        print("Cannot resolve host")
