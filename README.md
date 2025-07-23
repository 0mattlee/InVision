# InVision - Controle do Rato por Gestos Faciais

O InVision é uma aplicação de acessibilidade que permite controlar o cursor do rato e simular cliques usando movimentos faciais, com o objetivo de auxiliar pessoas com deficiência motora a interagir com o computador.

## Funcionalidades

- **Movimento do Cursor:** A posição do nariz controla o movimento do cursor do mouse na tela, usando um sistema de movimento relativo para maior estabilidade.
- **Clique e Arraste:** Manter a boca aberta pressiona o botão do rato, e fechá-la solta-o, permitindo a funcionalidade de "arrastar e soltar".
- **Scroll com a Cabeça:** Inclinar a cabeça para a direita ou para a esquerda faz o scroll da página para baixo ou para cima, respetivamente.
- **Feedback Visual:** Exibe o vídeo da webcam com a malha facial (Face Mesh) desenhada sobre o rosto, mostrando os pontos que estão a ser rastreados.
- **Controle de Cliques:** Inclui um sistema de cooldown para evitar cliques múltiplos e indesejados.

## Requisitos do Sistema

- Python 3.8 ou superior.
- Uma webcam conectada ao computador.

## Instalação

1.  **Clone o repositório (ou baixe os arquivos):**
    ```bash
    git clone https://github.com/seu-usuario/InVision.git
    cd InVision
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**
    Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Para instalá-las, execute o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```

## Como Rodar o Projeto

1.  **Permissão de Acesso à Câmera:**
    Ao executar o programa pela primeira vez, o seu sistema operativo pode solicitar permissão para que o script acesse a webcam. Certifique-se de conceder essa permissão.

2.  **Execute o script principal:**
    Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no terminal:
    ```bash
    python main.py
    ```

3.  **Uso:**
    - Ao iniciar, o programa estará pronto para uso. Não é necessária calibração.
    - Mova a cabeça para controlar o cursor do mouse.
    - Abra a boca para pressionar o botão do rato (e mantenha-a aberta para arrastar). Feche a boca para soltar.
    - Incline a cabeça para a direita para fazer scroll para baixo.
    - Incline a cabeça para a esquerda para fazer scroll para cima.
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
│   └── mouse_controller.py # Classe para controlar as ações do rato
└── README.md             # Este arquivo
