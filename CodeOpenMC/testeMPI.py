#######################################################################
####                                                               ####
####              UNIVERSIDADE FEDERAL DE MINAS GERAIS             ####
####               Departamento de Engenharia Nuclear              ####
####                   Thalles Oliveira Campagnani                 ####
####                 Jefferson Quintão Campos Duarte               ####
####                                                               ####
#######################################################################

import libChicagoDenR1

chicago = libChicagoDenR1.ChigagoDenR1(material="u_nat", particulas=100000, ciclos=400, inativo=40, fonte=False)
chicago.run(mpi=38)
