import matplotlib.pyplot as plt



def cumulative(l):

	a = []



	cnt = 1
	sum = 0
	for i in range(0,len(l)):
		sum = sum + l[i]
		a.append(sum/(cnt))
		cnt = cnt + 1


	return a


def xaxis(l):

	a = []

	for i in range(0,len(l)):
		a.append(i+1)


	return a










l1 = [0.78000000000000003, 0.94999999999999996, 0.93000000000000005, 0.96999999999999997, 1.0, 0.98999999999999999, 1.0, 1.0, 0.98999999999999999, 0.98999999999999999, 1.0, 1.0, 1.0, 0.98999999999999999, 0.97999999999999998, 1.0, 0.98999999999999999, 1.0]
l2 = [0.62, 0.89000000000000001, 0.93000000000000005, 0.97999999999999998, 0.98999999999999999, 0.92000000000000004, 1.0, 0.97999999999999998, 0.98999999999999999, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


l1 = cumulative(l1)
l2 = cumulative(l2)





plot1, = plt.plot(xaxis(l1),l1,'r--')
plot2, = plt.plot(xaxis(l2),l2,'r')

x1,x2,y1,y2 = plt.axis()

plt.axis((x1,x2,y1,y2))

plt.xlabel('time step')
plt.ylabel('accuracy')


plt.legend([plot1, plot2], ('GA-PA', 'Inc-PA'))

plt.show()


print('done')