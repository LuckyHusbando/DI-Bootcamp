#Exercise XP - Week 2 Day 6

# Exercise 3 : Who’s the song producer?

# Step 1: Create the Song Class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Example usage
stairway = Song(["There’s a lady who's sure", 
                 "all that glitters is gold", 
                 "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()
# Expected Output:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven