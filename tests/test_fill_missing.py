import pandas as pd

from src.preprocessing.fill_missing import fill_missing_data


def test_fill_missing():
    # 1. Создаём простой DataFrame с пропуском
    df = pd.DataFrame({"A": [1, None, 3]})

    # 2. Применяем функцию
    result = fill_missing_data(df)

    # 3. Проверяем, что пропусков больше нет
    assert result.isnull().sum().sum() == 0
    # Проверяем, что значение заполнено (например, средним = 2)
    assert result.loc[1, "A"] == 2
