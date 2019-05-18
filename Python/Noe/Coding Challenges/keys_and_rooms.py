'''
Problem: https://leetcode.com/problems/keys-and-rooms
Author: Noé
Function Description:
# There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1,
# and each room may have some keys to access the next room.

# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an
# integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

# Initially, all the rooms start locked (except for room 0).

# You can walk back and forth between rooms freely.

# Return true if and only if you can enter every room.
'''

class Solution:
    def canVisitAllRooms(self, rooms):
        return len(self.navigateRooms(0, set(), rooms)) == len(rooms)

    def navigateRooms(self, currentRoom, unlockedRooms, rooms):
        if currentRoom in unlockedRooms:
            return unlockedRooms
        unlockedRooms.add(currentRoom)
        for key in rooms[currentRoom]:
            if key not in unlockedRooms:
                unlockedRooms.update(self.navigateRooms(key, unlockedRooms, rooms))
        return unlockedRooms




s = Solution()
dungeon = [[1,3],[3,0,1],[2],[0]]
print(s.canVisitAllRooms(dungeon))
