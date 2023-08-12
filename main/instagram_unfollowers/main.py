followers = open("./followers.txt", "r", encoding="utf-8")
following = open("./following.txt", "r", encoding="utf-8")
unfollowers = open("./unfollowers.txt", "w", encoding="utf-8")

followers1 = followers.readlines()
following1 = following.readlines()

followers_list = []
following_list = []
index_number = 0

for i in followers1:
    if index_number%2==0:
        followers_list.append(i)
    else:
        pass
    index_number += 1

index_number = 0

for i in following1:
    if index_number%2==0:
        following_list.append(i)
    else:
        pass
    index_number += 1
    
for i in following_list:
    if i not in followers_list:
        unfollowers.write(i)
    else:
        pass

followers.close()
following.close()
unfollowers.close()

