# Python Estudos

Pequenos programas de terminal que fiz para praticar Python (entrada de dados, funções, validação e testes). Os exemplos vêm do meu dia a dia no jiu-jitsu e na produção de kimonos.

| Programa | O que faz | Executar |
|---|---|---|
| `placar.py` | Placar de luta com pontuação no estilo IBJJF (queda, passagem, montada...) | `python placar.py` |
| `chaves.py` | Sorteia as lutas de um torneio e trata número ímpar de atletas | `python chaves.py` |
| `preco.py` | Calcula preço de venda e lucro por peça a partir do custo e da margem | `python preco.py` |

## Testes
```bash
python -m unittest discover -s tests
```

## O que aprendi
- Separar a lógica (funções que dá para testar) da entrada e saída do terminal.
- Validar entradas (margem fora do intervalo, técnica desconhecida) em vez de deixar o programa quebrar.
- Corrigir um bug real do `chaves.py` original: com número ímpar de atletas ele dava erro; agora o último passa direto.

Requisito: Python 3.10+. Sem dependências externas.
