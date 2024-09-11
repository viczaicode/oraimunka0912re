
atmero = int(input("Kérlek adj meg egy egész számot(kör átmérője lesz): "))


def keruletszamitas(atmero):
    sugar = atmero / 2
    return 2 * 3.14159 * sugar

def teruletszamitas(atmero):
    sugar = atmero / 2
    return 3.14159 * sugar ** 2


kerulet = keruletszamitas(atmero)
terulet = teruletszamitas(atmero)

print(f"Kör kerülete: {kerulet}")
print(f"Kör területe: {terulet}")

