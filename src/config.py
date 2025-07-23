# -*- coding: utf-8 -*-
"""
Ficheiro de configuração para centralizar todas as constantes e parâmetros.
"""

# -- Configurações do Mouse --
SENSITIVITY = 2500  # Sensibilidade do movimento do rato
DEAD_ZONE_THRESHOLD = 0.002  # Margem para ignorar micromovimentos relativos

# -- Configurações de Ações Faciais --
MOUTH_OPEN_THRESHOLD = 0.009  # Limiar para considerar a boca aberta
HEAD_TILT_THRESHOLD = 0.10  # Limiar para detetar inclinação da cabeça

# -- Configurações de Scroll --
SCROLL_AMOUNT = 70  # Quantidade de píxeis para rolar por evento
SCROLL_COOLDOWN = 0.1  # Cooldown em segundos para evitar scrolls múltiplos
