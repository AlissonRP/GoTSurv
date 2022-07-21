#%%
import pandas as pd
import numpy as np

#%%
df = (
    pd.read_csv("data/deaths.csv")
    .fillna(value=np.nan)
    .replace("None", np.nan)
    .rename(columns={"Book of Death": "time_death"})
    .query("Allegiances == Allegiances")
)
#%%

#%%

#%%
censored = df.query("time_death != time_death")

#%%
censored.rename(
    columns={"GoT": "AP1", "CoK": "AP2", "SoS": "AP3", "FfC": "AP4", "DwD": "AP5"},
    inplace=True,
)

#%%
teste = censored.reset_index()
x = []
y = []
for i in range(40):
    if teste.iloc[i, 12] == 1:
        x.append(5)
        y.append(teste.iloc[i, 1])
        teste.drop([i], inplace=True)
        teste.reset_index()

#%%
x
y

#%%
pd.DataFrame({"Name": y, "Time": x})

#%%

teste

#%%
