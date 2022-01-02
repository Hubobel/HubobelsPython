import dropbox
import os

access_token = 'wolWNcuUBx8AAAAAAAAAAewgSIDDcM7gBELKKuQyTup-iaMigFASlRULaav4e_N7'

dbx = dropbox.Dropbox(access_token)

a = os.getcwd() + "/Stick/"
b = os.getcwd() + "/testa/"
inhalta = (os.listdir(a))

for i in inhalta:
    with open(a + str(i), 'rb') as f:
        dbx.files_upload(f.read(), '/' + str(i))

inhalt = dbx.files_list_folder('')


for entry in dbx.files_list_folder('').entries:
    print(entry.name)
    download_Path = b + entry.name

    dropbox_Path = '/' + entry.name

    dbx.files_download_to_file(download_Path, dropbox_Path)

