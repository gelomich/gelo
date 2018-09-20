# ROZLICZENIOWY CZAS PRACY
# Pobrać liczbę przepracowanych godzin w tygodniu
# Pobrać stawkę bazową za godzinę
# Standardowy czas pracy 35h w tygodniu
# Stawka za nadgodziny: jeśli mniej niż 11 to stawka bazowa * 1.5 per godzina
# Stawka za nadgodziny: jeżeli więcej niż 10 to stawka bazowa * 2 per godzina
# Obliczyć wypłatę za tydzień pracy

worked_hours = input("Podaj liczbę przepracowanych godzin: ")
base_salary = input("Podaj wysokość bazowej stawki godzinowej: ")

worked_hours = float(worked_hours)
base_salary = float(base_salary)
regular_hours = 35
overtime_small = 10
overtime_factor_small = 1.5
overtime_factor_large = 2

if worked_hours <= regular_hours:
    basetime_salary = worked_hours * base_salary
    overtime_salary_small = 0
    overtime_salary_large = 0
elif worked_hours <= regular_hours + overtime_small:
    basetime_salary = regular_hours * base_salary
    overtime_salary_small = (worked_hours - regular_hours) * \
                            overtime_factor_small * base_salary
    overtime_salary_large = 0
else:
    basetime_salary = regular_hours * base_salary
    overtime_salary_small = (worked_hours - regular_hours) * \
                            overtime_factor_small
    overtime_salary_large = (worked_hours - regular_hours - overtime_small) * \
                            overtime_factor_large * \
                            base_salary

full_salary = basetime_salary + overtime_salary_small + overtime_salary_large
print("Twoja wypłata to: {:.2f}".format(full_salary))