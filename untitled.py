from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
import time

# Die Klasse MUSS von ServiceListener erben
class MyListener(ServiceListener):
    def update_service(self, zc, type_, name):
        print(f"Service aktualisiert: {name}")

    def remove_service(self, zc, type_, name):
        print(f"Service entfernt: {name}")

    def add_service(self, zc, type_, name):
        info = zc.get_service_info(type_, name)
        print(f"Gerät gefunden: {name}")
        if info:
            print(f"  - IP: {info.parsed_addresses()}")

# Instanziiere Zeroconf
zc = Zeroconf()
listener = MyListener()

# Suche nach allen Diensten im lokalen Netz (_services._dns-sd._udp.local.)
print("Suche läuft für 15 Sekunden... Bitte warten.")
browser = ServiceBrowser(zc, "_services._dns-sd._udp.local.", listener)

try:
    time.sleep(15)
finally:
    zc.close()
    print("\nSuche beendet.")








