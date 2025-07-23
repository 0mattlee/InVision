# -*- coding: utf-8 -*-
"""
Módulo responsável pela deteção e rastreamento facial usando MediaPipe.
"""
import cv2
import mediapipe as mp
import math

class FaceTracker:
    """
    Classe que encapsula a lógica de deteção facial do MediaPipe.
    """
    def __init__(self):
        """Inicializa o MediaPipe Face Mesh."""
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawing_spec = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

    def process_frame(self, frame):
        """
        Processa um frame de vídeo para detetar pontos faciais.

        Args:
            frame: O frame do vídeo (imagem BGR).

        Returns:
            A tupla (landmarks, frame_processado) onde 'landmarks' são os pontos
            faciais detetados e 'frame_processado' é o frame com a malha desenhada.
            Retorna (None, frame) se nenhum rosto for detetado.
        """
        # Converte a imagem para RGB, que é o formato esperado pelo MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            # Desenha a malha facial no frame original para feedback visual
            self.mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=results.multi_face_landmarks[0],
                connections=self.mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=self.drawing_spec,
                connection_drawing_spec=self.drawing_spec
            )
            return landmarks, frame
        
        return None, frame

    @staticmethod
    def calcular_distancia(p1, p2):
        """Calcula a distância euclidiana entre dois pontos (landmarks)."""
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    def close(self):
        """Libera os recursos do MediaPipe."""
        self.face_mesh.close()
