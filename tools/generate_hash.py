import bcrypt

password = "Adminkpu2026!"

hashed = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print(hashed.decode("utf-8"))