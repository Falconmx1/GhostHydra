def score_password(pwd, username):
    score = 0

    if username in pwd:
        score += 5
    if any(char.isdigit() for char in pwd):
        score += 2
    if len(pwd) >= 8:
        score += 3
    if "@" in pwd or "!" in pwd:
        score += 2

    return score


def sort_by_score(passwords, username):
    return sorted(passwords, key=lambda p: score_password(p, username), reverse=True)
