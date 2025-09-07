# Big Data Projesi - Kapsamlı Sunum

## 📊 Proje Genel Bakış

Bu proje, **gerçek zamanlı veri işleme** ve **büyük veri analitiği** için tasarlanmış kapsamlı bir Big Data mimarisidir. Proje, modern veri mühendisliği teknolojilerini kullanarak hava durumu verilerinin toplanması, işlenmesi ve analiz edilmesi sürecini içerir.

---

## 🏗️ Mimari Genel Bakış

### Temel Bileşenler

1. **Apache Kafka** - Gerçek zamanlı veri akışı
2. **Apache Hadoop** - Dağıtık veri depolama (HDFS)
3. **Apache Spark** - Büyük veri işleme
4. **Apache Zeppelin** - İnteraktif veri analizi
5. **Docker** - Konteynerleştirme ve orkestrasyon

---

## 🔄 Veri Akış Mimarisi

```
[Hava Durumu API] 
    ↓
[Kafka Producer] → [Kafka Cluster] → [Kafka Consumer]
    ↓                                       ↓
[Real-time Processing]              [HDFS Storage]
    ↓                                       ↓
[Spark Processing] ← ← ← ← ← ← ← ← ← ← ← ← [Batch Processing]
    ↓
[Zeppelin Analytics & Visualization]
```

---

## 📡 Kafka Streaming Katmanı

### Kafka Cluster Yapılandırması
- **2 Kafka Broker** (kafka:9092, kafka2:9093)
- **Zookeeper** koordinasyonu
- **Kafka UI** yönetim arayüzü (Port: 8081)

### Producer Özellikleri
- **Veri Kaynağı**: weather.com hava durumu API'si
- **Toplanan Veriler**: 
  - Sıcaklık değeri
  - Zaman damgası
  - Şehir bilgisi (Paris)
- **Güncelleme Frekansı**: 2 saniyede bir

### Consumer Özellikleri
- Gerçek zamanlı veri tüketimi
- JSON formatında veri deserializasyonu
- Otomatik offset yönetimi

---

## 🗂️ Hadoop Dağıtık Depolama

### HDFS Cluster Yapılandırması
- **1 NameNode** - Metadata yönetimi (Port: 9870)
- **2 DataNode** - Veri blokları depolama
- **YARN ResourceManager** - Kaynak yönetimi (Port: 8088)
- **YARN NodeManager** - İş düğümü yönetimi

### Depolama Özellikleri
- **Replikasyon Faktörü**: 2
- **Dağıtık veri depolama**
- **Fault tolerance** (hata toleransı)

---

## ⚡ Apache Spark İşleme Katmanı

### Spark Entegrasyonu
- **Spark 3.5.0** with Hadoop 3 support
- **Zeppelin entegrasyonu** ile interaktif processing
- **Batch ve stream processing** desteği

### İşleme Yetenekleri
- Büyük veri setleri üzerinde paralel işleme
- Machine Learning algoritmaları
- SQL sorguları
- Data transformation pipeline'ları

---

## 📊 Apache Zeppelin Analytics

### Notebook Özellikleri
- **İnteraktif veri analizi** (Port: 8080)
- **Scala, Python, SQL** desteği
- **Görselleştirme araçları**
- **Paylaşılabilir notebook'lar**

### Mevcut Notebook'lar
- `exemple1_2KE4U7FUG.zpln` - Temel örnekler
- `micro_processing_2KEDXRJU4.zpln` - Mikro batch işleme
- `bash_processing_2KFWZ3P7B.zpln` - Bash komut işleme
- `script01_2KFBT59MC.zpln` - Custom script işleme

---

## 🐳 Docker Orchestration

### Container Yapılandırması
```yaml
Services:
├── zookeeper:2181
├── kafka:9092
├── kafka2:9093
├── kafka-ui:8081
├── producer (Python)
├── consumer (Python)
├── namenode:9870,8080
├── datanode_1 & datanode_2
├── resourcemanager:8088
└── nodemanager
```

### Avantajları
- **Kolay deployment**
- **Ölçeklenebilir mimari**
- **İzole ortamlar**
- **Tutarlı yapılandırma**

---

## 🛠️ Teknoloji Stack'i

