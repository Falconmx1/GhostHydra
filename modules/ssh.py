def attack(target, username):
    print(f"[+] Simulando ataque SSH en {target} con usuario {username}")

    passwords = ["1234", "admin", "password"]

    for pwd in passwords:
        print(f"[*] Probando: {pwd}")

        # Simulación
        if pwd == "admin":
            print(f"[SUCCESS] Password encontrada: {pwd}")
            return

    print("[-] No se encontró password")
