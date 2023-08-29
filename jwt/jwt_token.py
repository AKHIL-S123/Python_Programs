import jwt
from datetime import datetime, timezone,timedelta

key = "secret"


#jwt.encode({"nbf": datetime.now(tz=timezone.utc)}, "secret")
#(example: 2023-08-29 12:00:00 UTC)
nbf_time = datetime(2023, 8, 29, 11, 0, 0, tzinfo=timezone(timedelta(hours=5, minutes=30)))


encoded_jwt = jwt.encode({"nbf": nbf_time}, key, algorithm="HS256")
print("Encoded JWT:", encoded_jwt)

decoded_payload = jwt.decode(encoded_jwt, key, algorithms="HS256")
print("Decoded Payload:", decoded_payload)


