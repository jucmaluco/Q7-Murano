import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("Data/Stocks/abmd.us.txt")
df['Date'] = pd.to_datetime(df['Date'])
df['Close'] = pd.to_numeric(df['Close'])

def plot_sma(type, id):
    df = pd.read_csv("Data/"+type+"/"+id+".us.txt")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Close'] = pd.to_numeric(df['Close'])
    df['SMA10'] = df['Close'].rolling(window=10).mean()
    df['SMA20'] = df['Close'].rolling(window=20).mean()
    df['SMA50'] = df['Close'].rolling(window=50).mean()
    df['SMA200'] = df['Close'].rolling(window=200).mean()

    plt.figure(figsize=(20, 10))  # Set figure size
    plt.plot(df['Date'], df['Close'], label='Close Price', marker='o', linewidth=1)
    plt.plot(df['Date'], df['SMA10'], label='SMA (Window = 10)', marker='o', linewidth=1)
    plt.plot(df['Date'], df['SMA20'], label='SMA (Window = 20)', marker='o',linewidth=1)
    plt.plot(df['Date'], df['SMA50'], label='SMA (Window = 50)', marker='o', linewidth=1)
    plt.plot(df['Date'], df['SMA200'], label='SMA (Window = 200)', marker='o', linewidth=1)

    plt.title('Stock:' + id, fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price', fontsize=12)
    plt.legend()  # Add a legend
    plt.grid()  # Add a grid
    plt.show()


def close_prices(input_folder, output_file):
    all_data = {}

    # Percorre todos os arquivos na pasta
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(input_folder, file_name)

            # Lê o arquivo .txt em um DataFrame
            try:
                df = pd.read_csv(file_path)  # Ajuste o separador conforme necessário
                if 'Close' in df.columns and len(df['Close']) >= 100:
                    # Extrai as últimas 100 linhas da coluna 'Close'
                    last_100_close = df['Close'].tail(100).reset_index(drop=True)
                    # Armazena no dicionário com o nome do arquivo (sem extensão) como chave
                    all_data[file_name.replace('.txt', '')] = last_100_close
            except Exception as e:
                print(f"Erro ao processar {file_name}: {e}")

    # Consolida os dados em um único DataFrame
    consolidated_data = pd.DataFrame(all_data)

    # Salva os dados em um novo arquivo .txt
    consolidated_data.to_csv(output_file, index=False)

def most_correlated_pairs(file_path, top_n=5):
        df = pd.read_csv(file_path, sep=',')  # Adjust separator if necessary (e.g., ',' or '\t')
        correlation_matrix = df.corr()
        correlations = correlation_matrix.unstack().reset_index()
        correlations.columns = ['Column_1', 'Column_2', 'Correlation']
        correlations = correlations[correlations['Column_1'] != correlations['Column_2']]
        correlations = correlations.drop_duplicates(subset=['Correlation'])
        most_correlated = correlations.reindex(
            correlations['Correlation'].abs().sort_values(ascending=False).index
        ).head(top_n)
        print(most_correlated)

# Caminhos de entrada e saída
input_folder = "Data/Stocks"  # Substitua pelo caminho real
output_file = "Data/open.txt"  # Substitua pelo caminho real

# Processa os arquivos
close_prices(input_folder, output_file)
most_correlated_pairs("Data/open.txt")

plot_sma("Stocks", "abax")
plot_sma("Stocks", "bcc")
plot_sma("Stocks", "aapl")
plot_sma("Stocks", "amza")
plot_sma("Stocks", "awf")
plot_sma("ETFs", "cred")
plot_sma("ETFs", "croc")
plot_sma("ETFs", "adra")
plot_sma("ETFs", "adru")
plot_sma("ETFs", "bsji")

