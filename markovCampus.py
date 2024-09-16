import random
from random import choices
#import matplotlib.pyplot as plt
#from PIL import Image
#from matplotlib.offsetbox import OffsetImage, AnnotationBbox


class Campus:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.locations = list(transition_matrix.keys())

    def get_next_location(self, current_location):
        next_location = random.choices(list(self.transition_matrix.keys()), weights=list(self.transition_matrix[current_location].values()))
        return next_location[0]

    def make_schedule(self, schedule_length=15):
        schedule = ["Dorm"]
        current_location = "Dining Hall"
        #while len(schedule) < schedule_length:
        while current_location != "Dorm" and len(schedule) < schedule_length:
            next_location = self.get_next_location(current_location)
            schedule.append(next_location)
            current_location = next_location
        if schedule[-1] != "Dorm":
            schedule.append("Dorm")
        return schedule


def main():
    
    schedule_maker = Campus({
        "Dorm": {"Dorm": .01, "Dining Hall": .7, "Class": .2, "Fields": .0},
        "Dining Hall": {"Dorm": .03, "Dining Hall": .1, "Class": .5, "Fields": .1},
        "Class": {"Dorm": .02, "Dining Hall": .5, "Class": .3, "Fields": .0},
        "Fields": {"Dorm": .06, "Dining Hall": .3, "Class": .0, "Fields": .1}
        })
    

    print(schedule_maker.make_schedule())

 

if __name__ == "__main__":
    main()