🎯 Objetivo
Criar a primeira versão do componente standalone dos flashcards.

🧠 Prompt Completo
```
Levando em conta o design dos componentes já existentes no repositório: https://github.com/thalesmenegueco/thalesmenegueco.github.io

Atue como um engenheiro sênior Angular (v17+), especialista em 
componentes reutilizáveis com TypeScript, SCSS e HTML.

Preciso de um componente FlashcardComponent para um site existente.

Requisitos funcionais:

Lado A: exibe uma frase em português (texto) OU um vídeo em Libras
Lado B: exibe a tradução no idioma oposto
No lado português, pode exibir uma imagem opcional relacionada à frase
O card deve ter animação de flip (clique para virar)

Interface do modelo de dados:

type: 'portugues' | 'libras'
frase?: string (se type === 'portugues')
videoUrl?: string (se type === 'libras')
traducao: string
imagemUrl?: string (opcional, só quando type === 'portugues')

Entregue: componente standalone, template HTML, estilos SCSS com 
animação CSS 3D de flip, sem dependências externas de UI.
```

🤖 Modelo Utilizado
- Modelo: gpt-5.1
- Adicionais: usado em conjunto com o agente "AdaptaOne26"

📦 Contexto e Arquivos de Referência
- referenciei o repositório na qual a feature seria adicionada na esperança de ele levar em conta a estrutura ja existente

🔄 Iterações
1. Versão 1 (o que funcionou: as implementações ficaram bem estruturadas, a maioria seguindo os padrões de código já existentes | não funcionou: a forma de implementação sugerida pela IA contava com o CommonModule já estando adicionado ao projeto, portanto essa implementação não funcionou)
2. Versão 2 (ajustes solicitados)
3. Versão final

💡 Insights e Aprendizados
- Poderia especificar quais coisas do repositório ele poderia levar em conta (estrutura de pastas, padrões de nomeação de variáveis etc)
- Especificar para ele usar práticas de código novas, pode se adicionar um arquivo com as atualizações da linguagem / padrões de desenvolvimento nos últimos 3 anos (se por acaso o dia de corte dos dados usados para treinamento foi anterior às atualizações)
- Quando for pedida a sugestão de uma feature, adicionar ao contexto os módulos que estão presentes no projeto e pedir que a implementação siga esse padrão com o mínimo de mudanças possível nas configurações do projeto - e se necessário realizar alguma mudança nas configurações por causa da nova feature, pedir que ele explique os motivos
- para ter certeza que a IA leve em conta os padrões de projeto já existentes, pode se colocar como contexto uma visualização de árvore do projeto e arquivos de pelo menos um componente
