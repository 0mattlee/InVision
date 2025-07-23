# -*- coding: utf-8 -*-
"""
Ponto de entrada principal para a aplicação de controlo do rato por gestos faciais.
"""
import cv2
import time
from src.face_tracker import FaceTracker
from src.mouse_controller import MouseController

def main():
    """
    Orquestra a aplicação: captura de vídeo, rastreamento facial e controlo do rato.
    """
    # Inicializa os componentes principais
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro: Não foi possível abrir a câmera.")
        return

    face_tracker = FaceTracker()
    mouse_controller = MouseController()
    
    p_time = 0  # Para cálculo de FPS

    try:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            # Inverte o frame para um efeito de espelho
            frame = cv2.flip(frame, 1)

            # Processa o frame para encontrar landmarks e desenhar a malha
            landmarks, processed_frame = face_tracker.process_frame(frame)

            # Se um rosto for detetado, atualiza o controlador do rato
            if landmarks:
                mouse_controller.update(landmarks)

            # --- Exibição de Informações na Tela ---
            # Calcula e exibe o FPS
            c_time = time.time()
            if p_time > 0:
                fps = 1 / (c_time - p_time)
                cv2.putText(processed_frame, f'FPS: {int(fps)}', (20, 40), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            p_time = c_time
            
            # Exibe o status do clique
            status = mouse_controller.get_status()
            cv2.putText(processed_frame, f'Clique: {status["mouth"]}', (20, 80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Mostra o resultado
            cv2.imshow('InVision - Pressione "q" para sair', processed_frame)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
    finally:
        # Garante que os recursos são libertados
        print("A encerrar a aplicação...")
        cap.release()
        face_tracker.close()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
