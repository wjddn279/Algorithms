# def solution(phone_book):
#     for i in range(len(phone_book)):
#         number = phone_book[i]
#         for j in range(i+1,len(phone_book)):
#             if len(number) <= len(phone_book[j]):
#                 print(phone_book[j][0:len(number)])
#                 if number == phone_book[j][0:len(number)]:
#                     return False
#     return True
#
# print(solution(['119', '97674223', '1195524421']))

#

# def solution(genres, plays):
#     dic = {}
#     turn = 0
#     for genre in genres:
#         if genre not in dic:
#             dic[genre] = {}
#             dic[genre][-1] = 0
#         dic[genre][turn] = plays[turn]
#         dic[genre][-1] += plays[turn]
#         turn += 1
#     print(dic)
#     result = []
#     for genre in dic:
#         arr = [dic[genre][-1]]
#         if len(dic[genre]) > 2:
#             for i in range(2):
#                 max_value, max_index = -999999, 999999
#                 for key, value in dic[genre].items():
#                     if key >= 0:
#                         if value > max_value:
#                             max_value, max_index = value, key
#                         elif value == max_value:
#                             if max_index > key:
#                                 max_value, max_index = value, key
#                 dic[genre][max_index] = 0
#                 arr.append(max_index)
#         else:
#             for key, value in dic[genre].items():
#                 if key >= 0:
#                     arr.append(key)
#         result.append(arr)
#     for i in range(len(result)):
#         for j in range(i, len(result)):
#             if result[i][0] < result[j][0]:
#                 result[i], result[j] = result[j], result[i]
#     print(result)
#     for i in range(len(result)):
#         re += result[i][1:len(result[i])]
#     print(re)
#     return re

    # for key,value in result.items():

def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))
    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    print(dic)
    album_list = sorted(album_list, reverse=True)
    print(album_list)


    while len(dic) > 0:
        play_genre = dic.pop(0)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer
class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play

ans = solution(['classic', 'pop', 'classic', 'classic', 'pop','a','a','a','a','a','b'],[500, 600, 150, 800, 2500,1000,1000,100,200,1000,10000])
print(ans)

#
# arr = [1,2,3,2,3,1,4]
# ab = {}
#
# # for i in arr:
# #     if i not in ab:
# #         ab[i] = 1
# #     else:
# #         ab[i] += 1
#
# for i in arr:
#     ab[i] = ab.get(i,0) + 1
#
# print(ab)

def solution(clothes):
    dic,brr = {},[]
    sum = 0
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = 1
        else:
            dic[cloth[1]] += 1
    for i in dic:
        brr.append(dic[i])
    ans = 1
    for j in range(len(dic)):
        ans = ans * (brr[j]+1)
    return sum-1

print(solution())