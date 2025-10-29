# Trabalho-Pratico-Sistemas-Distribuidos
Trabalho Prático da matéria de Sistemas Distribuídos 

# 🤖 MCP Local – Servidor de IA com Modelo Offline

## 📘 Descrição do Projeto
O **MCP Local** é uma aplicação desenvolvida em **Python** com **FastAPI** que executa um **modelo local de linguagem** (como o GPT-2 da Hugging Face) diretamente no servidor, sem depender de conexões externas.  
Seu objetivo é permitir a geração de texto de forma **offline**, rápida e segura, mantendo um histórico completo das interações realizadas pelo usuário.

O projeto é ideal para estudos de **IA local**, **desenvolvimento de chatbots autônomos**, ou **testes de inferência com modelos pré-treinados**.

---

## ⚙️ Funcionalidades
- 🧠 **Geração de texto local** com modelo Hugging Face (ex: GPT-2);  
- 📴 **Execução 100% offline**, sem chamadas a APIs externas;  
- 📜 **Histórico de interações** via endpoint `/mcp/logs`;  
- 🌐 **API RESTful** simples e compatível com qualquer frontend;  
- ⚡ **Execução rápida** com o servidor assíncrono **Uvicorn**.

---

## 🗺️ Arquitetura
<img width="982" height="267" alt="design" src="https://github.com/user-attachments/assets/d86ed983-3bbd-405d-a758-7c81663a90ba" />
