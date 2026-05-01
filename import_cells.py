from mybus.models import Cell, Sector

file_path = "location_tables_data.sql"

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

start = False

for line in lines:
    # Detect start of cells data
    if "COPY public.users_cell" in line:
        start = True
        continue

    # Stop at end of section
    if start and line.strip() == "\\.":
        break

    if start:
        parts = line.strip().split("\t")

        # Expected format:
        # id, name, latitude, longitude, sector_id
        if len(parts) == 5:
            try:
                cell_id = int(parts[0])
                name = parts[1]

                # Handle NULL values (\N)
                latitude = None if parts[2] == "\\N" else float(parts[2])
                longitude = None if parts[3] == "\\N" else float(parts[3])

                sector_id = int(parts[4])

                # Get related sector
                sector = Sector.objects.get(id=sector_id)

                # Create ONLY if not exists (avoid duplicate error)
                Cell.objects.get_or_create(
                    id=cell_id,
                    defaults={
                        'name': name,
                        'sector': sector,
                        'latitude': latitude,
                        'longitude': longitude
                    }
                )

            except Sector.DoesNotExist:
                print(f"Sector not found for cell: {name}")
            except Exception as e:
                print(f"Error: {e}")