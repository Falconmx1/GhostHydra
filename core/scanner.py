import subprocess

def detect_services(target):
    print("[*] Escaneando servicios...")

    result = subprocess.getoutput(f"nmap -p 22,21,80 {target}")

    services = []

    if "22/tcp open" in result:
        services.append("ssh")
    if "21/tcp open" in result:
        services.append("ftp")
    if "80/tcp open" in result:
        services.append("http")

    return services
