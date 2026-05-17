# Program Flow 

## extractor.py 
- menerima input file dari sys.argv
- mambaca isi file 
- mencari keyword sensitif
- membuat dictionary
- convert ke JSON
- memanggil reporter.py menggunakan subprocess

## reporter.py 
- menerima JSON 
- menambahkan header Content-Type
- mengirim data menggunakan requests.post()
