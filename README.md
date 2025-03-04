# 🏩 almatyOSMdata

## 📌 Project Description

**Goal:**  
A web application that provides OSM data for Almaty in a clear and structured format (without irrelevant layers, unnecessary fields, and with meaningful names in Russian).  
This web application aggregates open data and attribute information on base maps like Google Maps and OSM. The project is built with Django to work with open geospatial data from OpenStreetMap.

**Target Audience:**  
Urban planners, analysts, and urbanists who need quick access to open Almaty geospatial data without using GIS software like QGIS or ArcGIS.

**Key Features:**
- Data filtering by layers and attributes without complex queries.
- A simple interface for viewing and analyzing data without GIS software.
- Localized data with meaningful Russian names and relevant attributes.
- Flexible export system – download required data in GeoJSON, Shapefile, or CSV formats.
- Integration with analytics – for example, density calculations, transport accessibility, and dashboard visualization.

## 📂 Project Structure

```plaintext
DjangoProject_name_2025_v1/
│── apps/                         # Django applications
│   ├── core/                     # Core settings application
│   ├── users/                    # User management (login, API keys)
│   ├── maps/                     # Maps and spatial data handling
│   │   ├── views.py               # Map views logic
│   │   ├── models.py              # Models (PostGIS objects)
│   │   ├── serializers.py         # Django REST Framework serializers
│   │   ├── urls.py                # API endpoints for maps
│   │   ├── tasks.py               # Background tasks (data updates)
│   │   └── utils.py               # Helper functions (Overpass API queries)
│   ├── api/                      # REST API for data access
│   └── frontend/                 # Frontend (Django + Leaflet)
│
├── DjangoProject_name_2025_v1/  # Django core configuration
│   ├── __init__.py       # Makes the directory a Python module
│   ├── settings.py       # Main project settings
│   ├── urls.py           # Global project routes
│   ├── wsgi.py           # WSGI server entry point
│   └── asgi.py           # ASGI entry point (for WebSockets, etc.)
│
├── media/                # User-uploaded files
│   ├── images/           # Images
│   ├── documents/        # Documents
│   └── temp/             # Temporary files
│
├── postgresql/           # PostgreSQL database (if stored locally)
│   ├── data/             # Data directory
│   └── backups/          # Database backups
│
├── static/               # Static files (CSS, JS, images)
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript scripts
│   ├── images/           # Graphics
│   └── fonts/            # Fonts
│
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Homepage
│   ├── auth/             # Authentication templates
│   ├── dashboard/        # Admin panel templates
│   └── maps/             # Map interface templates
│
├── venv/                 # Virtual environment (should not be included in the repository)
│
├── .env                  # Environment variables (should not be included in the repository)
├── .gitignore            # Git ignore file
├── manage.py             # Django management script
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 🔧 Technologies Used
- **Django** – backend framework
- **PostgreSQL + PostGIS** – geospatial data handling
- **HTML, CSS, JavaScript** – frontend
- **Leaflet** – interactive maps
- **GeoDjango** – spatial data processing

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/DjangoProject_name_2025_v1.git
cd DjangoProject_name_2025_v1
```

### 2️⃣ Create and Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file and add the required configuration:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

### 5️⃣ Apply Migrations & Start the Server
```sh
python manage.py migrate
python manage.py runserver
```

## 🐝 License
This project is distributed under an open-source license. Use it for educational and research purposes.

## 💎 Contacts
email@example.com | [GitHub](https://github.com/your-repo)

