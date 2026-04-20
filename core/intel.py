def get_target_intel(target):
    print(f"[*] Recolectando intel de {target}")

    # Simulación controlada (puedes conectar APIs reales después)
    return {
        "open_ports": [22, 80],
        "services": ["ssh", "http"],
        "possible_vulns": ["weak_passwords"]
    }
