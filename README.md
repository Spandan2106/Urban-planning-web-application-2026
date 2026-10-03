# 🏙️ Urban Planning Graph Coloring Application

> A powerful Python & Streamlit web application designed for urban planners to assign administrative categories to neighboring regions efficiently using graph coloring algorithms and spatial validation.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live-Demo-success.svg)](https://urban-planning-web-application-2026.streamlit.app/)

---

## ✨ Key Features

* 📁 **Flexible Dataset Ingestion:** Upload or paste TXT graph datasets supporting edge lists, adjacency lists, and custom formats.
* 📊 **Interactive Graph Visualization:** Build and explore NetworkX graphs complete with custom labels, colored nodes, edge weights, and dynamic legends.
* 🧠 **Advanced Algorithms:** Run **Greedy Graph Coloring** or **Backtracking Graph Coloring** seamlessly.
* ✅ **Constraint Validation:** Instantly validate neighboring-region conflicts to ensure planning compliance.
* 📈 **Comprehensive Analytics:** Track execution time, chromatic numbers, node/edge counts, graph density, and database metrics.
* 💾 **Dual Persistence Layer:** Save and retrieve datasets via MongoDB (**PyMongo**) with an automatic in-memory fallback when offline.
* 📤 **Multi-Format Exports:** Export your final reports and graphs to CSV, Excel, PDF, and PNG formats.
* 📝 **Robust Logging & Testing:** Maintain rotating application logs and verify system integrity using comprehensive `pytest` test suites.

---

## 🚀 Quick Start & Installation

Get the application running locally in just a few steps:

```bash
# 1. Clone the repository
git clone [https://github.com/Spandan2106/Urban-planning-web-application-2026.git](https://github.com/Spandan2106/Urban-planning-web-application-2026.git)
cd Urban-planning-web-application-2026

# 2. Create and activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```
**⚙️ Configuration**
Copy the example configuration file and customize your settings as needed:

```Bash
cp .env.example .env
```
Environment Variables:

```Code snippet
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=graph_coloring
```
***Note: MongoDB is recommended for persistent storage, but the app will automatically fall back to an in-memory database if offline.***

**💻 How to Run**
Launch the Streamlit interface locally:

```Bash
python -m streamlit run app.py
```
**📄 Dataset Format Guidelines**
The application accepts clean .txt files adhering to the following line formats:

* Edge Lists: A B or A,B

* Adjacency Lists: A: B C D

* Single Nodes: A

***Note: Blank lines and comment lines beginning with # are automatically ignored.***

📂 Project Structure
```Plaintext
graph-coloring-project/
├── app.py                # Main Streamlit entry point
├── config/               # Application configuration settings
├── frontend/             # UI components and layout views
├── routes/               # API and application route logic
├── services/             # Core business logic & graph algorithms
├── models/               # Data models and schemas
├── database/             # Database connection & persistence handlers
├── utils/                # Helper utilities and loggers
├── uploads/              # Temporary user dataset storage
├── outputs/              # Exported report files and graphs
├── assets/               # Static images and branding resources
├── tests/                # Pytest unit and integration tests
└── sample_data/          # Example dataset files
```
**🔮 Future Scope**
* [ ] Add user authentication and role-based review workflows for planning departments.

* [ ] Implement advanced algorithms such as DSATUR and exact Branch-and-Bound coloring.

* [ ] Introduce geographic file support for GeoJSON and Shapefiles.

* [ ] Provide official Docker containers and cloud deployment templates.

**📜 License**
Distributed under the MIT License. See LICENSE for more details.
