import requests
import json
def internet_baglantisi_testi(url='http://www.google.com'):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
        
# API'den veri çekme
url = 'https://qrkilit.com.tr/wp-admin/admin-ajax.php?action=notifications@kurumkodu=726102'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # JSON formatında veri al
    print(data)
    
else:
    print("Veri çekme hatası:", response.status_code)
#https://qrkilit.com.tr/wp-admin/admin-ajax.php?action=notifications&kurumkodu=0000001&id=017338b63db5d3d623eec50c6a3421026fb9598a8bd61a7b99a60b87fd2ea551&system=0
