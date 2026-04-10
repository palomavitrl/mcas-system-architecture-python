import random

class AoASensor:
    def __init__(self, name, is_defective=False):
        self.name = name
        self.is_defective = is_defective
        self.base_angle = 2.0

    def read_angle(self):
        # Simula a leitura do sensor. Se defeituoso, envia um valor perigoso (SPOF mitigado)
        if self.is_defective:
            return self.base_angle + random.uniform(15.0, 25.0) 
        return self.base_angle + random.uniform(-0.5, 0.5)