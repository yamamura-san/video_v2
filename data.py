import pandas as pd

def mini(file):
    df = pd.read_csv(file)

    val = df["val"]

    tmp = 100000
    for v in val:
        if v <= tmp:
            tmp = v
        else:
            pass

    return tmp

if __name__ == "__main__":
    print(mini("data.csv"))