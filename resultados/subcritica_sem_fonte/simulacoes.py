#######################################################################
####                                                               ####
####              UNIVERSIDADE FEDERAL DE MINAS GERAIS             ####
####               Departamento de Engenharia Nuclear              ####
####                   Thalles Oliveira Campagnani                 ####
####                 Jefferson Quintão Campos Duarte               ####
####                                                               ####
#######################################################################

import libChicagoDenR1
libChicagoDenR1.simu = True

# FONTE FIXA

#chicago = libChicagoDenR1.ChigagoDenR1(altura_fonte=0, fonte=True, particulas=10000000, ciclos=100)
#chicago.plot2D_secao_transversal(basis="xz",width=[142,170],pixels=[15000,15000],origin=(0,0,0))
#chicago.plot2D_secao_transversal(basis='xy',width=[142,142],pixels=[15000,15000],origin=(0,0,0))
#chicago.plot2D_secao_transversal(basis='yz',width=[142,170],pixels=[15000,15000],origin=(0,0,0))
#chicago.plot2D_secao_transversal('xz',width=[142,170])
#chicago.tallies()

# AUTOVALOR

chicago = libChicagoDenR1.ChigagoDenR1(altura_fonte=0, fonte=False, particulas=10000000, ciclos=1000, inativo=200)
chicago.tallies_basicos()
chicago.run()