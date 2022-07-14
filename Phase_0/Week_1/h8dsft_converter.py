t_celsius = 0.0

def ktoc(t_kelvin):
    "Konversi Kelvin -> Celsius"
    t_celsius = t_kelvin - 273.15
    return t_celsius

def ctok(t_celsius):
    "Konversi Celsius -> Kelvin"
    t_kelvin = t_celsius + 273.15
    return t_kelvin

def ktof(t_kelvin):
    "Konversi Kelvin -> Fahrenheit"
    t_fahrenheit = (t_kelvin * (9.0 / 5.0)) + 32.0
    return t_fahrenheit

def ctof(t_celsius):
    "Konversi Celsius -> Fahrenheit"
    t_fahrenheit = (t_celsius * (9.0 / 5.0)) + 32.0
    return t_fahrenheit

def ftok(t_fahrenheit):
    "Konversi Fahrenheit -> Kelvin"
    t_kelvin = (t_fahrenheit - 32.0) * (5.0 / 9.0)
    return t_kelvin

def ftoc(t_fahrenheit):
    "Konversi Fahrenheit -> Celsius"
    t_celsius = (t_fahrenheit - 32.0) * (5.0 / 9.0)
    return t_celsius

t_celsiuskelvin = ctok(t_celsius)
print(f"{t_celsius} C = {t_celsiuskelvin} K")
t_kelvincelsius = ktoc(t_celsiuskelvin)
print(f"{t_celsiuskelvin} K = {t_kelvincelsius} C")
t_celsiusfahrenheit = ctof(t_kelvincelsius)
print(f"{t_kelvincelsius} C = {t_celsiusfahrenheit} F")
t_kelvinfahrenheit = ktof(t_celsiuskelvin)
print(f"{t_celsiuskelvin} K = {t_kelvinfahrenheit} F")
t_fahrenheitcelsius = ftoc(t_celsiusfahrenheit)
print(f"{t_celsiusfahrenheit} F = {t_fahrenheitcelsius} C")
t_fahrenheitkelvin = ftok(t_kelvinfahrenheit)
print(f"{t_kelvinfahrenheit} F = {t_fahrenheitkelvin} K")

#Saya masih belum kepikiran bagaimana caranya membuat supaya semua nilainya dinamis,
#mengingat saya masih menetapkan tk sebagai konstanta awal.

#Log_07142022_1330: Saya baru cek lagi, ternyata saya tidak boleh konversi langsung dari Kelvin ke Fahrenheit dan sebaliknya.