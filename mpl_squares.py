import matplotlib.pyplot as plt

#draw line
# squares_x = [1, 2, 3, 4, 5]
# squares_y= [1, 4, 9, 16, 25]
squares_x = list(range(1,101))
squares_y= [x**2 for x in squares_x]
# plt.plot(squares_x,squares_y,'b-s')

#draw gride line
plt.grid(color = 'black',linestyle = '-',linewidth = 1)

#draw dots
# plt.scatter(squares_x,squares_y,s=30)
# plt.scatter(squares_x,squares_y,c= 'red',edgecolor = 'none',s=30)
# plt.scatter(squares_x,squares_y,c= (0,0,0.8),edgecolor = 'none',s=30)
plt.scatter(squares_x,squares_y,c= squares_y,cmap = plt.cm.Blues,edgecolor = 'none',s=30)

plt.title("Squares Number",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Squares of Value",fontsize = 14)
plt.tick_params(axis='both',which = 'major',labelsize = 14)

#set line ranges
plt.axis([0,110,0,11000])
# plt.axis([0,10,0,200])

plt.show()
# plt.savefig('squares_plot.png',bbox_inches = 'tight')