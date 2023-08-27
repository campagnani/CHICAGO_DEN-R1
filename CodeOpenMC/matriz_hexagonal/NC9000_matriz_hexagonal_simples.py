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

#Barra combustível:
	#Composição: urânio natural compactado
	#Revestimento: alumínio (Espessura do revestimento?)
	#Quantidade: 			1410
Barra_combustivel_Densidade = 			18.0	#± 0,1 g/cm³.
	#Geometria: Barra anelar
	#Dimensões:
Barra_combustivel_Comprimento       =   21.45   #± 0,5 mm.
Barra_combustivel_Diametro_externo  =   3.07    #± 0,1 mm.
Barra_combustivel_Diametro_interno  =   1.27    #± 0,1 mm.
    #Peso: 				1,867	Kg
		#Peso total: 			2,63	t

#Vareta combustível:
	#Composição: Alumínio
	#Quantidade: 283 (282 com combustível e 1 com a fonte de nêutrons).
	#Dimensões:
Vareta_combustivel_Espessura        = 	0.1     #mm
Vareta_combustivel_Diametro_interno =   3.32    #± 0,2 mm.
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

#Moderador e refletor:
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
moderador.add_element('H', 2)
moderador.add_element('O', 1)
moderador.set_density('g/cm3', 1.0)
 
ar = openmc.Material(name='Ar')
ar.add_element('O', 1)
ar.set_density('g/cm3', 0.001225)

aluminio = openmc.Material(name='Alúminio')
ar.add_element('Al', 1)
ar.set_density('g/cm3', 2.7)

inox = openmc.Material(name='Aço Inox')
inox.add_element('Fe', 80)
inox.add_element('C', 2)
inox.add_element('Cr', 18)
inox.set_density('g/cm3', 8.0)

materiais = openmc.Materials([combustivel,moderador,ar,aluminio,inox])
materiais.export_to_xml()






################################################
############ Definição da Geometria ############
################################################


#Variáveis de Dimenções dos planos
referencia_terra = 0                                            #Fronteira de vácuo
fundo_tanque = referencia_terra + Tanque_Espessura
vareta_altura = fundo_tanque + Vareta_combustivel_Comprimento   #Fronteira de vácuo
lateral_tanque_interna = Tanque_Diametro - Tanque_Espessura
lateral_tanque_externa = Tanque_Diametro

##Planos externos a vareta
grade_inferior = fundo_tanque + Grade_Espessura
refletor_inferior_externo = fundo_tanque + Grade_Posicionamento 
grade_superior = refletor_inferior_externo + Grade_Espessura
refletor_superior_externo = vareta_altura - 6*2.54 #Nível d'água

##Planos internos a vareta
refletor_interno = fundo_tanque + 6.5*2.54
suporte_interno = refletor_interno + 0.2
elemento_combustivel = suporte_interno + Barra_combustivel_Comprimento*5







#Criação das formas geométricas
plano_referencia                = openmc.ZPlane(z0=referencia_terra,boundary_type='vacuum')
plano_vareta_altura             = openmc.ZPlane(z0=referencia_terra,boundary_type='vacuum')
plano_fundo_tanque              = openmc.ZPlane(z0=fundo_tanque)
plano_grade_inferior            = openmc.ZPlane(z0=grade_inferior)
plano_refletor_inferior_externo = openmc.ZPlane(z0=refletor_inferior_externo)
plano_grade_superior            = openmc.ZPlane(z0=grade_superior)
plano_refletor_superior_externo = openmc.ZPlane(z0=refletor_superior_externo)
plano_refletor_interno          = openmc.ZPlane(z0=refletor_interno)
plano_suporte_interno           = openmc.ZPlane(z0=suporte_interno)
plano_elemento_combustivel      = openmc.ZPlane(z0=elemento_combustivel)
cilindro_raio_interno_elemento  = openmc.ZCylinder(r=Barra_combustivel_Diametro_interno/2)
cilindro_raio_externo_elemento  = openmc.ZCylinder(r=Barra_combustivel_Diametro_externo/2)
cilindro_raio_interno_vareta    = openmc.ZCylinder(r=Vareta_combustivel_Diametro_interno/2)
cilindro_raio_externo_vareta    = openmc.ZCylinder(r=Vareta_combustivel_Diametro_interno/2+Vareta_combustivel_Espessura)
cilindro_raio_interno_tanque    = openmc.ZCylinder(r=lateral_tanque_interna/2)
cilindro_raio_externo_tanque    = openmc.ZCylinder(r=lateral_tanque_externa/2, boundary_type='vacuum')


