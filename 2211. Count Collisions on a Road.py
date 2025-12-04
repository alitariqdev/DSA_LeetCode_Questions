class Solution:
    def countCollisions(self, directions: str) -> int:
        
        # Step 1: Ignore all leading 'L'
        i = 0
        n = len(directions)
        while i < n and directions[i] == 'L':
            i += 1
        
        # Step 2: Ignore all trailing 'R'
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        # Step 3: Count collisions in the remaining section
        collisions = 0
        while i <= j:
            if directions[i] != 'S':   # Only 'L' or 'R' cause collisions
                collisions += 1
            i += 1
        
        return collisions


# Leading 'L' cars on the far left move away and never collide, so we ignore them.
# Trailing 'R' cars on the far right also move away and never collide, so we ignore them too.
# In the remaining middle section, every moving car ('L' or 'R') is guaranteed to hit something—either another car or a stopped car.
# Stopped cars ('S') don’t cause collisions, but cars hitting them do.
# So the number of collisions equals the count of 'L' and 'R' in the middle section.
