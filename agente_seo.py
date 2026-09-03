"""
Módulo de SEO e Indexação
Otimiza artigos e solicita indexação no Google
"""

import os
import re
from datetime import datetime
from xml.etree import ElementTree as ET
from xml.dom import minidom


class SEOOtimizador:
    """Classe para otimizar SEO dos artigos"""
    
    def __init__(self, pasta_raiz: str = "."):
        self.pasta_raiz = pasta_raiz
    
    def analisar_artigo(self, conteudo: str, palavra_chave: str) -> dict:
        """Analisa o SEO de um artigo"""
        # Contar palavras
        palavras = len(conteudo.split())
        
        # Verificar título H1
        tem_h1 = bool(re.search(r'<h1[^>]*>.*?</h1>', conteudo, re.DOTALL))
        
        # Verificar subtítulos H2
        h2_count = len(re.findall(r'<h2[^>]*>.*?</h2>', conteudo, re.DOTALL))
        
        # Contar palavra-chave
        pk_lower = palavra_chave.lower()
        conteudo_lower = conteudo.lower()
        pk_no_conteudo = conteudo_lower.count(pk_lower)
        
        # Verificar meta description
        tem_meta = bool(re.search(r'<meta\s+name="description"', conteudo))
        
        # Verificar imagens
        imagens = len(re.findall(r'\[INSERIR IMAGEM', conteudo))
        
        # Verificar links
        link_externo = bool(re.search(r'\[Inserir link externo', conteudo))
        link_interno = bool(re.search(r'\[Inserir link para artigo interno', conteudo))
        
        # Verificar FAQ
        tem_faq = bool(re.search(r'perguntas frequentes|faq', conteudo, re.IGNORECASE))
        
        # Calcular pontuação
        pontuacao = 0
        if palavras >= 1200: pontuacao += 20
        if tem_h1: pontuacao += 10
        if h2_count >= 3: pontuacao += 10
        if pk_no_conteudo >= 5: pontuacao += 15
        if tem_meta: pontuacao += 10
        if imagens == 3: pontuacao += 15
        if link_externo: pontuacao += 10
        if link_interno: pontuacao += 5
        if tem_faq: pontuacao += 5
        
        return {
            "palavras": palavras,
            "tem_h1": tem_h1,
            "h2_count": h2_count,
            "palavra_chave_qtd": pk_no_conteudo,
            "tem_meta": tem_meta,
            "imagens": imagens,
            "link_externo": link_externo,
            "link_interno": link_interno,
            "tem_faq": tem_faq,
            "pontuacao": pontuacao,
            "aprovado": pontuacao >= 80
        }
    
    def sugestoes_melhoria(self, analise: dict) -> list:
        """Retorna sugestões de melhoria"""
        sugestoes = []
        
        if not analise["tem_h1"]:
            sugestoes.append("Adicionar título H1")
        
        if analise["h2_count"] < 3:
            sugestoes.append(f"Adicionar mais subtítulos H2 (atual: {analise['h2_count']})")
        
        if analise["palavra_chave_qtd"] < 5:
            sugestoes.append(f"Repetir mais a palavra-chave (atual: {analise['palavra_chave_qtd']})")
        
        if not analise["tem_meta"]:
            sugestoes.append("Adicionar meta description")
        
        if analise["imagens"] != 3:
            sugestoes.append(f"Adicionar imagens (atual: {analise['imagens']}, ideal: 3)")
        
        if not analise["link_externo"]:
            sugestoes.append("Adicionar link externo de autoridade")
        
        if not analise["link_interno"]:
            sugestoes.append("Adicionar link interno (Leia também)")
        
        if not analise["tem_faq"]:
            sugestoes.append("Adicionar seção de Perguntas Frequentes (FAQ)")
        
        return sugestoes


