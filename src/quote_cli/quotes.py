# src/quote_cli/quotes.py
from __future__ import annotations

from quote_cli.models import Quote


class QuoteCollection:
    def __init__(self, quotes: list[Quote]) -> None:
        self._quotes = quotes
    
    def get_all(self) -> list[Quote]:
        return self._quotes.copy()
    
    def count(self) -> int:
        return len(self._quotes)


def create_default_collection() -> QuoteCollection:
    quotes = [
        Quote(
            text="The only way to do great work is to love what you do.",
            author="Steve Jobs"
        ),
        Quote(
            text="Life is what happens when you're busy making other plans.",
            author="John Lennon"
        ),
        Quote(
            text="The future belongs to those who believe in the beauty of their dreams.",
            author="Eleanor Roosevelt"
        ),
        Quote(
            text="It is during our darkest moments that we must focus to see the light.",
            author="Aristotle"
        ),
        Quote(
            text="Be yourself; everyone else is already taken.",
            author="Oscar Wilde"
        ),
        Quote(
            text="The only impossible journey is the one you never begin.",
            author="Tony Robbins"
        ),
        Quote(
            text="In the end, we will remember not the words of our enemies, "
                 "but the silence of our friends.",
            author="Martin Luther King Jr."
        ),
        Quote(
            text="The best time to plant a tree was 20 years ago. The second best time is now.",
            author="Chinese Proverb"
        ),
        Quote(
            text="Success is not final, failure is not fatal: it is the courage to continue "
                 "that counts.",
            author="Winston Churchill"
        ),
        Quote(
            text="The mind is everything. What you think you become.",
            author="Buddha"
        ),
    ]
    return QuoteCollection(quotes)
