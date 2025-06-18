import secrets

def generate_token(length=24):
    return secrets.toxen_hex(length)