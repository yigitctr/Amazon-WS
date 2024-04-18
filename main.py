import pandas as pd
import matplotlib.pyplot as plt

# Örnek olarak CSV dosyasından veri okuma
veri = pd.read_csv("istanbul_trafik_verisi.csv")

# Veriyi inceleme
print(veri.head())

# Trafik durumuna göre sayıları sayma
trafik_durumu_sayisi = veri['durum'].value_counts()

# Trafik durumlarını çubuk grafikle gösterme
plt.figure(figsize=(10, 6))
trafik_durumu_sayisi.plot(kind='bar', color='skyblue')
plt.title('Trafik Durumları')
plt.xlabel('Trafik Durumu')
plt.ylabel('Sayı')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Araç hızlarının histogramını çizme
plt.figure(figsize=(10, 6))
plt.hist(veri['hız'], bins=20, color='orange', edgecolor='black')
plt.title('Araç Hızları Histogramı')
plt.xlabel('Hız (km/s)')
plt.ylabel('Frekans')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#Ücret Hesaplama Otoyollar için
def calculate_fee():
    try:
        # Girişlerden değerleri al
        km = float(entry1.get())
        vehicle_class = int(entry2.get())

        # Veri setinden ilgili ücreti al
        fee = data.loc[data['Vehicle Class'] == vehicle_class, 'Fee'].iloc[0]

        # Hesaplanan ücreti ekrana yazdır
        messagebox.showinfo("Ücret", f"Ödenecek Ücret: {fee * km} TL")
    except Exception as e:
        messagebox.showerror("Hata", "Hesaplama sırasında bir hata oluştu. Lütfen girdileri kontrol edin.")
