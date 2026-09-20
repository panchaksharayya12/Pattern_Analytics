"""
Pattern Analytics - European Banking Intelligence
Source package initialization.
"""

from .data_loader import load_data
from .preprocessing import add_age_group
from .segmentation import add_segments
from .analytics import (
    churn_rate,
    churn_by_group,
    geographic_risk_index,
    high_value_analysis
)

__all__ = [
    "load_data",
    "add_age_group",
    "add_segments",
    "churn_rate",
    "churn_by_group",
    "geographic_risk_index",
    "high_value_analysis"
]
