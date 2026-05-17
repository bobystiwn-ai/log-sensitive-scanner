# Log Sensitive Scanner
Program Python untuk mencari keyword sensitive pada file log lalu mengubah hasilnya menjadi JSON dan mengirimnya ke end point menggunakan HTTP POST

## fitur
- Parsing file log
- Mencari keyword sensitif 
- Convert hasil ke JSON
- HTTP POST request 
- Otomatis menjalankan reporter.py menggunakan subprocess

## Teknologi
- Python
- request
- sys
- subprocess
- json

## Cara menjalankan 

'''bash
python3 extractor.py file.log
