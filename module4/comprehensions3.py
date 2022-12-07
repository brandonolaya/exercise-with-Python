# For the following list of temperatures in Fahrenheit,
# express these same values ​​in a new list of temperature
# values ​​in Celsius. The conversion between types of
# units is as follows:

# °C = (°F - 32) * (5/9)


temperature_fahrenheit = [32, 212, 275]
degrees_celsius = [(n-32) * (5/9) for n in temperature_fahrenheit]