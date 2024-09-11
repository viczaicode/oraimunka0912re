a = int(input("Kérlek adj meg egy egész számot(teglalap a oldala lesz): "))
b = int(input("Kérlek adj meg egy egész számot(teglalap b oldala lesz): "))

def keruletszamitas(a, b):
    return 2 * (a + b)


def teruletszamitas(a, b):
    return a * b

kerulet = keruletszamitas(a, b)
terulet = teruletszamitas(a, b)

print(f"Téglalap kerülete: {kerulet}")
print(f"Téglalap területe: {terulet}")
