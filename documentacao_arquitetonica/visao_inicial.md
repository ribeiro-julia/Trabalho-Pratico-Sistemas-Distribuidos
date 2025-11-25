# 1. Visão Arquitetônica Inicial

## 1.1. Introdução
O projeto consiste em um sistema distribuído cujo objetivo é fornecer um **chatbot** para o planejamento de reuniões e criação de posts de marketing, auxiliando integrantes do núcleo **NEURON – Núcleo de Estudos da UFLA**.  
A aplicação permite que o usuário gere textos estruturados (como planos de reunião) e imagens de postagens a partir de templates pré-definidos.

## 1.2. Solução Proposta e Componentes

A solução é composta por múltiplos componentes distribuídos que trabalham juntos para oferecer geração de texto e imagens, além de uma interface amigável ao usuário.

### Componentes Principais

- **Frontend**: Interface web utilizada pelo usuário para interagir com o chatbot.  
- **Backend**: API responsável por receber solicitações do frontend, coordenar os serviços e acionar os agentes de IA.  
- **Agente de IA Local**: Modelo DeepSeek-R1 executado via Ollama (em contêiner), responsável por geração de texto local.  
- **Agente de IA Externo**: Serviço Gemini, utilizado para aumentar a capacidade e precisão das respostas.  
- **Serviço de Renderização de Imagens**: API externa (ex: Cloudinary) usada para geração e manipulação de imagens.  
- **Orquestração / Infraestrutura**: Docker e Docker Compose para execução dos serviços em contêineres isolados.

## Tabela 1 — Tecnologias e Componentes

| Componente | Tecnologia / Framework | Responsabilidade |
|-----------|------------------------|------------------|
| **Frontend** | Open WebUI | Interface com o usuário e interação com o backend |
| **Backend** | Python 3.14 | Orquestração das requisições entre frontend e agentes de IA |
| **Agente de IA Local** | DeepSeek-R1 + Ollama (Docker) | Geração local de texto |
| **Agente de IA Externo** | Gemini API | Geração avançada de respostas e complementação do agente local |
| **Serviço de Imagens** | Cloudinary (API externa) | Geração e hospedagem de imagens para posts |
| **Infraestrutura** | Docker / Docker Compose | Deploy, isolamento e escalabilidade |
| **Comunicação** | HTTP/REST | Troca de dados entre os serviços |

## 1.3. Fluxo de Dados Inicial

1. **Usuário → Frontend:** O usuário acessa a interface web e envia seu prompt ao chatbot.
2. **Frontend → Backend:** O frontend faz uma chamada de API para o backend, passando o prompt.
3. **Backend → Agentes de IA:**  
   - Para geração de texto: o backend encaminha o prompt ao DeepSeek (local) ou ao Gemini (externo).  
   - Para geração de imagens: o backend chama o serviço externo responsável (ex: Cloudinary).
4. **Agentes de IA → Backend:** Os agentes retornam o texto gerado ou metadados/imagens criadas.
5. **Backend → Frontend:** O backend processa e formata o resultado e envia ao frontend.
6. **Frontend → Usuário:** O frontend exibe o texto final ou a imagem gerada.

