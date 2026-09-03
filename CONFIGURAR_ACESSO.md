# 🔐 CONFIGURAR ACESSO AO GITHUB

## O que aconteceu?

O Git precisa de autenticação para enviar arquivos ao GitHub. Existem 2 formas seguras:

---

## Opção 1: GitHub CLI (Mais Fácil)

### 1. Instale o GitHub CLI
Acesse: https://cli.github.com/
Baixe e instale para Windows

### 2. Faça login
Abra o terminal e digite:
```bash
gh auth login
```

### 3. Siga as instruções
- Escolha: GitHub.com
- Escolha: HTTPS
- Escolha: Login with a web browser
- Digite o código que aparecer

### 4. Depois rode:
```bash
git push -u origin main
```

---

## Opção 2: Personal Access Token (Mais Seguro)

### 1. Crie um token no GitHub
1. Vá em: https://github.com/settings/tokens
2. Clique em "Generate new token"
3. Nome: "blog-financeiro"
4. Marque: `repo` (controle total)
5. Clique em "Generate token"
6. **COPIE O TOKEN** (só aparece uma vez!)

### 2. Configure no Git
Rode este comando (substitua SEU_TOKEN pelo token copiado):
```bash
git config --global credential.helper store
```

### 3. Envie os arquivos
```bash
git push -u origin main
```

Quando pedir usuário e senha:
- **Usuário**: TrabalhoHub
- **Senha**: Cole o token que copiou

---

## ⚠️ IMPORTANTE

- O token é como uma senha - **NÃO compartilhe**
- Guarde em local seguro
- Se perder, gere um novo no GitHub

---

## 📝 Me avise quando configurar!

Assim que fizer login, me avise que eu envio os arquivos automaticamente!
