class DashboardObserver:
    def update(self, event_type, message):
        """Recebe notificações do sistema central e exibe no painel"""
        print(f"[PAINEL DA CABINE] Alerta: {event_type} | Mensagem: {message}")

    def show_status(self, mcas_active, circuit_breaker_open):
        status_mcas = "BLOQUEADO" if circuit_breaker_open else ("ATIVO" if mcas_active else "EM ESPERA")
        print(f"--- STATUS DO VOO | MCAS: {status_mcas} ---")