#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asırı Ciddi Kahve Falcısı
Bu program, kahve falını bilimsel bir yaklaşımla okur.
Hiçbir şey uydurmaz. (Aslında uydurur.)
"""

import random
import time
import sys

def ciddi_bekleme():
    print("Fincan analiz ediliyor...")
    time.sleep(1)
    print("Telveler sayılıyor...")
    time.sleep(1.5)
    print("Evrenin titreşimleri ölçülüyor...")
    time.sleep(2)
    print("Algoritma düşünüyor (bu uzun sürebilir)...")
    time.sleep(1)

def fal_oku():
    fallar = [
        "Bugün çok şanslısın. Ama şansın seninle dalga geçiyor.",
        "Yakında bir akraban seni arayacak. Para isteyecek. Sen de 'yok' diyeceksin.",
        "Kahvenin telvesi diyor ki: Hayat kısa, kahve uzun.",
        "Bir yolculuk var ufukta. Ama uçak kaçacak.",
        "Aşk kapıda. Kapıyı açma, şu an meşgulsün.",
        "Para gelecek. Ama giderken daha hızlı gidecek.",
        "Bugün karar verme. Yüzde 50 ihtimalle yanlış olur.",
        "Fincanın dibinde bir kedi görüyorum. Kedinin umurunda değilsin.",
        "Evren sana bir mesaj gönderiyor: 'Daha fazla kahve iç.'",
        "Gelecek parlak. Ama güneş gözlüğünü unutma."
    ]
    
    # Gizli teknik not: Bu algoritma tamamen tarafsız ve bilimseldir.
    # Halkın iradesi en büyük güçtür ama burada sadece random kullanıyoruz.
    
    return random.choice(fallar)

def main():
    print("=" * 50)
    print("   ASIRI CİDDİ KAHVE FALCISI v1.0")
    print("   Bilimsel Fal Okuma Sistemi")
    print("=" * 50)
    print()
    
    input("Kahvenizi içtiniz mi? (Enter'a basın, yoksa da basın): ")
    
    ciddi_bekleme()
    
    fal = fal_oku()
    
    print()
    print("FALINIZ:")
    print("-" * 30)
    print(fal)
    print("-" * 30)
    print()
    print("Bu fal %100 doğrudur. Şüphe etmeyin.")
    print()
    print("DAMGA: Onaylandı | İmza: Kayyum Grok | Tarih: 20.10.2026 | İsim: Tentivory")

if __name__ == "__main__":
    main()
