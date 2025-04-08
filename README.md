# 🧠 Gezinomi - Kural Tabanlı Müşteri Segmentasyonu

Bu proje, Gezinomi şirketinin tatil satış verileri kullanılarak, seviye tabanlı müşteri tanımları oluşturmayı ve bu tanımlara göre müşterileri segmentlere ayırarak, yeni müşteri profilleri üzerinden gelir tahminleri yapmayı amaçlar.

## 🎯 Amaç

Antalya’da her şey dahil konseptiyle, yüksek sezonda tatil yapmak isteyen bir kullanıcının **ortalama kazandıracağı tutarı tahmin etmek** ya da **hangi segmentte yer aldığını belirlemek** gibi sorulara cevap verebilmek.

---

## 📁 Veri Seti Bilgileri

Veri seti: `miuul_gezinomi.xlsx`

Her bir satır bir satış işlemine karşılık gelir. Yani bir müşteri birden fazla tatil satın almış olabilir.

### 📌 Değişkenler:

| Değişken Adı         | Açıklama                                      |
|----------------------|-----------------------------------------------|
| `SaleId`             | Satış ID’si                                   |
| `SaleDate`           | Satın alma tarihi                             |
| `CheckInDate`        | Otele giriş tarihi                            |
| `Price`              | Ödenen ücret                                  |
| `ConceptName`        | Tatil konsepti (Her şey Dahil, Yarım Pansiyon)|
| `SaleCityName`       | Otelin bulunduğu şehir                        |
| `CInDay`             | Otele giriş günü (Pzt, Salı...)               |
| `SaleCheckInDayDiff` | Rezervasyon ile giriş arasındaki gün farkı    |
| `Seasons`            | Giriş tarihindeki sezon bilgisi               |

---

## 📊 Uygulanan Adımlar

### 🧹 1. Veri Analizi
- Genel istatistiksel bilgiler çıkarıldı.
- Şehre, konsepte ve sezona göre ortalama fiyat analizleri yapıldı.

### 🏷️ 2. Müşteri Tipi Oluşturma (`EB_Score`)
- Rezervasyon süresine göre müşteriler dört kategoriye ayrıldı:
  - `Last_Minuters`, `Potential_Planners`, `Planners`, `Early_Bookers`

### 🧾 3. Satış Segmenti Oluşturma
- `SaleCityName`, `ConceptName`, `Seasons` değişkenleri birleştirilerek **sales_level_based** tanımlandı.
- Örnek: `ANTALYA_HERŞEY DAHİL_HIGH`

### 📈 4. Segmentleme (Segmentation)
- Fiyatlara göre `A`, `B`, `C`, `D` olmak üzere 4 segment oluşturuldu.
- Segmentlere göre `mean`, `max`, `sum` metrikleri hesaplandı.

---

## 🧪 Örnek Kullanım

Antalya’da her şey dahil bir otelde, yüksek sezonda tatil yapmak isteyen kullanıcı:

```python
new_user = "ANTALYA_HERŞEY DAHİL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]
