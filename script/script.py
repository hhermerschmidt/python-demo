from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

FOLDER = Path(__file__).parent

def plot(df: pd.DataFrame, save_path: Path = FOLDER):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_axes((0.05, 0.05, 0.9, 0.9))
    
    ax.plot(df["Index"].array, df["First Column"].array)
    fig.savefig(save_path / "figure.png")
    
def read_data(file: Path):
    df = pd.read_csv(file, skipinitialspace=True)
    return df

def main(file: Path):
   df = read_data(file)
   plot(df)
    
if __name__ == "__main__":

    data_file = FOLDER / "data.csv"
    main(data_file)