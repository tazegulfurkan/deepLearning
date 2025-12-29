import gradio as gr
import torch
import torch.nn as nn
import joblib
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

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

model = LSTMModelDemo()
try:
    model.load_state_dict(torch.load("lstm_model.pth", map_location=torch.device('cpu')))
    model.eval()
    scaler = joblib.load("scaler.gz")
except Exception as e:
    print("HATA: Model dosyaları bulunamadı! Lütfen önce train_model.py çalıştırın veya dosyaları yükleyin.")
    raise e

SEQ_LENGTH = 60 

def predict_future(days_to_plot):
    try:
        days_to_plot = int(days_to_plot)
        if days_to_plot < SEQ_LENGTH:
            days_to_plot = SEQ_LENGTH + 10
        
        period_str = f"{days_to_plot + 10}d"
        df = yf.download('BTC-USD', period=period_str, interval='1d')
        
        if len(df) < SEQ_LENGTH:
            return "Hata: Yeterli veri yok, daha uzun bir tarih aralığı gerekli.", None

        close_prices = df['Close'].values
        dates = df.index
        
        last_seq_data = close_prices[-SEQ_LENGTH:].reshape(-1, 1)
        
        input_scaled = scaler.transform(last_seq_data)
        test_seq = torch.tensor(input_scaled, dtype=torch.float32).unsqueeze(0) 
        
        with torch.no_grad():
            pred_scaled = model(test_seq)
        
        pred_price = scaler.inverse_transform(pred_scaled.numpy()).item()
        
        current_price = close_prices[-1].item()
        change = pred_price - current_price
        direction = "YÜKSELİŞ 🟢" if change > 0 else "DÜŞÜŞ 🔴"
        percentage = (change / current_price) * 100
        
        result_text = (
            f"Analiz Edilen Aralık: Son {SEQ_LENGTH} Gün (Model Hafızası)\n"
            f"Mevcut Fiyat: {current_price:.2f} $\n"
            f"Tahmin Edilen: {pred_price:.2f} $\n"
            f"Beklenti: {direction} (%{percentage:.2f})"
        )

        plot_dates = dates[-days_to_plot:]
        plot_prices = close_prices[-days_to_plot:]

        fig = plt.figure(figsize=(10, 6))
        plt.plot(plot_dates, plot_prices, label='Geçmiş Fiyatlar', color='#1f77b4', linewidth=2)
        
        next_date = dates[-1] + np.timedelta64(1, 'D')
        plt.plot([dates[-1], next_date], [current_price, pred_price], 'r--', label='Tahmin Yolu')
        plt.scatter(next_date, pred_price, color='red', s=100, label=f'Hedef: {pred_price:.0f}$', zorder=5)
        
        plt.title(f'Bitcoin Analizi (Model Son {SEQ_LENGTH} Günü Baz Aldı)')
        plt.xlabel('Tarih')
        plt.ylabel('Fiyat (USD)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return result_text, fig

    except Exception as e:
        return f"Hata: {str(e)}", None

interface = gr.Interface(
    fn=predict_future,
    inputs=gr.Number(value=180, label="Grafikte kaç günlük geçmiş görmek istersin?"),
    outputs=[
        gr.Textbox(label="Sonuç Raporu"),
        gr.Plot(label="Analiz Grafiği")
    ],
    title="Gelişmiş Bitcoin LSTM Tahmincisi",
    description="LSTM Modeli ile Bitcoin Trend Analizi",
    examples=[[90], [180], [365]]
)

if __name__ == "__main__":
    interface.launch()
