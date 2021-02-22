class Movie:
    def __init__(self, name, year, director, box_office):
        self.name = name
        self.year = year
        self.director = director
        self.box = box_office
        self.totalbox= int(box_office[0])+int(box_office[1])

    def box_office(self):
        return self.totalbox  ## return "$%d millions" % sum(self.box)
    def is_earlier_than(self,other_movie):
        if (other_movie.year - self.year) > 0 :  ## return self.year < other.year
            return True
        else :
            return False


frozen = Movie('Frozen', 2013, 'Jennifer', [1000, 200])
lionKing = Movie('Lion King', 1994, 'Robert Ralph', [4000, 500])
print(frozen.box_office()) # $1200 millions
print(frozen.is_earlier_than(lionKing)) # False