from elements.models import *
import requests
import json

def populate_db():
    url = 'https://periodic-table-elements-info.herokuapp.com/elements'
    source = requests.get(url)
    source = source.text
    data = json.loads(source)
    for i in data:
        try:
            element = Element.objects.get(symbol=i['symbol'])
        except:
            element = Element(symbol=i['symbol'])
            element.save()
        element.atomic_number = i['atomicNumber']
        element.name = i['name']
        element.atomic_mass = i['atomicMass']
        element.electronic_configuration = i['electronicConfiguration']
        if i['electronegativity'] != 'unknown':
            element.electronegativity = i['electronegativity']
        if i['atomicRadius'] != 'unknown':
            element.atomic_radius = i['atomicRadius']
        element.ion_radius = i['ionRadius']
        element.vanderwaalsradius = i['vanDerWaalsRadius']
        if i['ionizationEnergy'] != 'unknown':
            element.ionization_energy = i['ionizationEnergy']
        element.electron_afinity = i['electronAffinity']
        element.oxidation_states = i['oxidationStates']
        element.standard_state = i['standardState']
        element.bonding_type = i['bondingType']
        if i['meltingPoint'] != 'unknown':
            element.melting_point = i['meltingPoint']
        if i['boilingPoint'] != 'unknown':
            element.boiling_point = i['boilingPoint']
        if i['density'] != 'unknown':
            element.density = i['density']
        element.group_block = i['groupBlock']
        element.block = i['block']
        if i['yearDiscovered'] != 'unknown':
            element.year_discovered = i['yearDiscovered']
        element.cpx_hex_color = i['cpkHexColor']
        element.period = i['period']
        element.group = i['group']
        print(element.symbol, element.group)
        element.save()
        if element.name == 'Boron':
            element.period = 2
            element.save()
        print(element, 'saved succesfully!')
