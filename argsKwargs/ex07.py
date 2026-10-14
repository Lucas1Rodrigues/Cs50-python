def configurar_sistema(**kwargs):
    return kwargs
    

configuracoes = configurar_sistema(
    tema="escuro",
    idioma="pt-BR",
    notificacoes=True
)

print(configuracoes)