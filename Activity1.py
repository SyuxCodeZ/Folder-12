# the input variables

string = input("Enter Your String: ")

char = input("Enter The Amount Of Characters You Want To Find In The Given String: ")

# intialized variables

char_count = 0

count = 0

# the complicated stuff

while (char_count < len(string)):

        if (string[char_count] == char):

            count = count + 1

        char_count = char_count + 1

print (f"amount of {char}s in in the given string is {count}")