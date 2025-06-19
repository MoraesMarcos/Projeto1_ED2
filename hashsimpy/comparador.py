def comparar_assinaturas(assinatura1, assinatura2):
    if len(assinatura1) != len(assinatura2):
        raise ValueError("As assinaturas devem ter o mesmo comprimento.")

    iguais = sum(1 for a, b in zip(assinatura1, assinatura2) if a == b)
    similaridade = iguais / len(assinatura1)
    return round(similaridade, 4)
