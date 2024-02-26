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

# Plotar 2D em 3 vistas e plotar em 3D *SEM FONTE*
libChicagoDenR1.mkdir(voltar=False, nome="Plots_sem_fonte", data=False)
chicago = libChicagoDenR1.ChigagoDenR1()
chicago.geometriaAgua()
chicago.plot2D_secao_transversal_agua('xy')
chicago.plot2D_secao_transversal_agua('yz')
chicago.plot2D_secao_transversal_agua('xz')
chicago.plot3D_agua()

# Plotar 2D em 3 vistas e plotar em 3D *COM FONTE*
libChicagoDenR1.mkdir(voltar=True, nome="Plots_com_fonte", data=False)
chicago = libChicagoDenR1.ChigagoDenR1()
chicago.geometriaFonte()
chicago.plot2D_secao_transversal_fonte('xy')
chicago.plot2D_secao_transversal_fonte('yz')
chicago.plot2D_secao_transversal_fonte('xz')
chicago.plot3D_fonte()

# Calcular Keff
libChicagoDenR1.mkdir(voltar=True, nome="keff", data=False)
chicago = libChicagoDenR1.ChigagoDenR1(material="u_nat", particulas=1000, ciclos=100, inativo=10, fonte=False)
chicago.geometriaAgua()
chicago.run()

# Operaçao com fonte fixa
libChicagoDenR1.mkdir(voltar=True, nome="fonte", data=False)
chicago = libChicagoDenR1.ChigagoDenR1(material="u_nat", particulas=1000, ciclos=100, inativo=10, fonte=True)
chicago.geometriaFonte()
chicago.run()