n1=input('Digite uma nota 1:')
n2=input('Digite uma nota 2:')
n3=input('Digite uma nota 3:')
n4=input('Digite uma nota 4:')

media=(float(n1)+float(n2)+float(n3)+float(n4))/4
print('Sua media e:',media)

if media>=7:
    print('Aprovado!')
elif media<5:
    print('Reprovado!')