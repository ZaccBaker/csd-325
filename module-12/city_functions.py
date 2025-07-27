
def city_country(city, country, language='', population=0):

    place = '{}, {}'.format(city,country).title()

    if population != 0:
        place += ' - population {}'.format(population)
    
    if language != '':
        place += ', {}'.format(language).title()

    return place


if __name__ == "__main__":

    print(city_country('papillion', 'united states'))
    print(city_country('copenhagen', 'denmark',population='8500000'))
    print(city_country('seoul', 'south korea',population='4000000',language='korean'))