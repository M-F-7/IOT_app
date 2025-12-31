import pandas as pd

tab = pd.DataFrame()

try:
    assert isinstance(tab, pd.DataFrame)
    print("OK 😀")
except AssertionError as e:
    print(f"{e}")