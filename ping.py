import socket
import time

def ping(host):
    try:
        host = self.extarg1
        ip = socket.gethostbyname(host)
        self.pr(f"Ping to {host} [{ip}]")

        start = time.time()

        s = socket.create_connection((host, 80), timeout=2)

        end = time.time()
        s.close()

        ms = (end - start) * 1000

        self.pr(f"Awnser from {ip}: time={ms:.2f}ms")

    except socket.timeout:
        self.pr("Timeout has finished")

    except Exception:
        self.pr("Cannot resolve host")
