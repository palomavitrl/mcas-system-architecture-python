import time
from sensors import AoASensor
from dashboard import DashboardObserver
from mcas_system import MCAS2026

def run_simulation():
    print("Iniciando Simulação do Voo (Arquitetura 2026)...\n")
    
    # 1. Setup da Arquitetura
    # Simulamos o sensor esquerdo com defeito (Causa do acidente original)
    sensor_l = AoASensor("Esquerdo", is_defective=True) 
    sensor_r = AoASensor("Direito", is_defective=False)
    
    mcas = MCAS2026(sensor_l, sensor_r)
    dashboard = DashboardObserver()
    mcas.add_observer(dashboard) # Conecta a interface ao sistema

    # 2. Loop de Simulação do Voo
    for step in range(1, 6):
        print(f"\n--- Tempo: {step}s ---")
        mcas.evaluate_flight_data()
        dashboard.show_status(mcas_active=False, circuit_breaker_open=mcas.circuit_breaker_open)
        
        # Simulando intervenção do piloto no 3º segundo
        if step == 3:
            print("\n[PILOTO] Acionando interruptores de corte (Cut-out switches)!")
            mcas.manual_cutout()
            
        time.sleep(1)

if __name__ == "__main__":
    run_simulation()