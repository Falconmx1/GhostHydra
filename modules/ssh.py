from core.engine import run_threads
from core.wordlist import generate_wordlist
from core.stealth import random_delay
from core.utils import save_result

def attack(target, username):
    print(f"[+] Ataque SSH en {target}")

    passwords = generate_wordlist(username)
    found = {"status": False}

    def worker(pwd):
        if found["status"]:
            return

        random_delay()

        print(f"[*] Probando {pwd}")

        # Simulación controlada
        if pwd == username + "123":
            print(f"[SUCCESS] {pwd}")
            save_result(target, "ssh", username, pwd)
            found["status"] = True

    run_threads(passwords, worker, threads=5)
