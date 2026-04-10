class MCAS2026:
    def __init__(self, sensor_left, sensor_right):
        self.sensor_left = sensor_left
        self.sensor_right = sensor_right
        self.observers = []
        self.circuit_breaker_open = False # Se True, o sistema é isolado
        self.max_divergence = 5.0 # Diferença máxima tolerada entre os sensores

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, event_type, message):
        for obs in self.observers:
            obs.update(event_type, message)

    def manual_cutout(self):
        # Simula o piloto desligando o sistema (Circuit Breaker)
        self.circuit_breaker_open = True
        self.notify_observers("SISTEMA DESLIGADO", "Controle manual assumido pela tripulação.")

    def evaluate_flight_data(self):
        if self.circuit_breaker_open:
            return # Sistema isolado, não faz nada

        angle_l = self.sensor_left.read_angle()
        angle_r = self.sensor_right.read_angle()

        print(f"Leitura Sensores -> L: {angle_l:.2f}º | R: {angle_r:.2f}º")

        # Regra de Votação/Redundância
        if abs(angle_l - angle_r) > self.max_divergence:
            self.notify_observers("AOA DISAGREE", "Divergência crítica nos sensores. Atuação do MCAS bloqueada.")
            return

        # Atuação normal do MCAS se ambos concordarem que o ângulo está muito alto
        if angle_l > 10.0 and angle_r > 10.0:
            print("[SISTEMA] MCAS Atuando: Empurrando o nariz para baixo (Trim Down).")
        else:
            print("[SISTEMA] Voo estabilizado.")