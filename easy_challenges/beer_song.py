class BeerSong:

    @classmethod
    def verse(cls, num):
        if num == 0:
            verse = (
                "No more bottles of beer on the wall, "
                "no more bottles of beer.\n"
                "Go to the store and buy some more, "
                "99 bottles of beer on the wall."
            )
        
        elif num == 1:
            verse = (
                f"{num} bottle of beer on the wall, "
                f"{num} bottle of beer.\n"
                f"Take it down and pass it around, "
                "no more bottles of beer on the wall.\n"
                )
        
        else:
            verse = (
            f"{num} bottles of beer on the wall, "
            f"{num} bottles of beer.\n"
            "Take one down and pass it around, "
            )

            if num - 1 == 1:
                verse += (
                    "1 bottle of beer on the wall.\n"
                    )

            else:    
                verse += (
                    f"{num - 1} bottles of beer on the wall.\n"
                    )
            
        return verse

    @classmethod
    def verses(cls, start, stop):
        select_verses = []

        for num in range(start, stop - 1, -1):
            select_verses.append(cls.verse(num))

        return "\n".join(select_verses)

    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)

print(BeerSong.verses(2, 0))