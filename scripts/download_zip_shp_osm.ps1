# Скачиваем ZIP-архив
Invoke-WebRequest -Uri "https://download.geofabrik.de/asia/kazakhstan-latest-free.shp.zip" -OutFile "..\data\kazakhstan-latest.zip"

Write-Host "Load complete!"

