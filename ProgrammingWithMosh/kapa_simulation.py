# KAPA Simulation program
# How long will KAPA last given growth per month (in %)


class KapaMember:

    def __init__(self, name, amount, mode=1):
        self.name = name
        self.principal_amount = amount
        self.withrawals = dict()
        self.amount_left = amount
        self.months_as_member = 1

    def total_money(self, months):
        amount_left = self.principal_amount*(1.3 ** months)
        self.amount_left = amount_left
        self.months_as_member = months
        self.principal_amount = amount_left
        return amount_left

    def blessings(self, months, withraw=False):
        if months < self.months_as_member:

            print("cannot be")
        else:
            print("Can be")

#         if withraw == True:
#             withrawn = self.total_money(
#                 months) - self.amount_left
#             self.amount_left = self.total_money - withrawn
#             self.withrawals[months] = withrawn
#         return withrawn


member1 = KapaMember("Allan", 5000, 1)
member1.blessings(2)

# print(f"Member name: {member1.name}")
# print(f"Principal: {member1.principal_amount}")
# print(f"Withdrawals: {member1.withrawals}")
# print(f"Amount Left: {member1.amount_left}")
# print(f"Member for: {member1.months_as_member} months")
# print("___________________________")
# member1.total_money(3)

# print(f"Member name: {member1.name}")
# print(f"Principal: {member1.principal_amount}")
# print(f"Withdrawals: {member1.withrawals}")
# print(f"Amount Left: {member1.amount_left}")
# print(f"Member for: {member1.months_as_member} months")


# bong = KapaMember("Bong", 200000, 3)
# months = 4
# print(f"Total Money: {bong.total_money}")
# print(f"blessing: {bong.blessing(3, True)}")
