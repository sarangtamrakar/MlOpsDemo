import os
import yaml
import argparse
import pandas as pd


def read_config(config_path):
    try:
        with open(config_path,'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
        return config
    except Exception as e:
        raise Exception



def get_dataframe(config_path):
    try:
        config = read_config(config_path)
        data_path =  config['data_source']['s3_source']
        dataframe = pd.read_csv(data_path)
        return dataframe
    except Exception as e:
        raise Exception
        