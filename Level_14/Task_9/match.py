from pydantic import BaseModel
from typing import List

class CricketSeries(BaseModel):
    year: int        
    series_type: str  
    series_name: str 
    series_href: str  


class CricketSeriesList(BaseModel):
    series: List[CricketSeries]