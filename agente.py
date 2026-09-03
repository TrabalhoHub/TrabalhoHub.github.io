"""
Agente Full-Stack para Blog
Módulo principal que integra todos os componentes
"""

import os
import sys
from datetime import datetime

# Importar módulos
from agente_conteudo import gerar_prompt, criar_estrutura_artigo, salvar_artigo, checklist_artigo
from agente_publicacao import PublicadorGitHub
from agente_seo import SEOOtimizador, GeradorSitemap, IndexadorGoogle
from agente_trafego import CampanhaTráfego, GerenciadorNewsletter


class AgenteBlog:
    """Agente principal que gerencia o blog completo"""
    
    def __init__(self, pasta_raiz: str = "."):
        self.pasta_raiz = pasta_raiz
        
        # Inicializar componentes
        self.publicador = PublicadorGitHub(pasta_raiz)
        self.seo = SEOOtimizador(pasta_raiz)
        self.trafego = CampanhaTráfego()
        self.newsletter = GerenciadorNewsletter(os.path.join(pasta_raiz, "dados"))
        
        # Configurações
        self.dominio = "financas-inteligentes.com"
        self.nome_blog = "Finanças Inteligentes"
    
    def novo_artigo(self, tema: str, palavra_chave: str, categoria: str = "Finanças"):
        """Cria um novo artigo do zero"""
        print(f"\n{'#'*60}")
        print(f"CRIANDO NOVO ARTIGO")
        print(f"{'#'*60}\n")
        
        # 1. Gerar prompt para a IA
        print("1. Gerando prompt para IA...")
        prompt = gerar_prompt(tema, palavra_chave)
        
        # Salvar prompt para referência
        os.makedirs("prompts", exist_ok=True)
        slug = tema.lower().replace(" ", "-")[:50]
        with open(f"prompts/prompt-{slug}.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        
        print(f"   ✓ Prompt salvo em prompts/prompt-{slug}.txt")
        
        # 2. Mostrar instruções
        print("\n" + "="*60)
        print("PRÓXIMO PASSO:")
        print("="*60)
        print("1. Copie o prompt gerado")
        print("2. Cole no ChatGPT, Claude ou outra IA")
        print("3. Copie o resultado gerado")
        print("4. Execute: agente.salvar_conteudo(slug, conteudo)")
        print("="*60)
        
        # 3. Criar estrutura do artigo
        estrutura = criar_estrutura_artigo(titulo=tema, slug=slug, categoria=categoria)
        estrutura["palavra_chave"] = palavra_chave
        
        return {
            "prompt": prompt,
            "estrutura": estrutura,
            "slug": slug
        }
    
    def salvar_conteudo(self, slug: str, conteudo: str, metadados: dict):
        """Salva o conteúdo gerado pela IA"""
        print(f"\n{'='*60}")
        print(f"SALVANDO ARTIGO: {slug}")
        print(f"{'='*60}\n")
        
        # 1. Verificar qualidade do conteúdo
        print("1. Verificando qualidade do conteúdo...")
        analise = checklist_artigo(conteudo)
        
        print(f"   • Palavras: {analise['palavras']} {'✓' if analise['minimo_1200'] else '✗ (mínimo 1.200)'}")
        print(f"   • H1: {'✓' if analise['tem_h1'] else '✗'}")
        print(f"   • H2: {analise['h2_count']} {'✓' if analise['h2_count'] >= 3 else '✗ (mínimo 3)'}")
        print(f"   • Imagens: {analise['qtd_imagens']} {'✓' if analise['qtd_imagens'] == 3 else '✗ (ideal: 3)'}")
        print(f"   • Link externo: {'✓' if analise['tem_link_externo'] else '✗'}")
        print(f"   • Link interno: {'✓' if analise['tem_link_interno'] else '✗'}")
        print(f"   • FAQ: {'✓' if analise['tem_faq'] else '✗'}")
        
        # 2. Salvar artigo
        print("\n2. Salvando artigo...")
        arquivo = salvar_artivo(conteudo, metadados, os.path.join(self.pasta_raiz, "blog-financeiro"))
        print(f"   ✓ Artigo salvo em: {arquivo}")
        
        # 3. Verificar SEO
        print("\n3. Verificando SEO...")
        analise_seo = self.seo.analisar_artigo(conteudo, metadados.get("palavra_chave", ""))
        print(f"   • Pontuação SEO: {analise_seo['pontuacao']}/100")
        
        if not analise_seo["aprovado"]:
            print("\n   Sugestões de melhoria:")
            for s in self.seo.sugestoes_melhoria(analise_seo):
                print(f"     - {s}")
        
        print(f"\n{'='*60}")
        print("ARTIGO SALVO COM SUCESSO!")
        print(f"{'='*60}")
        
        return {
            "arquivo": arquivo,
            "analise": analise,
            "analise_seo": analise_seo
        }
    
    def publicar_artigo(self, titulo: str, arquivo: str):
        """Publica um artigo no blog"""
        return self.publicador.publicar_artigo(titulo, arquivo)
    
    def campanha_artigo(self, titulo: str, resumo: str, url: str, slug: str):
        """Cria campanha de tráfego para um artigo"""
        return self.trafego.campanha_novo_artigo(titulo, resumo, url, slug)
    
    def atualizar_sitemap(self, artigos: list):
        """Atualiza o sitemap do blog"""
        sitemap = GeradorSitemap(self.dominio, self.pasta_raiz)
        arquivo = sitemap.gerar_sitemap(artigos)
        print(f"✓ Sitemap atualizado: {arquivo}")
        return arquivo
    
    def status_blog(self):
        """Mostra o status completo do blog"""
        print(f"\n{'#'*60}")
        print(f"STATUS DO BLOG: {self.nome_blog}")
        print(f"{'#'*60}\n")
        
        # Status do git
        status_git = self.publicador.verificar_status()
        print("📁 REPOSITÓRIO:")
        if status_git["repositorio_ok"]:
            print(f"   ✓ Git configurado")
            print(f"   • Arquivos pendentes: {status_git['arquivos_pendentes']}")
        else:
            print("   ✗ Git não configurado")
        
        # Últimos commits
        commits = self.publicador.obter_log(5)
        if commits:
            print("\n📝 ÚLTIMOS COMMITS:")
            for c in commits:
                print(f"   • {c}")
        
        # Estatísticas de leads
        stats_leads = self.newsletter.obter_estatisticas()
        print(f"\n👥 LEADS:")
        print(f"   • Total: {stats_leads['total']}")
        print(f"   • Ativos: {stats_leads['ativos']}")
        
        # Artigos pendentes
        artigos_pasta = os.path.join(self.pasta_raiz, "blog-financeiro")
        if os.path.exists(artigos_pasta):
            artigos = [f for f in os.listdir(artigos_pasta) if f.startswith("artigo-") and f.endswith(".html")]
            print(f"\n📄 ARTIGOS:")
            print(f"   • Publicados: {len(artigos)}")
        
        print(f"\n{'#'*60}")
    
    def ajuda(self):
        """Mostra ajuda do agente"""
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║           AGENTE FULL-STACK - COMANDOS                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  COMANDOS PRINCIPAIS:                                        ║
║                                                              ║
║  agente.novo_artigo(tema, palavra_chave, categoria)          ║
║     → Gera prompt para criar novo artigo                     ║
║                                                              ║
║  agente.salvar_conteudo(slug, conteudo, metadados)           ║
║     → Salva conteúdo gerado pela IA                          ║
║                                                              ║
║  agente.publicar_artigo(titulo, arquivo)                     ║
║     → Publica artigo no GitHub Pages                         ║
║                                                              ║
║  agente.campanha_artigo(titulo, resumo, url, slug)           ║
║     → Gera posts para redes sociais                          ║
║                                                              ║
║  agente.atualizar_sitemap(artigos)                           ║
║     → Atualiza sitemap.xml                                   ║
║                                                              ║
║  agente.status_blog()                                        ║
║     → Mostra status completo do blog                         ║
║                                                              ║
║  agente.ajuda()                                              ║
║     → Mostra esta mensagem de ajuda                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")


# Função principal para uso via terminal
def main():
    """Função principal"""
    agente = AgenteBlog()
    
    if len(sys.argv) < 2:
        agente.ajuda()
        return
    
    comando = sys.argv[1]
    
    if comando == "novo":
        if len(sys.argv) < 4:
            print("Uso: python agente.py novo [tema] [palavra-chave]")
            return
        tema = sys.argv[2]
        palavra_chave = sys.argv[3]
        agente.novo_artigo(tema, palavra_chave)
    
    elif comando == "status":
        agente.status_blog()
    
    elif comando == "ajuda":
        agente.ajuda()
    
    else:
        print(f"Comando desconhecido: {comando}")
        agente.ajuda()


if __name__ == "__main__":
    main()
