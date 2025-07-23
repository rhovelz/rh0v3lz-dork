## Radivan - Rh0v3lz
## Github.com/rhovelz


from googlesearch import search

def cari_keyword_di_google(keyword, jumlah_hasil=50):
    hasil = []
    for url in search(keyword, num_results=jumlah_hasil):
        hasil.append(url)
    return hasil

# Contoh penggunaan
if __name__ == "__main__":
    keyword = "fill-it"
    hasil_pencarian = cari_keyword_di_google(keyword)
    for i, url in enumerate(hasil_pencarian, start=1):
        print(f"{i}. {url}")

