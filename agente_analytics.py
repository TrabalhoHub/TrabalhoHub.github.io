"""
Módulo de Analytics e Métricas
Acompanha desempenho do blog e gera relatórios
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, List


class AnalyticsBlog:
    """Classe para analytics do blog"""
    
    def __init__(self, pasta_dados: str = "dados"):
        self.pasta_dados = pasta_dados
        self.arquivo_analytics = os.path.join(pasta_dados, "analytics.json")
        os.makedirs(pasta_dados, exist_ok=True)
    
    def carregar_dados(self) -> Dict:
        """Carrega dados de analytics"""
        if os.path.exists(self.arquivo_analytics):
            with open(self.arquivo_analytics, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "pageviews": {},
            "artigos": {},
            "fontes_trafego": {},
            "receita": {},
            "leads": []
        }
    
    def salvar_dados(self, dados: Dict):
        """Salva dados de analytics"""
        with open(self.arquivo_analytics, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    
    def registrar_pageview(self, pagina: str, fonte: str = "direto"):
        """Registra uma visualização de página"""
        dados = self.carregar_dados()
        
        # Data de hoje
        hoje = datetime.now().strftime("%Y-%m-%d")
        
        # Atualizar pageviews
        if pagina not in dados["pageviews"]:
            dados["pageviews"][pagina] = {}
        
        if hoje not in dados["pageviews"][pagina]:
            dados["pageviews"][pagina][hoje] = 0
        
        dados["pageviews"][pagina][hoje] += 1
        
        # Atualizar fontes de tráfego
        if fonte not in dados["fontes_trafego"]:
            dados["fontes_trafego"][fonte] = 0
        dados["fontes_trafego"][fonte] += 1
        
        self.salvar_dados(dados)
    
    def registrar_artigo(self, titulo: str, slug: str):
        """Registra um novo artigo"""
        dados = self.carregar_dados()
        
        if slug not in dados["artigos"]:
            dados["artigos"][slug] = {
                "titulo": titulo,
                "data_publicacao": datetime.now().isoformat(),
                "pageviews_total": 0,
                "receita_total": 0
            }
        
        self.salvar_dados(dados)
    
    def registrar_receita(self, valor: float, fonte: str = "adsense", data: str = None):
        """Registra receita"""
        dados = self.carregar_dados()
        
        if not data:
            data = datetime.now().strftime("%Y-%m-%d")
        
        if data not in dados["receita"]:
            dados["receita"][data] = 0
        
        dados["receita"][data] += valor
        
        self.salvar_dados(dados)
    
    def obter_estatisticas_periodo(self, dias: int = 7) -> Dict:
        """Retorna estatísticas dos últimos N dias"""
        dados = self.carregar_dados()
        
        data_inicio = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d")
        
        # Calcular pageviews do período
        pageviews_periodo = 0
        for pagina, datas in dados["pageviews"].items():
            for data, count in datas.items():
                if data >= data_inicio:
                    pageviews_periodo += count
        
        # Calcular receita do período
        receita_periodo = 0
        for data, valor in dados["receita"].items():
            if data >= data_inicio:
                receita_periodo += valor
        
        # Artigos mais populares
        artigos_populares = []
        for slug, info in dados["artigos"].items():
            artigos_populares.append({
                "titulo": info["titulo"],
                "slug": slug,
                "pageviews": info["pageviews_total"]
            })
        artigos_populares.sort(key=lambda x: x["pageviews"], reverse=True)
        
        return {
            "periodo": f"Últimos {dias} dias",
            "pageviews": pageviews_periodo,
            "receita": receita_periodo,
            "rpm": (receita_periodo / (pageviews_periodo / 1000)) if pageviews_periodo > 0 else 0,
            "artigos_mais_populares": artigos_populares[:5],
            "fontes_trafego": dados["fontes_trafego"]
        }
    
    def gerar_relatorio(self) -> str:
        """Gera relatório completo em texto"""
        stats = self.obter_estatisticas_periodo(30)
        
        relatorio = f"""
