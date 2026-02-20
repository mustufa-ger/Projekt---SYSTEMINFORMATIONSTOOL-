import psutil 
import platform 
import socket 

print("=============SYSTEMINFORMATIONSTOOL==========\n")

#Betriebssystem Informationen
print("Betriebssystem:", platform.system)
print("OS-Version:", platform.version)
print("Architektur-Maschine", platform.machine)
print()

#CPU- Informationen : 
print("Informationen:")
print("Physische Kerne:", psutil.cpu_count(logical=False ))
#wiir zahlen die physische kerne also wie viele es insgesamt sind mit cpu_count und logical false erzahlt python dass er nur die physiische zahlen soll
print("Gesamtanzahl Kerne:", psutil.cpu_count(logical=True))
print("CPU-Auslastung (%):", psutil.cpu_percent(interval=1)) 
#misst die leistung von CPU uber 1 sekunde ( interval = 1 ) und cpu_percent benutzen wir um die leistung zu sehen also mit wie viel ihrer leistung arbeitet CPU  
print()

# Netzwerk-Informationen
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Netzwerk-Informationen")
print("hostname:", hostname)
print("IP-adresse:", ip_address)

print("\n===== ENDE =====")