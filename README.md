# Processo Seletivo MonkAI — Estagiário em IA

## Teste Técnico de Estresse

Bem-vindo(a) ao processo seletivo da **MonkAI**. Este é um teste prático com tempo limitado que avalia sua capacidade de **usar Inteligência Artificial como ferramenta de produtividade real**.

---

## Como funciona

1. No **dia e horário combinados**, você receberá acesso a este repositório template
2. A partir desse momento, o relógio de **2 horas** começa a contar
3. Crie um **repositório privado** na sua conta do GitHub com base neste template
4. Adicione o usuário **@arthurvaz05** como colaborador do seu repositório privado
5. Trabalhe localmente e faça **push** dos seus commits
6. O horário do seu **último push** será considerado como entrega
7. Commits após o prazo de 2h **não serão considerados**

---

## Regras

| Item | Detalhe |
|---|---|
| **Tempo total** | **2 horas** a partir do recebimento do link do repositório |
| **Controle de tempo** | O horário do seu **último push** é o que conta como entrega |
| **Ferramentas permitidas** | Qualquer IDE e qualquer ferramenta de IA (Claude, ChatGPT, Copilot, Cursor, etc.) |
| **Restrição** | Não pode pedir ajuda a outras pessoas |
| **Entrega** | Tudo deve ser commitado e enviado (push) para este repositório |

> **Importante:** Você **deve documentar** todas as ferramentas de IA, IDEs e modelos que utilizou (detalhes na Tarefa 5).

---

## Credenciais

O token de licença da lib AtendentePro para uso neste teste:

```
ATENDENTEPRO_LICENSE_KEY=ATP_eyJvcmciOiJNb25rQUktRXN0YWdpby1JQSIsImV4cCI6MTc4MTk1MTkwMywiZmVhdCI6WyJmdWxsIl0sInYiOjF9.e6f882d00e9d510c
```

Adicione ao seu `.env` ou exporte como variável de ambiente antes de rodar a aplicação.

---

## Tarefas

Você deve completar **todas as tarefas abaixo**. Leia tudo antes de começar e planeje seu tempo.

---

### Tarefa 1 — API com a lib AtendentePro

Na pasta `/docs` você encontrará o `README` da lib **AtendentePro** e na pasta `/examples` alguns exemplos de uso.

**Você deve:**
- Criar uma API funcional dentro da pasta `/src` utilizando a lib AtendentePro
- A API deve ter **no mínimo 2 endpoints** funcionais
- A API deve estar funcional e rodando localmente

**Entregável:** Código na pasta `/src` + instruções de como rodar no seu README pessoal (`ENTREGA.md`)

---

### Tarefa 2 — Gerenciamento de Secrets com Azure

Suas credenciais e secrets **não podem estar hardcoded** no código.

**Você deve:**
- Configurar o **Azure Key Vault** (ou serviço equivalente de secrets da Azure) para armazenar as credenciais da API
- A aplicação da Tarefa 1 deve consumir os secrets a partir do vault
- Caso não tenha acesso à Azure, implemente a **lógica de integração** com Key Vault usando variáveis de ambiente como fallback, mas o código deve estar preparado para consumir do vault

**Entregável:** Código integrado + evidência da configuração (prints ou logs na pasta `/reports`)

---

### Tarefa 3 — Testes de Performance via MonkAI Hub

**Você deve:**
- Criar testes de performance/carga para os endpoints da Tarefa 1 utilizando o **MonkAI Hub**
- Executar os testes e gerar um relatório

**Entregável:** Relatório salvo em `/reports/performance-report.json` (ou `.html`)

---

### Tarefa 4 — Deploy no Railway via MCP

**Você deve:**
- Fazer deploy da aplicação em um servidor de teste no **Railway**
- Configurar o deploy utilizando **MCP (Model Context Protocol)**
- A aplicação deve estar acessível via URL pública

**Entregável:** URL do servidor no `ENTREGA.md` + evidências da configuração MCP em `/reports`

---

### Tarefa 5 — Documentação de Stacks de IA

**Você deve:** preencher o arquivo `STACKS_IA.md` (template já incluso na raiz) com:

- IDE utilizada e versão
- Modelo(s) de IA utilizados (nome e versão)
- Ferramentas auxiliares
- Detalhamento de uso por tarefa
- Reflexão sobre o que funcionou e o que não funcionou

**Entregável:** Arquivo `STACKS_IA.md` preenchido

---

## Estrutura do Repositório

```
monkai-estagio-ia-teste/
├── README.md              ← Você está aqui
├── ENTREGA.md             ← Seu README pessoal de entrega
├── STACKS_IA.md           ← Template para documentar uso de IA
├── src/                   ← Seu código da API (Tarefa 1)
├── docs/                  ← README da lib AtendentePro
├── examples/              ← Exemplos de uso da lib
├── reports/               ← Relatórios e evidências (Tarefas 2, 3, 4)
└── .github/               ← Configurações (se necessário)
```

---

## Critérios de Avaliação

| Critério | Peso | O que avalia |
|---|---|---|
| **Uso de IA** | 30% | Quão bem soube usar IA para acelerar e entregar |
| **Completude** | 25% | Quantas tarefas conseguiu entregar em 2h |
| **Qualidade do código** | 15% | Código limpo, organizado, funcional |
| **Infraestrutura** | 15% | Key Vault + Railway configurados corretamente |
| **Comunicação** | 15% | Clareza da documentação, do STACKS_IA.md e do raciocínio |

---

## Dica

> Este teste foi projetado para ser **impossível de completar em 2 horas sem o uso intensivo de IA**.
> Não tente fazer tudo manualmente. Use IA desde o primeiro minuto.
> Saber **o que perguntar** e **como usar** a IA é a habilidade que estamos avaliando.

---

**Boa sorte!**

*Equipe MonkAI*
