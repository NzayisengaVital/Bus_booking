from mybus.models import Sector, District

with open("location_tables_data.sql", encoding="utf-8") as file:
    lines = file.readlines()

start = False

for line in lines:
    if line.startswith("COPY public.users_sector"):
        start = True
        continue
    if start and line.strip() == "\\.":
        break

    if start:
        parts = line.strip().split("\t")

        if len(parts) == 5:
            try:
                sector_id = int(parts[0])
                name = parts[1]

                # ✅ FIX NULL VALUES
                latitude = float(parts[2]) if parts[2] != "\\N" else None
                longitude = float(parts[3]) if parts[3] != "\\N" else None

                district_id = int(parts[4])

                district = District.objects.get(id=district_id)

                # ✅ prevent duplicate crash
                Sector.objects.update_or_create(
                    id=sector_id,
                    defaults={
                        "name": name,
                        "district": district,
                        "latitude": latitude,
                        "longitude": longitude,
                    }
                )

            except Exception as e:
                print("Error:", e)

print("✅ Sectors imported successfully!")