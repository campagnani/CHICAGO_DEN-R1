
#######################################################################
####                                                               ####
####              UNIVERSIDADE FEDERAL DE MINAS GERAIS             ####
####               Departamento de Engenharia Nuclear              ####
####                   Thalles Oliveira Campagnani                 ####
####                 Jefferson Quintão Campos Duarte               ####
####                                                               ####
#######################################################################

import openmc
import openmc.data
import os
os.system("clear")

########################################################################
##  Arquivo oficial de criação das bibliotecas HD5 para a subcritica  ##
########################################################################

## Selecionando os arquivos raw e as temperaturas de interesse

os.system("mkdir -p HDF5") 

H1    = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/H1.endf'  , temperatures=[293.,],stdout=True)
H1.export_to_hdf5('./HDF5/H1.h5')
H2    = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/H2.endf'  , temperatures=[293.,],stdout=True)
H2.export_to_hdf5('./HDF5/H2.h5')
N14   = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/N14.endf' , temperatures=[293.,],stdout=True)
N14.export_to_hdf5('./HDF5/N14.h5')
N15   = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/N15.endf' , temperatures=[293.,],stdout=True)
N15.export_to_hdf5('./HDF5/N15.h5')
O16   = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/O16.endf' , temperatures=[293.,],stdout=True)
O16.export_to_hdf5('./HDF5/O16.h5')
O17   = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/O17.endf' , temperatures=[293.,],stdout=True)
O17.export_to_hdf5('./HDF5/O17.h5')
O18   = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/O18.endf' , temperatures=[293.,],stdout=True)
O18.export_to_hdf5('./HDF5/O18.h5')
Al27  = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/Al27.endf', temperatures=[293.,],stdout=True)
Al27.export_to_hdf5('./HDF5/Al27.h5')
Ar36  = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/Ar36.endf', temperatures=[293.,],stdout=True)
Ar36.export_to_hdf5('./HDF5/Ar36.h5')
Ar38  = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/Ar38.endf', temperatures=[293.,],stdout=True)
Ar38.export_to_hdf5('./HDF5/Ar38.h5')
Ar40  = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/Ar40.endf', temperatures=[293.,],stdout=True)
Ar40.export_to_hdf5('./HDF5/Ar40.h5')
U234  = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/U234.endf', temperatures=[293.,],stdout=True)
U234.export_to_hdf5('./HDF5/U234.h5')
U235  = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/U235.endf', temperatures=[293.,],stdout=True)
U235.export_to_hdf5('./HDF5/U235.h5')
U238  = openmc.data.IncidentNeutron.from_njoy('/home/jefferson/git/CHICAGO_DEN-R1/libSubcritica/ENDF-B-VIII.0/U238.endf', temperatures=[293.,],stdout=True)
U238.export_to_hdf5('./HDF5/U238.h5')

## Criando a biblioteca HDF5

library = openmc.data.DataLibrary()
library.register_file('./HDF5/H1.h5'  )
library.register_file('./HDF5/H2.h5'  )
library.register_file('./HDF5/N14.h5' )
library.register_file('./HDF5/N15.h5' )
library.register_file('./HDF5/O16.h5' )
library.register_file('./HDF5/O17.h5' )
library.register_file('./HDF5/O18.h5' )
library.register_file('./HDF5/Al27.h5')
library.register_file('./HDF5/Ar36.h5')
library.register_file('./HDF5/Ar38.h5')
library.register_file('./HDF5/Ar40.h5')
library.register_file('./HDF5/U234.h5')
library.register_file('./HDF5/U235.h5')
library.register_file('./HDF5/U238.h5')
