# from pygal.i18n import COUNTRIES
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


# print(get_country_code('Andorra'))
# print(get_country_code('United Arab'))
# print(get_country_code('Afghanistan'))