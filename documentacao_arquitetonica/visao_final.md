# 3. Visão Arquitetônica Final (Pós-Mitigação)

## 3.1. Introdução
Após a análise de riscos detalhada no documento de Modelagem de Ameaças, a arquitetura inicial foi aprimorada com a adição de múltiplos controles de segurança. Esta Visão Arquitetônica Final descreve a estrutura do sistema com as medidas de mitigação implementadas para garantir a confidencialidade, integridade e disponibilidade das informações.

## 3.2. Estratégias de Mitigação e Aprimoramentos
As seguintes estratégias foram incorporadas ao design do sistema para tratar as ameaças identificadas pelo modelo STRIDE.

 - Remoção de chaves embutidas em imagens Docker, arquivos versionados ou logs
 - Usar OpenWebUi para manter um histórico de conversas com o chatbot
 - Deixar que o usuário impute as próprias chaves no arquivo .env 
 - Possibilidade de interromper chamadas para a LLM caso o sistema esteja sobrecarregado

## Conclusão

As mitigações propostas reforçam a segurança nas principais áreas de risco identificadas e garantem maior robustez à arquitetura distribuída. A adoção dessas práticas reduz consideravelmente a probabilidade e o impacto das ameaças classificadas como críticas ou de alto risco, resultando em um sistema mais resiliente e confiável.