from app.auth import hash_password, verify_password, create_access_token

password = "123456"

hashed = hash_password(password)

print("Hashed:", hashed)

print("Verify:", verify_password(password, hashed))

token = create_access_token({"sub": "satwant@gmail.com"})

print("JWT:", token)