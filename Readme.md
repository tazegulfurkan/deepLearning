Derin Öğrenme Tabanlı Bitcoin Fiyat Tahmin Sistemi (LSTM)

Bu proje, finansal zaman serilerinin analizi ve tahmini için Derin Öğrenme (Deep Learning) yöntemlerinden biri olan LSTM (Long Short-Term Memory) mimarisini kullanan bir yapay zeka uygulamasıdır. Sistem, tarihsel piyasa verilerini analiz ederek Bitcoin'in (BTC) kısa vadeli fiyat hareketlerini öngörmeyi amaçlar.

Proje Konusu

Seçilme Gerekçesi ve Alanın Önemi: Kripto para piyasaları, yüksek volatiliteye sahip olması ve geleneksel finansal araçlardan farklı dinamiklerle hareket etmesi nedeniyle tahmin edilmesi en zor alanlardan biridir. Geleneksel teknik analiz yöntemleri (RSI, MACD vb.) genellikle geçmiş fiyat hareketlerine dayalı gecikmeli sinyaller üretirken, Derin Öğrenme modelleri verideki gizli örüntüleri (patterns) ve momentumu öğrenerek daha dinamik tahminler sunabilir.

Neden LSTM? (Yöntem Analizi): Standart Yapay Sinir Ağları (ANN), veriler arasındaki zamansal ilişkiyi (önceki günün bugüne etkisi) kurmakta yetersiz kalır. Bu projede LSTM ağlarının tercih edilme sebebi şunlardır:
  Hafıza Hücreleri: LSTM, "Vanishing Gradient" problemini çözerek uzun vadeli bağımlılıkları öğrenebilir.,
  Sıralı Veri İşleme: Son 60 günün fiyat hareketlerini bir bütün (sequence) olarak işleyip, bu dizilimin sonucunda oluşacak 61. günü tahmin eder.

Veri Seti ve Ön İşleme
Harika, attığın örnekler gayet akademik ve profesyonel duruyor. Senin Bitcoin projesini de basit bir "kod deposu" olmaktan çıkarıp, sanki bir bitirme projesi veya akademik bir çalışmaymış gibi gösterecek dilde, attığın örneklerin formatına uygun bir README.md hazırladım.

Bunu kopyala ve README.md dosyanın içine yapıştır.

Derin Öğrenme Tabanlı Bitcoin Fiyat Tahmin Sistemi (LSTM)
Bu proje, finansal zaman serilerinin analizi ve tahmini için Derin Öğrenme (Deep Learning) yöntemlerinden biri olan LSTM (Long Short-Term Memory) mimarisini kullanan bir yapay zeka uygulamasıdır. Sistem, tarihsel piyasa verilerini analiz ederek Bitcoin'in (BTC) kısa vadeli fiyat hareketlerini öngörmeyi amaçlar.

Proje Konusu ve Motivasyonu
Seçilme Gerekçesi ve Alanın Önemi: Kripto para piyasaları, yüksek volatiliteye sahip olması ve geleneksel finansal araçlardan farklı dinamiklerle hareket etmesi nedeniyle tahmin edilmesi en zor alanlardan biridir. Geleneksel teknik analiz yöntemleri (RSI, MACD vb.) genellikle geçmiş fiyat hareketlerine dayalı gecikmeli sinyaller üretirken, Derin Öğrenme modelleri verideki gizli örüntüleri (patterns) ve momentumu öğrenerek daha dinamik tahminler sunabilir.

Neden LSTM? (Yöntem Analizi): Standart Yapay Sinir Ağları (ANN), veriler arasındaki zamansal ilişkiyi (önceki günün bugüne etkisi) kurmakta yetersiz kalır. Bu projede LSTM ağlarının tercih edilme sebebi şunlardır:

Hafıza Hücreleri: LSTM, "Vanishing Gradient" problemini çözerek uzun vadeli bağımlılıkları öğrenebilir.

Sıralı Veri İşleme: Son 60 günün fiyat hareketlerini bir bütün (sequence) olarak işleyip, bu dizilimin sonucunda oluşacak 61. günü tahmin eder.

Veri Seti ve Ön İşleme
Projede statik bir CSV dosyası yerine, Yahoo Finance API (yfinance) kullanılarak canlı ve güncel veri çekilmektedir.
  Veri Kaynağı: Yahoo Finance (BTC-USD)
  Kapsam: 01.01.2020 tarihinden günümüze kadar olan günlük kapanış (Close) fiyatları.
  Normalizasyon: Derin öğrenme modellerinin daha hızlı ve kararlı yakınsaması (convergence) için veriler MinMaxScaler kullanılarak 0 ile 1 aralığına ölçeklendirilmiştir.
  Pencereleme (Windowing): Modelin eğitilmesi için veri seti, 60 günlük kayan pencerelere (sliding window) bölünmüştür.

Model Mimarisi
Model, PyTorch kütüphanesi kullanılarak sıfırdan inşa edilmiştir.
  Giriş Katmanı: [Batch Size, Sequence Length (60), Input Size (1)]
  LSTM Katmanı: 50 nöronlu (hidden size) LSTM hücresi. Zaman serisindeki özellikleri çıkarır.
  Tam Bağlantılı Katman (Fully Connected): LSTM çıktısını tek bir fiyat tahminine dönüştüren doğrusal katman.
  Optimizasyon: Adam Optimizer (Learning Rate: 0.01)
  Kayıp Fonksiyonu: MSE (Mean Squared Error) - Regresyon problemleri için standart hata metriği.

  
