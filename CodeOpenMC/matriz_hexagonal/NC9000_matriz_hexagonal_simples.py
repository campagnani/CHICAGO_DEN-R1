#!/usr/bin/python

import openmc
import os
os.system('clear')

#####################################################
############ CARACTERÍSTICAS DA SUBCRÍTICA ##########
############          DO DEN-UFMG          ##########
#####################################################


#Fabricante: Nuclear Chicago Corporation
#Código: NC-9000
#Finalidade: pesquisa e fins didáticos.
#Inauguração: 17 de dezembro de 1960 no Instituto Tecnológico de Aeronáutica.
#Descomissionamento: 1990?



############ Características construtivas

######### Barra combustível ##########

	#Composição: urânio natural compactado
	#Revestimento: alumínio (0.1 cm de espessura)
clad_combustivel_diametro_externo = 3.07  #cm
clad_combustivel_diametro_interno = 1.27  #cm
	#Quantidade: 			1410
    #Densidade 
Barra_combustivel_Densidade = 			18.0	#± 0,1 g/cm³.
	#Geometria: Barra anelar
	#Dimensões:
Barra_combustivel_Comprimento       =   21.45   #± 0,5 cm.
Barra_combustivel_Diametro_externo  =   2.87    #± 0,1 cm.
Barra_combustivel_Diametro_interno  =   1.47    #± 0,1 cm.
    #Peso: 				1,867	Kg
		#Peso total: 			2,63	t

#Vareta combustível:
	#Composição: Alumínio
	#Quantidade: 283 (282 com combustível e 1 com a fonte de nêutrons).
	#Dimensões:
Vareta_combustivel_Espessura        = 	0.1     #cm
Vareta_combustivel_Diametro_interno =   3.32    #± 0,2 cm.
Vareta_combustivel_Comprimento      =   149.86  #59"

#Interior:
#Parte Superior: 5 barras de combustível em série e ar.
#Parte Inferior: Água
#Suporte/separador:
	#Material: alumínio
	#Altura:
	
#Reticulado:
	#Formato: hexagonal
Reticulado_Distancia=   5 #cm entre os centros de das barras mais próximas.
	
#Tanque:
	#Material: aço inoxidável
	#Dimensões:
Tanque_Altura       =	150
Tanque_Diametro     =	122
Tanque_Espessura    =	1.2

######### Moderador e refletor ##########

    #Tipo: água leve.
    #Obs:  sofre um contínuo tratamento por resinas de deionização. São usadas, em série, duas colunas de resina, uma para os aniontes e outra para os cationtes.
    #Nível: 1350 mm de altura do fundo do tanque
    #Espessura:
		#Fundo: 165mm (distância do fundo a parte mais baixa do comb.)
	    #Lateral: 200mm (distância da última vareta a lateral do tanque)
	    #Superior: 0mm (não é refletido).

#Grade:
    #Função: definir o arranjo
    #Composição: alumínio
    #Dimensões:
Grade_Espessura =   1
Grade_Diametro  =   Tanque_Diametro
    #Quantidade: duas.
    #Posicionamento:
        #Primeira: fundo do tanque
Grade_Posicionamento = 28.4        #Segunda: 28,4 cm do fundo do tanque.

#Fonte de nêutrons:
    #Composição: Plutônio + Berílio
    #Localização: Vareta central

#Diâmetro médio do núcleo: 800 mm




################################################
############ Definição dos Materiais ###########
################################################

combustivel = openmc.Material(name='Uránio Metálico')
combustivel.add_element('U', 1, enrichment=0.711)
combustivel.set_density('g/cm3', Barra_combustivel_Densidade)

moderador = openmc.Material(name='Água Leve')
moderador.add_nuclide('H1', 2)
moderador.add_nuclide('O16', 1)
moderador.set_density('g/cm3', 1.0)
 
ar = openmc.Material(name='Ar')
ar.add_nuclide('O16', 1)
ar.set_density('g/cm3', 0.001225)

aluminio = openmc.Material(name='Alúminio')
aluminio.add_element('Al', 1)
aluminio.set_density('g/cm3', 2.7)

materiais = openmc.Materials([combustivel,moderador,ar,aluminio,])
materiais.cross_sections = "/opt/nuclear-data2/endfb-vii.1-hdf5/cross_sections.xml"
materiais.export_to_xml()

################################################
############ Definição da Geometria ############
################################################


