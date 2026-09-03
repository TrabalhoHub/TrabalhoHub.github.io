# 📋 GUIA: Criar Repositório no GitHub

## Passo 1: Criar Conta no GitHub (se não tiver)

1. Acesse: https://github.com
2. Clique em "Sign up"
3. Preencha seus dados
4. Confirme o e-mail

---

## Passo 2: Criar o Repositório

1. Logue no GitHub
2. Clique no ícone "+" (canto superior direito)
3. Clique em "New repository"
4. Preencha:
   - **Repository name**: `seu-usuario.github.io` (substitua "seu-usuario" pelo seu nome de usuário)
   - **Description**: "Blog de Finanças Inteligentes"
   - **Visibility**: Public
5. **NÃO** marque nenhuma opção de inicialização
6. Clique em "Create repository"

---

## Passo 3: Conectar o Blog ao GitHub

Depois de criar o repositório, o GitHub vai mostrar uns comandos. Copie e cole ESTE comando no terminal:

```bash
git remote add origin https://github.com/SEU-USUARIO/seu-usuario.github.io.git
```

**IMPORTANTE:** Substitua "SEU-USUARIO" pelo seu nome de usuário do GitHub!

---

## Passo 4: Enviar os Arquivos

Depois de conectar, rode este comando:

```bash
git push -u origin main
```

---

## Passo 5: Ativar o GitHub Pages

1. Vá ao seu repositório no GitHub
2. Clique em "Settings" (Engrenagem)
3. No menu lateral, clique em "Pages"
4. Em "Source", selecione "main"
5. Clique em "Save"

---

## Passo 6: Acessar o Blog

Aguarde 2-3 minutos e acesse:
```
https://seu-usuario.github.io
```

---

## ⚠️ IMPORTANTE

- O nome do repositório DEVE ser `seu-usuario.github.io`
- Substitua "seu-usuario" pelo seu nome de usuário EXATO
- Exemplo: se seu usuário é "felipe123", o repositório será "felipe123.github.io"

---

## 📝 Me envie:

Quando terminar, me envie o **link do seu blog** (ex: https://felipe123.github.io) pra eu continuar a configuração!
