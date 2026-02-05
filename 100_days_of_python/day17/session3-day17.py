class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1 # when passing user argument - self (user1) inc the following +1,

user1 = User("001","Ammar")
user2 = User("002","Yasir")

user1.follow(user2) # user1 has following user2 , user2 has followers like user1
print(user1.followers)
print(user1.following) # o/p:1 user1 has following user2
print(user2.followers) # o/p:1 user2 has followers user1
print(user2.following)


