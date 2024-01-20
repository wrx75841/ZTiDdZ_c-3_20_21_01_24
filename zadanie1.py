import base64 
  
input = "testowy string"
input_bytes = input.encode("ascii") 
  
bity64 = base64.b64encode(input_bytes) 
string = bity64.decode("ascii") 
  
print(f"Encoded string: {string}") 
  
string ="dGVzdG93eSBzdHJpbmc="
bity64 = string.encode("ascii") 
  
input_bytes = base64.b64decode(bity64) 
input = input_bytes.decode("ascii") 
  
print(f"Decoded string: {input}") 