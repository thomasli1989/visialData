import matplotlib.pyplot as plt
from random_walk import RandomWalk
import time

if False:
    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()

        plt.figure(dpi = 192,figsize=(10,6))
        point_numbers = list(range(rw.num_points))
        # plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap = plt.cm.Blues,edgecolor = 'none',s = 15)
        plt.plot(rw.x_values,rw.y_values,'b-')
        #highlight the start and end point
        plt.scatter(0,0,c='green',edgecolor = 'none',s = 100)
        plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor = 'none',s = 100)

        #set the axex invisible
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        # plt.savefig('randomwalk.png',bbox_inches = 'tight')
        plt.show()

        keep_running = input("Make another walk?(y/n)")
        if keep_running == 'n':
            break
else:
    picnum = 6
    while picnum:
        rw = RandomWalk(90000)
        rw.fill_walk()

        plt.figure(dpi = 100,figsize=(10,6))
        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap = plt.cm.Blues,edgecolor = 'none',s = 25)
        # plt.scatter(rw.x_values,rw.y_values,c='blue',edgecolor = 'none',s = 10)
        # plt.plot(rw.x_values,rw.y_values,'b-')
        #highlight the start and end point
        # plt.scatter(0,0,c='green',edgecolor = 'none',s = 100)
        # plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor = 'none',s = 100)

        #set the axex invisible
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        filename = 'randomwwlk'+str(picnum)+'.png'

        plt.savefig(filename,bbox_inches = 'tight')
        plt.show()
        picnum -=1
        time.sleep(0.2)
    # plt.savefig('randomwalk5.png',bbox_inches = 'tight')