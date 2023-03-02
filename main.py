class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(4564, "Jim")
user_2 = User(8795, "Sam")
user_3 = User(1575, "Mary")

user_1.follow(user_2)
user_1.follow(user_3)

print(f"{user_1.username} is following {user_1.following} and has {user_1.followers} followers.")
print(f"{user_2.username} is following {user_2.following} and has {user_2.followers} followers.")
print(f"{user_3.username} is following {user_3.following} and has {user_3.followers} followers.")
