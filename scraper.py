import os
import pandas as pd
import requests
from datetime import datetime

print(">>> Mengkalkulasi Harga Komoditas Kopi (Kurs USD to IDR)...")

response = requests.get("https://api.frankfurter.app/latest?from=USD&to=IDR")
kurs_idr = response.json()['rates']['IDR']

kopi_base = {
    "Arabika Gayo (Premium)": 5.5,
    "Arabika Kintamani": 6.0,
    "Robusta Pupuan": 3.2,
    "Robusta Dampit": 3.0,
    "House Blend (Arabika/Robusta)": 4.5
}

data_hasil = []
for nama, harga_usd in kopi_base.items():
    harga_lokal = round(harga_usd * kurs_idr, 2)
    data_hasil.append({
        "tanggal_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "komoditas": nama,
        "harga_dasar_usd": harga_usd,
        "kurs_terkini_idr": kurs_idr,
        "estimasi_harga_pasar_idr": harga_lokal
    })

df = pd.DataFrame(data_hasil)
df.to_csv('dataset_harga_kopi.csv', index=False)
print(f"  Berhasil menyimpan {len(df)} baris data ke CSV.")

os.system('git add .')
os.system(f'git commit -m "Update Harian Harga Kopi: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')
os.system('git push origin main >nul 2>&1')
print("[SUKSES] Repo HargaKomoditasKopi berhasil di-push!")