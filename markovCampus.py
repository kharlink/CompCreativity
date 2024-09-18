import random
from random import choices
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.animation as animation
import matplotlib.cbook as cbook
# import pandas as pd
# import dataframe_image as dfi
# from importlib.metadata import version

LOCATIONS = {
    "Dorm" : (0,.92),
    "Dining Hall" : (.45,.62),
    "Class" : (.65, .4),
    "Field" : (.13, .98)
}

class Campus:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.locations = list(transition_matrix.keys())

    def get_next_location(self, current_location):
        next_location = random.choices(list(self.transition_matrix.keys()), weights=list(self.transition_matrix[current_location].values()))
        return next_location[0]

    def make_schedule(self, schedule_length=8):
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

    def make_campus(self, schedule):
        fig, myplt = plt.subplots()
        myplt.set_ylabel('blah1')
        myplt.set_xlabel('blah2')

        campusMap = OffsetImage(Image.open("assets/campus map.png"), zoom=0.4)
        theMap = AnnotationBbox(campusMap, (.5, .5), frameon=False)
        myplt.add_artist(theMap)

        pin = OffsetImage(Image.open("assets/pin.png"), zoom=0.02)
        thePin = AnnotationBbox(pin, LOCATIONS["Dorm"], frameon=False)
        myplt.add_artist(thePin)

        #failed animation attempt
        # img_file = cbook.get_sample_data("/Users/kaylieharlin/OneDrive - Bowdoin College/Computational Creativity/CompCreativity/pin.png")
        # img = plt.imread(img_file)
        # im = myplt.imshow(img, animated = True, extent = [0, 1, 0, 1], origin = 'upper')
        # pleaseWork = []

        for move in schedule:
            blah = AnnotationBbox(pin, LOCATIONS[move], frameon=False)
            print(move)
            myplt.add_artist(blah)
        
        #failed animation attempt
        # pleaseWork.append([im])
        # ani = animation.ArtistAnimation(fig=fig, artists=pleaseWork, interval=400)
        
        plt.show()
        


def main():
    
    schedule_maker = Campus({
        "Dorm": {"Dorm": .01, "Dining Hall": .7, "Class": .2, "Fields": .0},
        "Dining Hall": {"Dorm": .03, "Dining Hall": .0, "Class": .5, "Fields": .8},
        "Class": {"Dorm": .02, "Dining Hall": .5, "Class": .3, "Fields": .0},
        "Field": {"Dorm": .06, "Dining Hall": .3, "Class": .0, "Fields": .1}
        })
    

    schedule_maker.make_campus(schedule_maker.make_schedule())

 

if __name__ == "__main__":
    main()