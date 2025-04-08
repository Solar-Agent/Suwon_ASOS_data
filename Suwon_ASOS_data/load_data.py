import pandas as pd

def load_data():
    train_data = pd.read_csv("data/train_data.csv")
    valid_data = pd.read_csv("data/valid_data.csv")
    test_data = pd.read_csv("data/test_data.csv")
    return train_data, valid_data, test_data

if __name__ == "__main__":
    train_data, valid_data, test_data = load_data()

    print("학습 데이터")
    print(train_data.head)
    print("검증 데이터")
    print(valid_data.head)
    print("테스트 데이터")
    print(test_data.head)