# Exercise 8-13: User Profile

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

# Build a profile of yourself
user_profile = build_profile(
    "Marcelo",
    "Salvador",
    role="Software Engineer",
    location="USA",
    focus="AI/ML leadership"
)

print(user_profile)