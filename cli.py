from core.manager import AttackManager
from core.scanner import detect_services

def main():
    print("=== GhostHydra ===")

    target = input("Target IP: ")
    username = input("Username: ")

    services = detect_services(target)
    print(f"[+] Servicios detectados: {services}")

    for service in services:
        manager = AttackManager(target, service, username)
        manager.run()

if __name__ == "__main__":
    main()
