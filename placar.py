"""Placar de jiu-jitsu no terminal (pontuação no estilo IBJJF)."""

PONTOS = {
    "queda": 2,
    "raspagem": 2,
    "joelho": 2,  # joelho na barriga
    "passagem": 3,
    "montada": 4,
    "costas": 4,
}


def aplicar(tecnica: str, pontos: int) -> tuple[int, bool]:
    """Devolve (novos_pontos, luta_terminou). Lança ValueError se for desconhecida."""
    tecnica = tecnica.strip().lower()
    if tecnica in ("finalizacao", "finalização", "fim"):
        return pontos, True
    if tecnica not in PONTOS:
        raise ValueError(f"Técnica não reconhecida: {tecnica!r}")
    return pontos + PONTOS[tecnica], False


def main() -> None:
    pontos = 0
    print("Placar de jiu-jitsu")
    print("Técnicas:", ", ".join(PONTOS), "| 'finalização' ou 'fim' encerra")
    while True:
        print(f"\nPontuação atual: {pontos}")
        entrada = input("Técnica: ")
        try:
            pontos, terminou = aplicar(entrada, pontos)
        except ValueError as erro:
            print(erro)
            continue
        if terminou:
            print(f"\nLuta encerrada. Placar final: {pontos} pontos")
            return
        print(f">> +{PONTOS[entrada.strip().lower()]} pontos")


if __name__ == "__main__":
    main()
