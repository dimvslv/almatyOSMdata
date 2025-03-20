# Дли импорта требуется ogr2ogr встроенный в пакет QGIS
# Устанавливаем переменную окружения (на время сессии)
$env:Path += ";C:\Program Files\QGIS 3.28.0\bin"

# Запрашиваем ввод параметров
$DB_NAME = Read-Host "Enter database name"
$DB_USER = Read-Host "Enter database user"
$DB_PASSWORD = Read-Host "Enter database password" -AsSecureString

# Преобразуем пароль в обычный текст (нужно для передачи в ogr2ogr)
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($DB_PASSWORD)
$PlainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Импортируем в PostgreSQL через ogr2ogr
ogr2ogr -f "PostgreSQL" PG:"dbname=$DB_NAME user=$DB_USER password=$PlainPassword" `
    "..\data\kazakhstan-latest.osm.pbf" `
    -overwrite -progress `
    -lco GEOMETRY_NAME=geom -lco FID=id -lco SPATIAL_INDEX=GIST `
    -nlt PROMOTE_TO_MULTI

Write-Host "Import complete!"