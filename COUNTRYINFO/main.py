from countryinfo import CountryInfo

davlat = input("Davlat nomini kiriting: ")

try:
    country = CountryInfo(davlat)

    print("\n--- Davlat haqida ma'lumot ---")
    print("Poytaxti:", country.capital())
    print("Aholisi:", country.population())
    print("Hududi:", country.area(), "km²")
    print("Asosiy tillari:", country.languages())
    print("Valyutasi:", country.currencies())
    print("Mintaqa:", country.region())

except Exception as xato:
    print("Xatolik yuz berdi! Davlat nomini to‘g‘ri kiriting.")