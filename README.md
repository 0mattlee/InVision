# InVision - Acessibilidade e Controle por Gestos Faciais

O InVision é uma solução de tecnologia assistiva projetada para empoderar pessoas com deficiências motoras, oferecendo uma nova forma de interagir com o computador. Utilizando apenas uma webcam, o InVision traduz movimentos faciais em comandos de controle do mouse, quebrando barreiras e promovendo a inclusão digital.

## Uma Ferramenta de Inclusão

Acreditamos que a tecnologia deve ser uma ponte, não um obstáculo. O InVision foi criado com o propósito de garantir que todos possam navegar, trabalhar e se comunicar no ambiente digital com mais autonomia e liberdade.

## Funcionalidades

- **Controle Preciso do Mouse:** A posição do nariz guia o cursor do mouse pela tela, com um sistema de movimento relativo que garante estabilidade e precisão.
- **Clique e Arraste Intuitivos:** Manter a boca aberta pressiona o botão do mouse, e fechá-la o solta. Isso permite realizar cliques simples e operações complexas como "arrastar e soltar" de forma natural.
- **Navegação por Scroll:** Incline a cabeça para a direita ou para a esquerda para rolar (scroll) páginas para baixo ou para cima, facilitando a leitura de documentos e a navegação em websites.
- **Feedback Visual em Tempo Real:** A aplicação exibe o vídeo da webcam com uma malha facial (Face Mesh) sobre o rosto, fornecendo um feedback claro dos pontos que estão sendo rastreados.

## Requisitos do Sistema

- Python 3.8 ou superior.
- Uma webcam conectada ao computador.

## Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/0mattlee/InVision.git
    cd InVision
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Como Rodar o Projeto

1.  **Permissão de Acesso à Câmera:**
    Ao executar o programa pela primeira vez, seu sistema operacional pode solicitar permissão para que o script acesse a webcam. Certifique-se de conceder essa permissão.

2.  **Execute o script principal:**
    ```bash
    python main.py
    ```

3.  **Uso:**
    - Ao iniciar, o programa estará pronto para uso. Não é necessária calibração.
    - Mova a cabeça para controlar o cursor do mouse.
    - Abra a boca para pressionar o botão do mouse (e mantenha-a aberta para arrastar). Feche a boca para soltar.
    - Incline a cabeça para a direita para rolar a página para baixo.
    - Incline a cabeça para a esquerda para rolar a página para cima.
    - Pressione a tecla **'q'** para fechar a janela e encerrar o programa.

## Estrutura do Projeto

O projeto foi refatorado para uma estrutura mais organizada e modular:

```
InVision/
├── main.py               # Ponto de entrada que orquestra a aplicação
├── requirements.txt      # Lista de dependências Python
├── src/                  # Diretório com o código fonte
│   ├── config.py         # Ficheiro de configurações e constantes
│   ├── face_tracker.py   # Classe para deteção facial com MediaPipe
│   └── mouse_controller.py # Classe para controlar as ações do mouse
└── README.md             # Este arquivo
