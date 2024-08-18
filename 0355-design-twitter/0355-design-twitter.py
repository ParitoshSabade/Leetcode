class Twitter:

    def __init__(self):
        self.count = 0
        self.twitmap = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitmap[userId].append((self.count,tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        output = []

        for tweet in self.twitmap[userId]:
            heapq.heappush(heap, tweet)
        
        for followee in self.followmap[userId]:
            for tweet in self.twitmap[followee]:
                heapq.heappush(heap, tweet)
        for _ in range(10):
            if heap:
                tweet = heapq.heappop(heap)
                output.append(tweet[1])
            else:
                break
        
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)