# split the raw data
# save it in data/processed folder

import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_config


def split_and_saved_data(config_file_path):
    try:
        config = read_config(config_file_path)
        train_data_path = config['split_data']['train_path']
        test_data_path = config['split_data']['test_path']
        raw_data_path = config['load_data']['raw_dataset_csv']
        test_size = config['split_data']['test_size']
        random_state = config['base']['random_state']
        df = pd.read_csv(raw_data_path,sep=',')
        
        train,test = train_test_split(df,test_size=test_size,
        random_state=random_state)

        train.to_csv(train_data_path,sep=',',index=None,header=True)
        test.to_csv(test_data_path,sep=',',index=None,header=True)

    except Exception as e:
        raise  Exception


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",default="params.yaml")
    args = parser.parse_args()
    split_and_saved_data(args.config)
