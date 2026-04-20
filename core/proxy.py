import random

PROXIES = [
    "socks5://127.0.0.1:9050",  # Tor
    "http://127.0.0.1:8080"
]

def get_proxy():
    return random.choice(PROXIES)
