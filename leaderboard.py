import redis

#create a redis client
redisClient = redis.StrictRedis(host = 'localhost',port=6379,db=0,decode_responses=True)

#Name of the leaderboard
players = "Players"

# Add a player to the Redis sorted set against the score
for i in range(0,3):
    dict={}
    name = input("Give Player name:")
    score = int(input("Give Player points:"))
    #Add the name and score in the dict and then into the sorted set
    dict[name] = score
    print("\n")
    redisClient.zadd(players,dict)

#print the players in descending order
for key,score in redisClient.zrevrange(players, 0, -1, 'withscores'):
                            print(key,score)

maxVal = redisClient.zrevrange(players, 0, 0, 'withscores')
minVal = redisClient.zrevrange(players, -1, -1, 'withscores')

#bring the third player to the top
dict[minVal[0][0]] = maxVal[0][1]+1
redisClient.zadd(players,dict)

#print the new list
print("\nThe updated score: \n")
for key,score in redisClient.zrevrange(players, 0, -1, 'withscores'):
                            print(key,score)