class GeradorSitemap:
    """Gera e atualiza o sitemap.xml"""
    
    def __init__(self, dominio: str, pasta_raiz: str = "."):
        self.dominio = dominio.rstrip("/")
        self.pasta_raiz = pasta_raiz
        self.arquivo_sitemap = os.path.join(pasta_raiz, "sitemap.xml")
    
    def gerar_sitemap(self, artigos: list) -> str:
        """Gera o sitemap.xml"""
        # Criar XML
        urlset = ET.Element("urlset")
        urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
        
        # Adicionar página inicial
        url_principal = ET.SubElement(urlset, "url")
        ET.SubElement(url_principal, "loc").text = self.dominio
        ET.SubElement(url_principal, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url_principal, "changefreq").text = "daily"
        ET.SubElement(url_principal, "priority").text = "1.0"
        
        # Adicionar artigos
        for artigo in artigos:
            url = ET.SubElement(urlset, "url")
            ET.SubElement(url, "loc").text = f"{self.dominio}/{artigo['arquivo']}"
            ET.SubElement(url, "lastmod").text = artigo.get("data", datetime.now().strftime("%Y-%m-%d"))
            ET.SubElement(url, "changefreq").text = "weekly"
            ET.SubElement(url, "priority").text = "0.8"
        
        # Converter para string formatada
        xml_str = ET.tostring(urlset, encoding="unicode")
        xml_pretty = minidom.parseString(xml_str).toprettyxml(indent="  ")
        
        # Remover声明 XML duplicado
        xml_pretty = xml_pretty.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="UTF-8"?>')
        
        # Salvar arquivo
        with open(self.arquivo_sitemap, "w", encoding="utf-8") as f:
            f.write(xml_pretty)
        
        return self.arquivo_sitemap
    
    def adicionar_artigo(self, arquivo: str, data: str = None):
        """Adiciona um artigo ao sitemap"""
        # Ler sitemap existente ou criar novo
        artigos = []
        
        if os.path.exists(self.arquivo_sitemap):
            tree = ET.parse(self.arquivo_sitemap)
            root = tree.getroot()
            
            for url in root.findall("url"):
                loc = url.find("loc").text
                if loc and "/artigo-" in loc:
                    arquivo_existente = loc.split("/")[-1]
                    lastmod = url.find("lastmod").text if url.find("lastmod") is not None else ""
                    artigos.append({
                        "arquivo": arquivo_existente,
                        "data": lastmod
                    })
        
        # Adicionar novo artigo
        artigos.append({
            "arquivo": arquivo,
            "data": data or datetime.now().strftime("%Y-%m-%d")
        })
        
        # Remover duplicatas
        artigos_unicos = []
        arquivos_vistos = set()
        for artigo in artigos:
            if artigo["arquivo"] not in arquivos_vistos:
                artigos_unicos.append(artigo)
                arquivos_vistos.add(artigo["arquivo"])
        
        # Gerar sitemap atualizado
        return self.gerar_sitemap(artigos_unicos)


class IndexadorGoogle:
    """Classe para auxiliar na indexação no Google"""
    
    def __init__(self, dominio: str):
        self.dominio = dominio
    
    def gerar_instrucoes_indexacao(self, url: str) -> str:
        """Gera instruções para indexação manual"""
        return f"""
╔══════════════════════════════════════════════════════════════╗
║           INSTRUÇÕES PARA INDEXAÇÃO NO GOOGLE               ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  URL para indexar: {url}
║                                                              ║
║  1. Acesse Google Search Console:                            ║
║     https://search.google.com/search-console                 ║
║                                                              ║
║  2. No menu lateral, clique em "Inspeção de URL"             ║
║                                                              ║
║  3. Cole a URL completa e pressione Enter                    ║
║                                                              ║
║  4. Aguarde a análise do Google                              ║
║                                                              ║
║  5. Clique em "Solicitar Indexação"                          ║
║                                                              ║
║  6. Aguarde a confirmação (pode levar alguns minutos)        ║
║                                                              ║
║  DICA: Após publicar, faça isso IMEDIATAMENTE para           ║
║        o Google indexar mais rápido!                         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    
    def gerar_checklist_seo(self) -> str:
        """Gera checklist de SEO para antes de publicar"""
        return """
╔══════════════════════════════════════════════════════════════╗
║              CHECKLIST DE SEO ANTES DE PUBLICAR              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  [ ] Título contém a palavra-chave principal?                ║
║  [ ] Meta description está otimizada (até 160 caracteres)?   ║
║  [ ] Artigo tem no mínimo 1.200 palavras?                    ║
║  [ ] Parágrafos têm no máximo 2 linhas?                      ║
║  [ ] Existem 3 imagens no formato 1200x628?                  ║
║  [ ] Imagens têm atribuição de fonte?                        ║
║  [ ] Link externo de autoridade foi inserido?                ║
║  [ ] Link interno (Leia também) foi inserido?                ║
║  [ ] FAQ com 3-4 perguntas foi adicionado?                   ║
║  [ ] Conclusão com convite ao comentário existe?             ║
║  [ ] Arquivo foi salvo com nome correto?                     ║
║  [ ] Sitemap foi atualizado?                                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""


# Exemplo de uso
if __name__ == "__main__":
    # Testar otimizador
    otimizador = SEOOtimizador()
    
    # Exemplo de conteúdo
    conteudo_exemplo = """
    <h1>Como Montar uma Reserva de Emergência</h1>
    <p>A reserva de emergência é essencial.</p>
    <h2>O que é reserva de emergência?</h2>
    <p>É um dinheiro guardado para imprevistos.</p>
    [INSERIR IMAGEM - Dimensão: 1200x628 pixels]
    Fonte: Acervo pessoal / Finanças Inteligentes
    """
    
    analise = otimizador.analisar_artigo(conteudo_exemplo, "reserva de emergência")
    
    print("Análise de SEO:")
    print(f"  Palavras: {analise['palavras']}")
    print(f"  Pontuação: {analise['pontuacao']}/100")
    print(f"  Aprovado: {'✓' if analise['aprovado'] else '✗'}")
    
    sugestoes = otimizador.sugestoes_melhoria(analise)
    if sugestoes:
        print("\nSugestões de melhoria:")
        for s in sugestoes:
            print(f"  • {s}")
    
    # Gerar checklist
    indexador = IndexadorGoogle("financas-inteligentes.com")
    print(indexador.gerar_checklist_seo())
