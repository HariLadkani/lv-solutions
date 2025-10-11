class Twitter:

    def __init__(self):
        '''

        maintain time in init
        userid: [(tweetids, time)]
        follower: set(followees, include itself in get news feed])

        iterate from right side of all userids that user follows
        maintain index pointer and max heap
            pop max, 
            move its index and 
            add new element at index to heap, 
            add max we popped into array
            sort array in reverse and return

        run time for heap:
            10*log(users)


        '''

        self.follower_to_followee = defaultdict(set)
        self.user_to_tweet = defaultdict(list)
        self.time = 0
        self.max_heap = []
        

    #userId: tweetId
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweet[userId].append((self.time, tweetId))
        self.time -= 1
        
    
    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        goal: return array of tweetid with top 10 atmost
        contraint: 
            userid of tweets be of
                user itself
                users they follow
            tweetid from most recent to less recent
        '''
        length_user_tweets = len(self.user_to_tweet[userId])
        if length_user_tweets > 0:
            self.max_heap = [(self.user_to_tweet[userId][length_user_tweets-1],length_user_tweets-2, userId)]
        for followee in self.follower_to_followee[userId]:
            tweets = self.user_to_tweet[followee]
            if tweets:
                size = len(tweets)
                heapq.heappush(self.max_heap, (tweets[size-1], size-2, followee))

        tweets = []
        while len(tweets) < 10 and self.max_heap:
            (time, tweetId), index, user = heapq.heappop(self.max_heap)
            tweets.append((time, tweetId))
            if index > -1:
                heapq.heappush(self.max_heap, (self.user_to_tweet[user][index], index-1, user))
        print(tweets)
        res = [tweetId for _, tweetId in sorted(tweets, reverse=True, key=lambda x: -x[0])]
        return res


        


        
    #maintain set
    def follow(self, followerId: int, followeeId: int) -> None:
        '''
        follower follows followee
        cannot follow itself 
        '''
        if followerId != followeeId:
            self.follower_to_followee[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId in self.follower_to_followee and 
            followeeId in self.follower_to_followee[followerId]):
            self.follower_to_followee[followerId].remove(followeeId)

        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)