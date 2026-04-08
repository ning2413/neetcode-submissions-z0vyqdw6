class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) #userId: [user1ID, user2ID, ...]
        for i in range(101):
            self.followers[i].add(i)

        self.posts = defaultdict(list) #min heap by time -> userId: [[time, tweetId]]
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        total = []
        for user in self.followers[userId]:
            if user in self.posts:
                idx = len(self.posts[user]) - 1
                time, tweetId = self.posts[user][idx]
                heapq.heappush(total, [-time, tweetId, user, idx])
        while total and len(feed) < 10:
            time, tweetId, user, idx = heapq.heappop(total)
            feed.append(tweetId)
            if idx - 1 >= 0:
                time, tweetId = self.posts[user][idx - 1]
                heapq.heappush(total, [-time, tweetId, user, idx - 1])               
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId)