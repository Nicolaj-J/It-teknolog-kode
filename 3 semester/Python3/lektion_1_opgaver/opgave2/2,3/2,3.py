from datetime import date

current_year = date.today().year
birth_year = int(input("Indtast fødselsår: "))
print("Du er ", current_year - birth_year, " år")
