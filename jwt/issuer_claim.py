import jwt

# Set the issuer claim
issuer = "https://example.com"

# Create a payload dictionary
payload = {
    "iss": issuer,
    "exp": 1693377000,  # Expiration time in Unix timestamp format
    "nbf": 1693290600, # Not before time in Unix timestamp format
    'akhil': "my name is akhil"
}

# Sign the token with a secret key
key = "my_secret_key"
token = jwt.encode(payload, key, algorithm="HS256")

# Print the token
print(token)
print(jwt.decode(token,key,algorithms="HS256"))