#Variáveis de Dimenções dos planos
fundo_tanque_inferior = 0
fundo_tanque_superior = fundo_tanque_inferior + Tanque_Espessura
vareta_altura = Vareta_combustivel_Comprimento
nivel_dagua = vareta_altura - 6*2.54
lateral_tanque_interna = Tanque_Diametro - (2*Tanque_Espessura)
altura_tanque          = fundo_tanque_inferior + Tanque_Altura

##Planos internos a vareta
refletor_interno_superior = fundo_tanque_superior + 6.5*2.54
suporte_interno_superior = refletor_interno_superior + 0.2
elemento_combustivel = suporte_interno_superior + Barra_combustivel_Comprimento*5

##Planos internos a vareta central
#refletor_interno_central = fundo_tanque + 5*2.54
#suporte_interno_central = refletor_interno + 0.2

clad_comb_1               = suporte_interno_superior + 0.5    #
clad_comb_2               = clad_comb_1  + 20.45     # Fuel
clad_comb_3               = clad_comb_2  + 0.5       
clad_comb_4               = clad_comb_3  + 0.5       #
clad_comb_5               = clad_comb_4  + 20.45     # Fuel
clad_comb_6               = clad_comb_5  + 0.5  
clad_comb_7               = clad_comb_6  + 0.5       #
clad_comb_8               = clad_comb_7  + 20.45     # Fuel
clad_comb_9               = clad_comb_8  + 0.5  
clad_comb_10              = clad_comb_9  + 0.5       #
clad_comb_11              = clad_comb_10 + 20.45     # Fuel
clad_comb_12              = clad_comb_11 + 0.5  
clad_comb_13              = clad_comb_12 + 0.5       #
clad_comb_14              = clad_comb_13 + 20.45     # Fuel
clad_comb_15              = clad_comb_14 + 0.5  

#Criação das formas geométricas

# Planos Horizontais
plano_altura_tanque             = openmc.ZPlane(z0=altura_tanque,)
plano_fundo_tanque_superior     = openmc.ZPlane(z0=fundo_tanque_superior,)
plano_fundo_tanque_inferior     = openmc.ZPlane(z0=fundo_tanque_inferior,)
plano_refletor_interno          = openmc.ZPlane(z0=refletor_interno_superior)
plano_suporte_interno           = openmc.ZPlane(z0=suporte_interno_superior)
plano_elemento_combustivel      = openmc.ZPlane(z0=elemento_combustivel)
plano_vareta_altura             = openmc.ZPlane(z0=vareta_altura)
plano_refletor_lateral_superior = openmc.ZPlane(z0=nivel_dagua)                       

# Especial divisões no combustível
plano_clad_comb_1               = openmc.ZPlane(z0=clad_comb_1)      #
plano_clad_comb_2               = openmc.ZPlane(z0=clad_comb_2 )     # Fuel
plano_clad_comb_3               = openmc.ZPlane(z0=clad_comb_3 )     
plano_clad_comb_4               = openmc.ZPlane(z0=clad_comb_4 )     #
plano_clad_comb_5               = openmc.ZPlane(z0=clad_comb_5 )     # Fuel
plano_clad_comb_6               = openmc.ZPlane(z0=clad_comb_6 )
plano_clad_comb_7               = openmc.ZPlane(z0=clad_comb_7 )     #
plano_clad_comb_8               = openmc.ZPlane(z0=clad_comb_8 )     # Fuel
plano_clad_comb_9               = openmc.ZPlane(z0=clad_comb_9 )
plano_clad_comb_10              = openmc.ZPlane(z0=clad_comb_10)     #
plano_clad_comb_11              = openmc.ZPlane(z0=clad_comb_11)     # Fuel
plano_clad_comb_12              = openmc.ZPlane(z0=clad_comb_12)
plano_clad_comb_13              = openmc.ZPlane(z0=clad_comb_13)     #
plano_clad_comb_14              = openmc.ZPlane(z0=clad_comb_14)     # Fuel
plano_clad_comb_15              = openmc.ZPlane(z0=clad_comb_15)


#plano_suporte_interno_central   = openmc.ZPlane(z0=suporte_interno_central)
#plano_refletor_interno_central  = openmc.ZPlane(z0=refletor_interno_central)

# Superfícies de cilindros

