#######################################################################
####                                                               ####
####              UNIVERSIDADE FEDERAL DE MINAS GERAIS             ####
####               Departamento de Engenharia Nuclear              ####
####                   Thalles Oliveira Campagnani                 ####
####                 Jefferson Quintão Campos Duarte               ####
####                                                               ####
#######################################################################

import libChicagoDenR1

libChicagoDenR1.mkdir(voltar=False, nome="resultadosSimulações", data=True)

# Plotar 2D em 3 vistas e plotar em 3D
libChicagoDenR1.mkdir(voltar=False, nome="Plots", data=False)
chicago = libChicagoDenR1.ChigagoDenR1()
chicago.plot2D_secao_transversal('xy')
chicago.plot2D_secao_transversal('yz')
chicago.plot2D_secao_transversal('xz')
chicago.plot3D()

# Calcular Keff
libChicagoDenR1.mkdir(voltar=True, nome="keff", data=False)
chicago = libChicagoDenR1.ChigagoDenR1() 
chicago.run()

# keff
libChicagoDenR1.mkdir(voltar=True, nome="fonte", data=False)
chicago = libChicagoDenR1.ChigagoDenR1(fonte=True)
chicago.run()