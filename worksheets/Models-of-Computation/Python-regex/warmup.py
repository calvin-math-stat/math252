import re
import requests

# Download St. Augustine’s confessions from CCEL and print it
url = 'https://www.ccel.org/ccel/augustine/confess.txt'
r = requests.get(url)
book = r.text
print(len(book))
print(book[1015:1120])

numbers = re.compile(r"\d+")

print(numbers.findall(book[1:2000]))

url = "https://calvin.edu/academics/departments-programs/mathematics-statistics/faculty-staff/"
url = "https://calvin.edu"
mathstat = requests.get(url).text

print(len(mathstat))

phone = re.compile(r"\(?(\d{3})[ .)-]*(\d{3})[ .-]*(\d{4})")
email = re.compile(r"\w+@[a-zA-Z.]+")
print(phone.findall(mathstat))
print(email.findall(mathstat))
