# TRABALHO SISTEMAS DISTRIBUÍDOS UFLA

## 📘 CONTEXTO E RELEVÂNCIA

Durante uma entrevista com um dos discentes do NEURON - Núcleo de Estudos da UFLA em Robótica Interativa, foram encontradas dificuldades que o núcleo enfrenta no momento de planejar e executar reuniões e na hora de criar postagens efetivas de marketing. Entre as principais dores identificadas:

-   Falta de um modelo de planejamento de reunião efetivo e eficiente
    
-   Falta de tempo dos integrantes para criar conteúdo para melhorar as postagens em redes sociais.
    
## 🎯 SOLUÇÃO PROPOSTA

Com base na constatação dessa demanda, nosso grupo se propôs a desenvolver um sistema chatbot, no qual o usuário poderia, dado um template, criar um documento estruturado de planejamento de uma determinada reunião e adicionar a funcionalidade de gerar imagens para criar posts de marketing.

## 🛠️ TECNOLOGIAS UTILIZADAS

<table border="1" style="border-collapse: collapse; width: 100%;">  
  <!-- Front-end -->  
  <tr>  
    <td style="padding: 8px;">Open WebUI</td>  
    <td style="padding: 8px;">Front-End</td>  
  </tr>  
  <!-- Back-end -->  
  <tr>   
    <td style="padding: 8px;">Python 3.14</td>  
    <td style="padding: 8px;">Back-End</td>  
  </tr>  
  <!-- Deepseek -->  
  <tr>
    <td style="padding: 8px;">DeepSeek-R1 (1.5B)</td>  
    <td style="padding: 8px;">Modelo LLM usado dentro da Ollama para gerar texto / atender prompts</td>  
  </tr>  
  <!-- Gemini -->  
  <tr>  
    <td style="padding: 8px;">Gemini</td>  
    <td style="padding: 8px;">Segundo modelo</td>  
  </tr>  
  <!-- Ollama -->  
  <tr>
    <td style="padding: 8px;">Ollama</td>  
    <td style="padding: 8px;">Engine de inferência LLM local para carregar e executar modelos</td>  
  </tr>  
  <!-- Docker -->  
  <tr> 
    <td style="padding: 8px;">Docker / Docker Compose</td>  
    <td style="padding: 8px;">Conteinerização e orquestração dos serviços</td>  
  </tr>  
</table>


## ESTRUTURA DO PROJETO

O projeto terá a seguinte estrutura:

-   Toda parte do front end da aplicação estará organizado na pasta <>
    
-   Toda parte da api de comunicação do sistema estará localizado no <>
    
-   Toda documentação Arquitetônica estará na pasta <>
    
-   Toda imagem que projeto irá usar estará na pasta <>
    

## DOCUMENTAÇÃO ARQUITETÔNICA

Toda a análise arquitetônica, modelagem de ameaças e estratégias de mitigação do sistema estão detalhadas nos seguintes documentos:

1.  Visão Arquitetônica Inicial: Descreve a arquitetura funcional do sistema antes da análise de segurança.
    
2.  Modelagem de Ameaças: Apresenta a análise de riscos e ameaças utilizando.
    
3.  Visão Arquitetônica Final e Mitigações: Detalha a arquitetura aprimorada com os controles de segurança implementados.
    

## RODANDO O PROJETO:

### 🚀 Como executar o projeto

Siga os passos abaixo para configurar e executar a aplicação contida neste repositório.

```bash
# 1. Instale o Docker e Docker Compose

# 2. Clone o repositório

git clone https://github.com/ribeiro-julia/Trabalho-Pratico-Sistemas-Distribuidos
cd Trabalho-Pratico-Sistemas-Distribuidos

# 3. Ajuste as variáveis de ambiente

GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
CLOUDINARY_CLOUD_NAME="YOUR_CLOUDINARY_CLOUD_NAME_HERE"
CLOUDINARY_API_KEY="YOUR_CLOUDINARY_API_KEY_HERE"
CLOUDINARY_API_SECRET="YOUR_CLOUDINARY_API_SECRET_HERE"

# 4. Execute o comando 

docker compose up

# 5. Acesse o link no seu navegador

http://localhost:3000
```

## DESENVOLVEDORES

  - [Gabriel Venâncio](https://github.com/gabrielvavelar)
  - [Gilson](https://github.com/RATZogun)
  - [Júlia Ribeiro](https://github.com/ribeiro-julia)
  - [Raynner](https://github.com/raynnertaniguch1)
