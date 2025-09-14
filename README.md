# YT Downloader

Este é um aplicativo de desktop para macOS que permite baixar vídeos do YouTube em alta qualidade e convertê-los para o formato MP4, compatível com o QuickTime Player.

## Como Usar

Este aplicativo é **autocontido**, o que significa que ele não requer nenhuma instalação manual de dependências como Python, `yt-dlp` ou `ffmpeg`.

1.  **Baixe o Aplicativo**:
    Vá para a [página de Releases](https://github.com/vagnersantosaraujo/yt-downloader-app/releases) e baixe o arquivo `YT-Downloader.app.zip` da versão mais recente.

2.  **Descompacte o Arquivo**:
    Encontre o arquivo `.zip` na sua pasta de Downloads e dê um duplo clique para descompactá-lo.

3.  **Execute o Aplicativo**:
    Arraste o `YT Downloader.app` para a sua pasta de Aplicativos e dê um duplo clique para abri-lo.
    *Nota de Segurança do macOS: Na primeira vez que abrir, o macOS pode exibir um aviso de segurança. Se isso acontecer, clique com o botão direito no aplicativo, selecione "Abrir" e confirme a sua intenção.*

4.  **Baixe Vídeos**:
    - Cole a URL de um vídeo do YouTube no campo de texto.
    - Clique no botão "Baixar Vídeo".
    - O vídeo será salvo na sua pasta `~/Downloads`.

## Desenvolvimento

O aplicativo foi empacotado usando `py2app` para incluir todas as dependências necessárias (Python, Tkinter, yt-dlp, ffmpeg) dentro do próprio `.app`. O script de build utilizado para isso é o `setup.py`.


