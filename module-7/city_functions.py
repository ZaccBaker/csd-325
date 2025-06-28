
def city_country(city, country, population=0, language=''):
    place = f'{city.title()}, {country.title()}'

    if population != 0:
        place += f' - population {population}'

    if language != '':
        place += f', {language.title()}'

    return place

if __name__ == "__main__":

    print(city_country('Papillion','United states',population='210000',language='English'))
    print(city_country('Copenhagen','Denmark',population='8500000',language='Danish'))
    print(city_country('Seoul','South Korea',population='4000000',language='Korean'))