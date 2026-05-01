import re
from mybus.models import District, Province

file_path = "location_tables_data.sql"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

start = False

for line in lines:
    if "COPY public.users_district" in line:
        start = True
        continue

    if start:
        if line.strip() == "\\.":
            break

        parts = line.strip().split("\t")

        if len(parts) == 5:
            id, name, lat, lon, province_id = parts

            try:
                province = Province.objects.get(id=int(province_id))

                District.objects.create(
                    id=int(id),
                    name=name,
                    latitude=float(lat),
                    longitude=float(lon),
                    province=province
                )

            except Exception as e:
                print("Error:", e)