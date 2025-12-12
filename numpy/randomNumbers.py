import numpy as np

rng = np.random.default_rng()

print(rng.integers(low=1,high = 7,size=3))  # Dice roll simulation
print(rng.integers(low=1, high=100, size=(3,4)))  # 3x4 array of random integers between 1 and 100

print(np.random.uniform(low = -1,high=1,size=(2,3)))  # 2x3 array of random floats between -1 and 1 

# Shuffling an array
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print("Shuffled array:", array)

# Exercise : Generate a 5 x 5 array of random Emojis

emojis = np.array(['😀', '😂', '😍', '😎', '🤔', '😢', '😡', '👍', '🙏', '🎉'])
random_emojis = rng.choice(emojis, size=(5,5))
print("5x5 array of random emojis:\n", random_emojis)