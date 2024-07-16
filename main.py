from csv import reader
from collections import defaultdict
import time
from pathlib import Path


def processar_temperaturas(path_to_txt: Path):
    print("Iniciando o processando do arquivo.")
    start_time = time.time() # Tempo de inicio
    temperatura_por_station = defaultdict(list)
