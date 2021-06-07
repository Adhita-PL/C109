import plotly.figure_factory as ff
import pandas as pd
import statistics

df = pd.read_csv("c108data.csv")
weight =  df["Weight(Pounds)"].tolist() 
height =  df["Height(Inches)"].tolist() 
#fig = ff.create_distplot([height], ["Weight"], show_hist=False) 
#fig.show() 
"""
mean = statistics.mean(weight)
print(mean)
median = statistics.median(weight)
print(median)
mode = statistics.mode(weight) 
print(mode)
"""
mean_wt = statistics.mean(weight)
mean_ht = statistics.mean(height)
std_dev_wt = statistics.stdev(weight)
std_dev_ht = statistics.stdev(height)

height_first_stdev_start, height_first_stdev_end = mean_ht - std_dev_ht, mean_ht + std_dev_ht
height_second_stdev_start, height_second_stdev_end = mean_ht - (2*std_dev_ht), mean_ht + (2*std_dev_ht)
height_third_stdev_start, height_third_stdev_end = mean_ht - (3*std_dev_ht), mean_ht + (3*std_dev_ht)

weight_first_stdev_start, weight_first_stdev_end = mean_wt - std_dev_wt, mean_wt + std_dev_wt
weight_second_stdev_start, weight_second_stdev_end = mean_wt - (2*std_dev_wt), mean_wt + (2*std_dev_wt)
weight_third_stdev_start, weight_third_stdev_end = mean_wt - (3*std_dev_wt), mean_wt + (3*std_dev_wt) 

height_list_within_first_stdev = [result for result in height if result > height_first_stdev_start and result < height_first_stdev_end]
height_list_within_second_stdev = [result for result in height if result > height_second_stdev_start and result < height_second_stdev_end]
height_list_within_third_stdev = [result for result in height if result > height_third_stdev_start and result < height_third_stdev_end]

weight_list_within_first_stdev = [result for result in weight if result > weight_first_stdev_start and result < weight_first_stdev_end]
weight_list_within_second_stdev = [result for result in weight if result > weight_second_stdev_start and result < weight_second_stdev_end]
weight_list_within_third_stdev = [result for result in weight if result > weight_third_stdev_start and result < weight_third_stdev_end] 

print("{}% of data lies within 1 standard deviation of height".format(len(height_list_within_first_stdev)*100.0/len(height))) 
print("{}% of data lies within 2 standard deviation of height".format(len(height_list_within_second_stdev)*100.0/len(height))) 
print("{}% of data lies within 3 standard deviation of height".format(len(height_list_within_third_stdev)*100.0/len(height))) 

print("{}% of data lies within 1 standard deviation of weight".format(len(weight_list_within_first_stdev)*100.0/len(weight))) 
print("{}% of data lies within 2 standard deviation of weight".format(len(weight_list_within_second_stdev)*100.0/len(weight))) 
print("{}% of data lies within 3 standard deviation of weight".format(len(weight_list_within_third_stdev)*100.0/len(weight))) 
