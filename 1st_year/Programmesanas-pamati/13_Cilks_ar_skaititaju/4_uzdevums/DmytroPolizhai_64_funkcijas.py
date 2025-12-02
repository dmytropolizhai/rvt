"""
12. uzdevums

Pieprasa lietotāja ievadīt egles līmeņu daudzums un izvadas egle, izmantojot "*" simbolu

Izveidoja: Dmytro Polizhai
"""

n = int(input("Ievadiet egles līmeņu daudzums: "))

for i in range(1, 2 * n, 2):
  print(" " * (n - i // 2), "*" * i) 

print(" " * n + "| |")

print(" " * n + '''
█   █ ███ ██  ██  █ █     ███ █ █ ██  ███  ██ ███ █   █  █   ██ 
██ ██ █   █ █ █ █ █ █     █   █ █ █ █  █  █    █  ██ ██ ███ █   
█ █ █ ██  ██  ██   █      █   ███ ██   █  █    █  █ █ █ █ █ █   
█   █ █   █ █ █ █  █      █   █ █ █ █  █   █   █  █   █ ███  █  
█   █ █   █ █ █ █  █      █   █ █ █ █  █    █  █  █   █ █ █   █ 
█   █ ███ █ █ █ █  █      ███ █ █ █ █ ███ ██   █  █   █ █ █ ██  
''')