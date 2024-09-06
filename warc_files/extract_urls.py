import warcio
from warcio.archiveiterator import ArchiveIterator

def extract_urls_from_warc(warc_file):
    urls = []
    
    # Открываем WARC-файл для чтения
    with open(warc_file, 'rb') as stream:
        # Итерация по записям в файле
        for record in ArchiveIterator(stream):
            if record.rec_type == 'response':
                # Извлекаем URL из заголовков HTTP-запроса
                url = record.rec_headers.get_header('WARC-Target-URI')
                if url:
                    urls.append(url)
    
    return urls

def main():
    # Названия скачанных WARC-файлов
    warc_files = ['CC-MAIN-20240802234508-20240803024508-00000.warc', 'CC-MAIN-20240802234508-20240803024508-00001.warc']
    
    all_urls = []
    
    # Извлечение URL-адресов из каждого WARC-файла
    for warc_file in warc_files:
        try:
            print(f"Processing {warc_file}...")
            urls = extract_urls_from_warc(warc_file)
            all_urls.extend(urls)
            print(f"Extracted {len(urls)} URLs from {warc_file}")
        except Exception as e:
            print(f"Error processing {warc_file}: {e}")
    
    # Сохранение всех извлечённых URL в файл websites.txt
    with open('websites.txt', 'w') as output_file:
        for url in all_urls:
            output_file.write(url + '\n')
    
    print(f"Extraction complete! Total URLs extracted: {len(all_urls)}")

if __name__ == "__main__":
    main()