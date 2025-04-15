import argparse
import json
import csv
import pandas as pd

def csv_to_json(csv_filepath, json_filepath):
    """
    Converts a CSV file to a JSON file.
    Creates a json file with index starting at 1

    Args:
        csv_filepath (str): The path to the CSV file.
        json_filepath (str): The path to the output JSON file.
    """

    data = pd.read_csv(csv_filepath, header =FALSE, names= "items")
    data.index += 1
    data.to_json(json_filepath)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('--csv_filepath', type=str, help="csv filename to convert to json")
    parser.add_argument('--json_filepath', type=str, help="json filename")
    args = parser.parse_args()
    csv_to_json(args.csv_filepath, args.json_filepath)