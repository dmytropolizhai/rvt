mikus_paid = int(input("Cik Mikus samaksāja par konfektēm? "))
maris_paid = int(input("Cik Maris samaksāja par konfektēm? "))
maris_candy_more = int(input("Uz cik vairāk Maris nopirka konfektas nekā Mikus? "))

mikus_candy_count = (maris_candy_more * mikus_paid) // (maris_paid - mikus_paid)
candy_price = mikus_paid // mikus_candy_count

print(f"Cik nopirka Mikus: {mikus_candy_count}")
print(f"Konfektes cena: {candy_price}")
