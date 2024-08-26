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

import libChicagoDenR1

if __name__!="__main__":
    libChicagoDenR1.simu = False  

if libChicagoDenR1.simu:
    # Cria uma pasta para armazenar todos resultados com a data do teste e copie os inputs python
    libChicagoDenR1.mkdir(voltar=False, nome="resultados", data=True, cpinputs=True)

#####################################################
############     SIMULAÇÃO SEM FONTE       ##########
#####################################################

if libChicagoDenR1.simu:
    # Cria uma pasta para simulações sem fonte
    libChicagoDenR1.mkdir(voltar=False,nome="sem_fonte")

## Cria reator sem fonte e define configurações de simulação
chicago_sf = libChicagoDenR1.ChigagoDenR1(particulas=10000, ciclos=220, inativo=20)
## Plota vistas 2D
chicago_sf.plot2D_secao_transversal('xy')
chicago_sf.plot2D_secao_transversal('yz')
chicago_sf.plot2D_secao_transversal('xz')
## Executa simulação
chicago_sf.run()

#####################################################
############     SIMULAÇÃO COM FONTE       ##########
#####################################################

if libChicagoDenR1.simu:
    # Cria uma pasta para simulações com fonte
    libChicagoDenR1.mkdir(nome="com_fonte")

## Cria reator sem fonte e define configurações de simulação
chicago_cf = libChicagoDenR1.ChigagoDenR1(altura_fonte=50, particulas=10000, ciclos=100)
## Plota vistas 2D
chicago_cf.plot2D_secao_transversal('xy',)
chicago_cf.plot2D_secao_transversal('xy',origin=(0,0,-72.5))
chicago_cf.plot2D_secao_transversal('yz')
chicago_cf.plot2D_secao_transversal('xz')
## Constroi Tallies
### Tallies basicos
chicago_cf.tallies_nu()
chicago_cf.tallies_fission()
### Tallies espaciais
chicago_cf.t_energy_filter_thermal_fast()
chicago_cf.tallies_radial()
chicago_cf.tallies_axial()
chicago_cf.tallies_carteziano()
### Tallies espectrais
chicago_cf.t_energy_filter_espectrum_log()
chicago_cf.tallies_espectro()
### Gera XML dos talies
chicago_cf.export_tallies()
## Executa simulação
chicago_cf.run()
