# 🔒 CHECKLIST DE SEGURANÇA

## ✅ Segurança do Computador

### O que eu já fiz:
- [x] Criado arquivo `.gitignore` - impede envio de arquivos sensíveis
- [x] Protegidos: `.env`, `credentials.json`, `secrets.json`, `*.key`, `*.pem`
- [x] Protegidos: dados pessoais (`leads.json`, `analytics.json`)
- [x] Protegidos: logs e arquivos temporários
- [x] Protegidos: configurações de IDE (`.vscode`, `.idea`)

### Arquivos que NUNCA serão enviados pro GitHub:
```
.env                    # Senhas e chaves de API
*.key                   # Chaves privadas
*.pem                   # Certificados
credentials.json        # Credenciais
secrets.json            # Segredos
dados/leads.json        # Dados pessoais
dados/analytics.json    # Métricas privadas
```

---

## ✅ Segurança do Blog

### Configurações de proteção:
- [x] Blog é estático (HTML/CSS/JS) - sem banco de dados para hackear
- [x] Sem formulários de login - menos vulnerabilidades
- [x] GitHub Pages tem HTTPS automático - conexão segura
- [x] Sem scripts maliciosos - apenas código próprio

### Recomendações para você:
- [ ] Nunca colocar senhas nos arquivos HTML
- [ ] Usar autenticação de 2 fatores no GitHub
- [ ] Não compartilhar senha do GitHub com ninguém
- [ ] Manter o computador com antivírus atualizado

---

## ✅ Segurança das Contas

### GitHub:
- [ ] Usar senha forte (letras, números, símbolos)
- [ ] Ativar autenticação de 2 fatores
- [ ] Não usar a mesma senha de outros sites

### Google (AdSense/Search Console):
- [ ] Usar senha forte
- [ ] Ativar verificação em 2 etapas
- [ ] Não clicar em links suspeitos

---

## 🚨 O que NÃO fazer:

1. **NUNCA** colocar senhas nos arquivos do blog
2. **NUNCA** compartilhar suas chaves de acesso
3. **NUNCA** baixar arquivos de fontes desconhecidas
4. **NUNCA** ignorar atualizações de segurança

---

## 📞 Em caso de problema:

Se suspirar que sua conta foi comprometida:
1. Mude a senha IMEDIATAMENTE
2. Ative 2 fatores
3. Verifique os logs de acesso
4. Contate o suporte da plataforma
