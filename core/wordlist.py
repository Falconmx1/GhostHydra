def generate_wordlist(username):
    base = ["1234", "admin", "password"]

    smart = [
        username + "123",
        username + "2024",
        username + "@123",
        username + "!",
    ]

    return base + smart
