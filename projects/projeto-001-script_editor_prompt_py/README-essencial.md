# ✨ Editor de Prompts (Tkinter)

## 🎯 Descrição
Aplicativo simples em Python/Tkinter para carregar arquivos `.txt` contendo variáveis entre `{chaves}`, gerar automaticamente campos de entrada para cada variável e montar o texto final com substituições prontas para copiar para a área de transferência.

Criado totalmente a partir de um processo iterativo com IA, com ajustes de interface, regex, substituição e fallback multiplataforma para clipboard.

---

## 📸 Demonstração
Sugestões do que incluir:
- Tela inicial após carregar o arquivo.
- Campos dinâmicos gerados pelas variáveis.
- Texto final com variáveis substituídas.
- Botão de cópia funcionando.

---

## 🚀 Funcionalidades
- Carrega arquivos `.txt`.
- Detecta variáveis no formato `{nome}` usando regex.
- Gera inputs dinâmicos para cada variável única.
- Substitui variáveis no texto com um clique.
- Copia todo o conteúdo final (com ou sem *pyperclip*).
- Botão para instalar *pyperclip* (opcional).
- Botão para limpar campo de texto.
- Interface compacta em Tkinter.

---

## 🛠️ Tecnologias
- **Python 3.x**
- **Tkinter**
- **Regex (re)**
- **subprocess** (fallback de clipboard)
- **pyperclip** (opcional)

---

## ▶️ Como Executar

```
python editor_prompts.py
```

Dependência opcional:

```
pip install pyperclip
```

---

## 🧠 Estrutura Simples do Código
- Carregamento de arquivo via `filedialog`.
- Extração de variáveis: `re.findall(r"\{([^}]+)\}", texto)`.
- Campos dinâmicos criados no frame dedicado.
- Substituição com `re.sub`.
- Cópia via pyperclip ou fallback:
  - Windows → `clip`
  - macOS → `pbcopy`
  - Linux → `xclip` ou `xsel`

---

## 🔧 Melhorias Futuras
- Exportar texto final para arquivo.
- Pré-visualização em janela separada.
- Multiplicidade de templates carregados.
- Interface mais moderna.
- Empacotamento em executável.

---

## 📄 Licença
MIT

