import requests
from
file = open("LOTTO_ab_2017.csv", "br")
file=requests.get('http://www.lottotip-check.de')
#csv_reader = csv.reader(file, delimiter=",")
a=[]
for row in file:
    print(row)
    a.append(row)
file.close()
print(len(a))
print(a[len(a)-5])