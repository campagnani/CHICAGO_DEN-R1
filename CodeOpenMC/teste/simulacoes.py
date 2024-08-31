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
chicago = libChicagoDenR1.ChigagoDenR1(altura_fonte=0,particulas=10000,ciclos=100)
chicago.tallies()
