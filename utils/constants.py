"""Application-wide constants."""

from __future__ import annotations

APP_NAME = "Civic Region Planner"
DEFAULT_COLORS = [
    "#2f80ed",
    "#27ae60",
    "#f2994a",
    "#eb5757",
    "#9b51e0",
    "#00a8a8",
    "#6f4e37",
    "#34495e",
    "#d35400",
    "#16a085",
]
ALGORITHMS = ("Greedy", "Backtracking")
ALGORITHM_LABELS = {
    "Greedy": "Fast Allocation",
    "Backtracking": "Optimal Constraint Check",
}
DATASET_COLLECTION = "datasets"
REGION_COLLECTION = "regions"
RESULT_COLLECTION = "results"
MAX_BACKTRACKING_COLORS = 12
