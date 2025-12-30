Derin Öğrenme ile Canlı Bitcoin Fiyat Tahmin Sistemi (LSTM)


Bu proje, BİL403 - Yazılım Mühendisliği dersi kapsamında geliştirilmiştir. Statik veri setleri yerine Yahoo Finance API üzerinden anlık veri çeken ve LSTM (Long Short-Term Memory) mimarisi ile Bitcoin'in (BTC) gelecek fiyat hareketlerini tahmin eden dinamik bir yapay zeka uygulamasıdır.

Proje Hakkında

Kripto para piyasaları saniyelik değişir. Bu projede bayat veri dosyaları yerine gerçek zamanlı finansal veriler kullanılmıştır. Sistem şu adımları izler:

Canlı Veri Akışı: yfinance kütüphanesi ile 2020'den bugüne kadar olan tüm BTC verileri anlık çekilir.

Akıllı Pencereleme: Model, sadece düne değil, son 60 günün piyasa hareketlerine (momentum) bakarak karar verir.

Normalizasyon: Veriler MinMaxScaler ile 0-1 aralığına optimize edilir.

Tahmin ve Görselleştirme: Kullanıcı hiçbir veri girmek zorunda kalmadan, sistem otomatik olarak geleceği tahmin eder ve trend grafiğini çizer.

Kullanılan Teknolojiler
Python: Ana geliştirme dili.

PyTorch: LSTM modelinin mimarisi ve eğitimi.

yfinance: (Fark Yaratan Özellik) Canlı borsa verilerinin çekilmesi.

Gradio: İnteraktif ve modern web arayüzü.

Matplotlib: Dinamik fiyat grafiklerinin çizilmesi.

Scikit-Learn: Veri ölçeklendirme (Scaling).

Proje Yapısı
app.py: Web arayüzünü başlatan ve canlı tahmin yapan ana dosya.

train_model.py: Güncel veriyi çekip modeli sıfırdan eğiten modül.

lstm_model.pth: Eğitilmiş yapay zeka model dosyası.

scaler.gz: Veri ölçeklendirme dosyası.

requirements.txt: Gerekli kütüphane listesi.

Kurulum ve Çalıştırma
Projeyi çalıştırmak çok basittir. Veri indirme derdi yoktur, sistem her şeyi otomatik yapar.

1. Gereksinimleri Yükleyin

Bash

pip install -r requirements.txt
2. Uygulamayı Başlatın (Model dosyası hazır geldiği için eğitime gerek yoktur, direkt çalışır)

Bash

python app.py
Terminalde çıkan linke tıklayın (örn: http://127.0.0.1:7860).

Kullanım Senaryosu
Arayüz açılır.

"Grafikte kaç günlük geçmiş görmek istersin?" kutusuna bir sayı girilir (Örn: 180).

Gönder butonuna basılır.

Sistem saniyeler içinde internetten veriyi çeker, analiz eder ve sonucu ekrana basar.

Çıktı: Tahmin edilen fiyat, Yükseliş/Düşüş beklentisi ve detaylı grafik.