### Backend Technologies
- **Python 3.6+** - Veri işleme
- **Kafka Python** - Streaming
- **BeautifulSoup & Requests** - Web scraping
- **Apache Hadoop 3.4.1**
- **Apache Spark 3.5.0**
- **Apache Zeppelin 0.11.2**

### Infrastructure
- **Docker & Docker Compose**
- **CentOS 7** base images
- **Makefile** automation scripts

---

## 🚀 Sistem Kurulumu ve Çalıştırma

### Ön Gereksinimler
```bash
# Docker ve Docker Compose kurulu olmalı
docker --version
docker-compose --version
```

### Sistem Başlatma
```bash
# Tüm servisleri başlat
docker-compose up -d

# Servislerin durumunu kontrol et
docker-compose ps

# Logları izle
docker-compose logs -f producer consumer
```

### Web Arayüzleri
- **Kafka UI**: http://localhost:8081
- **HDFS NameNode**: http://localhost:9870
- **YARN ResourceManager**: http://localhost:8088
- **Zeppelin Notebooks**: http://localhost:8080

---

## 📈 Veri İşleme Pipeline'ı

### 1. Veri Toplama
- Hava durumu API'sinden gerçek zamanlı veri çekme
- JSON formatında strukturize etme
- Kafka topic'ine gönderme

### 2. Stream Processing
- Kafka consumer ile veri tüketme
- Real-time transformations
- HDFS'e kaydetme

### 3. Batch Processing
- Spark ile büyük veri analizi
- Zeppelin ile interactive analysis
- Machine learning modelleri

### 4. Visualization
- Zeppelin dashboard'ları
- Grafik ve chart'lar
- Interactive queries

---

## 🔧 Geliştirme ve Monitoring

### Log Management
```bash
# Kafka logs
docker-compose logs kafka kafka2

# Producer/Consumer logs
docker-compose logs producer consumer

# Hadoop logs
docker-compose logs namenode datanode_1 datanode_2
```

### Performance Monitoring
- Kafka UI ile message throughput
- YARN UI ile resource utilization
- HDFS UI ile storage metrics

---

## 🎯 Kullanım Senaryoları

### 1. Real-time Analytics
- Anlık hava durumu takibi
- Trend analizi
- Anomaly detection

### 2. Historical Analysis
- Geçmiş veri analizi
- Seasonal patterns
- Predictive modeling

### 3. Data Pipeline
- ETL processes
- Data quality checks
- Automated reporting

---

## 🔮 Gelecek Geliştirmeler

### Potansiyel İyileştirmeler
- **Elasticsearch & Kibana** entegrasyonu
- **Apache Airflow** workflow orchestration
- **Machine Learning pipeline'ları**
- **Multiple data sources** entegrasyonu
- **Real-time alerts** sistemi

### Ölçeklenebilirlik
- Kubernetes deployment
- Auto-scaling capabilities
- Multi-region setup
- Load balancing

---

## 📋 Sonuç

Bu Big Data projesi, modern veri mühendisliği pratiklerini ve teknolojilerini bir araya getirerek:

✅ **Gerçek zamanlı veri işleme** yetenekleri
✅ **Dağıtık depolama** altyapısı  
✅ **Ölçeklenebilir mimari** tasarımı
✅ **İnteraktif analiz** ortamı
✅ **Konteynerize deployment** kolaylığı

sağlamaktadır.

Proje, büyük veri ekosistemine giriş yapmak isteyen geliştiriciler ve veri mühendisleri için mükemmel bir öğrenme platformu oluşturmaktadır.

---

## 📞 Teknik Detaylar ve Destek

### Önemli Portlar
- Kafka UI: 8081
- Zeppelin: 8080  
- HDFS NameNode: 9870
- YARN ResourceManager: 8088

### Configuration Files
- `docker-compose.yml` - Ana orkestrasyon
- `config.env` - Hadoop yapılandırması
- `requirements.txt` - Python dependencies

**Not**: Bu sunum, projenin teknik mimarisini ve işleyişini kapsamlı bir şekilde açıklamaktadır. Daha detaylı bilgi için ilgili servis dokümantasyonlarına başvurabilirsiniz.