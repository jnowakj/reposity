def dodawanie(x, y):
	return x + y

def odejmowanie(x, y):
	return x - y

def mnozenie(x, y):
	return x * y

def dzielenie(x, y):
	if y != 0:
		return  x / y
	else:
		return "Nie można dzielić przez 0."

liczba1 = float(input("Podaj pierwsza liczbę:"))
liczba2 = float(input("Podaj drugą liczbę:"))

print("Wynik działania:")
print("Dodawanie:", dodawanie(liczba1,liczba2))
print("Odejmowanie:", odejmowanie(liczba1, liczba2))
print("Mnożenie:", mnozenie(liczba1,liczba2))
print("Dzielenie:", dzielenie(liczba1,liczba2))
