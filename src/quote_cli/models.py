# src/quote_cli/models.py
from __future__ import annotations

from pydantic import BaseModel, Field


class Quote(BaseModel):
    text: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    
    def format(self) -> str:
        return f'"{self.text}"\n  — {self.author}'
