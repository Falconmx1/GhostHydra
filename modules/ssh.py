import asyncio
from core.async_engine import run_async
from core.wordlist import generate_wordlist
from core.scoring import sort_by_score
from core.stealth import random_delay
from core.proxy import get_proxy
from core.db import save_entry

def attack(target, username):
    print(f"[+] Async SSH attack en {target}")

    passwords = generate_wordlist(username)
    passwords = sort_by_score(passwords, username)

    found = {"status": False}

    async def worker(pwd):
        if found["status"]:
            return

        await asyncio.sleep(0)  # yield control
        random_delay()

        proxy = get_proxy()
        print(f"[*] {pwd} via {proxy}")

        # Simulación segura
        if pwd == username + "123":
            print(f"[SUCCESS] {pwd}")

            save_entry({
                "target": target,
                "service": "ssh",
                "username": username,
                "password": pwd
            })

            found["status"] = True

    asyncio.run(run_async(passwords, worker, limit=10))
