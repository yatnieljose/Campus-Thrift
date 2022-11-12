import json
from pathlib import Path

filename = '../acc_info.json'
acc_file = Path(filename)

if (not(acc_file.exists())):
    file = open('acc_info.json', 'w')
