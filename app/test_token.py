from jose import jwt

SECRET_KEY = "hello123"  
ALGORITHM = "HS256"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2LCJleHAiOjE3NjAwNzkyNzB9.9AC-j5qONkojBIziutW53gaWbnFMNleZ1nwnsgJZGro"
decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print(decoded)
