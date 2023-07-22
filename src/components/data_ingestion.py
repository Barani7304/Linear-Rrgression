import os 
import sys
from src.exception import Customexception
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionconfig:
    train_data_path: str =os.path.join('artifacts','train.csv')
    test_data_path: str =os.path.join('artifacts','test.csv')
    raw_data_path: str =os.path.join('artifacts','raw.csv')
    
class dataingestion:
    def __init__(self):
        self.dataingest_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion")

        try:
            df=pd.read_csv('K:/Machine learning/project//notbook/dataset/stud.csv')

            logging.info("Exported dataset as csv as df")

            os.makedirs(os.path.dirname(self.dataingest_config.train_data_path),exist_ok=True)

            df.to_csv(self.dataingest_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.dataingest_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.dataingest_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is complete")

            return(

            self.dataingest_config.train_data_path,
            self.dataingest_config.test_data_path,
            )

        except Exception as e:
            raise Customexception(e,sys)


if __name__=="__main__":
    obj=dataingestion()
    obj.initiate_data_ingestion()

        

