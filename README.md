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

## Configuração

O arquivo `config.yaml` define algumas configurações:

```yaml
cost_increment: 10
delay_increment: 5
if_prefix: enp
```

O parâmetro `cost_increment` indica o tamanho do incremento (ou decremento) do custo das rotas no OSPF. O parâmetro `delay_increment` representa o número de vezes que um incremento dever ser solicitado para que uma mudança de custo seja realizada. Ou seja, se os sensores indicarem que o custo das interfaces do roteador devem aumentar, esse pedido deverá ser feito `delay_increment` vezes afim de evitar "bouncing" das rotas.
Por fim, `if_prefix` é o prefixo das interfaces de rede utilizado pelo código descoberta de interfaces. No caso, o padrão é `enp` pois as interfaces são `enp0s8` e `enp0s9`. Caso as interfaces fossem, por exemplo, `eth0` e `eth1`, esse prefixo deveria ser definido como `eth`.
