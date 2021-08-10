import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("studentMarks.csv")
data_file = pd.read_csv("data3.csv")

student_marks = df["Math_score"].tolist()
data = data_file["Math_score"].tolist()

mean_of_the_sample = statistics.mean(data)
mean = statistics.mean(student_marks)
standard_deviation = statistics.stdev(student_marks)

def random_set_of_mean(counter):
    data_set = []
    for i in range(counter):
        randomIndex = random.randint(0, len(student_marks)-1)
        value = student_marks[randomIndex]
        data_set.append(value)
    mean_of_dataset = statistics.mean(data_set)
    return mean_of_dataset

sampling_mean_list = []

for i in range(1000):
    sampling_mean = random_set_of_mean(100)
    sampling_mean_list.append(sampling_mean)

samplingMean = statistics.mean(sampling_mean_list)
sampling_standard_deviation = statistics.stdev(sampling_mean_list)

first_standard_deviation_start, first_standard_deviation_end = samplingMean - sampling_standard_deviation, samplingMean + sampling_standard_deviation
second_standard_deviation_start, second_standard_deviation_end = samplingMean - (2*sampling_standard_deviation), samplingMean + (2*sampling_standard_deviation)
third_standard_deviation_start, third_standard_deviation_end = samplingMean - (3*sampling_standard_deviation), samplingMean + (3*sampling_standard_deviation)

sampling_fig = ff.create_distplot([sampling_mean_list], ["Student Marks"], show_hist = False)
sampling_fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.20], mode = "lines", name = "Mean"))
sampling_fig.add_trace(go.Scatter(x = [first_standard_deviation_start, first_standard_deviation_start],y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 Start"))
sampling_fig.add_trace(go.Scatter(x = [first_standard_deviation_end, first_standard_deviation_end],y = [0, 0.17], mode = "lines", name = "Standard Deviation 1 End"))
sampling_fig.add_trace(go.Scatter(x = [second_standard_deviation_start, second_standard_deviation_start],y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 Start"))
sampling_fig.add_trace(go.Scatter(x = [second_standard_deviation_end, second_standard_deviation_end],y = [0, 0.17], mode = "lines", name = "Standard Deviation 2 End"))
sampling_fig.add_trace(go.Scatter(x = [third_standard_deviation_start, third_standard_deviation_start],y = [0, 0.17], mode = "lines", name = "Standard Deviation 3 Start"))
sampling_fig.add_trace(go.Scatter(x = [third_standard_deviation_end, third_standard_deviation_end],y = [0, 0.17], mode = "lines", name = "Standard Deviation 3 End"))
sampling_fig.add_trace(go.Scatter(x = [mean_of_the_sample, mean_of_the_sample], y = [0, 0.17], mode = "lines", name = "Mean of the Sample"))
sampling_fig.show()
# fig = ff.create_distplot([student_marks], ["Maths Score"], show_hist = False)
# fig.show()

print("Mean of the Scores of Students in Maths is {}".format(mean))
print("Standard Deviation is {}".format(standard_deviation))
print("Sampling Mean of the population is {}".format(samplingMean))
print("Standard Deviation of the sampling mean is {}".format(sampling_standard_deviation))