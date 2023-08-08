#import numpy as np
import openmc

# Create materials
combustivel = openmc.Material(name='Dióxido de Uránio')
combustivel.add_element('U', 1, enrichment=2.0)
combustivel.add_element('O', 2)
combustivel.set_density('g/cm3', 10.400)

moderador = openmc.Material(name='Água Leve')
moderador.add_element('H', 2)
moderador.add_element('O', 1)
moderador.set_density('g/cm3', 1.0)

materiais = openmc.Materials([combustivel,moderador])
materiais.export_to_xml()


# Create geometry

geometry = openmc.Geometry()
geometry.export_to_xml()

# Assign simulation settings
settings = openmc.Settings()
settings.export_to_xml()

openmc.run() 
