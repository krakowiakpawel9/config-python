import base64

# encode to base64
string = b'password'
encodedString = base64.b64encode(string)
print(encodedString)

# decode string from base64
decodedString = base64.b64decode(encodedString)
print(decodedString)
