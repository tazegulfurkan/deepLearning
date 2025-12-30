import torch
import torch.nn as nn
import numpy as np
import joblib
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler


class LSTMModelDemo(nn.Module):
    def __init__(self, input_size=1, hidden_size=50, output_size=1):
        super(LSTMModelDemo, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)        
        out = out[:, -1, :]         
        out = self.fc(out)           
        return out

if __name__ == "__main__":
    print("Model eğitimi için veri çekiliyor...")
    df = yf.download('BTC-USD', start='2020-01-01', interval='1d') 
    data = df['Close'].values.reshape(-1, 1)

    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data)
    joblib.dump(scaler, 'scaler.gz') 

    X = []
    y = []
    seq_length = 60 

    for i in range(len(data_scaled) - seq_length):
        X.append(data_scaled[i:i + seq_length])
        y.append(data_scaled[i + seq_length])

    X = torch.tensor(np.array(X), dtype=torch.float32)
    y = torch.tensor(np.array(y), dtype=torch.float32)

    model = LSTMModelDemo()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    epochs = 100 
    print(f"Model son {seq_length} güne bakarak eğitiliyor...")

    for epoch in range(epochs):
        optimizer.zero_grad()
        output = model(X)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
        
        if (epoch+1) % 20 == 0:
            print(f"Epoch {epoch+1}, Loss: {loss.item():.5f}")

    torch.save(model.state_dict(), "lstm_model.pth")
    print("Model eğitildi ve kaydedildi!")
