# Derin Öğrenme ile Canlı Bitcoin Fiyat Tahmin Sistemi (LSTM)


## Proje Hakkında

Kripto para piyasaları saniyelik değişir. Bu projede bayat veri dosyaları yerine gerçek zamanlı finansal veriler kullanılmıştır. Sistem temel olarak şu adımları izler:

1.  **Canlı Veri Akışı:** `yfinance` kütüphanesi ile 2020'den bugüne kadar olan tüm BTC verileri anlık çekilir.
2.  **Akıllı Pencereleme:** Model, sadece düne değil, son 60 günün piyasa hareketlerine (momentum) bakarak karar verir.
3.  **Normalizasyon:** Veriler `MinMaxScaler` ile 0-1 aralığına optimize edilir.
4.  **Tahmin ve Görselleştirme:** Kullanıcı hiçbir veri girmek zorunda kalmadan, sistem otomatik olarak geleceği tahmin eder ve trend grafiğini çizer.

## Kullanılan Teknolojiler

* **Python:** Ana geliştirme dili.
* **PyTorch:** LSTM modelinin mimarisi ve eğitimi.
* **yfinance:** (Fark Yaratan Özellik) Canlı borsa verilerinin çekilmesi.
* **Gradio:** İnteraktif ve modern web arayüzü.
* **Matplotlib:** Dinamik fiyat grafiklerinin çizilmesi.
* **Scikit-Learn:** Veri ölçeklendirme (Scaling).

## Proje Yapısı

* `app.py`: Web arayüzünü başlatan ve canlı tahmin yapan ana dosya.
* `train_model.py`: Güncel veriyi çekip modeli sıfırdan eğiten modül.
* `lstm_model.pth`: Eğitilmiş yapay zeka model dosyası.
* `scaler.gz`: Veri ölçeklendirme dosyası.
* `requirements.txt`: Gerekli kütüphane listesi.

## Kurulum ve Çalıştırma

Projeyi çalıştırmak oldukça basittir. Veri indirme gereksinimi yoktur, sistem gerekli verileri otomatik çeker.

### 1. Gereksinimleri Yükleyin
Terminal veya komut satırında proje dizinine giderek aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
