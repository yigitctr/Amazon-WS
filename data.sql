CREATE TABLE TrafikDurumu (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tarih_saat DATETIME,
    lokasyon VARCHAR(255),
    durum VARCHAR(255)
);

CREATE TABLE AraçBilgisi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plaka VARCHAR(20),
    model VARCHAR(255),
    renk VARCHAR(50),
    tarih_saat DATETIME
);

CREATE TABLE TrafikKamera (
    id INT PRIMARY KEY AUTO_INCREMENT,
    lokasyon VARCHAR(255),
    tarih_saat DATETIME,
    resim BLOB
);

/* NEW SQL */

CREATE TABLE TrafikDurumu (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tarih_saat DATETIME,
    lokasyon VARCHAR(255),
    durum VARCHAR(255),
    yoğunluk INT, -- Yoğunluğu ölçen bir sayı (örneğin, 0 - çok düşük, 5 - çok yüksek)
    kaza BOOLEAN, -- Kaza olup olmadığını belirten bir boolean değer
    yol_calismasi BOOLEAN, -- Yol çalışması olup olmadığını belirten bir boolean değer
    hava_durumu VARCHAR(100) -- Hava durumu bilgisi
);

CREATE TABLE AraçGeçiş (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plaka VARCHAR(20),
    gecis_tarihi_saat DATETIME,
    hız INT, -- Araç hızı (km/s)
    lokasyon VARCHAR(255), -- Geçişin olduğu lokasyon
    trafik_durumu_id INT, -- Trafik durumu tablosuna referans
    FOREIGN KEY (trafik_durumu_id) REFERENCES TrafikDurumu(id)
);

CREATE TABLE TrafikKamera (
    id INT PRIMARY KEY AUTO_INCREMENT,
    lokasyon VARCHAR(255),
    tarih_saat DATETIME,
    resim BLOB -- Görüntüyü saklamak için BLOB türü
);
