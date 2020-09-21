def solution(n, words):
    last = []
    turn,temp = 0, words[0][0]
    for idx,word in enumerate(words):
        if idx%n == 0:
            turn += 1
        if word[0] == temp and word not in last:
            temp = word[-1]
            last.append(word)
        else:
            return [idx%n+1,turn]
    return [0,0]


print(solution(3,["tank", "kick", "know", "wheel",
                  "land", "dream", "mother", "robot", "tank"]))