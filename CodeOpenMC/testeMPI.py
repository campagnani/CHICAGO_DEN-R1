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
chicago.run(nodesMPI=52, hostfile="hostfile.txt",)
chicago.run(nodesMPI=52, hosts=[
    #HOST,        #CORES
    "nuclear215", #8
    "nuclear214", #8
    "nuclear213", #8
    "nuclear212", #6
    "nuclear206", #16
    "nuclear205", #8
    ])
