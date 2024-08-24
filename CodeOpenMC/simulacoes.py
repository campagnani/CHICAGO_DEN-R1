#######################################################################
####                                                               ####
####              UNIVERSIDADE FEDERAL DE MINAS GERAIS             ####
####               Departamento de Engenharia Nuclear              ####
####                   Thalles Oliveira Campagnani                 ####
####                 Jefferson Quintão Campos Duarte               ####
####                                                               ####
#######################################################################

import libChicagoDenR1

# Cria uma pasta para armazenar todos resultados com a data do teste
libChicagoDenR1.mkdir(voltar=False, nome="resultados", data=True)

#####################################################
############     SIMULAÇÃO SEM FONTE       ##########
#####################################################

# Cria uma pasta para simulações sem fonte
libChicagoDenR1.mkdir(nome="sem_fonte")
## Cria reator sem fonte e define configurações de simulação
chicago = libChicagoDenR1.ChigagoDenR1(particulas=10000, ciclos=220, inativo=20)
## Plota vistas 2D
chicago.plot2D_secao_transversal('xy')
chicago.plot2D_secao_transversal('yz')
chicago.plot2D_secao_transversal('xz')
## Executa simulação
chicago.run()

#####################################################
############     SIMULAÇÃO COM FONTE       ##########
#####################################################

# Cria uma pasta para simulações com fonte
libChicagoDenR1.mkdir(nome="com_fonte")
## Cria reator sem fonte e define configurações de simulação
chicago = libChicagoDenR1.ChigagoDenR1(altura_fonte=50, particulas=1000, ciclos=100)
## Plota vistas 2D
chicago.plot2D_secao_transversal('xy',)
chicago.plot2D_secao_transversal('xy',origin=(0,0,-72.5))
chicago.plot2D_secao_transversal('yz')
chicago.plot2D_secao_transversal('xz')
## Constroi Tallies
### Tallies basicos
chicago.tallies_nu()
chicago.tallies_fission()
### Tallies espaciais
chicago.t_energy_filter_thermal_fast()
chicago.tallies_radial()
chicago.tallies_axial()
chicago.tallies_carteziano()
### Tallies espectrais
chicago.t_energy_filter_espectrum_log()
chicago.tallies_espectro()
### Gera XML dos talies
chicago.export_tallies()
## Executa simulação
chicago.run()