import pandas as pd


url = "https://storage.googleapis.com/kagglesdsdata/datasets/108980/260251/train.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260508%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260508T142723Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3831b16c618a27d4145c4718c01db661a58e15a8b8f5e328f2e38f657b345ea0707a04f1433a351950a46ab949cba5a2ab74f59c050cd29bcac6f39e92c8c84a37670d44b0f2dde8ec1e520349aa45c71fcd58de019c194cec459cb0a6ad15e6780204d12b9bf3f07a9b265bdcf706e22e2a82f23b04f815164762099d15ea99dc4ffdde0f639c0bde377500a4ef230ac8b246cd8277ada52cfdc78d8ed209ac6b2e4614427526280f91492106ea3b9daa47226fdf529cb5a2c5120c80eea7fab747d25ef158f8d504f83e3b5056884507d1bad183ce70ca30b2c22f05c531a5e1c6894c1b9c543b1d81597c0cfc0e9bbb0a92455c0695f2d1289babb6dbfef7"
home_data = pd.read_csv(url)
home_data.describe()


avg_lot_size = round(home_data["LotArea"].mean())
newest_home_age = 2026 - home_data["YearBuilt"].max()

print(avg_lot_size)
print(newest_home_age)
