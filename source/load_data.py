# read the data from data source (remote repository)
# & save it into the data/raw directory
import os
import argparse
from get_data import get_dataframe
from get_data import read_config


def save_data(config_file):
    try:
        config = read_config(config_file)
        raw_dir = config['load_data']['raw_dataset_csv']
        df = get_dataframe("params.yaml")
        col_lis = [col.replace(" ","_") for col in df.columns]
        df.to_csv(raw_dir,index=None,sep=",",header=col_lis)
        return True
    except Exception as e:
        raise Exception


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",default="params.yaml")
    args = parser.parse_args()
    save_data(args.config)