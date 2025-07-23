# -*- coding: utf-8 -*-
"""
Módulo responsável por traduzir os gestos faciais em ações do mouse.
"""
import pyautogui
import time
from src import config

class MouseController:
    """
    Classe que controla o mouse com base nos landmarks faciais.
    """
    def __init__(self):
        """Inicializa o controlador do mouse."""
        pyautogui.FAILSAFE = False
        self.screen_w, self.screen_h = pyautogui.size()
        self.last_nose_x, self.last_nose_y = 0, 0
        self.mouth_open = False
        self.last_scroll_time = 0
        self.first_frame = True

    def update(self, landmarks):
        """
        Atualiza o estado do mouse com base nos novos landmarks.

        Args:
            landmarks: A lista de pontos faciais detetados.
        """
        if not landmarks:
            return

        # --- Controlo de Movimento ---
        nose_tip = landmarks[4]
        if self.first_frame:
            self.last_nose_x, self.last_nose_y = nose_tip.x, nose_tip.y
            self.first_frame = False
        else:
            dx = nose_tip.x - self.last_nose_x
            dy = nose_tip.y - self.last_nose_y

            if abs(dx) > config.DEAD_ZONE_THRESHOLD or abs(dy) > config.DEAD_ZONE_THRESHOLD:
                current_mouse_x, current_mouse_y = pyautogui.position()
                mouse_x = current_mouse_x + dx * config.SENSITIVITY
                mouse_y = current_mouse_y + dy * config.SENSITIVITY
                
                mouse_x = max(1, min(self.screen_w - 1, mouse_x))
                mouse_y = max(1, min(self.screen_h - 1, mouse_y))
                pyautogui.moveTo(mouse_x, mouse_y)

            self.last_nose_x, self.last_nose_y = nose_tip.x, nose_tip.y

        # --- Controlo de Clique/Arrastar ---
        lip_top = landmarks[13]
        lip_bottom = landmarks[14]
        mouth_distance = self._calcular_distancia(lip_top, lip_bottom)

        if mouth_distance > config.MOUTH_OPEN_THRESHOLD:
            if not self.mouth_open:
                pyautogui.mouseDown()
                self.mouth_open = True
        else:
            if self.mouth_open:
                pyautogui.mouseUp()
                self.mouth_open = False
        
        # --- Controlo de Scroll ---
        left_eye_corner = landmarks[33]
        right_eye_corner = landmarks[263]
        tilt_diff = right_eye_corner.y - left_eye_corner.y
        
        current_time = time.time()
        if current_time - self.last_scroll_time > config.SCROLL_COOLDOWN:
            if tilt_diff > config.HEAD_TILT_THRESHOLD:
                pyautogui.scroll(-config.SCROLL_AMOUNT)
                self.last_scroll_time = current_time
            elif tilt_diff < -config.HEAD_TILT_THRESHOLD:
                pyautogui.scroll(config.SCROLL_AMOUNT)
                self.last_scroll_time = current_time

    def get_status(self):
        """Retorna o estado atual das ações para exibição."""
        return {
            "mouth": "Aperto" if self.mouth_open else "Solto"
        }

    @staticmethod
    def _calcular_distancia(p1, p2):
        """Método auxiliar para calcular distância."""
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
