import os
import sys
import pandas as pd


def verify_system() -> None:
    print(f"Python version: {sys.version}")

    packages = ["pandas", "numpy", "matplotlib", "seaborn", "flask"]
    for package in packages:
        try:
            __import__(package)
            print(f"{package}: ok")
        except ImportError:
            print(f"{package}: missing")

    file_path = os.path.join("data", "METABRIC_RNA_Mutation.csv")
    if os.path.exists(file_path):
        print("Data file: ok")
        try:
            df = pd.read_csv(file_path)
            print(f"Data loading: ok ({len(df)} rows)")
        except Exception as exc:
            print(f"Data loading: failed ({exc})")
    else:
        print(f"Data file: not found at {file_path}")


if __name__ == "__main__":
    verify_system()
