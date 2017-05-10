# Roteamento Sensível ao Contexto

Tomada de decisões de roteamento em uma rede interna com base no contexto dos dispositivos.


## Instalação

No diretório [raiz](.) do repositório, verifique se todos os submódulos estão atualizados com:

```bash
$ git submodule init
$ git submodule update
```

Garantido a sincronização dos submódulos, instale o pacote com:

```bash
$ pip3 install -e .
```

Para uma melhor estabilidade dos sistemas de teste, é recomendável que se faça uso de [ambientes virtuais](https://virtualenvwrapper.readthedocs.io/en/latest/), no intuito de evitar o conflito de versões pacotes.