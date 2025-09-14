# YT Downloader

Este é um aplicativo de desktop para macOS que permite baixar vídeos do YouTube em alta qualidade e convertê-los para o formato MP4, compatível com o QuickTime Player.

## Como Usar

Este aplicativo é **autocontido**, o que significa que ele não requer nenhuma instalação manual de dependências como Python, `yt-dlp` ou `ffmpeg`.

1.  **Baixe o Aplicativo**:
    Vá para a [página de Releases](https://github.com/vagnersantosaraujo/yt-downloader-app/releases) e baixe o arquivo `YT-Downloader.app.zip` da versão mais recente.

2.  **Descompacte o Arquivo**:
    Encontre o arquivo `.zip` na sua pasta de Downloads e dê um duplo clique para descompactá-lo.

3.  **Abra o Aplicativo pela Primeira Vez**:
    Arraste o `YT Downloader.app` para a sua pasta de Aplicativos. Devido às políticas de segurança do macOS para aplicativos não registrados na Apple Store, você precisará seguir estes passos na primeira execução:
    - **Clique com o botão direito** no ícone do `YT Downloader.app`.
    - No menu de contexto, selecione **"Abrir"**.
    - Uma janela de aviso aparecerá. Clique no botão **"Abrir"** novamente para confirmar.

    Fazendo isso, você cria uma exceção de segurança para o aplicativo, e nas próximas vezes, poderá abri-lo normalmente com um duplo clique.

4.  **Baixe Vídeos**:
    - Cole a URL de um vídeo do YouTube no campo de texto.
    - Clique no botão "Baixar Vídeo".
    - O vídeo será salvo na sua pasta `~/Downloads`.

## Desenvolvimento

O aplicativo foi empacotado usando `py2app` para incluir todas as dependências necessárias (Python, Tkinter, yt-dlp, ffmpeg) dentro do próprio `.app`. O script de build utilizado para isso é o `setup.py`.


