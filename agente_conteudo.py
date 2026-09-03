"""
Módulo de Geração de Conteúdo com IA
Gerador de artigos para blog de finanças
"""

import os
import json
from datetime import datetime

# Configuração do Prompt Mestre
PROMPT_MESTRE = """Você é um redator profissional de artigos de blog focado em SEO de conversão extrema, especialista em aprovação no Google AdSense e ranqueamento no Google Discover. Seu tom de voz deve ser acolhedor, empático, altamente didático e escrito estritamente na PRIMEIRA PESSOA DO SINGULAR (eu), utilizando o gatilho da "experiência própria compartilhada" para passar máxima autoridade aos leitores e algoritmos do Google.

Escreva um artigo de blog completo e aprofundado com base no seguinte tema e palavra-chave:
- TEMA DO ARTIGO: {tema}
- PALAVRA-CHAVE PRINCIPAL: {palavra_chave}

Você DEVE seguir rigorosamente as 9 REGRAS DE REDAÇÃO abaixo:

1. EXTENSÃO E ORGANIZAÇÃO: O artigo deve possuir no mínimo 1.200 palavras. Divida o conteúdo de forma lógica com Título H1 marcante e Subtítulos H2 bem definidos.

2. ESCANEABILIDADE ABSOLUTA: Todos os parágrafos do texto devem possuir no máximo 1 ou 2 linhas. Nunca crie blocos densos ou "paredões" de texto. Dê um espaço duplo entre cada um para garantir uma leitura fluida e limpa em celulares.

3. USO DE CHECKLISTS E LISTAS: Inclua de 1 a 2 listas numeradas ou checklists com ícones (emoji/pontos) ao longo do texto para quebrar o padrão visual e prender a atenção de quem escaneia a página rapidamente.

4. ENGENHARIA DE SEO: Repita a palavra-chave principal de forma natural no Título H1, no primeiro H2, no primeiro parágrafo do artigo, e espalhe-a ao menos 5 vezes no corpo do texto e no link/meta descrição sugeridos no fim.

5. MARCAÇÕES DE IMAGENS DO DISCOVER: O artigo deve possuir exatamente 3 imagens sugeridas. No ponto exato de inserção das imagens, exiba um bloco formatado em código assim:
[INSERIR IMAGEM - Dimensão: 1200x628 pixels, limpa, colorida, sem nenhum texto escrito na imagem. Descrição da imagem para IA: "Descrição da imagem que deve ser gerada por IA"]
Fonte: Acervo pessoal / Finanças Inteligentes

6. LINK EXTERNO DE AUTORIDADE: Identifique um termo técnico ou dado científico ao longo do artigo e simule uma âncora de link externo apontando para um grande portal de autoridade governamental ou de saúde (ex: Banco Central, Tesouro Nacional, Ministério da Saúde). Use a tag [Inserir link externo de autoridade apontando para o site confiável].

7. CHAMADA PARA LINK INTERNO (LEIA TAMBÉM): No meio do texto, insira um bloco visual destacado chamado "Leia também:" sugerindo um tema estritamente relacionado, usando a tag [Inserir link para artigo interno relevante].

8. SEÇÃO DE PERGUNTAS FREQUENTES (FAQ): Logo após o término do artigo principal, crie uma seção de FAQ contendo 3 a 4 perguntas reais que as pessoas buscam no Google sobre esse assunto, seguidas de respostas diretas e curtas de no máximo 2 linhas cada. Use muito SEO de cauda longa aqui.

9. CONCLUSÃO E FEEDBACK: Encerre o artigo com uma "Conclusão" carinhosa, incentivando os leitores a deixarem um comentário compartilhando a história deles ou dúvidas para eu responder de forma personalizada.

Não saia do personagem. Escreva de forma brilhante, focando em ajudar genuinamente quem está lendo o artigo."""


def gerar_prompt(tema: str, palavra_chave: str) -> str:
    """Gera o prompt completo para a IA"""
    return PROMPT_MESTRE.format(tema=tema, palavra_chave=palavra_chave)


def criar_estrutura_artigo(titulo: str, slug: str, categoria: str) -> dict:
    """Cria a estrutura básica de um artigo"""
    return {
        "titulo": titulo,
        "slug": slug,
        "categoria": categoria,
        "data_criacao": datetime.now().isoformat(),
        "status": "pendente",
        "palavra_chave": "",
        "meta_descricao": "",
        "imagens": [],
        "links_internos": [],
        "links_externos": []
    }


