import shelve

tup = ("ABC", "DEF", "MNO", "PKL", "QOK")

triagle_areas = {}
for name in tup:
    S = float(input(f"Area of triagle {name}: "))
    triagle_areas[name] = S

#Записати у бінарний файл
with shelve.open("file1.dat") as db:
    db["triagle_areas"] = triagle_areas

#Прочитати бінарний файл і вивести найбільшу площу
with shelve.open("file1.dat", "c") as db:
    triagle_areas = db["triagle_areas"]

max_triangle = max(triagle_areas, key=triagle_areas.get)
max_area = triagle_areas[max_triangle]
print(max_triangle, max_area)
