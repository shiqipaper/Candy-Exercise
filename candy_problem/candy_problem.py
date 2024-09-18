'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

def get_friends_favorite_candy_count(favorites):
    favorite_candy_counts = {
    }
    candies = []
    for friend_favorite in favorites:
        candies = friend_favorite[1]
        for candy in friend_favorite[1]:
            if candy not in favorite_candy_counts:
                favorite_candy_counts[candy] = 0
            else:
                favorite_candy_counts[candy] += 1
    return favorite_candy_counts    



get_friends_favorite_candy_count(friend_favorites)



'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(data):
    candy_with_names = {}
    for i in range(len(data)):
        # print(data[i])
        # print(data[i][0])
        # print(data[i][1])
        for candy in data[i][1]:
            if candy not in candy_with_names:
                candy_with_names[candy] = []
            candy_with_names[candy].append(data[i][0])
    return candy_with_names
    


'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def get_friends_who_like_specific_candy(data, candy_name):
    name_list = []
    for i in range(len(data)):
        name = data[i][0]
        favorite_candies = data[i][1]
        if candy_name in favorite_candies:
            name_list.append(name)
    result = tuple(name_list)
    return result

'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_candy_set(data):
    candies = set()
    for i in range(len(data)):
        for candy in data[i][1]:
            candies.add(candy)
    return candies

create_candy_set(friend_favorites)

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