# Combustivel
cilindro_raio_interno_combustivel = openmc.ZCylinder(r=Barra_combustivel_Diametro_interno/2)
cilindro_raio_externo_combustivel = openmc.ZCylinder(r=Barra_combustivel_Diametro_externo/2)
clad_raio_interno_combustivel     = openmc.ZCylinder(r=clad_combustivel_diametro_interno/2)
clad_raio_externo_combustivel     = openmc.ZCylinder(r=clad_combustivel_diametro_externo/2)

# Radial fora do combustivel
cilindro_raio_interno_vareta    = openmc.ZCylinder(r=Vareta_combustivel_Diametro_interno/2)
cilindro_raio_externo_vareta    = openmc.ZCylinder(r=Vareta_combustivel_Diametro_interno/2+Vareta_combustivel_Espessura)
cilindro_raio_interno_tanque    = openmc.ZCylinder(r=lateral_tanque_interna/2)
cilindro_raio_externo_tanque    = openmc.ZCylinder(r=Tanque_Diametro/2)


#Universo Vareta
celula_moderador                = openmc.Cell(fill=moderador,   region=+plano_fundo_tanque_superior&-plano_refletor_lateral_superior&+cilindro_raio_externo_vareta)
celula_refletor_interno         = openmc.Cell(fill=moderador,   region=+plano_fundo_tanque_superior&-plano_refletor_interno&-cilindro_raio_interno_vareta)

celula_clad_vareta              = openmc.Cell(fill=aluminio,    region=+plano_fundo_tanque_superior&-plano_vareta_altura&+cilindro_raio_interno_vareta&-cilindro_raio_externo_vareta)
celula_suporte_interno          = openmc.Cell(fill=aluminio,    region=+plano_refletor_interno&-plano_suporte_interno&-cilindro_raio_interno_vareta)
celula_clad_combustivel_interno = openmc.Cell(fill=aluminio,    region=+plano_suporte_interno&-plano_elemento_combustivel&+clad_raio_interno_combustivel&-cilindro_raio_interno_combustivel)
celula_clad_combustivel_externo = openmc.Cell(fill=aluminio,    region=+plano_suporte_interno&-plano_elemento_combustivel&+cilindro_raio_externo_combustivel&-clad_raio_externo_combustivel)
celula_ar_interno_elemento      = openmc.Cell(fill=ar,          region=+plano_suporte_interno&-plano_elemento_combustivel&-clad_raio_interno_combustivel)
celula_ar_externo_elemento      = openmc.Cell(fill=ar,          region=+plano_suporte_interno&-plano_elemento_combustivel&+clad_raio_externo_combustivel&-cilindro_raio_interno_vareta)
celula_ar_superior_interno      = openmc.Cell(fill=ar,          region=+plano_elemento_combustivel&-plano_vareta_altura&-cilindro_raio_interno_vareta)
celula_ar_externo_vareta        = openmc.Cell(fill=ar,          region=+plano_refletor_lateral_superior&-plano_vareta_altura&+cilindro_raio_interno_vareta)

