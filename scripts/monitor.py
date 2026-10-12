"""Server network port and service readiness checker."""
import socket
import sys

def check_port(host: str, port: int, timeout: float = 3.0) -> bool:
    """Probes TCP port connectivity."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
        return True
    except Exception:
        return False
    finally:
        sock.close()

if __name__ == "__main__":
    targets = [("127.0.0.1", 80), ("127.0.0.1", 443), ("127.0.0.1", 22)]
    for h, p in targets:
        status = "OPEN" if check_port(h, p) else "CLOSED"
        print(f"Target {h}:{p} -> {status}")