╔══════════════════════════════════════════════════════════════╗
║              RELATÓRIO DE ANALYTICS - BLOG                   ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📊 PERÍODO: {stats['periodo']}
║                                                              ║
║  👁️  PAGEVIEWS: {stats['pageviews']:,}
║                                                              ║
║  💰 RECEITA: R$ {stats['receita']:.2f}
║                                                              ║
║  📈 RPM (Receita por 1.000 views): R$ {stats['rpm']:.2f}
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🏆 ARTIGOS MAIS POPULARES:                                 ║
║                                                              ║
"""
        
        for i, artigo in enumerate(stats["artigos_mais_populares"], 1):
            relatorio += f"║  {i}. {artigo['titulo'][:40]}... ({artigo['pageviews']:,} views)\n"
        
        relatorio += f"""║
║  🌐 FONTES DE TRÁFEGO:                                      ║
║                                                              ║
"""
        
        for fonte, count in stats["fontes_trafego"].items():
            relatorio += f"║  • {fonte}: {count:,} visitas\n"
        
        relatorio += f"""║
╚══════════════════════════════════════════════════════════════╝
"""
        
        return relatorio
    
    def gerar_grafico_simples(self, dados: List[int], titulo: str) -> str:
        """Gera gráfico simples em ASCII"""
        if not dados:
            return "Sem dados para exibir"
        
        max_valor = max(dados)
        max_altura = 10
        
        grafico = f"\n{titulo}\n"
        grafico += "=" * 50 + "\n"
        
        for i, valor in enumerate(dados):
            altura = int((valor / max_valor) * max_altura) if max_valor > 0 else 0
            barra = "█" * altura
            grafico += f"Dia {i+1:2d} | {barra} {valor}\n"
        
        grafico += "=" * 50 + "\n"
        
        return grafico


class Dashboard:
    """Dashboard simplificado para terminal"""
    
    def __init__(self):
        self.analytics = AnalyticsBlog()
    
    def exibir_dashboard(self):
        """Exibe dashboard completo"""
        stats = self.analytics.obter_estatisticas_periodo(7)
        
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║                 📊 DASHBOARD - BLOG                         ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📅 ÚLTIMOS 7 DIAS                                          ║
║                                                              ║
║  ┌─────────────────┬─────────────────┐                      ║
║  │   PAGEVIEWS     │    RECEITA      │                      ║
║  │    {stats['pageviews']:>6,}       │   R$ {stats['receita']:>7.2f}    │                      ║
║  └─────────────────┴─────────────────┘                      ║
║                                                              ║
║  📈 RPM: R$ {stats['rpm']:.2f}                                    ║
║                                                              ║
║  🏆 TOP 5 ARTIGOS:                                          ║
║                                                              ║
""")
        
        for i, artigo in enumerate(stats["artigos_mais_populares"][:5], 1):
            print(f"║  {i}. {artigo['titulo'][:35]}")
            print(f"║     {artigo['pageviews']:,} views")
        
        print(f"""║
║  🌐 TRÁFEGO POR FONTE:                                      ║
║                                                              ║
"""
        for fonte, count in list(stats["fontes_trafego"].items())[:5]:
            print(f"║  • {fonte}: {count:,}")
        
        print(f"""║
╚══════════════════════════════════════════════════════════════╝
""")
    
    def exibir_metas(self):
        """Exibe metas e objetivos"""
        stats = self.analytics.obter_estatisticas_periodo(30)
        
        meta_pageviews = 10000
        meta_receita = 100
        
        progresso_pv = (stats["pageviews"] / meta_pageviews) * 100
        progresso_rec = (stats["receita"] / meta_receita) * 100
        
        barra_pv = "█" * int(progresso_pv / 5) + "░" * (20 - int(progresso_pv / 5))
        barra_rec = "█" * int(progresso_rec / 5) + "░" * (20 - int(progresso_rec / 5))
        
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║                   🎯 METAS - MÊS                            ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📊 PAGEVIEWS                                                ║
║  Meta: {meta_pageviews:,} | Atual: {stats['pageviews']:,}
║  [{barra_pv}] {progresso_pv:.1f}%
║                                                              ║
║  💰 RECEITA                                                  ║
║  Meta: R$ {meta_receita:.2f} | Atual: R$ {stats['receita']:.2f}
║  [{barra_rec}] {progresso_rec:.1f}%
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")


# Exemplo de uso
if __name__ == "__main__":
    analytics = AnalyticsBlog()
    dashboard = Dashboard()
    
    print("Exibindo dashboard...")
    dashboard.exibir_dashboard()
    
    print("\nExibindo metas...")
    dashboard.exibir_metas()
    
    print("\nGerando relatório completo...")
    print(analytics.gerar_relatorio())
