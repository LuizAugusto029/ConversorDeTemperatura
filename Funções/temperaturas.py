# Converter de °C para °F
def celsius_fahr(Tcelsius):
    temp_celsius = Tcelsius
    fahr = temp_celsius * (9.0 / 5.0) + 32.0
    return f'{fahr:.1f}'


# Converter de °C para °K
def celsius_kelvin(Tcelsius):
    temp_celsius = Tcelsius
    kelvin = temp_celsius + 273.15
    return f'{kelvin:.1f}'


# Converter de °F para °C
def fahr_celsius(Tfahr):
    temp_fahr = Tfahr
    celsius = 5.0 * (temp_fahr - 32.0)/9.0
    return f'{celsius:.1f}'


# Converter de °F para °K
def fahr_kelvin(Tfahr):
    temp_fahr = Tfahr
    kelvin = (temp_fahr - 32) * 5/9 + 273.15
    return f'{kelvin:.1f}'


# Converter de °K para °C
def kelvin_celsius(Tkelvin):
    temp_kelvin = Tkelvin
    celsius = temp_kelvin - 273.15
    return f'{celsius:.1f}'


# Converter de °K para °F
def kelvin_fahr(Tkelvin):
    temp_kelvin = Tkelvin
    fahr = (temp_kelvin - 273.15) * 9/5 + 32
    return f'{fahr:.1f}'

