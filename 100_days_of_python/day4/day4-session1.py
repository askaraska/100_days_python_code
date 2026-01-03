import random
# # RANDOMISATION AND PYTHON LISTS
# # RANDOMISATION : degree of unpredictability
#
# # end of day4: rock,paper,scissor = game project
#
random_number = random.randint(1,10)
print(random_number)
#
# # generating random floating number: its b/w 0 inclusive up to 1, 1 not inclusive
random_number_0_to_1 = random.random()
print(random_number_0_to_1)
#
# # somewhat multiply with others / 10 * 0.1 to 0.9
random_num_mul_0to10 = random.random() * 10
print(random_num_mul_0to10)

#return float point number range from 10 t0 20 , i think not 20
random_uni = random.uniform(10,20)
print(random_uni)

# coin toss: 0 = heads and 1 = tails
random_coin_toss = random.randint(0,1)
if random_coin_toss == 0:
    print("heads")
else:
    print("tails")
