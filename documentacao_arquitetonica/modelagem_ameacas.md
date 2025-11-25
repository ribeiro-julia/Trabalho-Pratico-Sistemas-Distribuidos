# 2. Modelagem de Ameaças

## 2.1. Metodologia de Análise

A modelagem de ameaças deste sistema foi conduzida utilizando o modelo **STRIDE**. O objetivo é compreender **como os dados fluem**, **quais são os limites de confiança**, **quais ativos devem ser protegidos** e **quais vetores de ataque podem ser explorados** por agentes maliciosos.

A análise considera os componentes principais do sistema:

*   **Frontend** baseado no Open WebUI
*   **Backend** desenvolvido em Python
*   **Serviços de IA/LLM** (Gemini, Ollama, DeepSeek-R1)
*   **Infraestrutura em Docker/Docker Compose**
*   **Usuários finais**
    
A metodologia aplicada se baseou nos seguintes passos:

1.  **Identificação dos ativos críticos**
2.  **Identificação dos trust boundaries**
3.  **Mapeamento da superfície de ataque**
4.  **Aplicação da análise STRIDE sobre cada componente crítico**
5.  **Proposição de mitigações** (não incluídas nesta seção)
    
## 2.2. Superfície de Ataque

A superfície de ataque representa todos os pontos acessíveis — direta ou indiretamente — nos quais um atacante pode tentar explorar vulnerabilidades. Com base na arquitetura estimada, a superfície de ataque inclui:

 - **1 Interface Web (Frontend)**
 - **2 Backend Python**
 - **3 LLMs (Modelos de Linguagem)**
 - **4 Infraestrutura Docker**
 - **5 Rede e Comunicação**
 - **6 Gestão de Segredos**

## 2.3. Matriz de Análise de Ameaças STRIDE

| Ameaça (STRIDE) | Descrição / Impacto |
| :--- | :--- |
| **S — Spoofing** | Algum container (ou serviço) malicioso se conecta como se fosse parte legítima. |
| **T — Tampering** | Manipulação das credenciais. |
| **R — Repudiation** | Falta de registro ou logs insuficientes. |
| **I — Information Disclosure** | Vazamento das chaves de API (ex: `GEMINI_API_KEY`) se não forem bem protegidas. |
| **D — Denial of Service** | Consumo massivo de LLM (custo elevado) para degradar serviço. |
| **E — Elevation of Privilege** | Explorar vulnerabilidades no LLM para executar código ou acessar dados que não deveria. |

## 2.4. Matriz de Risco

| Ameaça (STRIDE) | Descrição / Impacto | Probabilidade | Impacto | Nível de Risco | Justificativa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **S — Spoofing** | Algum container (ou serviço) malicioso se conecta como se fosse parte legítima. | Média | Alta | **Alto** | Ambientes Docker podem ser comprometidos caso portas estejam expostas ou não haja isolamento adequado. Ataques internos são plausíveis. |
| **T — Tampering** | Manipulação das credenciais. | Alta | Alta | **Crítico** | Credenciais em variáveis de ambiente ou arquivos `.env` são alvos comuns. Comprometimento leva a acesso total ao backend ou serviços externos. |
| **R — Repudiation** | Falta de registro ou logs insuficientes. | Média | Média | **Médio** | Se não houver logs estruturados, atividades maliciosas podem não ser rastreadas, mas não comprometem diretamente o sistema operacional. |
| **I — Information Disclosure** | Vazamento das chaves de API (ex: `GEMINI_API_KEY`) se não forem bem protegidas. | Alta | Alta | **Crítico** | Vazamento de chaves permite uso indevido de serviços externos, acesso a dados e custos financeiros elevados. É uma das vulnerabilidades mais exploradas em sistemas distribuídos. |
| **D — Denial of Service** | Consumo massivo de LLM (custo elevado) para degradar serviço. | Alta | Média | **Alto** | Não é necessário acesso privilegiado para gerar carga excessiva. Impacto financeiro e indisponibilidade tornam o risco relevante. |
| **E — Elevation of Privilege** | Explorar vulnerabilidades no LLM para executar código ou acessar dados que não deveria. | Baixa | Alta | **Médio** | Exploração direta no LLM é mais difícil, mas impacto é severo caso ocorra. Depende de falhas específicas no modelo ou implementação. |
