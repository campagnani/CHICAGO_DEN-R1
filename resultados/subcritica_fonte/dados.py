import openmc
import numpy as np

sp = openmc.StatePoint('statepoint.100.h5')

tempo      = sp.runtime
keff       = sp.keff

fission = sp.get_tally(scores=['fission'])
v       = sp.get_tally(scores=['nu-fission'])

fission_mean = fission.mean
fission_unc  = fission.std_dev
nu_fission_mean       = v.mean
nu_fission_unc        = v.std_dev

# CALCULO DE INCERTEZAS
nu_fission = nu_fission_mean[0][0][0]  # total neutrons by fission/source
sigma_nu_fission = nu_fission_unc[0][0][0]  # uncertainty in nu_fission
fission = fission_mean[0][0][0]  # fissions/s
sigma_fission = fission_unc[0][0][0]  # uncertainty in fission

# Calculando o valor de v
v = nu_fission / fission

# Propagação de erro (uncertainty propagation)
sigma_v = v * np.sqrt((sigma_nu_fission / nu_fission)**2 + (sigma_fission / fission)**2)

# Definindo A e B
A = fission * 1.01 * 10**7
B = v

# Incerteza de A
sigma_A = 1.01 * 10**7 * sigma_fission

# Incerteza de neutrons by fission
neutrons_by_fission = A * B
sigma_neutrons_by_fission = neutrons_by_fission * np.sqrt((sigma_A / A)**2 + (sigma_v / v)**2)

# Exibindo os resultados
print()
print(' Erro propagado:')
print()
print(f" v = {v}")
print(f" Uncertainty in v = {sigma_v}")
print(f" Neutrons by fission = {neutrons_by_fission}")
print(f" Uncertainty in neutrons by fission = {sigma_neutrons_by_fission}")
print()

print(' ###########################################################################################')
print()

# Calculando o fator de multiplicação subcrítico e sua incerteza
S = neutrons_by_fission + 1.01 * 10**7
sigma_S = sigma_neutrons_by_fission
subcritico = neutrons_by_fission / S
sigma_subcritico = subcritico * np.sqrt((sigma_neutrons_by_fission / neutrons_by_fission)**2 + (sigma_S / S)**2)

# Exibindo os resultados
print(f" Fator de multiplicação subcrítico (subcritico) = {subcritico}")
print(f" Incerteza em subcritico = {sigma_subcritico}")
print(' Porcentagem do erro:', sigma_subcritico/subcritico)
print()
# Calculando o fator de multiplicação de neutrons e sua incerteza
M = 1 / (1 - subcritico)
sigma_M = M * (sigma_subcritico / (1 - subcritico))

# Exibindo os resultados
print(f" Fator de multiplicação (M) = {M}")
print(f" Incerteza em M = {sigma_M}")
print(' Porcentagem do erro:', sigma_M/M)
print()
print(f" Fator de importância da fonte de neutrons =", (1-(1/0.841897))/(1-(1/subcritico)))
print(f" Incerteza do fator de importância da fonte de neutrons =", (1-(1/0.841897))/(1-(1/subcritico)) * 1.51e-05)
print(' Porcentagem do erro:', ((1-(1/0.841897))/(1-(1/subcritico)) * 1.51e-05)/(1-(1/0.841897))/(1-(1/subcritico)))
print()
print(' Porcentagem de erro keff:', 9e-06/0.841897)

print(' ###########################################################################################')
print()
#print()
#print(' v (nu-fission/fission):', nu_fission_mean[0][0][0]/fission_mean[0][0][0], '[neutrons/fission]')
#print()
#print(' nu-fission:', nu_fission_mean[0][0][0], '[total neutrons by fission/source]')
#print()
#print(' nu-fission uncertainty:', nu_fission_unc[0][0][0], '[total neutrons by fission/source]')
#print()
#print(' neutrons by fission :', (fission_mean[0][0][0]*1.01 * 10**7) * (nu_fission_mean[0][0][0]/fission_mean[0][0][0]), '[neutrons/s]')
#print()
#print(' fission :', fission_mean[0][0][0] *1.01 * 10**7, '[fissions/s]' )
#print()
#print(' fission uncertainty:', fission_unc[0][0][0] *1.01 * 10**7, '[fissions/s]')
#print()
#print(tempo)
#print()
