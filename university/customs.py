from typing import Any
from django.db import models
from datetime import datetime

def get_current_quarter():
    month = datetime.now().month
    if month in [1, 2, 3]:
        return "Winter"
    elif month in [4, 5, 6]:
        return "Spring"
    elif month in [7, 8, 9]:
        return "Summer"
    else:
        return "Fall"