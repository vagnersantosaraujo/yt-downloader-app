# YT Downloader

Este é um aplicativo de desktop para macOS que permite baixar vídeos do YouTube em alta qualidade e convertê-los para o formato MP4, compatível com o QuickTime Player.

## Como Usar

1.  Abra o aplicativo `YT Downloader.app`.
2.  Cole a URL do vídeo do YouTube no campo de texto.
3.  Clique no botão "Baixar Vídeo".
4.  O vídeo será baixado na melhor qualidade disponível e convertido para MP4.
5.  Após a conclusão, você será perguntado se deseja abrir o arquivo no Finder.

## Estrutura do Projeto

```
./
├── YT Downloader.app/  # O aplicativo macOS
│   └── Contents/
│       ├── MacOS/      # Contém o script de inicialização e o script Python
│       │   ├── YT Downloader
│       │   └── yt_downloader_gui.py
│       └── Info.plist  # Arquivo de configuração do aplicativo
└── README.md
└── .gitignore
```

## Requisitos

*   macOS
*   Homebrew (para `yt-dlp` e `ffmpeg`)
*   Python 3.11 (instalado via [python.org](https://www.python.org/downloads/macos/))

## Desenvolvimento

O aplicativo é construído com Python e Tkinter. Ele utiliza a ferramenta de linha de comando `yt-dlp` para o download e `ffmpeg` para a conversão.

