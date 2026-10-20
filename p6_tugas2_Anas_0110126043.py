i = 1
total = 0
teks_deret = ""

while i <= 19:
    total += i
    teks_deret += str(i)
    if i < 19:
        teks_deret += " + "
    i += 2

print(f"{teks_deret} = {total}")