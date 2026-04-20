from core.manager import AttackManager

def main():
    print("=== GhostHydra ===")

    target = input("Target IP: ")
    service = input("Service (ssh/ftp/http): ")
    username = input("Username: ")

    manager = AttackManager(target, service, username)
    manager.run()

if __name__ == "__main__":
    main()
