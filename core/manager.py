from core.plugin_loader import load_plugins

class AttackManager:
    def __init__(self, target, service, username):
        self.target = target
        self.service = service
        self.username = username
        self.plugins = load_plugins()

    def run(self):
        if self.service in self.plugins:
            self.plugins[self.service].attack(self.target, self.username)
        else:
            print("[!] Servicio no soportado")
