import zipfile

zip_open = zipfile.ZipFile('module9/series_number/Proyecto+Dia+9.zip','r') # archivo comprimido donde esta para descomprimir
zip_open.extractall('module9/series_number') # donde guardo el archivo cuando se descomprimio