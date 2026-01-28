# 🧠 Insights do Projeto

## 🔶 Visão Geral
Este projeto explora como usar IA para gerar scripts que se comportam como aplicativos para computador, experimentando a biblioteca Tkinter para fazer  algo que eu estava precisando - um editor de prompts.

---

## 🔶 Objetivos do Experimento  
- Queria poder transformar qualquer arquivo de texto em um template para editar informações específicas dentro de prompts
- Testar capacidade do Deekseek para geração de código "simples"
- Imaginava que sairia certo com os primeiros prompts  

---

## 🔶 Processo de Desenvolvimento Assistido por IA  
### 1. Prompt Inicial  
```
Quero um aplicativo Editor de Prompts capaz de editar a partir de templates. 

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

### 2. Iterações Importantes  
**Iteração 1 — Resultado & Ajustes**  
- Pedi um script para editar prompts feito em python e descrevi
- Recebi o código do script com quase todas tudo funcionando perfeitamente
- O que funcionou  
- Precisei ajustar a funcionalidade de "copiar o texto"  

**Iteração 2 — Resultado & Ajustes**  
- Relatei meu problema: "Mesmo que apareça "Texto copiado!", quando aperto Ctrl+V, não vem o texto."

---

## 🔶 Principais Aprendizados  
### ✅ O que funcionou bem  
-  
-  

### ⚠️ O que não funcionou tão bem  
-  O script apresentou um erro com relação a uma funcionalidade da biblioteca (que normalmente dava esse tipo de erro)
-  

### 🔧 Como resolvi  
-  Descrevi meu problema para o modelo (Iteração 2)
-  

---

## 🔶 Erros, Surpresas e Descobertas  
Use este espaço para registrar momentos inesperados:  
- Mesmo pedindo para ele seguir as melhores práticas, no código o modelo implementou uma estratégia que dava um erro conhecido (limitação na área de transferência do Tkinter)

---

## 🔶 Boas Práticas Descobertas  
- Para descrição das funcionalidades: seguir a ordem de ações do usuário
- Para a descrição da interface: seguir a ordem de leitura - da esquerda para a direira, de cima para baixo 
- Aplicar a técnica "few-shot prompting", ou seja, dar exemplos de input-processamento-output
- Blocos explicando: "Funcionalidades", "Interface" e "Dados"   
- Talvez seja interessante, depois de descrever o script/software, pedir para ele listar os erros que podem ocorrer implementando as funcionalidades descritas em relação à plataforma-alvo (computador, mobile, web  etc) e as bibliotecas usadas (como foi o caso do Tkinter), e - com base nos possíveis erros - refatorar o código pedindo para ele implementar de um jeito que evite os possíveis erros listados 

---

## 🔶 Possibilidades Futuras  
- Ideias que surgiram durante o projeto  
- Extensões possíveis  
- Experimentações que ficaram para depois  

---

## 🔶 Reflexão Final  
Uma conclusão pessoal:  
- Como este projeto evoluiu sua visão de desenvolvimento assistido por IA?  
- O que faria diferente se começasse hoje?  
- O que isso ensinou sobre seu próprio processo?  

---

## 🔶 Referências Úteis  
- Links que te ajudaram  
- Artigos, vídeos, documentação  
- Prompts importantes (além do inicial)
