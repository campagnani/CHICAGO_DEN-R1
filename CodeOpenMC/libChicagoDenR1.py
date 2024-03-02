#!/usr/bin/python

from datetime import datetime
import openmc
import numpy as np
import os
os.system('clear')


def mkdir(nome="teste_sem_nome",data=True,voltar=False):
    if (voltar==True):
        os.chdir("../")
    if (data==True):
        agora = datetime.now()
        nome = agora.strftime(nome+"_%Y%m%d_%H%M%S")
    if not os.path.exists(nome):
        os.makedirs(nome)
    os.chdir(nome)
    
def chdir(nome=None):
    if (nome != None):
        os.chdir(nome)
    else:
        diretorio_atual = os.getcwd()
        diretorios = [diretorio for diretorio in os.listdir(diretorio_atual) if os.path.isdir(os.path.join(diretorio_atual, diretorio))]

        data_mais_recente = 0
        pasta_mais_recente = None

        for diretorio in diretorios:
            data_criacao = os.path.getctime(os.path.join(diretorio_atual, diretorio))
            if data_criacao > data_mais_recente:
                data_mais_recente = data_criacao
                pasta_mais_recente = diretorio

        if pasta_mais_recente:
            os.chdir(os.path.join(diretorio_atual, pasta_mais_recente))
            print("Diretório mais recente encontrado:", pasta_mais_recente)
        else:
            print("Não foi possível encontrar um diretório mais recente.")


#####################################################
############ CARACTERÍSTICAS DA SUBCRÍTICA ##########
############          DO DEN-UFMG          ##########
#####################################################