def salvar_artigo(conteudo: str, metadados: dict, pasta: str = "artigos"):
    """Salva o artigo em arquivo HTML"""
    os.makedirs(pasta, exist_ok=True)
    
    # Template HTML do artigo
    html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_descricao}">
    <meta name="keywords" content="{palavra_chave}, finanças, investimentos">
    
    <title>{titulo} | Finanças Inteligentes</title>
    
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="index.html" class="logo">
                <span class="logo-icon">💰</span>
                <span class="logo-text">Finanças Inteligentes</span>
            </a>
            <nav class="nav">
                <a href="index.html" class="nav-link">Início</a>
                <a href="index.html#renda-fixa" class="nav-link">Renda Fixa</a>
                <a href="index.html#planejamento" class="nav-link">Planejamento</a>
                <a href="index.html#renda-variavel" class="nav-link">Renda Variável</a>
                <a href="contato.html" class="nav-link">Contato</a>
            </nav>
            <button class="menu-toggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <main class="main">
        <article class="article-page">
            <div class="container">
                <div class="article-header">
                    <span class="article-category">{categoria}</span>
                    <h1>{titulo}</h1>
                    <div class="article-meta">
                        <span class="date">{data}</span>
                        <span class="read-time">{tempo_leitura} min de leitura</span>
                        <span class="author">Por Finanças Inteligentes</span>
                    </div>
                </div>

                <div class="article-content">
                    {conteudo}
                </div>

                <div class="article-navigation">
                    <a href="index.html" class="nav-button">← Voltar para artigos</a>
                </div>
            </div>
        </article>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Finanças Inteligentes</h4>
                    <p>Seu portal de referência em dicas de finanças pessoais e investimentos.</p>
                </div>
                <div class="footer-section">
                    <h4>Categorias</h4>
                    <ul>
                        <li><a href="index.html#renda-fixa">Renda Fixa</a></li>
                        <li><a href="index.html#planejamento">Planejamento</a></li>
                        <li><a href="index.html#renda-variavel">Renda Variável</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Institucional</h4>
                    <ul>
                        <li><a href="quem-somos.html">Quem Somos</a></li>
                        <li><a href="contato.html">Fale Conosco</a></li>
                        <li><a href="privacidade.html">Política de Privacidade</a></li>
                        <li><a href="termos.html">Termos de Uso</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Redes Sociais</h4>
                    <div class="social-links">
                        <a href="#" aria-label="Instagram">📸</a>
                        <a href="#" aria-label="YouTube">🎥</a>
                        <a href="#" aria-label="Twitter">🐦</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Finanças Inteligentes. Todos os direitos reservados.</p>
                <div class="footer-links">
                    <a href="privacidade.html">Política de Privacidade</a>
                    <a href="termos.html">Termos de Uso</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>"""
    
    # Calcular tempo de leitura (200 palavras por minuto)
    palavras = len(conteudo.split())
    tempo_leitura = max(1, palavras // 200)
    
    # Preencher template
    html = html_template.format(
        meta_descricao=metadados.get("meta_descricao", ""),
        palavra_chave=metadados.get("palavra_chave", ""),
        titulo=metadados.get("titulo", ""),
        categoria=metadados.get("categoria", ""),
        data=datetime.now().strftime("%d %b %Y"),
        tempo_leitura=tempo_leitura,
        conteudo=conteudo
    )
    
    # Salvar arquivo
    filepath = os.path.join(pasta, f"artigo-{metadados['slug']}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    
    return filepath


def checklist_artigo(conteudo: str) -> dict:
    """Verifica se o artigo atende aos requisitos"""
    palavras = len(conteudo.split())
    
    return {
        "palavras": palavras,
        "minimo_1200": palavras >= 1200,
        "tem_h1": "<h1>" in conteudo.lower(),
        "tem_h2": "<h2>" in conteudo.lower(),
        "tem_imagens": "[INSERIR IMAGEM" in conteudo,
        "qtd_imagens": conteudo.count("[INSERIR IMAGEM"),
        "tem_link_externo": "[Inserir link externo" in conteudo,
        "tem_link_interno": "[Inserir link para artigo interno" in conteudo,
        "tem_faq": "perguntas frequentes" in conteudo.lower() or "faq" in conteudo.lower(),
        "tem_conclusao": "conclusão" in conteudo.lower()
    }


# Exemplo de uso
if __name__ == "__main__":
    # Exemplo: gerar artigo sobre reserva de emergência
    tema = "Como montar uma reserva de emergência em 2026"
    palavra_chave = "reserva de emergência"
    
    prompt = gerar_prompt(tema, palavra_chave)
    
    print("=" * 60)
    print("PROMPT GERADO PARA A IA")
    print("=" * 60)
    print(prompt)
    print("=" * 60)
    print("\nEnvie este prompt para o ChatGPT/Claude e salve o resultado")
    print("Depois use salvar_artigo() para criar o arquivo HTML")
