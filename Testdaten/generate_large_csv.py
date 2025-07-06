#!/usr/bin/env python3
import random
import os

# Listen für Zufallsdaten
first_names = [
    "Anna", "Ben", "Clara", "David", "Emma", "Felix", "Greta", "Hans", "Ida", "Jonas",
    "Klara", "Leon", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Rosa", "Simon", "Tina",
    "Urs", "Vera", "Walter", "Xaver", "Yara", "Zoe", "Alexander", "Barbara", "Christian", "Diana",
    "Erik", "Franziska", "Georg", "Helena", "Igor", "Julia", "Karl", "Laura", "Markus", "Nina",
    "Otto", "Petra", "Quentin", "Rita", "Stefan", "Theresa", "Ulrich", "Victoria", "Wolfgang", "Xenia"
]

last_names = [
    "Mueller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann",
    "Schaefer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schroeder", "Neumann", "Schwarz", "Zimmermann",
    "Braun", "Krueger", "Hofmann", "Hartmann", "Lange", "Schmitt", "Werner", "Schmitz", "Krause", "Meier",
    "Lehmann", "Schmid", "Schulze", "Maier", "Koehler", "Herrmann", "Koenig", "Walter", "Mayer", "Huber",
    "Kaiser", "Fuchs", "Peters", "Lang", "Scholz", "Moeller", "Weiss", "Jung", "Hahn", "Schubert"
]

cities = [
    "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Duesseldorf", "Dortmund", "Essen", "Leipzig",
    "Bremen", "Dresden", "Hannover", "Nuremberg", "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Muenster",
    "Karlsruhe", "Mannheim", "Augsburg", "Wiesbaden", "Gelsenkirchen", "Moenchengladbach", "Braunschweig", "Chemnitz", "Kiel", "Aachen",
    "Halle", "Magdeburg", "Freiburg", "Krefeld", "Luebeck", "Oberhausen", "Erfurt", "Mainz", "Rostock", "Kassel",
    "Hagen", "Hamm", "Saarbruecken", "Muelheim", "Potsdam", "Ludwigshafen", "Oldenburg", "Leverkusen", "Osnabrueck", "Solingen",
    "Vienna", "Zurich", "Geneva", "Basel", "Bern", "Lausanne", "Paris", "London", "Madrid", "Rome",
    "Amsterdam", "Brussels", "Stockholm", "Copenhagen", "Oslo", "Helsinki", "Warsaw", "Prague", "Budapest", "Athens"
]

def generate_large_csv(filename, target_size_mb):
    target_size_bytes = target_size_mb * 1024 * 1024
    
    with open(filename, 'w', encoding='utf-8') as f:
        # Header
        f.write("Name;Age;City\n")
        
        current_size = f.tell()
        record_count = 0
        
        print(f"Generating {filename} with target size {target_size_mb}MB...")
        
        while current_size < target_size_bytes:
            # Generiere einen zufälligen Namen
            first = random.choice(first_names)
            last = random.choice(last_names)
            name = f"{first} {last}"
            
            # Zufälliges Alter zwischen 18 und 85
            age = random.randint(18, 85)
            
            # Zufällige Stadt
            city = random.choice(cities)
            
            # Schreibe Zeile
            line = f"{name};{age};{city}\n"
            f.write(line)
            
            current_size += len(line.encode('utf-8'))
            record_count += 1
            
            # Fortschrittsanzeige alle 100000 Zeilen
            if record_count % 100000 == 0:
                progress = (current_size / target_size_bytes) * 100
                print(f"  Progress: {progress:.1f}% - {record_count} records - {current_size / 1024 / 1024:.1f}MB")
        
        print(f"Done! Generated {record_count} records, final size: {current_size / 1024 / 1024:.2f}MB")

if __name__ == "__main__":
    # Wechsle ins Testdaten-Verzeichnis
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Generiere 100MB CSV-Datei
    generate_large_csv("persons-100MB.csv", 100)
    
    # Optional: Generiere auch eine kleinere 10MB Datei für schnellere Tests
    print("\nGenerating additional test file...")
    generate_large_csv("persons-10MB.csv", 10)