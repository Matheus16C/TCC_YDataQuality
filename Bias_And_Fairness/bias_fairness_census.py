import pandas as pd
from ydata_quality.bias_fairness import BiasFairness


def main():
    # Carregando base de dados

    df = pd.read_csv('Census_50k.data')
    print(df.head())

    # Criação da engine

    bf = BiasFairness(df=df, sensitive_features=[
                      'race', 'sex'], label='income', random_state=42)

    # Avaliação completa

    results = bf.evaluate()
    print(results)

    # bias_fairness_warnings = bf.get_warnings()
    # print(bias_fairness_warnings)

    # # Conjunto de teste completo

    # print(list(results.keys()))

    # # Discriminação de desempenho

    # performances = bf.performance_discrimination()
    # print(performances)

    # # Identificação de proxy

    # print(bf.proxy_identification(th=0.2))

    # # Previsibilidade de atributos sensíveis

    # sens_pred = bf.sensitive_predictability()
    # print(sens_pred)

    # print(bf.sensitive_predictability(adjusted_metric=False))

    # # Representividade de atribudos sensíveis

    # print(bf.sensitive_representativity())


if __name__ == "__main__":
    main()
