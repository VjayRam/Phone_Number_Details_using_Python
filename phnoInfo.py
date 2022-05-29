import phonenumbers
from phonenumbers import geocoder, carrier, timezone

num = input("Enter phone number with country code: ")
phno = phonenumbers.parse(num)

print(geocoder.description_for_number(phno,'en'))
print(carrier.name_for_number(phno,'en'))
print(timezone.time_zones_for_number(phno))