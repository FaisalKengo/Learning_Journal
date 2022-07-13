tk = 0.0

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

tkc = ktoc(tk)
print(f"{tk} K = {tkc} C")
tck = ctok(tkc)
print(f"{tkc} C = {tck} K")
tkf = ktof(tck)
print(f"{tck} K = {tkf} F")
tcf = ctof(tkc)
print(f"{tkc} C = {tcf} F")
tfk = ftok(tkf)
print(f"{tkf} F = {tfk} K")
tfc = ftoc(tcf)
print(f"{tcf} F = {tfc} C")

#Saya masih belum kepikiran bagaimana caranya membuat supaya semua nilainya dinamis,
#mengingat saya masih menetapkan tk sebagai konstanta awal.