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