#Celulas para o Universo Vareta Combustível e vareta central
celula_fundo_tanque             = openmc.Cell(fill=aluminio,    region=+plano_referencia&-plano_fundo_tanque)
celula_vareta                   = openmc.Cell(fill=aluminio,    region=+plano_fundo_tanque&-plano_vareta_altura&+cilindro_raio_interno_vareta&-cilindro_raio_externo_vareta)
## Parte Inferior
celula_grade_inferior           = openmc.Cell(fill=aluminio,    region=+plano_fundo_tanque&-plano_grade_inferior&+cilindro_raio_externo_vareta)
celula_refletor_interno         = openmc.Cell(fill=moderador,   region=+plano_fundo_tanque&-plano_suporte_interno&-cilindro_raio_interno_vareta)
celula_refletor_externo         = openmc.Cell(fill=moderador,   region=+plano_grade_inferior&-plano_refletor_inferior_externo&+cilindro_raio_externo_vareta)
## Suporte
celula_suporte_interno          = openmc.Cell(fill=aluminio,    region=+plano_refletor_interno&-plano_suporte_interno&-cilindro_raio_interno_vareta)
## Parte superior
celula_ar_interno_elemento      = openmc.Cell(fill=ar,          region=+plano_suporte_interno&-plano_elemento_combustivel&-cilindro_raio_interno_elemento)
celula_elemento_combustivel     = openmc.Cell(fill=combustivel, region=+plano_suporte_interno&-plano_elemento_combustivel&+cilindro_raio_interno_elemento&-cilindro_raio_externo_elemento)
celula_ar_externo_elemento      = openmc.Cell(fill=ar,          region=+plano_suporte_interno&-plano_elemento_combustivel&+cilindro_raio_externo_elemento&-cilindro_raio_interno_vareta)
celula_grade_superior           = openmc.Cell(fill=aluminio,    region=+plano_refletor_inferior_externo&-plano_grade_superior&+cilindro_raio_externo_vareta)
celula_moderador                = openmc.Cell(fill=moderador,   region=+plano_grade_superior&-plano_refletor_superior_externo&+cilindro_raio_externo_vareta)
celula_ar_superior_interno      = openmc.Cell(fill=ar,          region=+plano_elemento_combustivel&-plano_vareta_altura&-cilindro_raio_interno_vareta)
celula_ar_superior_externo      = openmc.Cell(fill=ar,          region=+plano_refletor_superior_externo&-plano_vareta_altura&cilindro_raio_externo_vareta)

#Celulas específicas para o Universo Vareta Central (fonte)
celula_suporte_interno_fonte    = openmc.Cell(fill=aluminio,    region=+plano_refletor_interno&-plano_suporte_interno&-cilindro_raio_interno_vareta)
celula_moderador_interno_fonte  = openmc.Cell(fill=moderador,   region=+plano_suporte_interno&-plano_vareta_altura&+cilindro_raio_interno_vareta)
celula_ar_interno_fonte         = openmc.Cell(fill=ar,          region=+plano_refletor_superior_externo&-plano_vareta_altura&+cilindro_raio_externo_vareta)

#Celula para universo apenas com refletor
celula_refletor = openmc.Cell(fill=moderador, region=+plano_fundo_tanque&-plano_vareta_altura)

#Celula para definir a lateral do tanque (o fundo do tanque já está definido na matriz hexagonal)
celula_lateral_tanque           = openmc.Cell(fill=inox, region=+cilindro_raio_interno_tanque&-cilindro_raio_externo_tanque&+plano_referencia&-plano_vareta_altura)



#Universos
universo_vareta_combustível     = openmc.Universe(cells=(celula_fundo_tanque,celula_vareta,celula_grade_inferior,celula_refletor_interno,celula_refletor_externo,\
                                                         celula_suporte_interno, celula_ar_interno_elemento, celula_elemento_combustivel,celula_ar_externo_elemento,\
                                                         celula_grade_superior, celula_moderador, celula_ar_superior_interno, celula_ar_superior_externo,))

universo_vareta_central         = openmc.Universe(cells=(celula_fundo_tanque,celula_vareta,celula_grade_inferior,celula_refletor_interno,celula_refletor_externo,\
                                                         celula_suporte_interno_fonte, celula_moderador_interno_fonte,\
                                                         celula_grade_superior, celula_moderador,celula_ar_interno_fonte , celula_ar_superior_externo,))

universo_refletor               = openmc.Universe(cells=(celula_refletor,celula_fundo_tanque,))



