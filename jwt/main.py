import jwt
import time
import datetime
from datetime import datetime,timezone,timedelta
key = "secret"
payload={"my name is ": "akhil"}
encoded = jwt.encode(payload,key, algorithm="HS256")
print("encoded jwt : ",encoded)
decoded=jwt.decode(encoded, key, algorithms="HS256")
print("decoded jwt : ", decoded)
print(jwt.get_unverified_header(encoded))
indian_timezone = timezone(timedelta(hours=5, minutes=30))
x=jwt.encode({"exp": datetime.now(tz=indian_timezone)+ timedelta(seconds=20)},key,algorithm="HS256")
print(x)
y=jwt.decode(x,key,algorithms="HS256")
print(y)
print(jwt.decode(x, key, leeway=250, algorithms=["HS256"]))
