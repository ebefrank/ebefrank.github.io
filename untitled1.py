from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
import time

# Definition der Klasse mit allen notwendigen Methoden
class MyListener(ServiceListener):
    def add_service(self, zc, type_, name):
        info = zc.get_service_info(type_, name)
        print(f"Gefunden: {name}")
        if info:
            # Wir versuchen die IP-Adresse zu extrahieren
            addresses = [str(addr) for addr in info.addresses]
            print(f"  -> IP: {addresses}")

    def update_service(self, zc, type_, name):
        pass # Notwendig für die API, auch wenn wir nichts tun

    def remove_service(self, zc, type_, name):
        print(f"Entfernt: {name}")

# Hauptprogramm starten
print("Starte Netzwerk-Scan für 15 Sekunden...")
print("Suche nach BluOS, AirPlay und anderen Diensten...")
print("-" * 30)

aio_zc = Zeroconf()
listener = MyListener()

# Wir suchen nach dem allgemeinen DNS-SD Service, um ALLES zu finden
browser = ServiceBrowser(aio_zc, "_services._dns-sd._udp.local.", listener)

try:
    time.sleep(15)
finally:
    aio_zc.close()
    print("-" * 30)
    print("Scan abgeschlossen.")
