import random

class User:
    """Represents a Kuku FM user."""
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        # Simulate user preferences - in reality, this would come from listening history etc.
        self.preferences = {
            "preferred_genres": random.sample(["News", "Technology", "Fiction", "Biography", "Self-Help", "History"], k=random.randint(1, 3)),
            "preferred_authors": random.sample(["Author A", "Author B", "Author C", "Author D"], k=random.randint(0, 2)),
            "preferred_voice": random.choice(["Male Calm", "Female Energetic", "Male Deep", "Female Soothing"])
        }

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name}, prefs={self.preferences})"

# Simulate a user database
mock_users = {
    "user123": User("user123", "Alice"),
    "user456": User("user456", "Bob"),
    "user789": User("user789", "Charlie"),
}

def get_user(user_id):
    """Fetches a user by ID."""
    return mock_users.get(user_id)
