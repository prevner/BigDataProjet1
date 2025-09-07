# Big Data Projesi - Kapsamlı Dokümantasyon

## 🌟 Proje Hakkında

Bu repository, modern Big Data teknolojilerini kullanarak gerçek zamanlı veri işleme ve analiz platformu içerir. Proje, hava durumu verilerinin toplanması, işlenmesi ve görselleştirilmesi üzerine kurulmuştur.

## 📁 Dosya Yapısı

```
BigDataProjet1/
├── 📊 SUNUM.md              # Detaylı Türkçe sunum
├── 🎯 SUNUM_SLIDES.md       # Slayt formatında özet sunum  
├── 🐳 docker-compose.yml    # Ana orkestrasyon dosyası
├── ⚙️ config.env           # Hadoop yapılandırması
├── 📦 requirements.txt     # Python bağımlılıkları
├── 🔄 producer.py          # Kafka producer (hava durumu)
├── 🔄 consumer.py          # Kafka consumer
├── 📂 producer/            # Producer container files
├── 📂 consumer/            # Consumer container files  
├── 📂 namenode/            # Hadoop NameNode setup
├── 📂 spark-scripts/       # Zeppelin notebook files
└── 📂 dataset/            # Veri dosyaları (london_merged.csv)
```

## 🚀 Hızlı Başlangıç

### 1. Sistemi Başlatın
```bash
# Tüm servisleri Docker ile başlat
docker-compose up -d

# Servis durumlarını kontrol et
docker-compose ps
```

### 2. Web Arayüzlerine Erişin
- **Kafka UI**: http://localhost:8081 - Kafka cluster yönetimi
- **Zeppelin**: http://localhost:8080 - İnteraktif data analytics  
- **HDFS NameNode**: http://localhost:9870 - Distributed storage
- **YARN ResourceManager**: http://localhost:8088 - Resource management

### 3. Logları İzleyin
```bash
# Producer ve Consumer logları
docker-compose logs -f producer consumer

# Kafka cluster logları  
docker-compose logs -f kafka kafka2
```

## 🏗️ Sistem Mimarisi

```
┌─────────────────┐
│   Weather API   │ (weather.com hava durumu)
└─────────┬───────┘
          │ HTTP requests (2s interval)
          ▼
┌─────────────────┐
│ Kafka Producer  │ (Python - BeautifulSoup)
│ - Data scraping │
│ - JSON format   │
│ - Topic: test   │
└─────────┬───────┘
          │ Publish messages
          ▼
┌─────────────────┐    ┌──────────────┐
│   Kafka Cluster│◄──►│  Zookeeper   │
│ - Broker 1:9092 │    │   :2181      │  
│ - Broker 2:9093 │    │ Coordination │
│ - UI: 8081      │    └──────────────┘
└─────────┬───────┘
          │ Consume messages
          ▼
┌─────────────────┐    ┌──────────────┐
│ Kafka Consumer  │    │  HDFS Cluster│
│ - Real-time     │───►│ - NameNode   │
│ - JSON decode   │    │ - DataNodes  │
│ - Processing    │    │ - Replication│
└─────────────────┘    └──────┬───────┘
                              │ Data storage
                              ▼
┌─────────────────┐    ┌──────────────┐
│  Apache Spark   │◄──►│    YARN      │
│ - Batch process │    │ ResourceMgr  │
│ - ML algorithms │    │ NodeManager  │
│ - Data transform│    │ :8088        │
└─────────┬───────┘    └──────────────┘
          │ Analytics & Visualization
          ▼
┌─────────────────┐
│ Apache Zeppelin │
│ - Notebooks     │
│ - Interactive   │
│ - Dashboards    │
│ - Port: 8080    │
└─────────────────┘
```

## 📋 Sunum Dosyaları

### 📊 Detaylı Sunum: `SUNUM.md`
- Kapsamlı teknik açıklamalar
- Mimari detayları
- Kurulum ve yapılandırma
- Kullanım senaryoları
- Gelecek geliştirmeler

### 🎯 Slayt Sunumu: `SUNUM_SLIDES.md`  
- 10 slaytlık özet sunum
- Görsel diyagramlar
- Demo senaryosu
- Teknik özellikler
- Soru-cevap bölümü

## 🛠️ Teknoloji Stack

### Core Technologies
- **Apache Kafka 2.8+** - Stream processing
- **Apache Hadoop 3.4.1** - Distributed storage  
- **Apache Spark 3.5.0** - Big data processing
- **Apache Zeppelin 0.11.2** - Interactive analytics

### Development Stack
- **Python 3.6+** - Backend development
- **Docker & Docker Compose** - Containerization
- **BeautifulSoup4** - Web scraping
- **Kafka-Python** - Kafka client

### Infrastructure
- **CentOS 7** - Base OS for containers
- **Makefile** - Build automation
- **YAML** - Configuration management

## 🎯 Önemli Özellikler

### ✅ Gerçek Zamanlı Veri İşleme
- 2 saniyede bir hava durumu verisi toplama
- Kafka ile düşük latency messaging
- Stream processing capabilities

### ✅ Dağıtık Veri Depolama
- HDFS ile fault-tolerant storage
- 2x replication factor
- Scalable storage architecture

### ✅ İnteraktif Analiz
- Zeppelin notebook interface
- Scala, Python, SQL support
- Real-time visualization

### ✅ Konteyner Tabanlı Deployment
- Docker Compose orchestration
- Isolated service environments
- Easy scaling and management

## 🔧 Geliştirme ve Debug

### Faydalı Komutlar
```bash
# Container'ları yeniden başlat
docker-compose restart producer consumer

# Belirli servis logları
docker-compose logs namenode

# HDFS dosya sistemi kontrol
docker exec -it <namenode_container> hdfs dfs -ls /

# Kafka topic listesi
docker exec -it <kafka_container> kafka-topics.sh --list --bootstrap-server localhost:9092
```

### Troubleshooting
1. **Port conflicts**: Portların kullanımda olmadığından emin olun
2. **Memory issues**: En az 8GB RAM önerilir
3. **Network issues**: Docker network connectivity kontrol edin

## 📈 Performance ve Monitoring

### Metrics
- **Kafka throughput**: ~30 messages/second
- **Processing latency**: <100ms average
- **Storage efficiency**: HDFS compression enabled
- **Resource utilization**: YARN monitoring

### Monitoring Tools
- Kafka UI dashboard
- YARN ResourceManager UI  
- HDFS NameNode web interface
- Zeppelin monitoring

## 🤝 Katkıda Bulunma

Bu proje eğitim amaçlı hazırlanmıştır. Geliştirmeler ve öneriler için:

1. Fork the repository
2. Create feature branch
3. Commit changes  
4. Submit pull request

## 📄 Lisans

Bu proje eğitim ve öğrenme amaçlı açık kaynak olarak geliştirilmiştir.

---

## 🎉 Sonuç

Bu Big Data projesi, modern veri mühendisliği teknolojilerini öğrenmek ve pratikte uygulamak için mükemmel bir platform sunmaktadır. Kafka'dan Spark'a, Docker'dan Zeppelin'e kadar geniş bir teknoloji yelpazesi ile gerçek dünya senaryolarını deneyimleme imkanı sağlar.

**Sunumlar için `SUNUM.md` ve `SUNUM_SLIDES.md` dosyalarını inceleyiniz.** 🚀