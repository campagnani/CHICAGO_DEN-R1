#######################################################################
####                                                               ####
####              UNIVERSIDADE FEDERAL DE MINAS GERAIS             ####
####               Departamento de Engenharia Nuclear              ####
####                   Thalles Oliveira Campagnani                 ####
####                 Jefferson Quintão Campos Duarte               ####
####                                                               ####
#######################################################################

import libChicagoDenR1

libChicagoDenR1.mkdir(voltar=False, nome="resultados", data=True)

# Plotar 2D em 3 vistas e plotar em 3D *SEM FONTE*
libChicagoDenR1.mkdir(voltar=False, nome="Plots_sem_fonte", data=False)
chicago = libChicagoDenR1.ChigagoDenR1(fonte=False)
chicago.plot2D_secao_transversal('xy')
chicago.plot2D_secao_transversal('yz')
chicago.plot2D_secao_transversal('xz')
chicago.plot3D()

# Plotar 2D em 3 vistas e plotar em 3D *COM FONTE*
libChicagoDenR1.mkdir(voltar=True, nome="Plots_com_fonte", data=False)
chicago = libChicagoDenR1.ChigagoDenR1(fonte=True)
chicago.plot2D_secao_transversal('xy')
chicago.plot2D_secao_transversal('yz')
chicago.plot2D_secao_transversal('xz')
chicago.plot3D()

# Calcular Keff
#libChicagoDenR1.mkdir(voltar=True, nome="keff", data=False)
#chicago = libChicagoDenR1.ChigagoDenR1(material="u_nat", particulas=10000, ciclos=220, inativo=20, fonte=False)
#chicago.run()
##
### Operaçao com fonte fixa
#libChicagoDenR1.mkdir(voltar=True, nome="fonte", data=False)
#chicago = libChicagoDenR1.ChigagoDenR1(material="u_nat", particulas=10000, ciclos=220, inativo=20, fonte=True)
#chicago.run()