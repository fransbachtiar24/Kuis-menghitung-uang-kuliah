#Ran
#Careless
#Susu Beruang
#yang terpenting itu bukan apa yang kita ketahui melainkan apa yang bersedia kita pelajari
'''
Nama file : kuis dasprog
Nama      : FRANS BACHTIAR
Npm       : 2024240041
Jurusan   : Sistem Informasi
'''
print("Hitung uang kuliah")
print("===================")
npm=eval(input("NPM             : "))
nama=str(input('Nama             : '))
kelas=str(input('kelas (pagi/malam: '))
sks=eval(input('jumlah sks      : '))
beasiswa=input('beasiswa        : ')
kp=100000
km=150000
subtotalkp=kp*sks
subtotalkm=km*sks
pbkp=persen + subtotalkp
pbkm=persen + subtotalkm
ukkp = subtotalkp - subtotalkm
ukm = subtotalkm - pbkm
respon = 'Y'
while respon == 'Y' or respon == 'y':
    if kelas==("pagi"or"pagi"):
        
        print('{} dengan nama {} uang kuliah anda sebesar {} dengan rincian : '.format(npm,nama,ukkp))
        print()
        print('uang per sks : {} ribu'.format(kp))
        print('subtotal : {}'.format(subtotalkp))
        print('potongan beasiswa: {}'.format(pbkp))
        print(pbkp)
        print(ukkp)
        if respon == "Y" or respon == "y":
            continue
        elif respon == "T" or respon == "t" or respon != "y" or respon != "Y":
            break

    elif kelas==("malam"or"malam"):
        print('{} dengan nama {} uang kuliah anda sebesar {} dengan rincian : '.format(npm,nama,ukkm))
        print()
        print('uang per sks : {} ribu'.format(km))
        print('subtotal : {}'.format(subtotalkm))
        print('potongan beasiswa: {}'.format(pbkm))
        print(pbkm)
        print(ukkm)
    else:
        print('inputan salah')
#Pain today pride tomorrow
#Susu Beruang
#$exit
