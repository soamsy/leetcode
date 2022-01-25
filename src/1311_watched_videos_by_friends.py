def watchedVideosByFriends(watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
    q = collections.deque([(id, 0)])
    
    videos = []
    visited = set()
    while q:
        person, k = q.popleft()
        if person in visited:
            continue
        if k > level:
            continue
        visited.add(person)
        fs = friends[person]
        
        if k == level:
            videos.extend(watchedVideos[person])
        
        for f in fs:
            if f not in visited:
                q.append((f, k + 1))

    counts = collections.Counter(videos)
    unique_videos = sorted(list(set(videos)))
    return sorted(unique_videos, key=lambda x: counts[x])