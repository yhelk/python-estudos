"""Calculadora de preço de venda a partir do custo e da margem desejada."""


def calcular_preco(custo_total: float, margem_percentual: float) -> dict:
    """Preço = custo / (1 - margem). A margem é sobre o preço final."""
    if custo_total < 0:
        raise ValueError("O custo não pode ser negativo.")
    if not 0 <= margem_percentual < 100:
        raise ValueError("A margem deve estar entre 0 e 100 (exclusivo).")
    preco = custo_total / (1 - margem_percentual / 100)
    return {"preco_venda": preco, "lucro": preco - custo_total}


def ler_valor(texto: str) -> float:
    return float(input(texto).replace(",", "."))


def main() -> None:
    print("=== Calculadora de preço ===")
    try:
        custo = (ler_valor("Custo de produção (R$): ")
                 + ler_valor("Embalagem e etiquetas (R$): ")
                 + ler_valor("Frete médio por peça (R$): "))
        margem = ler_valor("Margem desejada (%): ")
        r = calcular_preco(custo, margem)
    except ValueError as erro:
        print(f"Valor inválido: {erro}")
        return
    print(f"\nCusto total: R$ {custo:.2f}")
    print(f"Preço de venda sugerido: R$ {r['preco_venda']:.2f}")
    print(f"Lucro por peça: R$ {r['lucro']:.2f}")


if __name__ == "__main__":
    main()
