class Solution:
    def canVisitAllRooms(self, rooms):
        unlockedRooms = set(0)
        unlockedRooms.update(openRooms(rooms[0], unlockedRooms, 0))

        return True

    def openRooms(self, keys, unlockedRooms, currentRoom):
        if currentRoom not in unlockedRooms:
            unlockedRooms.add(currentRoom)
        for i in range(keys):
            





son = Solution()
dungeon = [[1,3],[3,0,1],[2],[0]]
print(son.canVisitAllRooms(dungeon))



# class Solution:
#     def canVisitAllRooms(self, rooms):
#         keychain = set(rooms[0])
#         for i in range(1,len(rooms)):
#             if i not in keychain:
#                 return False
#             keychain.update(rooms[i])

#         return True