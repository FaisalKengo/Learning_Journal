tc = 0.0

def ktoc(t_kelvin):
    t_celsius = t_kelvin - 273.15
    return t_celsius

def ctok(t_celsius):
    t_kelvin = t_celsius + 273.15
    return t_kelvin

def ktof(t_kelvin):
    t_fahrenheit = (t_kelvin * (9.0 / 5.0)) + 32.0
    return t_fahrenheit

def ctof(t_celsius):
    t_fahrenheit = (t_celsius * (9.0 / 5.0)) + 32.0
    return t_fahrenheit

def ftoc(t_fahrenheit):
    t_celsius = (t_fahrenheit - 32.0) * (5.0 / 9.0)
    return t_celsius

def ftok(t_fahrenheit):
    t_kelvin = (t_fahrenheit - 32.0) * (5.0 / 9.0)
    return t_kelvin

tck = ctok(tc)
print(f"{tc} C = {tck} K")
tkc = ktoc(tck)
print(f"{tck} K = {tkc} C")
tcf = ctof(tkc)
print(f"{tkc} C = {tcf} F")
tkf = ktof(tck)
print(f"{tck} K = {tkf} F")
tfc = ftoc(tcf)
print(f"{tcf} F = {tfc} C")
tfk = ftok(tkf)
print(f"{tkf} F = {tfk} K")