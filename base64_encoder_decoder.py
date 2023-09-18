import base64

#Decode

original_cookie_string = input('Paste value to decode from base64: ')
original_cookie_bytes = original_cookie_string.encode('ascii')
  
cookie_string_bytes = base64.b64decode(original_cookie_bytes)
cookie_string = cookie_string_bytes.decode('ascii')
  
print(f'Decoded string: {cookie_string}')

#Encode

decoded_cookie_string = input('Paste value to encode in base64: ')
decoded_cookie_bytes = decoded_cookie_string.encode('ascii')

encoded_cookie = base64.b64encode(decoded_cookie_bytes)
encoded_cookie_string = encoded_cookie.decode('ascii')

print('Decoded value is = ', encoded_cookie_string)