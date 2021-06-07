from numpy import median
import random
import plotly_express as px
import plotly.figure_factory as ff
import statistics 

count = [] 
dice_result = []
for i in range(0, 1000) :
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)
    count.append(i)
"""
#fig = ff.create_distplot([dice_result], ["Result"], show_hist=False)  
#fig.show() 

#print(mean) 
#median = statistics.median(dice_result)
#print(median)
#mode = statistics.mode(dice_result)
#print(mode)  
"""
mean = statistics.mean(dice_result) 
std_dev = statistics.stdev(dice_result)
print("The standard deviation of the data is : ",std_dev) 
first_stdev_start, first_stdev_end = mean - std_dev, mean + std_dev
second_stdev_start, second_stdev_end = mean - (2*std_dev), mean + (2*std_dev)
third_stdev_start, third_stdev_end = mean - (3*std_dev), mean + (3*std_dev) 

list_within_first_stdev = [result for result in dice_result if result > first_stdev_start and result < first_stdev_end]
list_within_second_stdev = [result for result in dice_result if result > second_stdev_start and result < second_stdev_end]
list_within_third_stdev = [result for result in dice_result if result > third_stdev_start and result < third_stdev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_within_first_stdev)*100.0/len(dice_result))) 
print("{}% of data lies within 2 standard deviation".format(len(list_within_second_stdev)*100.0/len(dice_result))) 
print("{}% of data lies within 3 standard deviation".format(len(list_within_third_stdev)*100.0/len(dice_result))) 