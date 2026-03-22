#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo: Executar AtendentePro com template EasyDr

Este exemplo mostra como usar a biblioteca com o template EasyDr
para atendimento ao cliente em plataforma de saúde digital.

REQUISITOS:
    - ATENDENTEPRO_LICENSE_KEY: Token de licença
    - OPENAI_API_KEY: Chave da API OpenAI
"""

import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# ============================================================================
# 1. ATIVAR LICENÇA ATENDENTEPRO
# ============================================================================
from atendentepro import activate, is_activated

license_key = os.getenv("ATENDENTEPRO_LICENSE_KEY")
if not license_key:
    print("❌ ATENDENTEPRO_LICENSE_KEY não configurada!")
    print("\n🔑 Configure a variável de ambiente:")
    print('   export ATENDENTEPRO_LICENSE_KEY="ATP_seu-token"')
    print("\n   Ou crie um arquivo .env com:")
    print('   ATENDENTEPRO_LICENSE_KEY=ATP_seu-token')
    print("\n📧 Para obter um token: contato@bemonkai.com")
    sys.exit(1)

try:
    activate(license_key)
except Exception as e:
    print(f"❌ Erro ao ativar licença: {e}")
    sys.exit(1)

# ============================================================================
# 2. CONFIGURAR OPENAI
# ============================================================================

# Adicionar client_templates ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "client_templates"))

# Configurar cliente OpenAI ANTES de importar os agents
from agents import set_default_openai_client, set_default_openai_api
from openai import AsyncOpenAI

# Verificar API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY não configurada!")
    print("\n🔑 Configure a variável de ambiente:")
    print('   export OPENAI_API_KEY="sua-chave"')
    print("\n   Ou crie um arquivo .env com:")
    print('   OPENAI_API_KEY=sua-chave')
    sys.exit(1)

# Configurar cliente padrão
client = AsyncOpenAI(api_key=api_key)
set_default_openai_client(client)
set_default_openai_api("chat_completions")

from easydr import (
    create_easydr_network,
    create_easydr_simple_agent,
    create_sac_standalone_agent,
    SAC_TOOLS,
)
from agents import Runner


async def main_network():
    """Exemplo usando a rede completa de agentes."""
    templates_root = Path(__file__).parent.parent / "client_templates"
    
    print("🔧 Criando rede de agentes EasyDr...")
    network = create_easydr_network(
        templates_root=templates_root,
        include_sac_agent=True,
    )
    
    print("✅ Rede EasyDr criada!")
    print("\n📋 Funcionalidades disponíveis:")
    print("   - Onboarding de novos usuários")
    print("   - Atendimento via SAC")
    print("   - Registro de chamados")
    
    print("\n💬 Iniciando conversa...")
    print("-" * 50)
    
    messages = []
    
    while True:
        try:
            user_input = input("\n👤 Você: ").strip()
            
            if user_input.lower() in ["sair", "exit", "quit", "q"]:
                print("\n👋 Até logo!")
                break
            
            if not user_input:
                continue
            
            messages.append({"role": "user", "content": user_input})
            
            result = await Runner.run(
                network.triage,
                messages
            )
            
            response = str(result.final_output) if result.final_output else "..."
            print(f"\n🏥 EasyDr: {response}")
            
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")


async def main_sac():
    """Exemplo usando apenas o SAC Agent."""
    print("🔧 Criando SAC Agent EasyDr...")
    
    # Criar agente SAC standalone
    sac_agent = create_sac_standalone_agent(
        name="SAC EasyDr",
    )
    
    print("✅ SAC Agent criado!")
    print("\n📋 Funcionalidades disponíveis:")
    print("   - Registrar dúvidas")
    print("   - Enviar feedbacks")
    print("   - Reportar problemas")
    print("   - Fazer reclamações")
    print("   - Enviar sugestões")
    print("   - Consultar status de chamados")
    print("   - Listar meus chamados")
    
    print("\n📧 Notificações:")
    print("   - Email de confirmação para o usuário")
    print("   (Configure SMTP_* no .env para ativar)")
    
    print("\n💬 Iniciando conversa...")
    print("-" * 50)
    
    messages = []
    
    while True:
        try:
            user_input = input("\n👤 Você: ").strip()
            
            if user_input.lower() in ["sair", "exit", "quit", "q"]:
                print("\n👋 Até logo!")
                break
            
            if not user_input:
                continue
            
            messages.append({"role": "user", "content": user_input})
            
            result = await Runner.run(sac_agent, messages)
            
            response = str(result.final_output) if result.final_output else "..."
            print(f"\n📞 SAC: {response}")
            
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")


async def main_simple():
    """Exemplo usando agente simples."""
    print("🔧 Criando agente simples EasyDr...")
    
    agent = create_easydr_simple_agent(include_sac_tools=True)
    
    print("✅ Agente criado!")
    print("\n💬 Iniciando conversa...")
    print("-" * 50)
    
    messages = []
    
    while True:
        try:
            user_input = input("\n👤 Você: ").strip()
            
            if user_input.lower() in ["sair", "exit", "quit", "q"]:
                print("\n👋 Até logo!")
                break
            
            if not user_input:
                continue
            
            messages.append({"role": "user", "content": user_input})
            
            result = await Runner.run(agent, messages)
            
            response = str(result.final_output) if result.final_output else "..."
            print(f"\n🏥 EasyDr: {response}")
            
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")


def show_examples(mode: str):
    """Mostra exemplos de comandos baseado no modo escolhido."""
    print("\n" + "=" * 50)
    print("\n📋 Exemplos de comandos:\n")
    
    print("  📞 SAC (Serviço de Atendimento ao Cliente):")
    print("    - Quero registrar uma duvida")
    print("    - Tenho um problema para reportar")
    print("    - Quero fazer uma reclamacao")
    print("    - Tenho um feedback sobre o aplicativo")
    print("    - Tenho uma sugestao de melhoria")
    
    print("\n  📝 Criar Chamado:")
    print("    - Criar chamado de duvida: Como agendar consulta?")
    print("    - Meu email e joao@email.com")
    print("    - Prioridade alta")
    
    print("\n  🔍 Consultar Chamados:")
    print("    - Consultar status do chamado SAC-20240105120000")
    print("    - Listar meus chamados do email joao@email.com")
    print("    - Qual o status do meu chamado?")
    
    print("\n  📊 Tipos de Chamado:")
    print("    - duvida: Perguntas sobre o serviço")
    print("    - problema: Erro técnico ou operacional")
    print("    - reclamacao: Insatisfação formal")
    print("    - feedback: Opinião ou comentário")
    print("    - sugestao: Ideia de melhoria")
    
    print("\n  ⚡ Níveis de Prioridade:")
    print("    - baixa: Pode aguardar alguns dias")
    print("    - normal: Atendimento padrão")
    print("    - alta: Requer atenção prioritária")
    print("    - urgente: Atendimento imediato")
    
    print("\n" + "-" * 50)
    
    print("\n📧 Para ativar envio de emails, configure no .env:")
    print("    SMTP_SERVER=smtp.gmail.com")
    print("    SMTP_PORT=587")
    print("    SMTP_USERNAME=seu-email@gmail.com")
    print("    SMTP_PASSWORD=sua-senha-de-app")
    print("    SMTP_FROM_EMAIL=sac@easydr.com")
    print("    SMTP_FROM_NAME=SAC EasyDr")
    
    print("\nDigite 'sair' para encerrar.\n")


if __name__ == "__main__":
    print("=" * 50)
    print("  AtendentePro - EasyDr (Saúde Digital)")
    print("=" * 50)
    print("\nEscolha o modo de execução:")
    print("  1. Rede completa de agentes (Onboarding + SAC)")
    print("  2. Agente simples (SAC)")
    print("  3. SAC Agent (apenas atendimento ao cliente)")
    
    choice = input("\nOpção (1, 2 ou 3): ").strip()
    
    show_examples(choice)
    
    if choice == "2":
        asyncio.run(main_simple())
    elif choice == "3":
        asyncio.run(main_sac())
    else:
        asyncio.run(main_network())
