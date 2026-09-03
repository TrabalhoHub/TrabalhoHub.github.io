# 🤖 Agente Full-Stack para Blog

Sistema automatizado completo para gerenciar um blog profissional de finanças.

## 📁 Estrutura do Projeto

```
blog-financeiro/
├── index.html              # Página principal
├── styles.css              # Estilos
├── script.js               # Funcionalidades JS
├── artigo-*.html           # Artigos publicados
├── images/                 # Imagens do blog
├── dados/                  # Dados do agente
│   └── leads.json         # Lista de leads
├── redes-sociais/          # Posts gerados
├── prompts/                # Prompts para IA
├── logs/                   # Logs de execução
│
├── agente.py              # Módulo principal
├── agente_conteudo.py     # Geração com IA
├── agente_publicacao.py   # Publicação automática
├── agente_seo.py          # SEO e indexação
├── agente_trafego.py      # Redes sociais e leads
│
├── quem-somos.html        # Página institucional
├── contato.html           # Fale conosco
├── privacidade.html       # Política de privacidade
├── termos.html            # Termos de uso
├── AGENTE.md              # Documentação completa
└── README.md              # Este arquivo
```

## 🚀 Como Usar

### 1. Criar um Novo Artigo

```python
from agente import AgenteBlog

# Inicializar agente
agente = AgenteBlog()

# Criar novo artigo (gera prompt para IA)
resultado = agente.novo_artigo(
    tema="Como Montar uma Reserva de Emergência",
    palavra_chave="reserva de emergência",
    categoria="Renda Fixa"
)

# Copiar o prompt e gerar conteúdo com IA (ChatGPT/Claude)
# Depois salvar:
agente.salvar_conteudo(
    slug="reserva-emergencia",
    conteudo="conteúdo gerado pela IA aqui...",
    metadados={
        "titulo": "Como Montar uma Reserva de Emergência",
        "palavra_chave": "reserva de emergência",
        "categoria": "Renda Fixa"
    }
)
```

### 2. Publicar Artigo

```python
# Publicar no GitHub Pages
agente.publicar_artigo(
    titulo="Como Montar uma Reserva de Emergência",
    arquivo="artigo-reserva-emergencia.html"
)
```

### 3. Criar Campanha de Tráfego

```python
# Gerar posts para redes sociais
agente.campanha_artigo(
    titulo="Como Montar uma Reserva de Emergência",
    resumo="Descubra o passo a passo para criar sua reserva...",
    url="https://financas-inteligentes.com/artigo-reserva-emergencia.html",
    slug="reserva-emergencia"
)
```

### 4. Verificar Status

```python
# Ver status completo do blog
agente.status_blog()
```

## 📋 Checklist Automático

O agente verifica automaticamente:

- [ ] Mínimo 1.200 palavras
- [ ] Títulos H1 e H2 presentes
- [ ] 3 imagens no formato correto
- [ ] Links internos e externos
- [ ] FAQ com perguntas frequentes
- [ ] SEO otimizado

## 🔧 Configuração

### Variáveis de Ambiente (opcional)

Crie um arquivo `.env`:

```env
# GitHub (para publicação automática)
GITHUB_TOKEN=seu_token_aqui
GITHUB_REPO=seu-usuario/seu-usuario.github.io

# Google (para analytics e search console)
GOOGLE_ANALYTICS_ID=UA-XXXXXXXXX
GOOGLE_ADSENSE_ID=ca-pub-XXXXXXXXXXXXXXXX

# IA (para geração de conteúdo)
OPENAI_API_KEY=sk-...
```

## 📊 Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| `agente.novo_artigo()` | Cria prompt para novo artigo |
| `agente.salvar_conteudo()` | Salva conteúdo gerado |
| `agente.publicar_artigo()` | Publica no GitHub Pages |
| `agente.campanha_artigo()` | Gera posts para redes sociais |
| `agente.atualizar_sitemap()` | Atualiza sitemap.xml |
| `agente.status_blog()` | Mostra status completo |
| `agente.ajuda()` | Mostra ajuda |

## 📈 Fluxo de Trabalho Completo

```
1. IDEIA
   └→ agente.novo_artigo(tema, palavra_chave)

2. CONTEÚDO
   ├→ Copiar prompt gerado
   ├→ Colar no ChatGPT/Claude
   ├→ Copiar resultado
   └→ agente.salvar_conteudo(slug, conteudo)

3. PUBLICAÇÃO
   └→ agente.publicar_artigo(titulo, arquivo)

4. TRÁFEGO
   └→ agente.campanha_artigo(titulo, resumo, url)

5. MONETIZAÇÃO
   ├→ Solicitar AdSense após 15 artigos
   └→ Configurar anúncios no blog
```

## 🎯 Dicas

1. **Consistência**: Publique pelo menos 2-3 artigos por semana
2. **SEO**: Sempre verifique o checklist antes de publicar
3. **Tráfego**: Divulgue cada artigo em pelo menos 3 plataformas
4. **Analytics**: Monitore quais artigos trazem mais tráfego
5. **Monetização**: Aguarde 15+ artigos para solicitar AdSense

## 📚 Recursos

- [Guia de Monetização](guia-blog-monetizacao.md)
- [Documentação do Agente](AGENTE.md)
- [Google Search Console](https://search.google.com/search-console)
- [Google AdSense](https://www.google.com/adsense/)

## 🆘 Suporte

Em caso de dúvidas, execute:

```python
agente.ajuda()
```

Ou consulte a documentação em `AGENTE.md`.