celula_combustivel_1 = openmc.Cell(fill=combustivel, region=+plano_clad_comb_1&-plano_clad_comb_2&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_combustivel_2 = openmc.Cell(fill=combustivel, region=+plano_clad_comb_4&-plano_clad_comb_5&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_combustivel_3 = openmc.Cell(fill=combustivel, region=+plano_clad_comb_7&-plano_clad_comb_8&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_combustivel_4 = openmc.Cell(fill=combustivel, region=+plano_clad_comb_10&-plano_clad_comb_11&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_combustivel_5 = openmc.Cell(fill=combustivel, region=+plano_clad_comb_13&-plano_clad_comb_14&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)

celula_clad_bottom = openmc.Cell(fill=aluminio, region=+plano_suporte_interno&-plano_clad_comb_1&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_1      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_1&-plano_clad_comb_2&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_2      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_2&-plano_clad_comb_3&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_3      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_3&-plano_clad_comb_4&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_4      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_5&-plano_clad_comb_6&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_5      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_6&-plano_clad_comb_7&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_6      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_8&-plano_clad_comb_9&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_7      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_9&-plano_clad_comb_10&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_8      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_11&-plano_clad_comb_12&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_9      = openmc.Cell(fill=aluminio, region=+plano_clad_comb_12&-plano_clad_comb_13&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
celula_clad_10     = openmc.Cell(fill=aluminio, region=+plano_clad_comb_14&-plano_clad_comb_15&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)

#Celulas específicas para o Universo Vareta Central (fonte)
#celula_refletor_fonte           = openmc.Cell(fill=moderador,   region=+plano_fundo_tanque_superior&-plano_refletor_interno_central&-cilindro_raio_interno_vareta)
#celula_suporte_interno_fonte    = openmc.Cell(fill=aluminio,    region=+plano_refletor_interno_central&-plano_suporte_interno_central&-cilindro_raio_interno_vareta)
#celula_moderador_interno_fonte  = openmc.Cell(fill=moderador,   region=+plano_suporte_interno_central&-plano_vareta_altura&-cilindro_raio_interno_vareta)

#Celula para universo apenas com refletor
celula_refletor                 = openmc.Cell(fill=moderador, region=+plano_fundo_tanque_superior&-plano_refletor_lateral_superior)
celula_ar_externo               = openmc.Cell(fill=ar,        region=+plano_refletor_lateral_superior&-plano_vareta_altura)

#Universos
universo_vareta_combustível     = openmc.Universe(cells=(celula_clad_vareta,celula_refletor_interno, celula_suporte_interno, celula_ar_interno_elemento,
                                                         celula_combustivel_1,celula_combustivel_2, celula_combustivel_3, celula_combustivel_4,
                                                         celula_combustivel_5,celula_ar_externo_elemento, celula_moderador, celula_ar_superior_interno,
                                                         celula_clad_combustivel_interno,celula_clad_combustivel_externo,
                                                         celula_clad_1, celula_clad_2,celula_clad_3,celula_clad_4,celula_clad_5,celula_clad_6,celula_clad_7,
                                                         celula_clad_8,celula_clad_9,celula_clad_10,celula_clad_bottom,celula_ar_externo_vareta))

#universo_vareta_central         = openmc.Universe(cells=(celula_vareta,celula_refletor_fonte,celula_suporte_interno_fonte, \
#                                                         celula_moderador_interno_fonte, celula_moderador))

universo_agua_ar               = openmc.Universe(cells=(celula_refletor,celula_ar_externo,))

#Criação da Matriz Hexagonal

matriz_hexagonal = openmc.HexLattice()
matriz_hexagonal.center = (0., 0.)
matriz_hexagonal.pitch = (2*2.54,)
matriz_hexagonal.outer = universo_agua_ar
matriz_hexagonal.orientation = 'x'

#print(matriz_hexagonal.show_indices(num_rings=13))

anel_misturado_10 = [universo_agua_ar]*4 + [universo_vareta_combustível] + [universo_agua_ar] + [universo_vareta_combustível] + \
                    [universo_agua_ar]*7 + [universo_vareta_combustível] + [universo_agua_ar] + [universo_vareta_combustível] + \
                    [universo_agua_ar]*7 + [universo_vareta_combustível] + [universo_agua_ar] + [universo_vareta_combustível] + \
                    [universo_agua_ar]*7 + [universo_vareta_combustível] + [universo_agua_ar] + [universo_vareta_combustível] + \
                    [universo_agua_ar]*7 + [universo_vareta_combustível] + [universo_agua_ar] + [universo_vareta_combustível] + \
                    [universo_agua_ar]*7 + [universo_vareta_combustível] + [universo_agua_ar] + [universo_vareta_combustível] + \
                    [universo_agua_ar]*3
anel_comb_mod_9  = [universo_vareta_combustível]*54
anel_comb_mod_8  = [universo_vareta_combustível]*48
anel_comb_mod_7  = [universo_vareta_combustível]*42
anel_comb_mod_6  = [universo_vareta_combustível]*36
anel_comb_mod_5  = [universo_vareta_combustível]*30
anel_comb_mod_4  = [universo_vareta_combustível]*24
anel_comb_mod_3  = [universo_vareta_combustível]*18
anel_comb_mod_2  = [universo_vareta_combustível]*12
anel_comb_mod_1  = [universo_vareta_combustível]*6
anel_font_mod_0  = [universo_vareta_combustível]#[universo_vareta_central]

matriz_hexagonal.universes = [anel_misturado_10, anel_comb_mod_9, anel_comb_mod_8, anel_comb_mod_7, anel_comb_mod_6, anel_comb_mod_5, anel_comb_mod_4, anel_comb_mod_3, anel_comb_mod_2, anel_comb_mod_1, anel_font_mod_0]
print(matriz_hexagonal)
#A celula do reator é preenchida com a matriz_hexagonal e depois água, até chegar na superficie lateral do refletor
celula_reator_matriz_hexagonal  = openmc.Cell(fill=matriz_hexagonal, region=-cilindro_raio_interno_tanque&-plano_vareta_altura&+plano_fundo_tanque_superior)

## Celulas externas a matriz hexagonal

#Tanque
celula_tanque = openmc.Cell(fill=aluminio, region=+cilindro_raio_interno_tanque&-cilindro_raio_externo_tanque&+plano_fundo_tanque_superior&-plano_altura_tanque
                                                        | +plano_fundo_tanque_inferior&-plano_fundo_tanque_superior&-cilindro_raio_externo_tanque)

celula_ar_interna_tanque = openmc.Cell(fill=ar, region=-cilindro_raio_interno_tanque&+plano_vareta_altura&-plano_altura_tanque)

# Boundary conditions
fronteira = 10
cilindro_boundary        = openmc.ZCylinder (r=Tanque_Diametro/2 + fronteira, boundary_type='vacuum')
plano_superior_boundary  = openmc.ZPlane    (z0=altura_tanque + fronteira, boundary_type='vacuum')
plano_inferior_boundary  = openmc.ZPlane    (z0=fundo_tanque_inferior - fronteira, boundary_type='vacuum')

celula_ar_externa_tanque = openmc.Cell(fill=ar, region=-cilindro_boundary&-plano_superior_boundary&+plano_altura_tanque
                                                     | -cilindro_boundary&+cilindro_raio_externo_tanque&-plano_altura_tanque&+plano_fundo_tanque_inferior
                                                     | -cilindro_boundary&-plano_fundo_tanque_inferior&+plano_inferior_boundary)

# Universo outer
outer_universe = openmc.Universe(cells=(celula_reator_matriz_hexagonal,celula_tanque,celula_ar_externa_tanque,celula_ar_interna_tanque))
# Célula outer
celula_outer = openmc.Cell(fill=outer_universe, region=-cilindro_boundary&+plano_inferior_boundary&-plano_superior_boundary)

############ Exportar Geometrias

geometria = openmc.Geometry([celula_outer])
geometria.export_to_xml()


################################################
############ Plots                  ############
################################################

############ Plotar Secão Transversal

secao_transversal = openmc.Plot.from_geometry(geometria)
secao_transversal.type = 'slice'
secao_transversal.basis = 'xz'
secao_transversal.width = [200,200]
secao_transversal.origin = (0,0,vareta_altura/2)
secao_transversal.filename = 'plot_secao_transversal'
secao_transversal.pixels = [10000,10000]
secao_transversal.color_by = 'material'
secao_transversal.colors = colors = {
    moderador: 'blue',
    combustivel: 'yellow',
    ar: 'pink',
    aluminio: 'black'
}
#secao_transversal.to_ipython_image()

############ Plotar em 3D

plotar3d = "n"#input("Plortar em 3D? [S/n]")
if (plotar3d!="n"):
    plot_3d = openmc.Plot.from_geometry(geometria)
    plot_3d.type = 'voxel'
    plot_3d.filename = 'plot_voxel'
    plot_3d.pixels = (1000, 1000, 1000)
    plot_3d.color_by = 'material'
    plot_3d.colors = colors = {
        combustivel: 'olive',
        moderador: 'blue',
        ar: 'white',
        aluminio: 'green'
    }
    plot_3d.width = (15., 15., 15.)
    ############ Exportar Plots e Plotar
    plotagem = openmc.Plots((secao_transversal, plot_3d))
    plotagem.export_to_xml()  
    openmc.plot_geometry()
    os.system('openmc-voxel-to-vtk plot_voxel.h5 -o plot_voxel')
else:
    ############ Exportar Plots e Plotar
    plotagem = openmc.Plots((secao_transversal,))
    plotagem.export_to_xml()  
    openmc.plot_geometry()









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
#fuel_tally = openmc.Tally()
#fuel_tally.filters = [openmc.DistribcellFilter(celula_elemento_combustivel)]
#fuel_tally.scores = ['flux']
#
#tallies = openmc.Tallies([fuel_tally])
#tallies.export_to_xml()







################################################
############ Executando Código      ############
################################################
openmc.run()
