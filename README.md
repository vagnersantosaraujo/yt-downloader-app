# YT Downloader

Este é um aplicativo de desktop para macOS que permite baixar vídeos do YouTube em alta qualidade e convertê-los para o formato MP4, compatível com o QuickTime Player.

# YT Downloader

Este é um aplicativo de desktop para macOS que permite baixar vídeos do YouTube em alta qualidade e convertê-los para o formato MP4, compatível com o QuickTime Player.

## Guia de Instalação e Uso Passo a Passo

Siga estas instruções detalhadas para garantir que o aplicativo funcione perfeitamente.

### Passo 1: Instalar o Homebrew

O Homebrew é um gerenciador de pacotes que facilita a instalação de softwares no macOS. Se você já o tem instalado, pode pular para o próximo passo.

1.  **Verifique se o Homebrew está instalado**:
    Abra o aplicativo **Terminal** e execute o comando abaixo:
    ```bash
    brew --version
    ```
    Se você vir um número de versão (ex: `Homebrew 4.3.2`), pule para o **Passo 2**. Se receber um erro de "comando não encontrado", continue para o próximo ponto.

2.  **Instale o Homebrew**:
    Copie e cole o seguinte comando no seu Terminal e pressione Enter. Ele irá baixar e instalar o Homebrew automaticamente.
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    Você pode sempre encontrar o comando de instalação mais recente no [site oficial do Homebrew](https://brew.sh/index_pt-br).

### Passo 2: Instalar as Dependências do Aplicativo

Com o Homebrew pronto, agora você pode instalar todas as ferramentas que o YT Downloader precisa com um único comando.

1.  **Execute o comando de instalação**:
    Copie e cole o seguinte comando no seu Terminal. Ele instalará `yt-dlp`, `ffmpeg`, e a versão correta do `python` com o kit gráfico `python-tk`.
    ```bash
    brew install yt-dlp ffmpeg python python-tk
    ```

2.  **Por que isso é importante?**
    O aplicativo depende de ferramentas específicas para funcionar:
    *   `yt-dlp`: O motor principal que baixa os vídeos do YouTube.
    *   `ffmpeg`: A ferramenta que converte e combina os arquivos de vídeo e áudio.
    *   `python` e `python-tk`: A linguagem de programação e o kit de ferramentas gráficas que rodam a interface do aplicativo. Usar a versão do Homebrew é **crucial** para evitar crashes, pois a versão de Python que vem com o macOS não inclui esses componentes gráficos.

### Passo 3: Usar o Aplicativo

Com todos os pré-requisitos instalados, você está pronto para usar o aplicativo!

1.  Dê um duplo clique em `YT Downloader.app` para abri-lo.
2.  Copie a URL de um vídeo do YouTube e cole no campo de texto.
3.  Clique no botão "Baixar Vídeo".
4.  Aguarde o download e a conversão. O vídeo final será salvo na sua pasta de **Downloads** (`~/Downloads`).

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


