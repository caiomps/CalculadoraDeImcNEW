print('Vamos Calcular o seu IMC')
peso = float(input('Primeiro Digite o seu peso(kg): '))
altura = float(input('Agora Digite a sua altura: '))
imc = peso / (altura**2)

if imc <= 18.5:
    print('O seu IMC e {:.2f}, voce esta classificado como Magreza'.format(imc, ))

elif imc > 18.5 and imc <= 24.9:
    print('O seu imc e {:.2f}, voce esta classificado como Normal'.format(imc))

elif imc > 24.9 and imc <= 29.9:
    print('O seu imc e {:.2f}, voce esta classificado como SobrePeso I'.format(imc))

elif imc > 29.9 and imc <= 39.9:
    print('O seu imc e {:.2f}, voce esta classificado como Obesidade II'.format(imc))

else:
    print('O seu imc e {:.2f}, voce esta classificado como Obesidade Grave III'.format(imc))