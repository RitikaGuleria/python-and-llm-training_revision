first_name = 'Ritika'
last_name = 'Guleria'

print(f'Her name is {first_name} {last_name}')

# Indexing
print(first_name[0]) #R
print(first_name[0:6:1]) #last is exclusive #Ritika
print(first_name[0:6:2]) #Rtk
print(first_name[:6]) #Ritika
print(first_name[2:]) #tika
print(first_name[::-1]) #aikitR 

# Encoding
special_char = 'Ritika Gulēria'
encoded_text = special_char.encode('utf-8')
print(encoded_text)
print(encoded_text.decode('utf-8')) # Decoding



