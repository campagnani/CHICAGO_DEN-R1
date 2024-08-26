#######################################################################
#######################################################################
####                                                               ####
####              UNIVERSIDADE FEDERAL DE MINAS GERAIS             ####
####               Departamento de Engenharia Nuclear              ####
####                   Thalles Oliveira Campagnani                 ####
####                 Jefferson Quintão Campos Duarte               ####
####                                                               ####
#######################################################################
####                                                               ####
####               Código para executar as simulações              ####
####      Dados são processados posteriomente em outro código      ####
####                                                               ####
#######################################################################
#######################################################################

import simulacoes

# Entre na pasta "com_fonte"
simulacoes.libChicagoDenR1.chdir(nome="com_fonte")
# Crie a pasta dados_DATA para armazenar os dados processados
simulacoes.libChicagoDenR1.mkdir(nome="dados",data=True)
# Processe
simulacoes.chicago_cf.process_tallies_radial()
