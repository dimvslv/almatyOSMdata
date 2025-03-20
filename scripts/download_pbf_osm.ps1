# Скачиваем PBF-файл
Invoke-WebRequest -Uri "https://download.geofabrik.de/asia/kazakhstan-latest.osm.pbf" -OutFile "..\data\kazakhstan-latest.osm.pbf"

Write-Host "Load complete!"