# Leitor dos sensores

### Instalando depedências

```bash
# pip install -r requirements.txt
```

### Modo de uso

```bash
$ python3 main.py
```

##### Mais opções

```bash
$ python3 main.py --help
```

### FAQ


- *ImportError: No module named gpiozero*

Tenha certeza que esta chamando o `Python3` e que o `pip` esteja configurado para a mesma versão do Python que
esta sendo chamada. Se ainda assim o problema persistir, instale o pacote via `apt` com:

```bash
# apt install python3-gpiozero
```