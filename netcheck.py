import requests
import os
import subprocess
import sys
import hashlib
def runid(cmd):
  try:
    return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                     .stdout \
                     .strip()
  except:
    return None

def guid():
  if sys.platform == 'darwin':
    return runid(
      "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",
    )

  if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
    return run('wmic csproduct get uuid').split('\n')[2] \
                                         .strip()

  if sys.platform.startswith('linux'):
    return runid('cat /var/lib/dbus/machine-id') or \
           runid('cat /etc/machine-id')

  if sys.platform.startswith('openbsd') or sys.platform.startswith('freebsd'):
    return runid('cat /etc/hostid') or \
           runid('kenv -q smbios.system.uuid')
           
def internet_baglantisi_testi(url='http://www.google.com'):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

if internet_baglantisi_testi():
    print("İnternet bağlantısı mevcut.")
else:
    print("İnternet bağlantısı yok.")

import platform
print(platform.node())

import socket
print(os.uname()[1])
sid=str(guid())
print(sid)
systemid=sid[:10] #.encode()
print(systemid)
sha256 = hashlib.sha256()
sha256.update(systemid.encode())
kurum="554"
bilgi="-"+kurum+"-"+str(sha256.hexdigest())+"-0"


print(bilgi)
