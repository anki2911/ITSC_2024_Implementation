import hashlib
import hmac

key = "123456"
message = "WB0824"

# Create an HMAC object using SHA-512 as the hash function
#h = hmac.new(key.encode(), message.encode(), hashlib.sha512)

h = hmac.new(key.encode(), message.encode(), hashlib.sha512)

# Get the hexadecimal representation of the HMAC
hmac_hex = h.hexdigest()
print(hmac_hex)
