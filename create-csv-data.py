import pandas as pd
data = {
    'Name': ['Rob', 'Mike', 'Mohan', 'Kory', 'Gautam', 'Andrea', 'Arnold', 'Abdul', 'Dipika', 'Priyanka', 'Sid', 'Nick'],
    'Age': [27, 27, 27, 29, 29, 39, 38, 27, 39, 40, 41, 41],
    'Income(k$)': [70, 61, 150, 155, 162, 48, 58, 65, 64, 82, 43, 64]
}
df = pd.DataFrame(data)
csv_path = './dataset/income.csv'
df.to_csv(csv_path, index=False)
