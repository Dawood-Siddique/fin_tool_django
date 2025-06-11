import os
# import sys
# project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fin_django.settings")

import django
django.setup()


import csv
from datetime import datetime
from apps.home.models import EUModel

objects_to_create = []

with open('Data/data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        obj = EUModel(
            to=datetime.strptime(row['to'], "%Y-%m-%d %H:%M:%S"),
            open=float(row['open']),
            high=float(row['high']),
            low=float(row['low']),
            close=float(row['close']),
            y=int(float(row['y'])),  
        )
        objects_to_create.append(obj)

EUModel.objects.bulk_create(objects_to_create)
