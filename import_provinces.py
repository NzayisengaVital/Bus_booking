from mybus.models import Province

with open("location_tables_data.sql", encoding="utf-8") as file:
    start = False

    for line in file:
        if "COPY public.users_province" in line:
            start = True
            continue

        if start:
            if line.strip() == "\\.":
                break

            parts = line.strip().split("\t")

            if len(parts) >= 4:
                lat = float(parts[2]) if parts[2] != "\\N" else None
                lon = float(parts[3]) if parts[3] != "\\N" else None

                Province.objects.create(
                    id=int(parts[0]),  # 🔥 IMPORTANT
                    name=parts[1],
                    latitude=lat,
                    longitude=lon
                )