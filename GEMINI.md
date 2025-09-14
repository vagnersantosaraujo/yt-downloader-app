# Visão Geral do Projeto

Este é um aplicativo de desktop para macOS para baixar vídeos do YouTube. Ele foi construído com Python e Tkinter para a interface gráfica do usuário. A funcionalidade principal de baixar e converter vídeos é gerenciada pelas ferramentas de linha de comando `yt-dlp` e `ffmpeg`.

O aplicativo oferece uma interface simples para colar uma URL do YouTube, baixar o vídeo na melhor qualidade disponível e convertê-lo para o formato MP4, que é compatível com o QuickTime Player.

# Compilando e Executando

Este projeto é um aplicativo macOS pré-empacotado (um pacote `.app`) e não requer um processo de compilação para ser executado.

## Executando o Aplicativo

1.  Dê um duplo clique em `YT Downloader.app` para abrir o aplicativo.
2.  Cole a URL de um vídeo do YouTube no campo de entrada.
3.  Clique no botão "Baixar Vídeo".
4.  O vídeo será baixado na sua pasta `~/Downloads`.

## Dependências

O aplicativo depende das seguintes ferramentas de linha de comando, que devem ser instaladas no sistema:

*   **yt-dlp**: Para baixar vídeos do YouTube.
*   **ffmpeg**: Para converter o vídeo para MP4.

Elas podem ser instaladas via Homebrew:

```bash
brew install yt-dlp ffmpeg
```

# Convenções de Desenvolvimento

## Estrutura do Projeto

O projeto está estruturado como um pacote de aplicativo macOS:

```
./
├── YT Downloader.app/
│   └── Contents/
│       ├── MacOS/
│       │   ├── YT Downloader  # O lançador executável
│       │   └── yt_downloader_gui.py  # O script Python principal
│       └── Info.plist
└── README.md
```

## Lógica Principal

A lógica principal do aplicativo está contida em `yt_downloader_gui.py`. Ele usa:

*   **Tkinter**: Para a interface gráfica do usuário.
*   **subprocess**: Para chamar `yt-dlp` e `ffmpeg`.
*   **threading**: Para executar o processo de download em uma thread separada para manter a GUI responsiva.

## Script de Lançamento

O aplicativo é iniciado através do script de shell `YT Downloader` localizado em `Contents/MacOS/`. Este script é responsável por:

1.  **Logging**: Ele cria e escreve em um arquivo de log em `YT Downloader.app/Contents/MacOS/app_log.txt`.
2.  **Executando Python**: Ele lança o script `yt_downloader_gui.py` usando `/usr/bin/env python3` para localizar o interpretador Python 3 no `PATH` do usuário, tornando o aplicativo mais portável.