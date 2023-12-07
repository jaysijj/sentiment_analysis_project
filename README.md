# sentiment_analysis_project

# Aplicação Web de Análise de Sentimento
Este código engloba componentes de frontend e backend para uma aplicação web de análise de sentimento. Vamos detalhar.

## Frontend (HTML/JS)
### Estrutura HTML
O arquivo HTML (index.html) define a estrutura da página da web. Ele inclui:

- Metadados: Charset, configurações de viewport e título da página.
- Arquivos Estáticos: Carrega um arquivo CSS externo (style.css) para estilos.

### JavaScript
O script no arquivo HTML contém uma função analyzeSentiment:

Recupera a entrada do usuário da área de texto.
Verifica se a entrada está vazia e exibe um alerta se verdadeiro.
Envia uma solicitação POST assíncrona para um ponto de extremidade de API especificado (http://127.0.0.1:8000/api/analyze_sentiment/) com o texto do usuário.
Manipula a resposta, atualizando a página da web com o sentimento analisado.


## Backend (Django/Python)
### Dependências
O backend utiliza o Natural Language Toolkit (NLTK) e a biblioteca VaderSentiment para análise de sentimento.

### Ponto de Extremidade da API Django
Há um ponto de extremidade de API Django (/api/analyze_sentiment/) decorado com @api_view(['POST']). Este ponto de extremidade espera uma solicitação POST com dados JSON contendo o texto do usuário.

### Análise de Sentimento
A função backend analisa o sentimento usando o SentimentIntensityAnalyzer do NLTK/VaderSentiment.
A pontuação de sentimento composto é convertida em uma categoria de sentimento (Positivo, Negativo ou Neutro).
O resultado é retornado como JSON na resposta da API.


## Como Funciona em Conjunto
- O usuário insere texto na página da web.
- A função JavaScript analyzeSentiment envia o texto para o ponto de extremidade da API Django por meio de uma solicitação POST.
- O backend Django analisa o sentimento e retorna o resultado.
- O JavaScript atualiza a página da web com o sentimento analisado.
- Este código cria uma aplicação web simples de análise de sentimento, combinando componentes de frontend e backend para uma experiência do usuário integrada.






