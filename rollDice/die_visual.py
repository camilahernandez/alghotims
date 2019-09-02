from die import Die
import pygal
D6 = Die()
values = []
frequencies = []
labels = []
#Make some rools an store the results in a list

for i in range(1000):
    values.append(D6.roll())
print(values)

#freq of the side
for side in range(1,D6.num_sides+1):
    freq = values.count(side)
    frequencies.append(freq)
    labels.append(side)
print(frequencies)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results"
hist.x_labels = labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

