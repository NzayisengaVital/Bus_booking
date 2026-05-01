from mybus.models import Village, Cell

file_path = "location_tables_data.sql"

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

start = False

for line in lines:
    # Start reading village data
    if "COPY public.users_village" in line:
        start = True
        continue

    # Stop at end
    if start and line.strip() == "\\.":
        break

    if start:
        parts = line.strip().split("\t")

        # Expected: id, name, latitude, longitude, cell_id
        if len(parts) == 5:
            try:
                village_id = int(parts[0])
                name = parts[1]

                latitude = None if parts[2] == "\\N" else float(parts[2])
                longitude = None if parts[3] == "\\N" else float(parts[3])

                cell_id = int(parts[4])

                cell = Cell.objects.get(id=cell_id)

                Village.objects.get_or_create(
                    id=village_id,
                    defaults={
                        'name': name,
                        'cell': cell,
                        'latitude': latitude,
                        'longitude': longitude
                    }
                )

            except Cell.DoesNotExist:
                print(f"Cell not found for village: {name}")
            except Exception as e:
                print(f"Error: {e}")