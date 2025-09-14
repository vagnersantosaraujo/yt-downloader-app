# YT Downloader

Este é um aplicativo de desktop para macOS que permite baixar vídeos do YouTube em alta qualidade e convertê-los para o formato MP4, compatível com o QuickTime Player.

## Como Usar

Este aplicativo é **autocontido**, o que significa que ele não requer nenhuma instalação manual de dependências. Siga os passos abaixo para instalar e rodar.

### 1. Baixe o Aplicativo
Vá para a [página de Releases](https://github.com/vagnersantosaraujo/yt-downloader-app/releases) e baixe o arquivo `YT-Downloader.app.zip` da versão mais recente.

### 2. Descompacte e Mova
- Encontre o arquivo `.zip` na sua pasta de Downloads e dê um duplo clique para descompactá-lo.
- Arraste o `YT Downloader.app` para a sua pasta de **Aplicativos**.

### 3. Autorize a Execução (Apenas na Primeira Vez)
O macOS possui um sistema de segurança chamado Gatekeeper que bloqueia aplicativos de desenvolvedores não identificados. Para autorizar o YT Downloader, siga estes passos:

1.  **Tente abrir o aplicativo** dando um duplo clique. Você verá um alerta dizendo que a Apple não pôde verificar o app. Clique em **OK**.
2.  Abra os **Ajustes do Sistema**.
3.  Vá para **Privacidade e Segurança**.
4.  Role para baixo até a seção "Segurança". Você verá uma mensagem informando que o "YT Downloader.app" foi bloqueado.
5.  Clique no botão **"Abrir Mesmo Assim"** ao lado da mensagem.
6.  Confirme sua identidade com sua senha ou Touch ID.

O aplicativo irá abrir, e o macOS não perguntará novamente.

### 4. Baixe Vídeos
- Cole a URL de um vídeo do YouTube no campo de texto.
- Clique no botão "Baixar Vídeo".
- O vídeo será salvo na sua pasta `~/Downloads`.

## Desenvolvimento

O aplicativo foi empacotado usando `py2app` para incluir todas as dependências necessárias (Python, Tkinter, yt-dlp, ffmpeg) dentro do próprio `.app`. O script de build utilizado para isso é o `setup.py`.


