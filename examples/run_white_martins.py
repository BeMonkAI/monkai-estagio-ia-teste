#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo: Executar AtendentePro com template White Martins

Este exemplo mostra como usar a biblioteca com o template de IVA/Tributação.
"""

import asyncio
from pathlib import Path

from atendentepro import (
    create_standard_network,
    configure,
)
from agents import Runner


async def main():
    """Exemplo de uso do AtendentePro com template White Martins."""
    
    # Definir o caminho dos templates
    templates_root = Path(__file__).parent.parent / "client_templates"
    
    # Criar a rede de agentes para White Martins
    print("🔧 Criando rede de agentes White Martins...")
    network = create_standard_network(
        templates_root=templates_root,
        client="white_martins"
    )
    
    print("✅ Rede White Martins criada!")
    print("\n📋 Tópicos disponíveis:")
    print("   1. Compra Industrialização")
    print("   2. Compra Comercialização")
    print("   3. Compra Ativo Operacional")
    print("   4. Compra Ativo Projeto")
    print("   5. Consumo Administrativo")
    print("   6. Aquisição Frete")
    print("   7. Aquisição Energia Elétrica")
    print("   8. Serviços Ligados à Operação")
    print("   9. Serviços Não Ligados à Operação")
    
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
            print(f"\n🤖 GIGI: {response}")
            
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")


if __name__ == "__main__":
    print("=" * 50)
    print("  AtendentePro - White Martins (IVA/Tributação)")
    print("=" * 50)
    print("\nExemplos de perguntas:")
    print("  - 'Qual IVA para compra de industrialização?'")
    print("  - 'Preciso do código IVA para energia elétrica'")
    print("  - 'Como funciona a determinação de IVA?'")
    print("\nDigite 'sair' para encerrar.\n")
    
    asyncio.run(main())

