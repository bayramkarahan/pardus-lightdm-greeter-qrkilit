
import subprocess
class Qrkilit_Update:
  def qrkilit_guncelle(self):
  	try:
        	command = "wget https://github.com/bayramkarahan/pardus-lightdm-greeter-qrkilit/raw/refs/heads/master/debian/changelog -O /tmp/version 1>/dev/null 2>/dev/null"
        	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        	(output, err) = p.communicate()
        	p_status = p.wait()
        	#print("Dosya indirildi")
			
        	command = "cat /tmp/version|grep qrkilit"
        	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        	(output, err) = p.communicate()
        	p_status = p.wait()
        	remoteversion=output.split()
        	remoteversion=remoteversion[1]
        	remoteversion=remoteversion[1:-1]
        	#print(remoteversion)
        	#print("Dosya okundu")

        	command = "dpkg -s pardus-lightdm-greeter-qrkilit|grep -i version"
        	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        	(localversion, err) = p.communicate()
        	p_status = p.wait()
        	localversion=localversion[:-1:]
        	localversion=localversion[9:]
        	#print(str(localversion))

        	if remoteversion==localversion:
        		print("aynı version")
        	else:
        		print("version farklı")	

  	except subprocess.CalledProcessError as e:
        	print(f"Command failed with return code {e.returncode}")
