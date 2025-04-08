import os
import sys
import pandas as pd

def load_data():
    init_path = sys.modules['Suwon_ASOS_data'].__file__
    dir_path = init_path.replace('__init__.py', '')
    
    train_data = pd.read_csv(os.path.join(dir_path, "data/train_data.csv"))
    valid_data = pd.read_csv(os.path.join(dir_path, "data/valid_data.csv"))
    test_data = pd.read_csv(os.path.join(dir_path, "data/test_data.csv"))
    
    return train_data, valid_data, test_data

if __name__ == "__main__":
    train_data, valid_data, test_data = load_data()

    print("학습 데이터")
    print(train_data.head)
    print("검증 데이터")
    print(valid_data.head)
    print("테스트 데이터")
    print(test_data.head)