import openmc
import matplotlib.pyplot as plt

# Define materials
water_material = openmc.Material(1, "Water")
water_material.add_nuclide('H1', 2.0)
water_material.add_nuclide('O16', 1.0)
water_material.set_density('g/cm3', 1.0)

uranium_material = openmc.Material(2, "Uranium")
uranium_material.add_nuclide('U235', 1.0)
uranium_material.set_density('g/cm3', 19.1)

materiais = openmc.Materials([uranium_material,water_material])
materiais.export_to_xml()

# Create the water cell
water_cell = openmc.Cell(1, "Water Cell")
water_cell.fill = water_material

# Create the uranium cylinder
cylinder_radius = 0.5
cylinder_height = 4.0
uranium_cylinder = openmc.ZCylinder(r=cylinder_radius)
uranium_cell = openmc.Cell(2, "Uranium Cell")
uranium_cell.fill = uranium_material
uranium_cell.region = -uranium_cylinder

# Add the cells to a universe
universe = openmc.Universe(cells=[water_cell, uranium_cell])

# Create a geometry and set the root universe
geometry = openmc.Geometry(universe)

# Define the settings for the simulation
settings = openmc.Settings()
settings.batches = 10
settings.particles = 1000
settings.run_mode = 'fixed source'

# Define the source
source = openmc.Source()
source.space = openmc.stats.Point((0, 0, 0))
source.angle = openmc.stats.Isotropic()
source.energy = openmc.stats.Discrete([14e6], [1])
settings.source = source

# Create a model and set the geometry and settings
#model = openmc.model.Model(geometry, settings)

# Run the simulation
#model.run()

plot = openmc.Plot()
plot.basis = 'xz'
plot.origin = (5.0, 2.0, 3.0)
plot.width = (50., 50.)
plot.pixels = (400, 400)

plot.color_by = 'material'
plot.colors = {
    water_material: 'blue',
    uranium_material: 'black'
}


plots = openmc.Plots([plot])
plots.export_to_xml()
openmc.plot_geometry(plot)