import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import re
import subprocess
import platform
import os

class PromptEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Prompts")
        self.root.geometry("800x600")
        
        # Frame para botões superiores
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(pady=10)
        
        # Botão Escolher arquivo
        self.btn_choose_file = tk.Button(self.top_frame, text="Escolher arquivo", command=self.load_file)
        self.btn_choose_file.pack(side=tk.LEFT, padx=5)
        
        # Botão Apagar
        self.btn_clear = tk.Button(self.top_frame, text="Apagar", command=self.clear_text)
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        
        # Campo de texto grande com scrollbar
        self.text_frame = tk.Frame(root)
        self.text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.text_area = scrolledtext.ScrolledText(self.text_frame, wrap=tk.WORD, height=15)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Botão Reconhecer entradas
        self.btn_recognize = tk.Button(root, text="Reconhecer entradas", command=self.recognize_variables)
        self.btn_recognize.pack(pady=5)
        
        # Frame para campos de entrada dinâmicos
        self.entries_frame = tk.Frame(root)
        self.entries_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Frame para botões inferiores
        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack(pady=10)
        
        # Botão Aplicar
        self.btn_apply = tk.Button(self.bottom_frame, text="Aplicar", command=self.apply_variables)
        self.btn_apply.pack(side=tk.LEFT, padx=5)
        
        # Botão Copiar
        self.btn_copy = tk.Button(self.bottom_frame, text="Copiar", command=self.copy_to_clipboard)
        self.btn_copy.pack(side=tk.LEFT, padx=5)
        
        # Área de status
        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=5)
        
        self.variables = {}
        self.entries = {}
    
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
                    self.status_label.config(text="Arquivo carregado com sucesso.")
            except FileNotFoundError:
                messagebox.showerror("Erro", "Arquivo não encontrado.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar arquivo: {str(e)}")
    
    def clear_text(self):
        self.text_area.delete(1.0, tk.END)
        self.clear_entries()
        self.status_label.config(text="Texto apagado.")
    
    def recognize_variables(self):
        text = self.text_area.get(1.0, tk.END)
        # Encontrar todas as ocorrências entre {}
        matches = re.findall(r'\{([^}]+)\}', text)
        # Remover duplicatas
        unique_vars = list(set(matches))
        if unique_vars:
            self.clear_entries()
            self.variables = {var: "" for var in unique_vars}
            for var in unique_vars:
                frame = tk.Frame(self.entries_frame)
                frame.pack(fill=tk.X, pady=2)
                label = tk.Label(frame, text=f"{var}:")
                label.pack(side=tk.LEFT)
                entry = tk.Entry(frame)
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
                self.entries[var] = entry
            self.status_label.config(text=f"{len(unique_vars)} variáveis reconhecidas.")
        else:
            self.status_label.config(text="Nenhuma entrada encontrada.")
    
    def clear_entries(self):
        for widget in self.entries_frame.winfo_children():
            widget.destroy()
        self.entries = {}
        self.variables = {}
    
    def apply_variables(self):
        for var, entry in self.entries.items():
            self.variables[var] = entry.get()
        
        text = self.text_area.get(1.0, tk.END)
        for var, value in self.variables.items():
            text = re.sub(r'\{' + re.escape(var) + r'\}', value, text)
        
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, text)
        self.status_label.config(text="Variáveis aplicadas.")
    
    def copy_to_clipboard(self):
        text = self.text_area.get(1.0, tk.END).strip()
        if text:
            # Método universal que funciona em Windows, macOS e Linux
            system = platform.system()
            
            try:
                if system == "Windows":
                    # Windows - usa clip.exe
                    subprocess.run("clip", shell=True, input=text.encode('utf-8'), check=True)
                    self.status_label.config(text="✅ Texto copiado para área de transferência!")
                
                elif system == "Darwin":  # macOS
                    # macOS - usa pbcopy
                    subprocess.run("pbcopy", shell=True, input=text.encode('utf-8'), check=True)
                    self.status_label.config(text="✅ Texto copiado para área de transferência!")
                
                elif system == "Linux":
                    # Linux - usa xclip ou xsel
                    try:
                        subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode('utf-8'), check=True)
                    except:
                        subprocess.run(["xsel", "--clipboard", "--input"], input=text.encode('utf-8'), check=True)
                    self.status_label.config(text="✅ Texto copiado para área de transferência!")
                
                else:
                    # Método de fallback
                    self.root.clipboard_clear()
                    self.root.clipboard_append(text)
                    self.root.update()
                    self.status_label.config(text="Texto copiado (método alternativo).")
                    
            except Exception as e:
                # Método de fallback final
                self.root.clipboard_clear()
                self.root.clipboard_append(text)
                self.root.update()
                self.status_label.config(text="Texto copiado (método Tkinter).")
        else:
            self.status_label.config(text="Nenhum texto para copiar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PromptEditor(root)
    root.mainloop()
