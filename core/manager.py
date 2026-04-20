from modules import ssh, ftp, http

class AttackManager:
    def __init__(self, target, service, username):
        self.target = target
        self.service = service
        self.username = username

    def run(self):
        if self.service == "ssh":
            ssh.attack(self.target, self.username)
        elif self.service == "ftp":
            ftp.attack(self.target, self.username)
        elif self.service == "http":
            http.attack(self.target, self.username)
        else:
            print("Servicio no soportado")
