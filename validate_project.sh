#!/bin/bash

# BigData Projesi Doğrulama Script'i
# Bu script projenin temel bileşenlerini kontrol eder

echo "🔍 BigData Projesi Doğrulama Başlatılıyor..."
echo "=================================================="

# Dosya yapısı kontrolü
echo "📁 Dosya Yapısı Kontrolü:"
echo "✅ Ana dizin: $(pwd)"

required_files=(
    "docker-compose.yml"
    "producer.py" 
    "consumer.py"
    "requirements.txt"
    "config.env"
    "SUNUM.md"
    "SUNUM_SLIDES.md"
    "README.md"
)

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file - MEVCUT"
    else
        echo "❌ $file - EKSİK"
    fi
done

echo ""

# Dizin yapısı kontrolü
echo "📂 Dizin Yapısı Kontrolü:"
required_dirs=(
    "producer"
    "consumer"
    "namenode"
    "spark-scripts"
    "dataset"
)

for dir in "${required_dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir/ - MEVCUT"
    else
        echo "❌ $dir/ - EKSİK"
    fi
done

echo ""

# Python bağımlılıkları kontrolü
echo "🐍 Python Bağımlılıkları Kontrolü:"
if [ -f "requirements.txt" ]; then
    echo "📦 requirements.txt içeriği:"
    cat requirements.txt
    echo ""
else
    echo "❌ requirements.txt bulunamadı"
fi

# Sunum dosyaları kontrolü
echo "📊 Sunum Dosyaları Kontrolü:"
if [ -f "SUNUM.md" ]; then
    lines=$(wc -l < SUNUM.md)
    size=$(du -h SUNUM.md | cut -f1)
    echo "✅ SUNUM.md - $lines satır, $size boyut"
else
    echo "❌ SUNUM.md bulunamadı"
fi

if [ -f "SUNUM_SLIDES.md" ]; then
    lines=$(wc -l < SUNUM_SLIDES.md)
    size=$(du -h SUNUM_SLIDES.md | cut -f1)
    echo "✅ SUNUM_SLIDES.md - $lines satır, $size boyut"
else
    echo "❌ SUNUM_SLIDES.md bulunamadı"
fi

if [ -f "README.md" ]; then
    lines=$(wc -l < README.md)
    size=$(du -h README.md | cut -f1)
    echo "✅ README.md - $lines satır, $size boyut"
else
    echo "❌ README.md bulunamadı"
fi

echo ""

# Docker yapılandırması kontrolü
echo "🐳 Docker Yapılandırması Kontrolü:"
if [ -f "docker-compose.yml" ]; then
    services=$(grep -c "^  [a-zA-Z].*:" docker-compose.yml)
    echo "✅ docker-compose.yml - $services servis tanımlanmış"
    
    # Önemli servisler kontrolü
    important_services=("kafka" "zookeeper" "producer" "consumer" "namenode")
    for service in "${important_services[@]}"; do
        if grep -q "^  $service:" docker-compose.yml; then
            echo "  ✅ $service servisi tanımlanmış"
        else
            echo "  ❌ $service servisi bulunamadı"
        fi
    done
else
    echo "❌ docker-compose.yml bulunamadı"
fi

echo ""

# Kafka Producer/Consumer kontrolü
echo "🔄 Kafka Bileşenleri Kontrolü:"
if [ -f "producer.py" ]; then
    if grep -q "KafkaProducer" producer.py; then
        echo "✅ producer.py - KafkaProducer kullanımı tespit edildi"
    fi
    if grep -q "weather.com" producer.py; then
        echo "✅ producer.py - Weather API entegrasyonu mevcut"
    fi
fi

if [ -f "consumer.py" ]; then
    if grep -q "KafkaConsumer" consumer.py; then
        echo "✅ consumer.py - KafkaConsumer kullanımı tespit edildi"
    fi
fi

echo ""

# Sunum içerik kontrolü
echo "📋 Sunum İçerik Kontrolü:"
if [ -f "SUNUM.md" ]; then
    turkish_keywords=("Proje" "Mimari" "Kafka" "Hadoop" "Spark" "Zeppelin")
    echo "🇹🇷 Türkçe içerik kontrolleri:"
    for keyword in "${turkish_keywords[@]}"; do
        if grep -q "$keyword" SUNUM.md; then
            echo "  ✅ '$keyword' anahtar kelimesi mevcut"
        else
            echo "  ❌ '$keyword' anahtar kelimesi eksik"
        fi
    done
fi

echo ""
echo "=================================================="
echo "🎯 Doğrulama Tamamlandı!"
echo ""
echo "📖 Sunumları görüntülemek için:"
echo "   - Detaylı sunum: cat SUNUM.md"
echo "   - Slayt sunumu: cat SUNUM_SLIDES.md"  
echo "   - Genel dokümantasyon: cat README.md"
echo ""
echo "🚀 Projeyi başlatmak için:"
echo "   docker-compose up -d"
echo ""