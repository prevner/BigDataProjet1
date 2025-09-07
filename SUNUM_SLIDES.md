# 🎯 Big Data Projesi - Sunum Özeti

---

## 📑 Slayt 1: Proje Tanıtımı

### Big Data Gerçek Zamanlı İşleme Platformu
- **Hedef**: Hava durumu verilerinin gerçek zamanlı analizi
- **Teknolojiler**: Kafka + Hadoop + Spark + Zeppelin
- **Deployment**: Docker Compose ile tam otomatik
- **Veri Kaynağı**: weather.com API'si

---

## 📑 Slayt 2: Mimari Diyagram

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│   Weather API   │ -> │    Kafka     │ -> │     HDFS        │
│   (weather.com) │    │   Producer   │    │   Storage       │
└─────────────────┘    └──────────────┘    └─────────────────┘
                              │                      │
                              v                      v
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│   Kafka UI      │    │    Spark     │    │   Zeppelin      │
│  Management     │    │  Processing  │    │  Analytics      │
└─────────────────┘    └──────────────┘    └─────────────────┘
```

---

## 📑 Slayt 3: Temel Bileşenler

### 🔄 Kafka Streaming
- **2 Broker** (9092, 9093)
- **Zookeeper** koordinasyon
- **UI Management** (8081)

### 🗂️ Hadoop HDFS  
- **NameNode** (9870)
- **2 DataNode**
- **YARN** kaynak yönetimi (8088)

### ⚡ Spark + Zeppelin
- **Batch & Stream** processing
- **Interactive** notebooks (8080)
- **Scala, Python, SQL** desteği

---

## 📑 Slayt 4: Veri Akışı

### 1️⃣ Veri Toplama
```python
# Producer örneği
message = {
    'temperature': currentTemp,
    'timestamp': time.time(),
    'city': 'Paris'
}
producer.send('test_topic', message)
```

### 2️⃣ Gerçek Zamanlı İşleme
- **2 saniyede bir** güncelleme
- **JSON format** standardizasyon
- **Otomatik serialization**

### 3️⃣ Depolama & Analiz
- **HDFS** dağıtık depolama
- **Spark** büyük veri işleme
- **Zeppelin** görselleştirme

---

## 📑 Slayt 5: Kurulum ve Çalıştırma

### 🚀 Hızlı Başlangıç
```bash
# 1. Projeyi clone et
git clone <repository>

# 2. Servisleri başlat
docker-compose up -d

# 3. Web arayüzlerini aç
# Kafka UI:     http://localhost:8081
# Zeppelin:     http://localhost:8080  
# HDFS:         http://localhost:9870
# YARN:         http://localhost:8088
```

### 🔧 Gereksinimler
- Docker & Docker Compose
- 8GB+ RAM önerilen
- Portlar: 8080, 8081, 8088, 9870, 9092, 9093

---

## 📑 Slayt 6: Özellikler ve Avantajlar

### ✅ Ana Özellikler
- **Real-time** veri akışı
- **Fault tolerant** architecture  
- **Scalable** dağıtık sistem
- **Interactive** analysis tools
- **Containerized** deployment

### 🎯 Kullanım Alanları
- Gerçek zamanlı analytics
- Büyük veri machine learning
- ETL data pipeline'ları
- Historical trend analysis

---

## 📑 Slayt 7: Teknik Detaylar

### 📊 Performance Metrikleri
- **Throughput**: ~30 msg/sec
- **Latency**: <100ms processing
- **Storage**: Unlimited (HDFS)
- **Replication**: 2x factor

### 🛡️ Güvenilirlik
- **Auto failover** (Kafka)
- **Data replication** (HDFS) 
- **Resource management** (YARN)
- **Container orchestration** (Docker)

---

## 📑 Slayt 8: Demo Senaryosu

### 🎬 Canlı Demonstrasyon
1. **Producer başlatma** - Hava durumu verisi toplama
2. **Kafka UI** - Message flow gözlemleme  
3. **Consumer monitoring** - Real-time processing
4. **HDFS storage** - Veri depolama kontrolü
5. **Zeppelin analysis** - Interactive data exploration

### 📈 Beklenen Sonuçlar
- Anlık sıcaklık grafikleri
- Zaman serisi analizi
- Trend detection
- Anomaly identification

---

## 📑 Slayt 9: Gelecek Roadmap

### 🔮 Kısa Vadeli Hedefler
- **Multiple cities** support
- **Weather alerts** system
- **Advanced ML** models
- **Dashboard** improvements

### 🚀 Uzun Vadeli Vizyon
- **Kubernetes** migration
- **Multi-cloud** deployment  
- **AI-powered** predictions
- **Enterprise** integration

---

## 📑 Slayt 10: Sonuç ve Sorular

### 🎯 Proje Değeri
Bu proje, **modern Big Data teknolojilerini** öğrenmek ve **real-world scenarios** üzerinde pratik yapmak için ideal bir platform sunmaktadır.

### 🏆 Kazanımlar
- Kafka streaming expertise
- Hadoop ecosystem knowledge  
- Spark processing skills
- Docker orchestration experience

### ❓ Sorular ve Tartışma
**Herhangi bir sorunuz var mı?**

---

## 📞 İletişim

### 📧 Teknik Destek
- Repository: `prevner/BigDataProjet1`
- Docker Hub: Official images kullanılmıştır
- Documentation: README.md ve SUNUM.md

**Teşekkürler!** 🙏