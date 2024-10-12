import pandas as pd

class DataLoader:
    def __init__(self, split_percentage: list[int]):
        self.df = pd.read_csv("hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv")
        # self.train, self.valid, self.test = self.split_data(split_percentage)

    def print_data_info(self):
        print(f"first five rows of data:\n{self.df.head(5)}")

        # dimensions of the dataset
        print(f"shape of dataset is: {self.df.shape}")

        # variable types
        print(f"variable types:\n{self.df.dtypes}")
        
    def split_data(self, split_percentage: list[int]):
        # Split the data into train, validation and test sets
        pass
    
    def preprocess_data(self):
        # Preprocess the data
        pass


