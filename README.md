# MetroSimulation
Bu projede, bir metro ağında; 
* İki istasyon arasındaki en hızlı, 
* En az aktarmalı rotayı bulan bir simülasyon geliştirdik.
Projede Kullanılan Kütüphaneler;
* Collections -> Python'daki collections kütüphanesi, standart veri tiplerinin daha gelişmiş ve verimli versiyonlarını sağlayan bir modüldür. İçerisinde list, tuple, dict gibi yapıların daha özel versiyonları bulunur. Bazı önemli veri yapıları şunlardır: Counter, defaultdict, OrderedDict, deque, namedtuple.
* Heapq -> Python’daki heapq kütüphanesi, min heap (küçükten büyüğe sıralı yığın) veri yapısını uygular. Öncelikli Kuyruk (Priority Queue) işlemleri için kullanılır. O(log n) karmaşıklıkta hızlı ekleme ve çıkarma işlemleri yapar.
Bu kütüphaneleri verilere hızlı ve kolayca erişmek, en kısa yolu bulma ve en az aktarmalı rotayı bulmak için kullandık.
Örnek kullanım ve test sonuçları:
    1. AŞTİ'den OSB'ye:
    En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
    En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
    
    2. Batıkent'ten Keçiören'e:
    En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
    En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören
    
    3. Keçiören'den AŞTİ'ye:
    En az aktarmalı rota: Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
    En hızlı rota (19 dakika): Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
Proje İçin Öneriler: Metrolar gerçek zamanlı takip edilerek hangi durağa kaç dakika içerisinde ulaşacağı gösterilebilir.
