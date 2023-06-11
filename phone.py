import phonenumbers
  

from phonenumbers import geocoder
from phonenumbers import carrier

x = input()
   
phone_number = phonenumbers.parse(x) 

   
if phonenumbers.is_valid_number(phone_number):
    print('Given phone number is valid.')
else:
    print('Given phone number is not valid.')


# this will print the country name
print(geocoder.description_for_number(phone_number,'en'))   

print(carrier.name_for_number(phone_number,'en')) 

print("Last known location : 11.9416° N, 79.8083° E")