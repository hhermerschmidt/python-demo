from pathlib import Path

import pandas as pd


def read_data(file: Path):
    df = pd.read_csv(file)
    print(df)

def plot():
    pass

def main(file: Path):
   read_data(file) 
    
if __name__ == "__main__":

    data_file = Path(__file__).parent / "data.csv"
    main(data_file)