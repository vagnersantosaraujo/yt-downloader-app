import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import threading
import json
import os

def open_file_in_finder(path):
    """Abre o arquivo no Finder, selecionando-o."""
    subprocess.run(["open", "-R", path])

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("URL Vazia", "Por favor, insira uma URL do YouTube.")
        return

    # Desabilitar o botão para evitar cliques duplos
    download_button.config(state=tk.DISABLED)
    progress_bar.config(mode='indeterminate')
    progress_bar.start()
    status_label.config(text="Iniciando download...")

    # Executar o download em uma thread separada para não bloquear a GUI
    thread = threading.Thread(target=run_yt_dlp, args=(url,))
    thread.start()

def run_yt_dlp(url):
    try:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # Comando para yt-dlp
        # -o: Define o template do nome do arquivo de saída para a pasta Downloads
        # --recode-video mp4: Garante a compatibilidade com QuickTime
        # --progress: Envia o progresso como JSON
        # --no-warnings: Limpa a saída
        command = [
            "/opt/homebrew/opt/yt-dlp/bin/yt-dlp",
            "-f", "bestvideo+bestaudio", # Baixa a melhor qualidade de vídeo e áudio separadamente
            "--ffmpeg-location", "/opt/homebrew/bin/ffmpeg", # Caminho explícito para o ffmpeg
            "-o", f"{downloads_path}/%(title)s.%(ext)s",
            "--recode-video", "mp4",
            "--progress",
            "--no-warnings"
        ]
        
        # Adiciona a URL ao comando
        command.append(url)

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

        final_filepath = ""
        for line in process.stdout:
            try:
                # Tenta decodificar a linha como JSON (para progresso)
                progress_data = json.loads(line)
                
                # Atualiza a GUI a partir da thread principal
                if progress_data.get("status") == "downloading":
                    progress_bar.stop()
                    progress_bar.config(mode='determinate')
                    
                    total_bytes = progress_data.get("total_bytes")
                    downloaded_bytes = progress_data.get("downloaded_bytes")
                    
                    if total_bytes and downloaded_bytes:
                        percent = (downloaded_bytes / total_bytes) * 100
                        progress_bar['value'] = percent
                        status_label.config(text=f"Baixando... {percent:.1f}%")
                        
                elif progress_data.get("status") == "finished":
                    final_filepath = progress_data.get("filename")
                    status_label.config(text="Download concluído. Convertendo...")
                    progress_bar.config(mode='indeterminate')
                    progress_bar.start()

            except json.JSONDecodeError:
                # Se não for JSON, pode ser outra mensagem
                pass
        
        process.wait()
        progress_bar.stop()
        progress_bar.config(mode='determinate')

        if process.returncode == 0:
            progress_bar['value'] = 100
            status_label.config(text="Conversão concluída com sucesso!")
            if messagebox.askyesno("Sucesso", f"Download concluído!\nO arquivo está em: {final_filepath}\n\nDeseja vê-lo no Finder?"):
                print(f"Attempting to open: {final_filepath}") # Log the path
                open_file_in_finder(final_filepath)
        else:
            stderr_output = process.stderr.read()
            messagebox.showerror("Erro no Download", f"Ocorreu um erro:\n{stderr_output}")
            status_label.config(text="Falha no download.")
            progress_bar['value'] = 0

    except Exception as e:
        messagebox.showerror("Erro Inesperado", str(e))
        status_label.config(text="Ocorreu um erro inesperado.")
        progress_bar['value'] = 0
    finally:
        # Reabilitar o botão
        download_button.config(state=tk.NORMAL)


# --- Configuração da Interface Gráfica ---
root = tk.Tk()
root.title("YT Downloader")
root.geometry("500x200")

frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

url_label = ttk.Label(frame, text="URL do Vídeo do YouTube:")
url_label.pack(pady=5)

url_entry = ttk.Entry(frame, width=50)
url_entry.pack(fill=tk.X, expand=True, pady=5)

download_button = ttk.Button(frame, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=10)

progress_bar = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
progress_bar.pack(pady=5)

status_label = ttk.Label(frame, text="Aguardando URL...")
status_label.pack(pady=5)

root.mainloop()
