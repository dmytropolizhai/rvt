mark = int(input('Ievadiet atzīmi par "Sazarotas struktūras algoritmi": '))

if mark >= 6:
    if mark <= 8: # 6 < mark < 8
        print('Macību tēma "Sazarotas struktūras algoritmi" ir apgūtā uz optimālo apguves līmeni.')
    
    else: # Lielāks par 8
        print('Macību tēma "Sazarotas struktūras algoritmi" ir apgūtā uz augstāko apguves līmeni.')
else:
    print('Macību tēma "Sazarotas struktūras algoritmi" nav apgūtā uz optimālu apguves līmeni.')