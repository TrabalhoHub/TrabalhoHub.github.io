"""
Módulo de Tráfego e Leads
Gera posts para redes sociais e gerencia newsletter
"""

import os
import json
from datetime import datetime
from typing import List, Dict


class GeradorRedesSociais:
    """Gera conteúdo para redes sociais"""
    
    def __init__(self, nome_blog: str = "Finanças Inteligentes"):
        self.nome_blog = nome_blog
    
    def gerar_post_facebook(self, titulo: str, resumo: str, url: str, imagem: str = None) -> dict:
        """Gera post para Facebook"""
        # Hooks chamativos
        hooks = [
            f"💡 Você sabia que {titulo.lower()}?",
            f"🚨 ATENÇÃO: {titulo}",
            f"💰 {titulo} - Saiba como fazer isso agora!",
            f"📊 Descobri algo incrível sobre {titulo.lower()}",
            f"🔥 Não cometesse esse erro: {titulo}"
        ]
        
        import random
        hook = random.choice(hooks)
        
        post = f"""
{hook}

{resumo}

👉 Leia o artigo completo: {url}

{self.nome_blog} - Seu portal de finanças inteligentes 💰

#finanças #investimentos #rendafixa #economia #dinheiro
"""
        
        return {
            "plataforma": "facebook",
            "texto": post.strip(),
            "imagem": imagem,
            "url": url,
            "hashtags": ["finanças", "investimentos", "rendafixa", "economia", "dinheiro"]
        }
    
    def gerar_post_linkedin(self, titulo: str, resumo: str, url: str) -> dict:
        """Gera post para LinkedIn"""
        post = f"""
📈 {titulo}

{resumo}

Escrevi um artigo completo sobre esse assunto no {self.nome_blog}.

Nele, você vai descobrir:
✅ Conceitos básicos que todo mundo deveria saber
✅ Dicas práticas para aplicar no dia a dia
✅ Erros comuns que devem ser evitados

👉 Acesse aqui: {url}

#finanças #investimentos #carreira #desenvolvimentoprofissional
"""
        
        return {
            "plataforma": "linkedin",
            "texto": post.strip(),
            "url": url
        }
    
    def gerar_pin_pinterest(self, titulo: str, url: str, cor: str = "#10b981") -> dict:
        """Gera Pin para Pinterest"""
        pin = {
            "titulo": titulo,
            "url": url,
            "dimensoes": "1000x1500",  // Vertical
            "cor_fundo": cor,
            "sugestao_texto": f"""
IMAGEM VERTICAL:

Fundo: {cor}
Título grande e legível: {titulo}
Logo do blog no canto inferior

Exemplos de títulos para a imagem:
• "{titulo}"
• "Guia Completo: {titulo}"
• "Como {titulo.lower()} - Passo a Passo"
"""
        }
        
        return pin
    
    def gerar_short_youtube(self, titulo: str, url: str, pontos: List[str] = None) -> dict:
        """Roteiro para YouTube Short"""
        if not pontos:
            pontos = [
                "Problema que o artigo resolve",
                "Dica principal (rápida)",
                "Chamada para o artigo"
            ]
        
        roteiro = f"""
🎬 ROTEIRO - YOUTUBE SHORT (60 segundos)

ABERTURA (0-5s):
"Você sabia que {titulo.lower()}? Fica comigo que vou te ensinar!"

DESENVOLVIMENTO (5-45s):
"""
        
        for i, ponto in enumerate(pontos, 1):
            roteiro += f"""
Ponto {i}: {ponto}
(Câmera: close no rosto, tom empolgado)
"""
        
        roteiro += f"""
ENCERRAMENTO (45-60s):
"Quer saber mais? Clica no link aqui embaixo nos comentários!"

DESCRIÇÃO:
📌 {titulo}
🔗 Link completo: {url}
👆 Leia o artigo completo no blog!

#shorts #finanças #investimentos #dicas
"""
        
        return {
            "plataforma": "youtube_shorts",
            "roteiro": roteiro.strip(),
            "duracao": "60 segundos",
            "url": url
        }
    
    def gerar_todos_posts(self, titulo: str, resumo: str, url: str, slug: str) -> Dict:
        """Gera posts para todas as plataformas"""
        return {
            "facebook": self.gerar_post_facebook(titulo, resumo, url),
            "linkedin": self.gerar_post_linkedin(titulo, resumo, url),
            "pinterest": self.gerar_pin_pinterest(titulo, url),
            "youtube": self.gerar_short_youtube(titulo, url),
            "data_geracao": datetime.now().isoformat(),
            "artigo": titulo
        }
    
    def salvar_posts(self, posts: Dict, pasta: str = "redes-sociais"):
        """Salva os posts gerados em arquivos"""
        os.makedirs(pasta, exist_ok=True)
        
        data = datetime.now().strftime("%Y-%m-%d")
        arquivo = os.path.join(pasta, f"posts-{data}.json")
        
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
        
        return arquivo


