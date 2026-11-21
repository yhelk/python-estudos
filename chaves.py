"""Sorteia as lutas de um torneio. Com número ímpar, um atleta passa direto (bye)."""
import random


def sortear_chaves(atletas: list[str], semente=None) -> list[tuple[str, str | None]]:
    """Embaralha e forma pares. O último par tem None se sobrar um atleta."""
    if len(atletas) < 2:
        raise ValueError("São necessários pelo menos 2 atletas.")
    lista = list(atletas)
    random.Random(semente).shuffle(lista)
    pares = [(lista[i], lista[i + 1]) for i in range(0, len(lista) - 1, 2)]
    if len(lista) % 2:
        pares.append((lista[-1], None))
    return pares


def main() -> None:
    entrada = input("Atletas separados por vírgula: ")
    atletas = [a.strip() for a in entrada.split(",") if a.strip()]
    try:
        pares = sortear_chaves(atletas)
    except ValueError as erro:
        print(erro)
        return
    print("\n--- Chaves ---")
    for n, (a, b) in enumerate(pares, start=1):
        print(f"Luta {n}: {a} vs {b}" if b else f"Luta {n}: {a} (avança direto)")


if __name__ == "__main__":
    main()
