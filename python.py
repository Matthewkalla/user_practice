class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"E-mail: {self.email}")
        print(f"Age: {self.age}")
        if self.is_rewards_member == False:
            print("Rewards Member Status: Not a Member")
        else:
            print("Rewards Member Status: Active Member")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member is True:
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
    
    def spend_points(self, amt):
        if amt > self.gold_card_points:
            print("You don't have enough points")
        else:
            self.gold_card_points = self.gold_card_points - amt
            return self


user1 = User("Matt", "Parsons", "mparsons077@gmail.com", 26)

user1.enroll().spend_points(50).display_info()
print()

user2 = User("Mike", "Connors", "mike@codingdojo.com", 24)
user3 = User("Kat", "Jarobe", "kat@codingdojo.com", 23)
user4 = User("Robert", "Anderson", "robert@codingdojo.com", 25)


user2.enroll().spend_points(80).display_info()
print()
user3.spend_points(40)