class GerenciadorNewsletter:
    """Gerencia newsletter e captura de leads"""
    
    def __init__(self, pasta_dados: str = "dados"):
        self.pasta_dados = pasta_dados
        self.arquivo_leads = os.path.join(pasta_dados, "leads.json")
        os.makedirs(pasta_dados, exist_ok=True)
    
    def carregar_leads(self) -> List[Dict]:
        """Carrega lista de leads"""
        if os.path.exists(self.arquivo_leads):
            with open(self.arquivo_leads, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    
    def salvar_leads(self, leads: List[Dict]):
        """Salva lista de leads"""
        with open(self.arquivo_leads, "w", encoding="utf-8") as f:
            json.dump(leads, f, ensure_ascii=False, indent=2)
    
    def adicionar_lead(self, email: str, nome: str = "", fonte: str = "blog") -> bool:
        """Adiciona um novo lead"""
        leads = self.carregar_leads()
        
        # Verificar se já existe
        for lead in leads:
            if lead["email"] == email:
                return False
        
        novo_lead = {
            "email": email,
            "nome": nome,
            "fonte": fonte,
            "data_cadastro": datetime.now().isoformat(),
            "status": "ativo",
            "tags": []
        }
        
        leads.append(novo_lead)
        self.salvar_leads(leads)
        
        return True
    
    def remover_lead(self, email: str) -> bool:
        """Remove um lead"""
        leads = self.carregar_leads()
        leads_filtrados = [l for l in leads if l["email"] != email]
        
        if len(leads_filtrados) < len(leads):
            self.salvar_leads(leads_filtrados)
            return True
        return False
    
    def obter_estatisticas(self) -> Dict:
        """Retorna estatísticas dos leads"""
        leads = self.carregar_leads()
        
        total = len(leads)
        ativos = len([l for l in leads if l["status"] == "ativo"])
        
        # Leads por fonte
        fontes = {}
        for lead in leads:
            fonte = lead.get("fonte", "desconhecida")
            fontes[fonte] = fontes.get(fonte, 0) + 1
        
        return {
            "total": total,
            "ativos": ativos,
            "inativos": total - ativos,
            "por_fonte": fontes,
            "ultima_atualizacao": datetime.now().isoformat()
        }
    
    def gerar_template_email(self, assunto: str, conteudo: str) -> str:
        """Gera template de email para newsletter"""
        template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }}
        .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 8px; overflow: hidden; }}
        .header {{ background: #10b981; color: white; padding: 30px; text-align: center; }}
        .content {{ padding: 30px; }}
        .footer {{ background: #1f2937; color: white; padding: 20px; text-align: center; font-size: 12px; }}
        .button {{ background: #10b981; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px; display: inline-block; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💰 {self.nome_blog}</h1>
        </div>
        <div class="content">
            <h2>{assunto}</h2>
            {conteudo}
        </div>
        <div class="footer">
            <p>© 2026 {self.nome_blog}. Todos os direitos reservados.</p>
            <p><a href="#" style="color: #10b981;">Cancelar inscrição</a></p>
        </div>
    </div>
</body>
</html>
"""
        return template


class CampanhaTráfego:
    """Coordena campanhas de tráfego"""
    
    def __init__(self):
        self.redes = GeradorRedesSociais()
        self.newsletter = GerenciadorNewsletter()
    
    def campanha_novo_artigo(self, titulo: str, resumo: str, url: str, slug: str) -> Dict:
        """Cria campanha completa para novo artigo"""
        print(f"\n{'='*60}")
        print(f"CAMPANHA: {titulo}")
        print(f"{'='*60}\n")
        
        # Gerar posts para redes sociais
        posts = self.redes.gerar_todos_posts(titulo, resumo, url, slug)
        
        # Salvar posts
        arquivo_posts = self.redes.salvar_posts(posts)
        
        print("✓ Posts gerados para:")
        print(f"  • Facebook: {len(posts['facebook']['texto'])} caracteres")
        print(f"  • LinkedIn: {len(posts['linkedin']['texto'])} caracteres")
        print(f"  • Pinterest: Pin vertical")
        print(f"  • YouTube: Short de 60s")
        
        print(f"\n✓ Posts salvos em: {arquivo_posts}")
        
        # Instruções de publicação
        print("\n" + "="*60)
        print("PRÓXIMOS PASSOS:")
        print("="*60)
        print("1. Facebook: Copie o texto e publique na página do blog")
        print("2. LinkedIn: Copie e publique no seu perfil")
        print("3. Pinterest: Crie a imagem vertical e faça o pin")
        print("4. YouTube: Grave o short e adicione o link nos comentários")
        print("="*60)
        
        return posts


# Exemplo de uso
if __name__ == "__main__":
    # Testar gerador de redes sociais
    gerador = GeradorRedesSociais()
    
    titulo = "Como Montar uma Reserva de Emergência em 2026"
    resumo = "Descubra o passo a passo para criar sua reserva de emergência e proteger seu futuro financeiro."
    url = "https://financas-inteligentes.com/artigo-reserva.html"
    
    posts = gerador.gerar_todos_posts(titulo, resumo, url, "reserva-emergencia")
    
    print("POST PARA FACEBOOK:")
    print(posts["facebook"]["texto"])
    print("\n" + "-"*60)
    
    print("POST PARA LINKEDIN:")
    print(posts["linkedin"]["texto"])
    print("\n" + "-"*60)
    
    print("ROTEIRO PARA YOUTUBE SHORT:")
    print(posts["youtube"]["roteiro"])
