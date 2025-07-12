import datetime
from collections import defaultdict, Counter

class MoodEntry:
    def __init__(self, mood: str, date: datetime.date = None):
        self.mood = mood.lower()
        self.date = date or datetime.date.today()

class JournalEntry:
    def __init__(self, text: str, date: datetime.date = None):
        self.text = text
        self.date = date or datetime.date.today()

class Recommendation:
    # Very basic strategy system; could be enhanced by ML or rules.
    coping_strategies = {
        'sad': ['Talk to a friend', 'Try light exercise', 'Write in your journal'],
        'anxious': ['Practice deep breathing', 'Take a break from screens', 'Listen to calming music'],
        'angry': ['Go for a walk', 'Try grounding exercises', 'Write down your thoughts'],
        'happy': ['Reflect on what made you happy', 'Share your mood with someone', 'Celebrate small wins'],
        'neutral': ['Keep tracking!', 'Try a mindfulness activity', 'Set a small goal for today']
    }

    @classmethod
    def suggest(cls, recent_moods):
        if not recent_moods:
            return ['Start logging your moods to get personalized suggestions.']
        
        mood_counts = Counter(recent_moods)
        most_common_mood, _ = mood_counts.most_common(1)[0]
        return cls.coping_strategies.get(most_common_mood, ['Stay mindful and reflect.'])

class User:
    def __init__(self, username: str):
        self.username = username
        self.mood_log = []
        self.journal_log = []

    def add_mood(self, mood: str):
        entry = MoodEntry(mood)
        self.mood_log.append(entry)

    def add_journal(self, text: str):
        entry = JournalEntry(text)
        self.journal_log.append(entry)

    def get_mood_trend(self, days: int = 7):
        today = datetime.date.today()
        recent = [entry.mood for entry in self.mood_log if (today - entry.date).days <= days]
        return recent

    def get_recommendations(self):
        recent_moods = self.get_mood_trend()
        return Recommendation.suggest(recent_moods)
