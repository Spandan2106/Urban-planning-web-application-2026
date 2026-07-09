# Graph Coloring Web Application

A Python-only Streamlit application for urban planners who need to assign administrative categories to neighboring regions. The app parses TXT graph datasets, visualizes region adjacency, runs graph coloring algorithms, validates assignments, stores records in MongoDB, and exports reports.

## Features

- Upload or paste TXT graph datasets
- Parse edge lists and adjacency lists
- Build and visualize NetworkX graphs with labels, edge labels, colored nodes, and legends
- Run Greedy Graph Coloring or Backtracking Graph Coloring
- Validate neighboring-region constraints
- Show execution time, chromatic number, node count, edge count, graph density, and database statistics
- Save datasets, region graphs, and coloring results through PyMongo
- Fall back to in-memory persistence when MongoDB is offline
- Export CSV, Excel, PDF, and PNG graph files
- Maintain rotating logs in `logs/app.log`
- Include pytest coverage for parser, graph builder, coloring, validation, and API flow

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and adjust values when needed.

```env
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=graph_coloring
```

MongoDB is recommended for production persistence. The app still runs without MongoDB by using an in-memory fallback for the current process.

## How to Run

```bash
python -m streamlit run app.py
```

## Dataset Format

Accepted TXT line formats:

```text
A B
A,B
A: B C D
A
```

Comments beginning with `#` and blank lines are ignored.

## Folder Structure

```text
graph-coloring-project/
  app.py
  config/
  frontend/
  routes/
  services/
  models/
  database/
  utils/
  uploads/
  outputs/
  assets/
  tests/
  sample_data/
```

## Screenshots

Add screenshots of the Streamlit upload, graph visualization, results, and statistics pages after deployment.

## Future Scope

- Add authentication and user-owned datasets
- Add advanced algorithms such as DSATUR and exact branch-and-bound coloring
- Add geographic file support for GeoJSON and shapefiles
- Add deployment templates for Docker and cloud hosting
- Add role-based review workflows for planning departments

## License

MIT License.
