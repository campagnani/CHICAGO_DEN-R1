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
chicago.run(nodesMPI=24, hostfile="hostfile.txt",)
chicago.run(nodesMPI=24, hosts=[
    "nuclear215",
    "nuclear214",
    "nuclear213",
    "nuclear212",
    "nuclear206",
    "nuclear205",
    ])
