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
event = df.query("time_death == time_death")
#%%
censored.rename(
    columns={"GoT": "AP1", "CoK": "AP2", "SoS": "AP3", "FfC": "AP4", "DwD": "AP5"},
    inplace=True,
)

#%%
teste = censored.reset_index()
x = []
y = []
for i in range(teste.shape[0]):
    if teste.iloc[i, 13] == 1:
        x.append(5)
        y.append(teste.iloc[i, 1])
    elif teste.iloc[i, 12] == 1:
        x.append(4)
        y.append(teste.iloc[i, 1])  ##bruuh bad code runs only once
    elif teste.iloc[i, 11] == 1:
        x.append(3)
        y.append(teste.iloc[i, 1])
    elif teste.iloc[i, 10] == 1:
        x.append(2)
        y.append(teste.iloc[i, 1])
    else:
        x.append(1)
        y.append(teste.iloc[i, 1])


#%%
x
y

#%%
censor = pd.DataFrame({"Name": y, "Time": x})

#%%

censored.merge(censor, on="Name")
#%%

censura = (
    censor.merge(censored, on="Name", how="left")
    .drop(["Book Intro Chapter", "time_death", "Death Year"], axis=1)
    .rename(columns={"Time": "time_death"})
)


#%%
event = event.assign(status=np.repeat(1, event.shape[0]))
censura = censura.assign(status=np.repeat(0, censura.shape[0]))

#%%
final_df = pd.concat([censura, event]).drop(
    [
        "Death Chapter",
        "GoT",
        "CoK",
        "SoS",
        "FfC",
        "DwD",
        "Book Intro Chapter",
        "Death Year",
    ],
    axis=1,
)

#%%
final_df.to_csv("gotsurv.csv")

#%%

final = pd.read_csv("data/gotsurv.csv")

#%%
