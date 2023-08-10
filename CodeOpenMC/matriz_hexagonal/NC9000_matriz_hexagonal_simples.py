import openmc

################################################
############ Definição dos Materiais ###########
################################################
combustivel = openmc.Material(name='Uránio Metálico')
combustivel.add_element('U', 1, enrichment=0.711)
combustivel.set_density('g/cm3', 18.0)

moderador = openmc.Material(name='Água Leve')
moderador.add_element('H', 2)
moderador.add_element('O', 1)
moderador.set_density('g/cm3', 1.0)
 
ar = openmc.Material(name='Ar')
ar.add_element('O', 1)
ar.set_density('g/cm3', 0.001225)

materiais = openmc.Materials([combustivel,moderador,ar])
materiais.export_to_xml()






################################################
############ Definição da Geometria ############
################################################

limite_superior = openmc.ZPlane(z0=21.45*5/2,boundary_type='vacuum') #Barra combustível:	Dimensões: Comprimento: 	214,5	± 0,5 mm.
limite_inferior = openmc.ZPlane(z0=-21.45*5/2,boundary_type='vacuum')

re_ar                           = openmc.ZCylinder(r=3.32/2)                                           #Vareta combustível:      Diâmetro Interno:	33,2 	± 0,2 mm.
celula_ar_moderador_central     = openmc.Cell(fill=ar,  region=-re_ar & -limite_superior & +limite_inferior)
celula_moderador_central        = openmc.Cell(fill=moderador, region=+re_ar & -limite_superior & +limite_inferior)
universo_fonte_moderador        = openmc.Universe(cells=(celula_ar_moderador_central, celula_moderador_central))

re_barra_combustivel            = openmc.ZCylinder(r=3.07/2)                                           #Barra combustível:  Dimensões:  Diâmetro externo: 	30,7	± 0,1 mm.
ri_barra_combustivel            = openmc.ZCylinder(r=1.27/2)                                           #Barra combustível:  Dimensões:  Diâmetro interno: 	12,7	± 0,1 mm.
celula_ar                       = openmc.Cell     (fill=ar, region= -ri_barra_combustivel & -limite_superior & +limite_inferior)
celula_combustivel              = openmc.Cell     (fill=combustivel, region= +ri_barra_combustivel & -re_barra_combustivel & -limite_superior & +limite_inferior)
celula_moderador                = openmc.Cell     (fill=moderador,   region= +re_barra_combustivel  & -limite_superior & +limite_inferior)
universo_combustivel_moderador  = openmc.Universe (cells=(celula_ar,celula_combustivel, celula_moderador))

celula_refletor = openmc.Cell(fill=moderador, region= -limite_superior & +limite_inferior)
universo_refletor = openmc.Universe(cells=(celula_refletor,))

matriz_hexagonal = openmc.HexLattice()
matriz_hexagonal.center = (0., 0.)
matriz_hexagonal.pitch = (2*2.54,)                                                                        #Reticulado:   Distância: 5 cm entre os centros de das barras mais próximas.
matriz_hexagonal.outer = universo_refletor
matriz_hexagonal.orientation = 'x'

#print(matriz_hexagonal.show_indices(num_rings=13))

anel_misturado_10 = [universo_refletor]*4 + [universo_combustivel_moderador] + [universo_refletor] + [universo_combustivel_moderador] + \
                    [universo_refletor]*7 + [universo_combustivel_moderador] + [universo_refletor] + [universo_combustivel_moderador] + \
                    [universo_refletor]*7 + [universo_combustivel_moderador] + [universo_refletor] + [universo_combustivel_moderador] + \
                    [universo_refletor]*7 + [universo_combustivel_moderador] + [universo_refletor] + [universo_combustivel_moderador] + \
                    [universo_refletor]*7 + [universo_combustivel_moderador] + [universo_refletor] + [universo_combustivel_moderador] + \
                    [universo_refletor]*7 + [universo_combustivel_moderador] + [universo_refletor] + [universo_combustivel_moderador] + \
                    [universo_refletor]*3
anel_comb_mod_9  = [universo_combustivel_moderador]*54
anel_comb_mod_8  = [universo_combustivel_moderador]*48
anel_comb_mod_7  = [universo_combustivel_moderador]*42
anel_comb_mod_6  = [universo_combustivel_moderador]*36
anel_comb_mod_5  = [universo_combustivel_moderador]*30
anel_comb_mod_4  = [universo_combustivel_moderador]*24
anel_comb_mod_3  = [universo_combustivel_moderador]*18
anel_comb_mod_2  = [universo_combustivel_moderador]*12
anel_comb_mod_1  = [universo_combustivel_moderador]*6
anel_font_mod_0  = [universo_fonte_moderador]

matriz_hexagonal.universes = [anel_misturado_10,
    anel_comb_mod_9,
    anel_comb_mod_8,
    anel_comb_mod_7,
    anel_comb_mod_6,
    anel_comb_mod_5,
    anel_comb_mod_4,
    anel_comb_mod_3,
    anel_comb_mod_2,
    anel_comb_mod_1,
    anel_font_mod_0]
print(matriz_hexagonal)

superficie_reator = openmc.ZCylinder(r=120.8/2, boundary_type='vacuum')       #Tanque:    Dimensões:  Diâmetro:	1220 mm     Espessura:	12 mm
celula_reator = openmc.Cell(fill=matriz_hexagonal, region=-superficie_reator)
geometry = openmc.Geometry([celula_reator])
geometry.export_to_xml()

secao_transversal = openmc.Plot.from_geometry(geometry)
secao_transversal.filename = 'plot_secao_transversal'
secao_transversal.pixels = [5000,5000]
secao_transversal.color_by = 'material'
secao_transversal.colors = colors = {
    moderador: 'blue',
    combustivel: 'olive',
    ar: 'white'
}
secao_transversal.to_ipython_image()







################################################
############ Definição da Simulação ############
################################################
settings = openmc.Settings()
settings.particles = 10000
settings.batches = 110
settings.inactive = 10
settings.source = openmc.Source(space=openmc.stats.Point())
settings.export_to_xml()





################################################
############ Definição dos Tallies  ############
################################################
fuel_tally = openmc.Tally()
fuel_tally.filters = [openmc.DistribcellFilter(celula_combustivel)]
fuel_tally.scores = ['flux']

tallies = openmc.Tallies([fuel_tally])
tallies.export_to_xml()




################################################
############ Executando Código      ############
################################################
openmc.run()
