from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "hello123"  
ALGORITHM = "HS256"

# Generate a fresh token instead of using hardcoded one
data = {"user_id": 6}
expire = datetime.utcnow() + timedelta(minutes=60)
to_encode = data.copy()
to_encode.update({"exp": expire})
token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Now decode it
decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print(decoded)
