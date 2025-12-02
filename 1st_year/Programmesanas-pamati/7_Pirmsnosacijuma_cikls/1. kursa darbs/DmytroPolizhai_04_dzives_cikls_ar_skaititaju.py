"""
Uzdevums. 
Tu esi tīmekļa administrators. Tev jāraksta algoritmu, izmantojot ciklu ar skaititāju, kas parbauda vai maršrutētāja porti strādā(1) vai nē(0).

Piemērs. 
1 0 1 0 1 0 1 0 0 0 1 0 -> 8
1 0 1 0 -> 2
0 -> 0
1 -> 1

Ievadi.
Portu saraksts (0 vai 1)

Izvadi.
Portu daudzums, kuri strādā.
"""

ports = input().split(" ")
count = 0

for port in ports:
    if port == "1":
        count += 1

print(count)