#Criação da Matriz Hexagonal

matriz_hexagonal = openmc.HexLattice()
matriz_hexagonal.center = (0., 0.)
matriz_hexagonal.pitch = (2*2.54,)
matriz_hexagonal.outer = universo_refletor
matriz_hexagonal.orientation = 'x'

#print(matriz_hexagonal.show_indices(num_rings=13))

anel_misturado_10 = [universo_refletor]*4 + [universo_vareta_combustível] + [universo_refletor] + [universo_vareta_combustível] + \
                    [universo_refletor]*7 + [universo_vareta_combustível] + [universo_refletor] + [universo_vareta_combustível] + \
                    [universo_refletor]*7 + [universo_vareta_combustível] + [universo_refletor] + [universo_vareta_combustível] + \
                    [universo_refletor]*7 + [universo_vareta_combustível] + [universo_refletor] + [universo_vareta_combustível] + \
                    [universo_refletor]*7 + [universo_vareta_combustível] + [universo_refletor] + [universo_vareta_combustível] + \
                    [universo_refletor]*7 + [universo_vareta_combustível] + [universo_refletor] + [universo_vareta_combustível] + \
                    [universo_refletor]*3
anel_comb_mod_9  = [universo_vareta_combustível]*54
anel_comb_mod_8  = [universo_vareta_combustível]*48
anel_comb_mod_7  = [universo_vareta_combustível]*42
anel_comb_mod_6  = [universo_vareta_combustível]*36
anel_comb_mod_5  = [universo_vareta_combustível]*30
anel_comb_mod_4  = [universo_vareta_combustível]*24
anel_comb_mod_3  = [universo_vareta_combustível]*18
anel_comb_mod_2  = [universo_vareta_combustível]*12
anel_comb_mod_1  = [universo_vareta_combustível]*6
anel_font_mod_0  = [universo_vareta_central]

matriz_hexagonal.universes = [anel_misturado_10, anel_comb_mod_9, anel_comb_mod_8, anel_comb_mod_7, anel_comb_mod_6, anel_comb_mod_5, anel_comb_mod_4, anel_comb_mod_3, anel_comb_mod_2, anel_comb_mod_1, anel_font_mod_0]
print(matriz_hexagonal)
#A celula do reator é preenchida com a matriz_hexagonal e depois água, até chegar na superficie lateral do refletor
celula_reator_matriz_hexagonal  = openmc.Cell(fill=matriz_hexagonal, region=-cilindro_raio_interno_tanque)

############ Exportar Geometrias

geometria = openmc.Geometry([celula_reator_matriz_hexagonal,celula_lateral_tanque])
geometria.export_to_xml()









################################################
############ Plots                  ############
################################################

############ Plotar Secão Transversal

secao_transversal = openmc.Plot.from_geometry(geometria)
secao_transversal.type = 'slice'
secao_transversal.filename = 'plot_secao_transversal'
secao_transversal.pixels = [5000,5000]
secao_transversal.color_by = 'material'
secao_transversal.colors = colors = {
    moderador: 'blue',
    combustivel: 'olive',
    ar: 'white'
}
#secao_transversal.to_ipython_image()

############ Plotar em 3D

plot_3d = openmc.Plot.from_geometry(geometria)
plot_3d.type = 'voxel'
plot_3d.filename = 'plot_voxel'
plot_3d.pixels = (1000, 1000, 1000)
plot_3d.color_by = 'material'
plot_3d.colors = colors = {
    moderador: 'blue',
    combustivel: 'olive',
    ar: 'white'
}
plot_3d.width = (150., 150., 150.)


############ Exportar Plots e Plotar
plotagem = openmc.Plots((secao_transversal, plot_3d))
plotagem.export_to_xml()  
openmc.plot_geometry()
os.system('openmc-voxel-to-vtk plot_voxel.h5 -o plot_voxel.vtk')








################################################
############ Definição da Simulação ############
################################################
settings = openmc.Settings()
settings.particles = 1000
settings.batches = 110
settings.inactive = 10
settings.source = openmc.Source(space=openmc.stats.Point())
settings.export_to_xml()









################################################
############ Definição dos Tallies  ############
################################################
fuel_tally = openmc.Tally()
fuel_tally.filters = [openmc.DistribcellFilter(celula_elemento_combustivel)]
fuel_tally.scores = ['flux']

tallies = openmc.Tallies([fuel_tally])
tallies.export_to_xml()







################################################
############ Executando Código      ############
################################################
openmc.run()
