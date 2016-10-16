#import dari sys untuk memanggil fungsi argv
from sys import argv
#argv diberikan 2 variable yaitu script itu sendiri dan filename
script, filename = argv
#fungsi txt membuka file dengan nama "filename"
txt = open(filename)
#pemberitahuan bahwa "filename" siap dibuka
print("Here is your file %r:" % filename)
#membuka "filename"
print(txt.read()) #print harus dalam kurung
#meminta nama file kembali
print("Type the filename again:")
file_again = input("> ")
#membuka file
txt_again = open(file_again)
#menampilkan file
print(txt_again.read())
