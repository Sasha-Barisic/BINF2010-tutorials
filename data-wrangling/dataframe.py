"""
Basic pandas operations.

Usage:
    python3 data-wrangling/dataframe.py
    python3 dataframe.py

Author:
    Sasha Barisic

Date:
    01/10/2024
"""

import pandas as pd


def main():

    df = pd.read_csv("data-wrangling/data.csv")

    # Print the columns
    print(df.columns)
    cols = list(df.columns)
    print(cols)

    # Drop NA
    print(df)

    # Not inplace - Row 28 got deleted
    new_df = df.dropna(inplace=False)
    print(new_df)

    # In place
    print(df.dropna())

    # Loop through df
    for ind, row in df.iterrows():

        print(f"This is row: {ind}")

    for col in cols:
        print(f"The values for column `{col}` is {row[col]}")

    df.to_json("data.json")
    df.to_csv("without_index.tsv", sep="\t", index=False)
    df.to_csv("with_index.tsv", sep="\t")


if __name__ == "__main__":
    main()
