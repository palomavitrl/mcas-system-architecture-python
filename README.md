# Projeto: Arquitetura de Software - Simulação MCAS 2026

Este repositório contém a simulação desenvolvida para a disciplina de Arquitetura de Software. O objetivo é demonstrar uma proposta de solução moderna (visão 2026) para o sistema MCAS do Boeing 737 MAX, mitigando as falhas arquiteturais que levaram aos acidentes históricos.

## 🏗️ Decisões Arquiteturais
A solução foi desenhada utilizando uma arquitetura em camadas (N-Tier) para separar a aquisição de dados, regras de negócio e apresentação.
Implementamos os seguintes *Design Patterns*:
- **Observer:** Para garantir a observabilidade do sistema e notificar o painel (pilotos) sobre alertas de "AoA Disagree".
- **Circuit Breaker:** Para isolar o sistema automaticamente (ou manualmente) em caso de leituras erráticas contínuas.
- **Votação/Redundância:** Validação cruzada obrigatória entre sensores antes de qualquer atuação mecânica.

## 🚀 Como executar a simulação
O código foi escrito em Python puro, não sendo necessárias bibliotecas externas.

1. Clone o repositório:
`git clone (https://github.com/palomavitrl/mcas-system-architecture-python.git)`
2. Acesse a pasta do projeto e execute o arquivo principal:
`python main.py`

## 📊 Resultado Esperado
A simulação inicializa um voo com um sensor de Ângulo de Ataque defeituoso. Ao contrário da arquitetura original, a divergência será detectada, o alerta de `AOA DISAGREE` será disparado para a cabine e o MCAS será impedido de forçar o nariz da aeronave para baixo, salvando o voo simulado.
