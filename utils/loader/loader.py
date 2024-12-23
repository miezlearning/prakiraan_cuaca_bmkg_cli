# utils/loader/data_loader.py

import csv
import logging

logger = logging.getLogger(__name__)

def load_wilayah_from_csv(filename):
    """
    Membaca file CSV dan membangun struktur hierarki wilayah.
    Format CSV:
    adm_code,adm_name
    adm1_code,adm1_name
    adm2_code,adm2_name
    adm3_code,adm3_name
    adm4_code,adm4_name
    """
    wilayah_hierarchy = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # Cek apakah ada header
            first_row = next(reader)
            if first_row[0].lower().startswith('adm'):
                pass  # Sudah melewati header
            else:
                csvfile.seek(0)  # Tidak ada header, kembali ke awal
                reader = csv.reader(csvfile)
            
            current_adm1 = None
            current_adm2 = None
            current_adm3 = None

            for row in reader:
                if not row or len(row) < 2:
                    continue  # Lewati baris kosong atau tidak lengkap

                adm_code = row[0].strip()
                adm_name = row[1].strip()

                parts = adm_code.split('.')
                level = len(parts)

                if level == 1:
                    # adm1
                    if adm_code not in wilayah_hierarchy:
                        wilayah_hierarchy[adm_code] = {
                            'name': adm_name,
                            'children': {}
                        }
                    current_adm1 = adm_code
                    current_adm2 = None
                    current_adm3 = None

                elif level == 2:
                    # adm2
                    if current_adm1 is None:
                        logger.warning(f"adm2 {adm_code} tanpa adm1.")
                        continue
                    if adm_code not in wilayah_hierarchy[current_adm1]['children']:
                        wilayah_hierarchy[current_adm1]['children'][adm_code] = {
                            'name': adm_name,
                            'children': {}
                        }
                    current_adm2 = adm_code
                    current_adm3 = None

                elif level == 3:
                    # adm3
                    if current_adm2 is None:
                        logger.warning(f"adm3 {adm_code} tanpa adm2.")
                        continue
                    if adm_code not in wilayah_hierarchy[current_adm1]['children'][current_adm2]['children']:
                        wilayah_hierarchy[current_adm1]['children'][current_adm2]['children'][adm_code] = {
                            'name': adm_name,
                            'children': {}
                        }
                    current_adm3 = adm_code

                elif level == 4:
                    # adm4
                    if current_adm3 is None:
                        logger.warning(f"adm4 {adm_code} tanpa adm3.")
                        continue
                    wilayah_hierarchy[current_adm1]['children'][current_adm2]['children'][current_adm3]['children'][adm_code] = adm_name

                else:
                    logger.warning(f"Kode adm yang tidak dikenali: {adm_code}")
    except FileNotFoundError:
        logger.error(f"File {filename} tidak ditemukan.")
        raise
    except Exception as e:
        logger.error(f"Terjadi kesalahan saat membaca {filename}: {e}")
        raise
    
    return wilayah_hierarchy
