"""
Módulo de Publicação Automática
Publica artigos no GitHub Pages automaticamente
"""

import os
import subprocess
from datetime import datetime


class PublicadorGitHub:
    """Classe para publicar artigos no GitHub Pages"""
    
    def __init__(self, repo_path: str = ".", remote: str = "origin"):
        self.repo_path = repo_path
        self.remote = remote
        self.branch = "main"
    
    def executar_comando(self, comando: str) -> tuple:
        """Executa um comando git e retorna (sucesso, output)"""
        try:
            resultado = subprocess.run(
                comando,
                shell=True,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            return resultado.returncode == 0, resultado.stdout + resultado.stderr
        except Exception as e:
            return False, str(e)
    
    def verificar_git(self) -> bool:
        """Verifica se o diretório é um repositório git"""
        sucesso, _ = self.executar_comando("git status")
        return sucesso
    
    def inicializar_git(self) -> bool:
        """Inicializa um repositório git"""
        sucesso, output = self.executar_comando("git init")
        if sucesso:
            print("✓ Repositório git inicializado")
        else:
            print(f"✗ Erro ao inicializar: {output}")
        return sucesso
    
    def adicionar_arquivos(self, arquivos: list = None) -> bool:
        """Adiciona arquivos ao staging"""
        if arquivos:
            for arquivo in arquivos:
                sucesso, output = self.executar_comando(f"git add {arquivo}")
                if not sucesso:
                    print(f"✗ Erro ao adicionar {arquivo}: {output}")
                    return False
        else:
            sucesso, output = self.executar_comando("git add .")
            if not sucesso:
                print(f"✗ Erro ao adicionar arquivos: {output}")
                return False
        
        print("✓ Arquivos adicionados ao staging")
        return True
    
    def commit(self, mensagem: str) -> bool:
        """Cria um commit"""
        sucesso, output = self.executar_comando(f'git commit -m "{mensagem}"')
        if sucesso:
            print(f"✓ Commit criado: {mensagem}")
        else:
            print(f"✗ Erro ao criar commit: {output}")
        return sucesso
    
    def push(self) -> bool:
        """Envia as alterações para o repositório remoto"""
        sucesso, output = self.executar_comando(f"git push {self.remote} {self.branch}")
        if sucesso:
            print("✓ Alterações enviadas para o GitHub")
        else:
            print(f"✗ Erro ao enviar: {output}")
        return sucesso
    
    def publicar_artigo(self, titulo: str, arquivo: str) -> bool:
        """Publica um artigo no blog"""
        print(f"\n{'='*60}")
        print(f"PUBLICANDO ARTIGO: {titulo}")
        print(f"{'='*60}\n")
        
        # Verificar se é um repositório git
        if not self.verificar_git():
            print("Inicializando repositório git...")
            if not self.inicializar_git():
                return False
        
        # Adicionar arquivos
        if not self.adicionar_arquivos():
            return False
        
        # Criar commit
        data = datetime.now().strftime("%d/%m/%Y")
        mensagem = f"Novo artigo: {titulo}"
        if not self.commit(mensagem):
            return False
        
        # Enviar para o GitHub
        if not self.push():
            return False
        
        print(f"\n{'='*60}")
        print("✓ ARTIGO PUBLICADO COM SUCESSO!")
        print(f"{'='*60}")
        print(f"O artigo '{titulo}' está agora live no blog.")
        print("O GitHub Pages atualizará automaticamente em alguns minutos.")
        
        return True
    
    def verificar_status(self) -> dict:
        """Verifica o status do repositório"""
        sucesso, output = self.executar_comando("git status --porcelain")
        
        if sucesso:
            arquivos_pendentes = len(output.strip().split('\n')) if output.strip() else 0
            return {
                "repositorio_ok": True,
                "arquivos_pendentes": arquivos_pendentes,
                "detalhes": output
            }
        else:
            return {
                "repositorio_ok": False,
                "arquivos_pendentes": 0,
                "detalhes": output
            }
    
    def obter_log(self, limite: int = 5) -> list:
        """Retorna os últimos commits"""
        sucesso, output = self.executar_comando(f"git log --oneline -{limite}")
        
        if sucesso and output.strip():
            return output.strip().split('\n')
        return []


class PublicadorSimples:
    """Publicador simplificado para uso via terminal"""
    
    def __init__(self):
        self.publicador = PublicadorGitHub()
    
    publicar_artigo(self, titulo: str, arquivo: str):
        """Publica um artigo"""
        return self.publicador.publicar_artigo(titulo, arquivo)
    
    def status(self):
        """Mostra o status do repositório"""
        status = self.publicador.verificar_status()
        
        print("\n" + "="*60)
        print("STATUS DO REPOSITÓRIO")
        print("="*60)
        
        if status["repositorio_ok"]:
            print("✓ Repositório git configurado")
            print(f"  Arquivos pendentes: {status['arquivos_pendentes']}")
        else:
            print("✗ Repositório git não encontrado")
            print("  Execute: git init")
        
        # Últimos commits
        commits = self.publicador.obter_log(5)
        if commits:
            print("\nÚltimos commits:")
            for commit in commits:
                print(f"  • {commit}")
        
        print("="*60)
    
    def publicar(self, titulo: str, arquivo: str):
        """Interface simplificada para publicação"""
        resposta = input(f"\nPublicar '{titulo}'? (s/n): ")
        
        if resposta.lower() == 's':
            sucesso = self.publicador.publicar_artigo(titulo, arquivo)
            
            if sucesso:
                print("\n✓ Artigo publicado com sucesso!")
                print("Aguarde alguns minutos para o GitHub Pages atualizar.")
            else:
                print("\n✗ Erro ao publicar artigo.")
        else:
            print("\nPublicação cancelada.")


# Exemplo de uso
if __name__ == "__main__":
    pub = PublicadorSimples()
    
    print("="*60)
    print("PUBLICADOR AUTOMÁTICO DE BLOG")
    print("="*60)
    
    pub.status()
    
    # Exemplo de publicação
    # pub.publicar("Como Montar Reserva de Emergência", "artigo-reserva.html")
