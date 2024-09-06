import os
import requests

def download_warc_files(warc_paths_file, download_dir):
    # Создаем директорию для скачанных файлов
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    base_url = "https://data.commoncrawl.org/"
    
    # Читаем файл с путями
    with open(warc_paths_file, 'r') as file:
        warc_paths = file.readlines()

    for path in warc_paths:
        path = path.strip()
        file_url = base_url + path
        file_name = os.path.join(download_dir, os.path.basename(path))

        # Скачиваем файл
        print(f"Downloading {file_url}...")
        response = requests.get(file_url, stream=True)

        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"Downloaded {file_name}")
        else:
            print(f"Failed to download {file_url}")

if __name__ == "__main__":
    warc_paths_file = 'warc.paths'  # Путь к файлу warc.paths
    download_dir = './warc_files'   # Папка для скачанных файлов
    download_warc_files(warc_paths_file, download_dir)