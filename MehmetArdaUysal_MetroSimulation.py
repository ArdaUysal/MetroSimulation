from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """
        # TODO: Bu fonksiyonu tamamlayın
        pass
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        #Ziyaret edilen düğümleri tutmak için bir küme oluşturduk başlangıç düğümünü ziyaret ettiğimiz için bu düğümü içine attık
        ziyaret_edildi = {baslangic}     
        #BFS için bir kuyruk oluştur
        kuyruk = deque([(baslangic,[baslangic])])
        #Kuyruk boş olana kadar dön
        while kuyruk:
            mevcut_istasyon, yol = kuyruk.popleft() #Kuyrukta gezilen mevcut istasyonu ve o istasyona kadar gidilen yolu değişkenlere ata
            #Gelinen istasyon hedef istasyona eşit mi
            if mevcut_istasyon == hedef:
                return yol   #Eğer eşitse en kısa yolu dön
            
            #En kısa yolu bulamadıysak komşuları dolaşıyoruz
            for komsu, _ in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edildi: #Komşu ziyaret edilmemiş ise:
                    ziyaret_edildi.add(komsu) #Komşu ziyaret edildi olarak işaretle
                    kuyruk.append((komsu,yol + [komsu])) #Kuyruğa komşuyu ekle ve şimdiye kadar ziyaret edilen yolun sonuna da komşuyu ekle

        return None #Eğer rota bulunamazsa None dön
    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur
        
        1. Başlangıç ve hedef istasyonlarının varlığını kontrol et
        2. A* algoritması ile en hızlı rotayı bul
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) döndür
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        # Başlangıç ve hedef istasyonları
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # A* algoritması için öncelik kuyruğu
        pq = [(0, id(baslangic), baslangic, [baslangic])]  # (toplam_sure, benzersiz_id, istasyon, yol)
        ziyaret_edildi = {}  # Ziyaret edilen istasyonlar ve bunlara ulaşmak için harcanan süre

        while pq:
            toplam_sure, _, mevcut, yol = heapq.heappop(pq)  # Kuyruktan en düşük maliyetli yolu al

            # Eğer hedef istasyonu bulunursa, rota ve toplam süre döndürülür
            if mevcut == hedef:
                return yol, toplam_sure

            # Eğer bu istasyon daha önce daha kısa bir süre ile ziyaret edilmişse, devam etme
            if mevcut in ziyaret_edildi and ziyaret_edildi[mevcut] <= toplam_sure:
                continue

            # Mevcut istasyonu ziyaret edilenlere ekle
            ziyaret_edildi[mevcut] = toplam_sure

            # Komşu istasyonları kontrol et
            for komsu, sure in mevcut.komsular:
                # Yeni yolun toplam süresi hesaplanır
                yeni_sure = toplam_sure + sure

                # A* algoritmasında heuristic kullanarak tahmini toplam maliyet (f) hesaplanır
                # Burada, hedefe olan mesafe basitçe sabit bir değer olarak kullanılabilir
                heuristic = 0  # Gerçek bir heuristic fonksiyonu eklenebilir
                toplam_maliyet = yeni_sure + heuristic

                # Yeni istasyon ve yol, kuyruktaki öncelik sırasına eklenir
                heapq.heappush(pq, (toplam_maliyet, id(komsu), komsu, yol + [komsu]))
        return None


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    metro_graf = {      #Metro Grafı (Maliyetleri ile beraber)
            "M1": {"M2": 5},
            "M2": {"M1": 5, "M3": 3, "K1": 2},
            "M3": {"M2": 3, "M4": 4},
            "M4": {"M3": 4, "T3": 2},

            "K1": {"M2": 2, "K2": 4},
            "K2": {"K1": 4, "K3": 6},
            "K3": {"K2": 6, "K4": 8, "T2": 3},
            "K4": {"K3": 8},

            "T1": {"T2": 7},
            "T2": {"K3": 3, "T3": 9,"T1":7},
            "T3": {"T2": 9, "M4": 2,"T4":5},
            "T4": {"T3": 5}
        }
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 