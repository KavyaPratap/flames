#flames is a fun game that predicts relationships like friend enemy etc for 2 names,

#########code begins###############
your_name = input("Enter your name: ")
friend_name = input("Enter friend's name: ")
flames = ["f", "l", "a", "m", "e", "s"]

# Convert names to lists
list_your_name = list(your_name.lower())
list_friend_name = list(friend_name.lower())

# Remove common letters
popped = set()
for i in list_your_name[:]:  # Use a slice to avoid modifying the list while iterating
    for j in list_friend_name[:]:
        if i == j:
            list_your_name.remove(i)
            list_friend_name.remove(j)
            popped.add(i)
            break  # Exit inner loop after popping to avoid unnecessary comparisons

# Count remaining letters
count = len(list_your_name) + len(list_friend_name)

# FLAMES logic----------------------tricky part
while len(flames) > 1:
    # Calculate the index to eliminate
    index = (count - 1) % len(flames)
    flames.pop(index)
"""count - 1: We subtract 1 from the count because lists in Python are zero-indexed. If count is 5, the valid indices are 0 to 4.
% len(flames): The modulo operator ensures that if the index exceeds the length of the flames list, it wraps around. This creates a circular effect. For example, if there are 3 elements in flames and count is 4, the index would be 3 % 3 = 0, which means the first element will be removed.
Element Removal:

flames.pop(index)
This line removes the element at the calculated index from the flames list. The pop() method not only removes the element but also returns it (though we’re not using the return value here)."""
    
# Final result
result = flames[0]
if result == "f":
    relationship = "Friends"
elif result == "l":
    relationship = "Love"
elif result == "a":
    relationship = "Admirers"
elif result == "m":
    relationship = "Marriage"
elif result == "e":
    relationship = "Enemies"

print(f"The relationship is: {relationship}")
