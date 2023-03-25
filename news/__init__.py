from bs4 import BeautifulSoup
import requests
"""
method = Fungsi
Field / Atrribute = variable
constructor = method yang dipanggil pertama kali saat object diciptakan.Gunakan untuk mendeklarasikan semua field
              pada class ini.
"""

class news:
    def __init__(self, url, description):
        self.description = description
        self.result = None
        self.url = url

    def description_show(self):
        print(self.description)

    def data_extraction(self):
        print("data_extraction not yet implement")

    def data_show(self):
        print("data_show not yet implement")

    def run(self):
        self.data_extraction()
        self.data_show()

class mostpopulernewsdetik(news):
    def __init__(self, url):
        super(mostpopulernewsdetik, self).__init__(url, "NOT YET IMPLEMENTED, "
                                                       "but should to get most populer news from detik.com")

    def description_show(self):
        print(f"UNDER CONSTRUCTION {self.description}")

class mostpopulernewskompas(news):
    def __init__(self, url):
        super(mostpopulernewskompas, self).__init__(url, "To get most populer news from kompas.com")


    def data_extraction(self):
        """
        Examples of the 10 most popular news
        A
        1.Istri Pamer Harta, Ini Alasan LHKPN Pejabat Kemensetneg Esha Rahmansah Tak Bisa Ditelusuri
        B
        2.Isak Tangis Iringi Jenazah Syabda Perkasa Belawa dan Ibunya Saat Tiba di Rumah Duka
        C
        3.Viral, Foto Istrinya Pamer Tas Mewah Hermes dan Gucci, Sekda Riau: Itu KW, Belinya di Mangga Dua
        D
        4.Kronologi Syabda Perkasa Belawa Meninggal Kecelakaan, Pahlawan Piala Thomas Berpulang...
        E
        5.Kabar Duka, Tunggal Putra Indonesia Syabda Perkasa Belawa Meninggal Dunia
        F
        6.Luhut ke IMF: Kalian Jangan Macam-macam...
        G
        7.Saat "Netizen" Bantu KPK Bongkar Pejabat yang Pamer Harta...
        H
        8.Sempat Terbengkalai di Bandara YIA, 38 Calon Jemaah Umrah Asal Rembang Pulang,
        Seorang Perantara Dilaporkan sebagai Penipu
        I
        9.Kala Megawati Semprot Ribuan Kades yang Minta Anggaran Jumbo...
        J
        10.Kapolda Jateng Resmi Pecat 5 Polisi yang Jadi Calo Penerimaan Bintara Polri 2022
        :return:
        """
        try:
            content = requests.get(self.url)
        except Exception:
            return None
        if content.status_code == 200:
            soup = BeautifulSoup(content.text, "html.parser") #1. Instatioation = Instansiasi = PENCIPTAAN OBJECT DARI CLASS

            result = soup.find("div", {"class": "most__list  clearfix"})
            result = soup.findChildren("h4")

            i = 0
            A = None
            B = None
            C = None
            D = None
            E = None
            F = None
            G = None
            H = None
            I = None
            J = None
            for res in result:
                if i == 1:
                    A = res.text
                elif i == 2:
                    B = res.text
                elif i == 3:
                    C = res.text
                elif i == 4:
                    D = res.text
                elif i == 5:
                    E = res.text
                elif i == 6:
                    F = res.text
                elif i == 7:
                    G = res.text
                elif i == 8:
                    H = res.text
                elif i == 9:
                    I = res.text
                elif i == 10:
                    J = res.text
                i = i + 1

            hasil = dict()
            hasil["A"] = A
            hasil["B"] = B
            hasil["C"] = C
            hasil["D"] = D
            hasil["E"] = E
            hasil["F"] = F
            hasil["G"] = G
            hasil["H"] = H
            hasil["I"] = I
            hasil["J"] = J
            self.result = hasil
        else:
            return None

    def data_show(self):
        if self.result is None:
            print("Couldn't find the Most Popular News data from the Kompas.com site")
            return
        print("\nThe 10 most popular news based on Kompas.com site")
        print(f"1. {self.result['A']}")
        print(f"2. {self.result['B']}")
        print(f"3. {self.result['C']}")
        print(f"4. {self.result['D']}")
        print(f"5. {self.result['E']}")
        print(f"6. {self.result['F']}")
        print(f"7. {self.result['G']}")
        print(f"8. {self.result['H']}")
        print(f"9. {self.result['I']}")
        print(f"10. {self.result['J']}")




if __name__ == '__main__':
    news_in_kompas = mostpopulernewskompas("https://www.kompas.com")
    news_in_kompas.description_show()
    news_in_kompas.run()

    news_in_detik = mostpopulernewsdetik("NOT YET")
    news_in_detik.description_show()
    news_in_detik.run()

    daftar_news = [news_in_kompas, news_in_detik]
    print("\nAll News")
    for news in daftar_news:
        news.description_show()
    # news_in_detik = mostpopulernewskompas("https://www.kompas.com")
    # print("\nDescription class news", news_in_detik.description)
    # news_in_detik.run()
    # news_in_Indonesia.data_extraction()
    # news_in_Indonesia.data_show()
