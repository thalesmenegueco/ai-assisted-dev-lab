🎯 Objetivo
Gerar um script em Python para editar prompts.

🧠 Prompt Completo
```
Funcionalidades:

- Um botão 'Escolher arquivo' para escolher um arquivo de onde será extraído o texto do prompt.
- O texto extraído será colocado num campo editável abaixo do primeiro botão descrito previamente. 
- Logo depois de extrair o texto, aparece um botão 'Reconhecer entradas'.
- Um botão "Apagar" que apaga todo o texto dentro do campo de texto. 
- O botão 'Reconhecer entradas' que acha todos "{}" que estão dentro do texto disponível para edição e para cada um dos "{}" cria um campo de entrada com o mesmo nome que está dentro dos {}. Exemplo: para o texto "Meu nome é {Nome}" será criada uma entrada com o nome "Nome". 
- Um botão 'Aplicar' que insere o texto dentro de cada uma das entradas nos lugares que onde estava no campo de texto. Exemplo: no campo "Nome" é digitado "Matheus", depois de apertado o botão 'Aplicar' o texto no campo ficará "Meu nome é Matheus"
- Um botão 'Copiar' que copia o texto final.
- Um espaço para avisar "Texto copiado!" ou "Nenhuma entrada encontrada"

Interface:

- Use a biblioteca Tkinter.
- O aplicativo terá somente uma tela
- Quero os botões 'Escolher arquivo' na parte de cima e do lado o botão 'Apagar'.
- Abaixo estará o campo de texto que terá de ser grande.
- Abaixo estarão os campos de entrada que aparecerão.
- Abaixo estará o botão 'Aplicar' e do lado o botão 'Copiar'

Dados:

- Se o texto tiver duas vezes o mesmo nome dentro de dois ou mais '{}', o app deve criar apenas um que preencha ambos. Exemplo: para o texto "Meu nome é {Nome}. Meu nome completo é {Nome} {Sobrenome}", no campo "Nome" é digitado "Matheus" e no campo "Sobrenome" é digitado "Barbosa", depois de apertado o botão 'Aplicar' o texto no campo ficará "Meu nome é Matheus. Meu nome completo é Matheus Barbosa"
- O texto original do prompt será retirado de um arquivo .txt dentro do próprio computador.
- O aplicativo não deve alterar o arquivo .txt original.
```

🤖 Modelo Utilizado
- Modelo: DeekSeek V3.2

📦 Contexto e Arquivos de Referência
- nenhum contexto

🔄 Iterações
1. Versão 1 (script quase perfeitamente funcional) -> ESTE PROMPT
2. Versão 2 (fazer uma versão onde seja possível copiar o texto gerado)

💡 Insights e Aprendizados
- Pedir para ele pensar nos possíveis erros e refatorar o código com base neles, pode evitar que aconteçam erros mais comuns

