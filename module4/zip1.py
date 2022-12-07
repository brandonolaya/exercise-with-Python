##Use the zip function, loops, and the following lists of
#  countries and capitals to solve it quickly and efficiently.

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

the_tuple = list(zip(countries,capitals))
for country, capital in the_tuple:
    print(f'The capital of {country} is {capital}')