together = int(input("Cik divatā atrada baravikas? "))
more_mother = int(input("Uz cik vairāk mamma atrada baravikas? "))

janis_mushroom_count = (together - more_mother) // 2
mother_mushroom_count = janis_mushroom_count + more_mother

print(f"Mamma: {mother_mushroom_count}")
print(f"Jānis: {janis_mushroom_count}")