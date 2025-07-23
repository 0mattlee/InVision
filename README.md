<p align="center">
  <img src="https://i.imgur.com/wbiVTb9.png" alt="InVision Logo" width="400"/>
</p>

# InVision - Acessibilidade e Controle por Gestos Faciais

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/github/license/0mattlee/InVision)

O InVision é uma solução de tecnologia assistiva projetada para empoderar pessoas com deficiências motoras, oferecendo uma nova forma de interagir com o computador. Utilizando apenas uma webcam, o InVision traduz movimentos faciais em comandos de controle do mouse, quebrando barreiras e promovendo a inclusão digital.

## Uma Ferramenta de Inclusão

Acreditamos que a tecnologia deve ser uma ponte, não um obstáculo. O InVision foi criado com o propósito de garantir que todos possam navegar, trabalhar e se comunicar no ambiente digital com mais autonomia e liberdade.

## Funcionalidades

- **Controle Preciso do Mouse:** A posição do nariz guia o cursor do mouse pela tela, com um sistema de movimento relativo que garante estabilidade e precisão.
- **Clique e Arraste Intuitivos:** Manter a boca aberta pressiona o botão do mouse, e fechá-la o solta. Isso permite realizar cliques simples e operações complexas como "arrastar e soltar" de forma natural.
- **Navegação por Scroll:** Incline a cabeça para a direita ou para a esquerda para rolar (scroll) páginas para baixo ou para cima, facilitando a leitura de documentos e a navegação em websites.
- **Feedback Visual em Tempo Real:** A aplicação exibe o vídeo da webcam com uma malha facial (Face Mesh) sobre o rosto, fornecendo um feedback claro dos pontos que estão sendo rastreados.

## Segurança e Privacidade

O InVision **não grava nem armazena** imagens ou vídeos capturados pela webcam. Todo o processamento é feito **localmente**, garantindo a privacidade do usuário.

## Status do Projeto

:warning: **Em Desenvolvimento**

O InVision é um projeto que está em desenvolvimento ativo por mim, Matheus. As funcionalidades atuais são estáveis, mas novas melhorias e recursos estão sendo planejados. Sinta-se à vontade para testar, mas tenha em mente que bugs podem ocorrer.

## Planejamento Futuro (Roadmap)

- [ ] Interface gráfica para configuração de sensibilidade e limiares.
- [ ] Suporte a múltiplos gestos (ex: piscar de olhos para clique direito).
- [ ] Perfis de configuração personalizáveis para diferentes usuários.
- [ ] Suporte a múltiplos idiomas.
- [ ] Instalador simplificado para Windows, macOS e Linux.

## Como Contribuir

Sua contribuição é muito bem-vinda! Se você tem ideias para novas funcionalidades, encontrou um bug ou quer melhorar o código, sinta-se à vontade para:

1.  Abrir uma **Issue** para discutir a sua ideia ou reportar um problema.
2.  Fazer um **Fork** do projeto, criar uma nova branch e enviar um **Pull Request** com as suas melhorias.

Juntos, podemos tornar o InVision uma ferramenta ainda mais poderosa e acessível.

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