class ChigagoDenR1:

    def __init__(self, material="u_nat", fonte=False, particulas=1000, ciclos=100, inativo=10):
        #Definindo Material
        if(material=="u_nat"):
            self.material = self.u_nat()
        else:
            self.__del__(self)
        
        #Definindo geometria
        self.geometriaPadrao(fonte)

        #Definindo simulação
        self.configuracoes(fonte=fonte,particulas=particulas,ciclos=ciclos,inativo=inativo)
        
    def __del__(self):
        print(f"Objeto destruído.")

    def u_nat(self, tempCombustivel=294,tempModerador=294, densidadeCombustivel=18.0, densidadeModerador=1.0):
        print("################################################")
        print("############ Definição dos Materiais ###########")
        print("############          U_nat          ###########")
        print("################################################")

        self.combustivel = openmc.Material(name='Uránio Natural')
        self.combustivel.add_nuclide('U234', 5.50000E-05, percent_type='ao')
        self.combustivel.add_nuclide('U235', 7.20000E-03, percent_type='ao')
        self.combustivel.add_nuclide('U238', 9.92745E-01, percent_type='ao')
        self.combustivel.set_density('g/cm3', densidadeCombustivel)

        self.moderador = openmc.Material(name='Água Leve')
        self.moderador.add_nuclide('H1' , 1.1187E-01 , percent_type='wo')
        self.moderador.add_nuclide('H2' , 3.3540E-05 , percent_type='wo')
        self.moderador.add_nuclide('O16', 8.8574E-01 , percent_type='wo')
        self.moderador.add_nuclide('O17', 3.5857E-04 , percent_type='wo')
        self.moderador.add_nuclide('O18', 1.9982E-03 , percent_type='wo')
        self.moderador.set_density('g/cm3', densidadeModerador)
        
        self.ar = openmc.Material(name='Ar')
        self.ar.add_nuclide('N14' , 7.7826E-01 , percent_type='ao')
        self.ar.add_nuclide('N15' , 2.8589E-03 , percent_type='ao')
        self.ar.add_nuclide('O16' , 1.0794E-01 , percent_type='ao')
        self.ar.add_nuclide('O17' , 1.0156E-01 , percent_type='ao')
        self.ar.add_nuclide('O18' , 3.8829E-05 , percent_type='ao')
        self.ar.add_nuclide('Ar36', 2.6789E-03 , percent_type='ao')
        self.ar.add_nuclide('Ar38', 3.4177E-03 , percent_type='ao')
        self.ar.add_nuclide('Ar40', 3.2467E-03 , percent_type='ao')
        self.ar.set_density('g/cm3', 0.001225)

        self.aluminio = openmc.Material(name='Alúminio')
        self.aluminio.add_nuclide('Al27', 1 , percent_type ='wo')
        self.aluminio.set_density('g/cm3', 2.7)

        self.SS304 = openmc.Material(name='Aço INOX')
        self.SS304.add_nuclide('C12',   2.9639E-04, percent_type = 'wo')
        self.SS304.add_nuclide('C13',   3.6051E-06, percent_type = 'wo')
        self.SS304.add_nuclide('N14',   9.9608E-04, percent_type = 'wo')
        self.SS304.add_nuclide('N15',   3.9196E-06, percent_type = 'wo')
        self.SS304.add_nuclide('S32',   2.8424E-04, percent_type = 'wo')
        self.SS304.add_nuclide('S33',   2.3137E-06, percent_type = 'wo')
        self.SS304.add_nuclide('S34',   1.3380E-05, percent_type = 'wo')
        self.SS304.add_nuclide('S36',   6.7303E-08, percent_type = 'wo')
        self.SS304.add_nuclide('P31',   4.5000E-04, percent_type = 'wo')
        self.SS304.add_nuclide('Si28',  6.8905E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Si29',  3.6136E-04, percent_type = 'wo')
        self.SS304.add_nuclide('Si30',  2.4813E-04, percent_type = 'wo')
        self.SS304.add_nuclide('Fe54',  3.6055E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Fe56',  5.8692E-01, percent_type = 'wo')
        self.SS304.add_nuclide('Fe57',  1.3797E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Fe58',  1.8683E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Mn55',  2.0000E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Cr50',  3.3926E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Cr52',  6.8034E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Cr53',  7.8631E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Cr54',  1.9942E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Ni58',  8.0637E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Ni60',  3.2131E-02, percent_type = 'wo')
        self.SS304.add_nuclide('Ni61',  1.4202E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Ni62',  4.6012E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Ni64',  1.2103E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Mo92',  3.5544E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Mo94',  2.2637E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Mo95',  3.9375E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Mo96',  4.1688E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Mo97',  2.4118E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Mo98',  6.1566E-03, percent_type = 'wo')
        self.SS304.add_nuclide('Mo100', 2.5073E-03, percent_type = 'wo')
        self.SS304.set_density('g/cm3', 8.0)

        self.fonte = openmc.Material(name='Plutonio Berilio')
        self.fonte.add_nuclide('Pu239', percent=1, percent_type='wo')
        self.fonte.add_nuclide('Be9', percent=3, percent_type='wo')
        self.fonte.set_density('g/cm3', 15.0)

        self.materiais = openmc.Materials([self.combustivel,self.moderador,self.ar,self.aluminio,self.SS304,self.fonte,])
        self.materiais.cross_sections = '/opt/nuclear-data/endfb-viii.0-hdf5/cross_sections.xml' 
        self.materiais.export_to_xml()
        
        #Já definir as cores dos materiais para futuros plots
        self.colors = {
            self.moderador: 'blue',
            self.combustivel: 'yellow',
            self.ar: 'pink',
            self.aluminio: 'black',
            self.SS304: 'brown',
            self.fonte: 'red'
        }


    def geometriaPadrao(self, fonte = True):
        print("################################################")
        print("############ Definição da Geometria ############")
        print("################################################")

        #Fabricante: Nuclear Chicago Corporation
        #Código: NC-9000
        #Finalidade: pesquisa e fins didáticos.
        #Inauguração: 17 de dezembro de 1960 no Instituto Tecnológico de Aeronáutica.
        #Descomissionamento: 1990?
        ############ Características construtivas

        ######### Barra combustível ##########

            #Composição: urânio natural compactado
            #Revestimento: alumínio (0.1 cm de espessura)
        clad_combustivel_diametro_externo = 3.07  #cm
        clad_combustivel_diametro_interno = 1.27  #cm
            #Quantidade: 			1410
            #Densidade 
        Barra_combustivel_Densidade = 			18.0	#± 0,1 g/cm³.
            #Geometria: Barra anelar
            #Dimensões:
        Barra_combustivel_Comprimento       =   21.45   #± 0,5 cm.
        Barra_combustivel_Diametro_externo  =   2.87    #± 0,1 cm.
        Barra_combustivel_Diametro_interno  =   1.47    #± 0,1 cm.
            #Peso: 				1,867	Kg
                #Peso total: 			2,63	t

        #Vareta combustível:
            #Composição: Alumínio
            #Quantidade: 283 (282 com combustível e 1 com a fonte de nêutrons).
            #Dimensões:
        Vareta_combustivel_Espessura        = 	0.1     #cm
        Vareta_combustivel_Diametro_interno =   3.32    #± 0,2 cm.
        Vareta_combustivel_Comprimento      =   59*2.54  #59"

        #Interior:
        #Parte Superior: 5 barras de combustível em série e ar.
        #Parte Inferior: Água
        #Suporte/separador:
            #Material: alumínio
            #Altura:
            
        #Reticulado:
            #Formato: hexagonal
        Reticulado_Distancia=   5 #cm entre os centros de das barras mais próximas.
            
        #Tanque:
            #Material: aço inoxidável
            #Dimensões:
        Tanque_Altura       =	152.5
        Tanque_Diametro     =	122
        Tanque_Espessura    =	1.2

        ######### Moderador e refletor ##########

            #Tipo: água leve.
            #Obs:  sofre um contínuo tratamento por resinas de deionização. São usadas, em série, duas colunas de resina, uma para os aniontes e outra para os cationtes.
            #Nível: 1350 mm de altura do fundo do tanque
            #Espessura:
                #Fundo: 165mm (distância do fundo a parte mais baixa do comb.)
                #Lateral: 200mm (distância da última vareta a lateral do tanque)
                #Superior: 0mm (não é refletido).

        #Grade:
            #Função: definir o arranjo
            #Composição: alumínio
            #Dimensões:
        Grade_Espessura  =   1   # em altura
        Grade_ressalto   =   0.4 # Altura do ressalto / apoio da barra
        Grade_Diametro   =   101 #cm 
            #Quantidade: duas.
            #Posicionamento:
                #Primeira: fundo do tanque
        Grade_Posicionamento = 26.0        # Em relação a grade de baixo (cm)

        #Fonte de nêutrons:
            #Composição: Plutônio + Berílio
            #Localização: Vareta central

        #Diâmetro médio do núcleo: 800 mm

        #Variáveis de Dimenções dos planos
        fundo_tanque_inferior = -Tanque_Altura/2
        fundo_tanque_superior = fundo_tanque_inferior + Tanque_Espessura
        lateral_tanque_interna = Tanque_Diametro - (2*Tanque_Espessura)
        altura_tanque          = fundo_tanque_inferior + Tanque_Altura
        nivel_dagua = altura_tanque - 6*2.54
        grade_inferior_down = fundo_tanque_superior + 2.54
        grade_interior_ressalto = grade_inferior_down + Grade_ressalto
        grade_inferior_up   = grade_inferior_down + Grade_Espessura
        grade_superior_down = grade_inferior_up + Grade_Posicionamento
        grade_superior_up   = grade_superior_down + Grade_Espessura
        vareta_altura       = grade_interior_ressalto + Vareta_combustivel_Comprimento

        ##Planos internos a vareta
        refletor_interno_superior = grade_inferior_down + 6.5*2.54
        suporte_interno_superior = refletor_interno_superior + 0.2
        elemento_combustivel = suporte_interno_superior + Barra_combustivel_Comprimento*5

        clad_comb_1               = suporte_interno_superior + 0.5    #
        clad_comb_2               = clad_comb_1  + 20.45     # Fuel
        clad_comb_3               = clad_comb_2  + 0.5       
        clad_comb_4               = clad_comb_3  + 0.5       #
        clad_comb_5               = clad_comb_4  + 20.45     # Fuel
        clad_comb_6               = clad_comb_5  + 0.5  
        clad_comb_7               = clad_comb_6  + 0.5       #
        clad_comb_8               = clad_comb_7  + 20.45     # Fuel
        clad_comb_9               = clad_comb_8  + 0.5  
        clad_comb_10              = clad_comb_9  + 0.5       #
        clad_comb_11              = clad_comb_10 + 20.45     # Fuel
        clad_comb_12              = clad_comb_11 + 0.5  
        clad_comb_13              = clad_comb_12 + 0.5       #
        clad_comb_14              = clad_comb_13 + 20.45     # Fuel
        clad_comb_15              = clad_comb_14 + 0.5  

        #Criação das formas geométricas

        # Planos Horizontais
        plano_grade_superior_1          = openmc.ZPlane(z0=grade_superior_down,)
        plano_grade_superior_2          = openmc.ZPlane(z0=grade_superior_up,)
        plano_ressalto_grade            = openmc.ZPlane(z0=grade_interior_ressalto)
        plano_grade_inferior_1          = openmc.ZPlane(z0=grade_inferior_down,)
        plano_grade_inferior_2          = openmc.ZPlane(z0=grade_inferior_up,)
        plano_altura_tanque             = openmc.ZPlane(z0=altura_tanque,)
        plano_beirada_altura_tanque     = openmc.ZPlane(z0=altura_tanque - 1.2)
        plano_divisao_altura_tanque_sup = openmc.ZPlane(z0=altura_tanque - 76 + 1.2)
        plano_divisao_altura_tanque_inf = openmc.ZPlane(z0=altura_tanque - 76 - 1.2)
        plano_fundo_tanque_superior     = openmc.ZPlane(z0=fundo_tanque_superior,)
        plano_fundo_tanque_inferior     = openmc.ZPlane(z0=fundo_tanque_inferior,)
        plano_refletor_interno          = openmc.ZPlane(z0=refletor_interno_superior)
        plano_suporte_interno           = openmc.ZPlane(z0=suporte_interno_superior)
        plano_elemento_combustivel      = openmc.ZPlane(z0=elemento_combustivel)
        plano_vareta_altura             = openmc.ZPlane(z0=vareta_altura)
        plano_refletor_lateral_superior = openmc.ZPlane(z0=nivel_dagua)                       

        # Especial divisões no combustível
        plano_clad_comb_1               = openmc.ZPlane(z0=clad_comb_1)      #
        plano_clad_comb_2               = openmc.ZPlane(z0=clad_comb_2 )     # Fuel
        plano_clad_comb_3               = openmc.ZPlane(z0=clad_comb_3 )     
        plano_clad_comb_4               = openmc.ZPlane(z0=clad_comb_4 )     #
        plano_clad_comb_5               = openmc.ZPlane(z0=clad_comb_5 )     # Fuel
        plano_clad_comb_6               = openmc.ZPlane(z0=clad_comb_6 )
        plano_clad_comb_7               = openmc.ZPlane(z0=clad_comb_7 )     #
        plano_clad_comb_8               = openmc.ZPlane(z0=clad_comb_8 )     # Fuel
        plano_clad_comb_9               = openmc.ZPlane(z0=clad_comb_9 )
        plano_clad_comb_10              = openmc.ZPlane(z0=clad_comb_10)     #
        plano_clad_comb_11              = openmc.ZPlane(z0=clad_comb_11)     # Fuel
        plano_clad_comb_12              = openmc.ZPlane(z0=clad_comb_12)
        plano_clad_comb_13              = openmc.ZPlane(z0=clad_comb_13)     #
        plano_clad_comb_14              = openmc.ZPlane(z0=clad_comb_14)     # Fuel
        plano_clad_comb_15              = openmc.ZPlane(z0=clad_comb_15)


        #plano_suporte_interno_central   = openmc.ZPlane(z0=suporte_interno_central)
        #plano_refletor_interno_central  = openmc.ZPlane(z0=refletor_interno_central)

        # Superfícies de cilindros

        # Combustivel
        cilindro_raio_interno_combustivel = openmc.ZCylinder(r=Barra_combustivel_Diametro_interno/2)
        cilindro_raio_externo_combustivel = openmc.ZCylinder(r=Barra_combustivel_Diametro_externo/2)
        clad_raio_interno_combustivel     = openmc.ZCylinder(r=clad_combustivel_diametro_interno/2)
        clad_raio_externo_combustivel     = openmc.ZCylinder(r=clad_combustivel_diametro_externo/2)

        # Radial fora do combustivel
        cilindro_raio_interno_vareta    = openmc.ZCylinder(r=Vareta_combustivel_Diametro_interno/2)
        cilindro_raio_externo_vareta    = openmc.ZCylinder(r=Vareta_combustivel_Diametro_interno/2+Vareta_combustivel_Espessura)
        cilindro_raio_interno_tanque    = openmc.ZCylinder(r=lateral_tanque_interna/2)
        cilindro_raio_externo_tanque    = openmc.ZCylinder(r=Tanque_Diametro/2)
        cilindro_raio_externo_grade     = openmc.ZCylinder(r=Grade_Diametro/2)

        # Ressalto da grade
        cilindro_ressalto = openmc.ZCylinder(r=(Vareta_combustivel_Diametro_interno/2+Vareta_combustivel_Espessura)/2-0.2)

        # Beirada externa do tanque
        cilindro_beirada_tanque = openmc.ZCylinder(r=Tanque_Diametro/2+3.0)

        # Células Vareta
        self.celula_moderador1               = openmc.Cell(fill=self.moderador,   region=+plano_fundo_tanque_superior&-plano_grade_inferior_1&+cilindro_raio_externo_vareta)
        self.celula_moderador2               = openmc.Cell(fill=self.moderador,   region=+plano_grade_inferior_2&-plano_grade_superior_1&+cilindro_raio_externo_vareta)
        self.celula_moderador3               = openmc.Cell(fill=self.moderador,   region=+plano_grade_superior_2&-plano_refletor_lateral_superior&+cilindro_raio_externo_vareta)
        self.celula_refletor_interno         = openmc.Cell(fill=self.moderador,   region=+plano_ressalto_grade&-plano_refletor_interno&-cilindro_raio_interno_vareta
                                                          | +plano_grade_inferior_1&-plano_ressalto_grade&-cilindro_ressalto
                                                          | +plano_fundo_tanque_superior&-plano_grade_inferior_1&-cilindro_raio_externo_vareta)

        self.celula_clad_vareta              = openmc.Cell(fill=self.aluminio,    region=+plano_ressalto_grade&-plano_vareta_altura&+cilindro_raio_interno_vareta&-cilindro_raio_externo_vareta)
        self.celula_suporte_interno          = openmc.Cell(fill=self.aluminio,    region=+plano_refletor_interno&-plano_suporte_interno&-cilindro_raio_interno_vareta)
        self.celula_clad_combustivel_interno = openmc.Cell(fill=self.aluminio,    region=+plano_suporte_interno&-plano_elemento_combustivel&+clad_raio_interno_combustivel&-cilindro_raio_interno_combustivel)
        self.celula_clad_combustivel_externo = openmc.Cell(fill=self.aluminio,    region=+plano_suporte_interno&-plano_elemento_combustivel&+cilindro_raio_externo_combustivel&-clad_raio_externo_combustivel)

        self.celula_ar_interno_elemento      = openmc.Cell(fill=self.ar,          region=+plano_suporte_interno&-plano_elemento_combustivel&-clad_raio_interno_combustivel)
        self.celula_ar_externo_elemento      = openmc.Cell(fill=self.ar,          region=+plano_suporte_interno&-plano_elemento_combustivel&+clad_raio_externo_combustivel&-cilindro_raio_interno_vareta)
        self.celula_ar_superior_interno      = openmc.Cell(fill=self.ar,          region=+plano_elemento_combustivel&-plano_vareta_altura&-cilindro_raio_interno_vareta)
        self.celula_ar_externo_vareta        = openmc.Cell(fill=self.ar,          region=+plano_refletor_lateral_superior&-plano_vareta_altura&+cilindro_raio_externo_vareta)

        self.celula_combustivel_1 = openmc.Cell(fill=self.combustivel, region=+plano_clad_comb_1&-plano_clad_comb_2&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_combustivel_2 = openmc.Cell(fill=self.combustivel, region=+plano_clad_comb_4&-plano_clad_comb_5&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_combustivel_3 = openmc.Cell(fill=self.combustivel, region=+plano_clad_comb_7&-plano_clad_comb_8&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_combustivel_4 = openmc.Cell(fill=self.combustivel, region=+plano_clad_comb_10&-plano_clad_comb_11&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_combustivel_5 = openmc.Cell(fill=self.combustivel, region=+plano_clad_comb_13&-plano_clad_comb_14&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)

        self.celula_clad_bottom = openmc.Cell(fill=self.aluminio, region=+plano_suporte_interno&-plano_clad_comb_1&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_1      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_1&-plano_clad_comb_2&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_2      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_2&-plano_clad_comb_3&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_3      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_3&-plano_clad_comb_4&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_4      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_5&-plano_clad_comb_6&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_5      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_6&-plano_clad_comb_7&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_6      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_8&-plano_clad_comb_9&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_7      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_9&-plano_clad_comb_10&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_8      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_11&-plano_clad_comb_12&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_9      = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_12&-plano_clad_comb_13&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)
        self.celula_clad_10     = openmc.Cell(fill=self.aluminio, region=+plano_clad_comb_14&-plano_clad_comb_15&+cilindro_raio_interno_combustivel&-cilindro_raio_externo_combustivel)

        # Celulas grade de espaçamento (construída de cima para baixo)
        self.celula_ressalto_inferior = openmc.Cell(fill=self.aluminio, region=+plano_grade_inferior_1&-plano_ressalto_grade&+cilindro_ressalto)
        self.celula_grade_inferior    = openmc.Cell(fill=self.aluminio, region=+plano_ressalto_grade&-plano_grade_inferior_2&+cilindro_raio_externo_vareta)        
        self.celula_grade_superior    = openmc.Cell(fill=self.aluminio, region=+plano_grade_superior_1&-plano_grade_superior_2&+cilindro_raio_externo_vareta)        

        ####################################################################################################################################
        ############################### Celulas e superfícies específicas para o Universo Vareta Central (fonte)############################
        ####################################################################################################################################

        ##Planos internos a vareta central
        suporte_interno_central = fundo_tanque_superior + 5*2.54
        refletor_inferior_interno_central = suporte_interno_central - 0.2
        limite_fonte_inferior              = suporte_interno_central + 0.1
        limite_fonte_superior              = suporte_interno_central + 19.9
        limite_clad_fonte_superior        = suporte_interno_central + 20
        diametro_cilindro_fonte = 2.9 # cm
        diametro_clad_fonte     = 3.0 # cm

        plano_superior_suporte_fonte = openmc.ZPlane(z0=suporte_interno_central)
        plano_inferior_suporte_fonte = openmc.ZPlane(z0=refletor_inferior_interno_central)
        plano_superior_fonte         = openmc.ZPlane(z0=limite_fonte_superior)
        plano_inferior_fonte         = openmc.ZPlane(z0=limite_fonte_inferior)
        plano_clad_fonte_superior    = openmc.ZPlane(z0=limite_clad_fonte_superior)

        superficie_radial_fonte      = openmc.ZCylinder(r=diametro_cilindro_fonte/2)
        superficie_radial_clad_fonte = openmc.ZCylinder(r=diametro_clad_fonte/2)

        self.celula_refletor_inferior_fonte  = openmc.Cell(fill=self.moderador,   region=+plano_fundo_tanque_superior&-plano_inferior_suporte_fonte&-cilindro_raio_interno_vareta)
        self.celula_suporte_interno_fonte    = openmc.Cell(fill=self.aluminio,    region=+plano_inferior_suporte_fonte&-plano_superior_suporte_fonte&-cilindro_raio_interno_vareta)
        self.celula_fonte                    = openmc.Cell(fill=self.fonte,   region=+plano_inferior_fonte&-plano_superior_fonte&-superficie_radial_fonte)  #trocar para a fonte
        self.celula_clad_fonte               = openmc.Cell(fill=self.aluminio,    region=+plano_inferior_fonte&-plano_superior_fonte&-superficie_radial_clad_fonte&+superficie_radial_fonte
                                                                        | +plano_superior_suporte_fonte&-plano_inferior_fonte&-superficie_radial_clad_fonte
                                                                        | +plano_superior_fonte&-plano_clad_fonte_superior&-superficie_radial_clad_fonte)  #trocar para aço inox
        self.celula_refletor_lateral_fonte   = openmc.Cell(fill=self.moderador,   region=+plano_superior_suporte_fonte&-plano_clad_fonte_superior&-cilindro_raio_interno_vareta&+superficie_radial_clad_fonte)
        self.celula_refletor_superior_fonte  = openmc.Cell(fill=self.moderador,   region=+plano_clad_fonte_superior&-plano_refletor_lateral_superior&-cilindro_raio_interno_vareta)

        # CÉLULAS QUE FORAM DUPLICADAS PELO FATO DE NÃO PODER REUTILIZAR CÉLULAS PARA OUTROS UNIVERSOS
        self.celula_moderador1_fonte          = openmc.Cell(fill=self.moderador,   region=+plano_fundo_tanque_superior&-plano_grade_inferior_1&+cilindro_raio_externo_vareta)
        self.celula_moderador2_fonte          = openmc.Cell(fill=self.moderador,   region=+plano_grade_inferior_2&-plano_grade_superior_1&+cilindro_raio_externo_vareta)
        self.celula_moderador3_fonte          = openmc.Cell(fill=self.moderador,   region=+plano_grade_superior_2&-plano_refletor_lateral_superior&+cilindro_raio_externo_vareta)
        self.celula_grade_inferior_fonte      = openmc.Cell(fill=self.aluminio,    region=+plano_grade_inferior_1&-plano_grade_inferior_2&+cilindro_raio_externo_vareta)
        self.celula_grade_superior_fonte      = openmc.Cell(fill=self.aluminio,    region=+plano_grade_superior_1&-plano_grade_superior_2&+cilindro_raio_externo_vareta)
        self.celula_clad_vareta_fonte         = openmc.Cell(fill=self.aluminio,    region=+plano_fundo_tanque_superior&-plano_vareta_altura&+cilindro_raio_interno_vareta&-cilindro_raio_externo_vareta)
        self.celula_ar_externo_vareta_fonte   = openmc.Cell(fill=self.ar,          region=+plano_refletor_lateral_superior&-plano_vareta_altura&+cilindro_raio_externo_vareta)
        self.celula_ar_superior_interno_fonte = openmc.Cell(fill=self.ar,          region=+plano_elemento_combustivel&-plano_vareta_altura&-cilindro_raio_interno_vareta)


        self.universo_fonte = openmc.Universe(cells=(self.celula_clad_vareta_fonte,self.celula_refletor_inferior_fonte,self.celula_suporte_interno_fonte,
                                                self.celula_fonte,self.celula_clad_fonte,self.celula_refletor_lateral_fonte,
                                                self.celula_refletor_superior_fonte,self.celula_ar_externo_vareta_fonte,
                                                self.celula_grade_superior_fonte, self.celula_grade_inferior_fonte,self.celula_ar_superior_interno_fonte,
                                                self.celula_moderador1_fonte, self.celula_moderador2_fonte, self.celula_moderador3_fonte,))  # Identidade da fonte
        
        ####################################################################################################################################
        ####################################################################################################################################

        ####################################################################################################################################
        ###############################     Celulas e superfícies específicas para o Universo agua (central)    ############################
        ####################################################################################################################################

        self.celula_agua               = openmc.Cell(fill=self.moderador,   region=+plano_fundo_tanque_superior&-plano_refletor_lateral_superior&-cilindro_raio_externo_vareta)
        self.celula_agua_2             = openmc.Cell(fill=self.moderador,   region=+plano_fundo_tanque_superior&-plano_grade_inferior_1&+cilindro_raio_externo_vareta)
        self.celula_agua_3             = openmc.Cell(fill=self.moderador,   region=+plano_grade_inferior_2&-plano_grade_superior_1&+cilindro_raio_externo_vareta)
        self.celula_agua_4             = openmc.Cell(fill=self.moderador,   region=+plano_grade_superior_2&-plano_refletor_lateral_superior&+cilindro_raio_externo_vareta)
        self.celula_ar_central         = openmc.Cell(fill=self.ar,          region=+plano_refletor_lateral_superior&-plano_vareta_altura&-cilindro_raio_externo_vareta)
        self.celula_ar_central_externa = openmc.Cell(fill=self.ar,          region=+plano_refletor_lateral_superior&-plano_vareta_altura&+cilindro_raio_externo_vareta)

        self.celula_central_grade_inferior  = openmc.Cell(fill=self.aluminio,    region=+plano_grade_inferior_1&-plano_grade_inferior_2&+cilindro_raio_externo_vareta)
        self.celula_central_grade_superior  = openmc.Cell(fill=self.aluminio,    region=+plano_grade_superior_1&-plano_grade_superior_2&+cilindro_raio_externo_vareta)
        
        self.universo_agua = openmc.Universe(cells=(self.celula_agua,self.celula_agua_2, self.celula_agua_3, self.celula_agua_4, self.celula_ar_central, 
                                                    self.celula_ar_central_externa, self.celula_central_grade_inferior, self.celula_central_grade_superior))  
                                                    # Identidade da agua

        ####################################################################################################################################
        ####################################################################################################################################

        #Celula para universo apenas com refletor
        self.celula_refletor_matriz          = openmc.Cell(fill=self.moderador, region=+plano_fundo_tanque_superior&-plano_grade_inferior_1
                                                                                     | +plano_grade_inferior_2&-plano_grade_superior_1
                                                                                     | +plano_grade_superior_2&-plano_refletor_lateral_superior                                                                                     )
        self.celula_grade_externa_inferior   = openmc.Cell(fill=self.aluminio,  region=+plano_grade_inferior_1&-plano_grade_inferior_2)
        self.celula_grade_externa_superior   = openmc.Cell(fill=self.aluminio,  region=+plano_grade_superior_1&-plano_grade_superior_2)
        self.celula_ar_externo               = openmc.Cell(fill=self.ar,        region=+plano_refletor_lateral_superior&-plano_vareta_altura)

        #Universos
        self.universo_vareta_combustível     = openmc.Universe(cells=(self.celula_clad_vareta,self.celula_refletor_interno, self.celula_suporte_interno, self.celula_ar_interno_elemento,
                                                                self.celula_combustivel_1,self.celula_combustivel_2, self.celula_combustivel_3, self.celula_combustivel_4,
                                                                self.celula_combustivel_5,self.celula_ar_externo_elemento, self.celula_moderador1, self.celula_moderador2, self.celula_moderador3, 
                                                                self.celula_ar_superior_interno, self.celula_clad_combustivel_interno,self.celula_clad_combustivel_externo,
                                                                self.celula_clad_1, self.celula_clad_2,self.celula_clad_3,self.celula_clad_4,self.celula_clad_5,self.celula_clad_6,self.celula_clad_7,
                                                                self.celula_clad_8,self.celula_clad_9,self.celula_clad_10,self.celula_clad_bottom,self.celula_ar_externo_vareta,
                                                                self.celula_grade_superior, self.celula_grade_inferior, self.celula_ressalto_inferior))

        #self.universo_vareta_central         = openmc.Universe(cells=(self.celula_vareta,self.celula_refletor_fonte,self.celula_suporte_interno_fonte, \
        #                                                         self.celula_moderador_interno_fonte, self.celula_moderador))

        self.universo_agua_ar               = openmc.Universe(cells=(self.celula_refletor_matriz,self.celula_ar_externo,self.celula_grade_externa_inferior,
                                                                self.celula_grade_externa_superior))

        #Criação da Matriz Hexagonal

        matriz_hexagonal = openmc.HexLattice()
        matriz_hexagonal.center = (0., 0.)
        matriz_hexagonal.pitch = (2*2.54,)
        matriz_hexagonal.outer = self.universo_agua_ar
        matriz_hexagonal.orientation = 'x'

        #print(matriz_hexagonal.show_indices(num_rings=13))

        anel_misturado_10 = [self.universo_agua_ar]*4 + [self.universo_vareta_combustível] + [self.universo_agua_ar] + [self.universo_vareta_combustível] + \
                            [self.universo_agua_ar]*7 + [self.universo_vareta_combustível] + [self.universo_agua_ar] + [self.universo_vareta_combustível] + \
                            [self.universo_agua_ar]*7 + [self.universo_vareta_combustível] + [self.universo_agua_ar] + [self.universo_vareta_combustível] + \
                            [self.universo_agua_ar]*7 + [self.universo_vareta_combustível] + [self.universo_agua_ar] + [self.universo_vareta_combustível] + \
                            [self.universo_agua_ar]*7 + [self.universo_vareta_combustível] + [self.universo_agua_ar] + [self.universo_vareta_combustível] + \
                            [self.universo_agua_ar]*7 + [self.universo_vareta_combustível] + [self.universo_agua_ar] + [self.universo_vareta_combustível] + \
                            [self.universo_agua_ar]*3
        anel_comb_mod_9  = [self.universo_vareta_combustível]*54
        anel_comb_mod_8  = [self.universo_vareta_combustível]*48
        anel_comb_mod_7  = [self.universo_vareta_combustível]*42
        anel_comb_mod_6  = [self.universo_vareta_combustível]*36
        anel_comb_mod_5  = [self.universo_vareta_combustível]*30
        anel_comb_mod_4  = [self.universo_vareta_combustível]*24
        anel_comb_mod_3  = [self.universo_vareta_combustível]*18
        anel_comb_mod_2  = [self.universo_vareta_combustível]*12
        anel_comb_mod_1  = [self.universo_vareta_combustível]*6
        if fonte:
            anel_font_mod_0  = [self.universo_fonte]
        else:
            anel_font_mod_0  = [self.universo_agua]

        matriz_hexagonal.universes = [anel_misturado_10, anel_comb_mod_9, anel_comb_mod_8, anel_comb_mod_7, anel_comb_mod_6, anel_comb_mod_5, anel_comb_mod_4, anel_comb_mod_3, anel_comb_mod_2, anel_comb_mod_1, anel_font_mod_0]
        print(matriz_hexagonal)
        #A celula do reator é preenchida com a matriz_hexagonal e depois água, até chegar na superficie lateral do refletor
        self.celula_reator_matriz_hexagonal  = openmc.Cell(fill=matriz_hexagonal, region=-cilindro_raio_externo_grade&-plano_vareta_altura&+plano_fundo_tanque_superior)

        ## Celulas externas a matriz hexagonal

        #Tanque
        self.celula_refletor = openmc.Cell(fill=self.moderador, region=+plano_fundo_tanque_superior&-plano_refletor_lateral_superior&+cilindro_raio_externo_grade&-cilindro_raio_interno_tanque)
        self.celula_ar_externo_matriz = openmc.Cell(fill=self.ar, region=+plano_refletor_lateral_superior&-plano_altura_tanque&+cilindro_raio_externo_grade&-cilindro_raio_interno_tanque)
        self.celula_tanque   = openmc.Cell(fill=self.SS304, region=+cilindro_raio_interno_tanque&-cilindro_raio_externo_tanque&+plano_fundo_tanque_superior&-plano_divisao_altura_tanque_inf
                                                                | +cilindro_raio_interno_tanque&-cilindro_beirada_tanque&+plano_divisao_altura_tanque_inf&-plano_divisao_altura_tanque_sup
                                                                | +cilindro_raio_interno_tanque&-cilindro_raio_externo_tanque&+plano_divisao_altura_tanque_sup&-plano_beirada_altura_tanque
                                                                | +plano_fundo_tanque_inferior&-plano_fundo_tanque_superior&-cilindro_raio_externo_tanque
                                                                | +plano_beirada_altura_tanque&-plano_altura_tanque&+cilindro_raio_interno_tanque&-cilindro_beirada_tanque)

        self.celula_ar_interna_tanque = openmc.Cell(fill=self.ar, region=-cilindro_raio_interno_tanque&+plano_vareta_altura&-plano_altura_tanque)

        # Boundary conditions
        fronteira = 10
        self.fronteira_ar_lateral = Tanque_Diametro/2 + fronteira
        self.fronteira_ar_superior = altura_tanque + fronteira
        self.fronteira_ar_inferior = fundo_tanque_inferior - fronteira
        cilindro_boundary        = openmc.ZCylinder (r=self.fronteira_ar_lateral, boundary_type='vacuum')
        plano_superior_boundary  = openmc.ZPlane    (z0=self.fronteira_ar_superior, boundary_type='vacuum')
        plano_inferior_boundary  = openmc.ZPlane    (z0=self.fronteira_ar_inferior, boundary_type='vacuum')

        self.celula_ar_externa_tanque = openmc.Cell(fill=self.ar, region=-cilindro_boundary&-plano_superior_boundary&+plano_altura_tanque
                                                            | -cilindro_boundary&+cilindro_beirada_tanque&+plano_beirada_altura_tanque&-plano_altura_tanque
                                                            | -cilindro_boundary&+cilindro_raio_externo_tanque&-plano_beirada_altura_tanque&+plano_divisao_altura_tanque_sup
                                                            | -cilindro_boundary&+cilindro_beirada_tanque&-plano_divisao_altura_tanque_sup&+plano_divisao_altura_tanque_inf
                                                            | -cilindro_boundary&+cilindro_raio_externo_tanque&-plano_divisao_altura_tanque_inf&+plano_fundo_tanque_inferior
                                                            | -cilindro_boundary&-plano_fundo_tanque_inferior&+plano_inferior_boundary)

        # Universo outer
        self.universo_fora = openmc.Universe(cells=(self.celula_reator_matriz_hexagonal, self.celula_refletor, self.celula_ar_externo_matriz,self.celula_tanque,self.celula_ar_externa_tanque,self.celula_ar_interna_tanque))
        # Célula outer
        self.celula_outer = openmc.Cell(fill=self.universo_fora, region=-cilindro_boundary&+plano_inferior_boundary&-plano_superior_boundary)

        ############ Exportar Geometrias
        self.geometria = openmc.Geometry([self.celula_outer])
        self.geometria.export_to_xml()

    
    def plot2D_secao_transversal(self,basis="xz",width=[200,200],pixels=[5000,5000],origin=(0,0,0)):
        print("################################################")
        print("############        Plot 2D         ############")
        print("################################################")
        ############ Plotar Secão Transversal
        secao_transversal = openmc.Plot.from_geometry(self.geometria)
        secao_transversal.type = 'slice'
        secao_transversal.basis = basis
        secao_transversal.width = width
        secao_transversal.origin = origin
        secao_transversal.filename = 'plot_secao_transversal_' + basis
        secao_transversal.pixels = pixels
        secao_transversal.color_by = 'material'
        secao_transversal.colors = self.colors
        ############ Exportar Plots e Plotar
        plotagem = openmc.Plots((secao_transversal,))
        plotagem.export_to_xml()  
        openmc.plot_geometry()

    def plot3D(self):
        print("################################################")
        print("############        Plot 3D         ############")
        print("################################################")
        ############ Plotar em 3D
        plot_3d = openmc.Plot.from_geometry(self.geometria)
        plot_3d.type = 'voxel'
        plot_3d.filename = 'plot_voxel'
        plot_3d.pixels = (500, 500, 500)
        plot_3d.color_by = 'material'
        plot_3d.colors = self.colors
        plot_3d.width = (150., 150., 150.)
        ############ Exportar Plots e Plotar
        plotagem = openmc.Plots((plot_3d,))
        plotagem.export_to_xml()  
        openmc.plot_geometry()
        openmc.voxel_to_vtk(plot_3d.filename+'.h5', plot_3d.filename)


    def configuracoes(self,fonte=True,particulas=1000,ciclos=100,inativo=10,atrasados=True):
        print("################################################")
        print("########### Definição da Simulação  ############")
        print("################################################")
        self.settings = openmc.Settings()
        self.settings.particles = particulas
        self.settings.batches = ciclos
        self.settings.create_delayed_neutrons = atrasados
        if fonte:
            self.settings.inactive = 0
            self.settings.run_mode = 'fixed source'
        else:
            self.settings.inactive = inativo
            self.settings.source = openmc.Source(space=openmc.stats.Point())
        self.settings.export_to_xml()
        #Faça ciclos ser acessada de fora
        self.ciclos = ciclos
        print(self.settings)

    def run(self,mpi=0):
        if(mpi!=0):
            print("################################################")
            print("###########    Executando com MPI   ############")
            print("################################################")
            openmc.run(mpi_args=['mpiexec', '-n', str(mpi)])
        else:
            print("################################################")
            print("###########        Executando       ############")
            print("################################################")
            openmc.run()

    def tallies(self,):
        print("################################################")
        print("###########        Mesh Radial      ############")
        print("################################################")
        r_divisions = np.linspace(0.0,self.fronteira_ar_lateral,101).tolist()    
        z_divisions = [self.fronteira_ar_inferior, self.fronteira_ar_superior,]  
        #energy_filter = openmc.EnergyFilter([1.0E-05, 1.0, 20.0E+06])
        mesh_radial = openmc.CylindricalMesh(r_grid = (r_divisions), z_grid = (z_divisions))
        mesh_filter_radial = openmc.MeshFilter(mesh_radial)
        tally_radial = openmc.Tally(name='MESH_Radial')
        #tally_radial.filters.append(mesh_filter_radial, energy_filter)
        tally_radial.scores.append('flux')

        #print("################################################")
        #print("###########        Mesh Cubico      ############")
        #print("################################################")
        #x_divisions = np.linspace(-self.fronteira_ar_lateral,self.fronteira_ar_lateral,101).tolist()
        #y_divisions = np.linspace(-self.fronteira_ar_lateral,self.fronteira_ar_lateral,101).tolist()  
        #z_divisions = np.linspace( self.fronteira_ar_inferior,self.fronteira_ar_superior,101).tolist() 
        #energy_filter = openmc.EnergyFilter([1.0E-05, 1, 20E+06]) 
        #mesh_cubico = openmc.RectilinearMesh(x_grid = (x_divisions), y_grid = (y_divisions), z_grid = (z_divisions))
        #mesh_filter_cubico = openmc.MeshFilter(mesh_cubico)
        #tally_cubico = openmc.Tally(name='MESH_Cubico')
        #tally_cubico.filters.append(mesh_filter_cubico, energy_filter)
        #tally_cubico.scores.append('flux')

        ############## Coleção de tallies ##############
        tallies = openmc.Tallies([tally_radial,])# tally_cubico])
        tallies.export_to_xml()

        self.run()

        sp = openmc.StatePoint('statepoint.'+str(self.ciclos)+'.h5')

        print("################################################")
        print("###########    Trabalhando dados    ############")
        print("################################################")
        # Retirando o keff
        print('')
        keff = sp.keff
        print("\t" , " keff (valor combinado de abs/col/t.length) :",keff, "[neutrons/source]")
        print('')

        # Acesse os resultados do tally radial
        flux_radial  = sp.get_tally(scores=['flux'], name='MESH_Radial')
        flux_cubico  = sp.get_tally(scores=['flux'], name='MESH_Cubico')

        flux_rad     = flux_radial.mean
        flux_rad_dev = flux_radial.std_dev
        flux_cub     = flux_cubico.mean
        flux_cub_dev = flux_cubico.std_dev

        # Retirando o mesh radial
        print('')
        print("Mesh Radial:")
        print('')

        # Volumes das areas do mesh
        #volume = []
        #for i in range(0, 100):  # Use o número apropriado de intervalos
        #    r1 = r_divisions[i]
        #    r2 = r_divisions[i + 1]
        #    h = z_divisions[1] - z_divisions[0]
        #    volume.append(3.14159265359 * (r2**2 - r1**2) * h)

        for i in range(0,100):
            fluxo     = flux_rad[i]
            incerteza = flux_rad_dev[i]
            fluxo_científico = format(fluxo, '.4e')
            inc_cientifico   = format(incerteza, '.4e')
            print("  Intervalo ", (self.fronteira_ar_lateral/101)*i,": ","\t"," Fluxo : ", fluxo_científico[i][0][0], "+/-", inc_cientifico[i][0][0], "[neutron/cm².s]")




        