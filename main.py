# Author: Snehith Raj Bada

import csv
from flask import Flask, render_template, request
import matplotlib.pyplot as pyplot
from numpy import vstack,array
from scipy.cluster.vq import kmeans,vq
import collections
import math
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Method to find clusters,total number of points, number of clusters centroid locations, distances for numeric values
@app.route('/cluster', methods=['POST', 'GET'])
def cluster():
   if request.method == 'POST':
       column1=str(request.form['col1'])
       column2=str(request.form['col2'])
       k = str(request.form['cluster'])
       k = int(k)
       dataset = []
       input = csv.reader(open('titanic3.csv', "r"), delimiter=",")
       headers = next(input)
       column1 = headers.index(column1)
       column2 = headers.index(column2)
       for row in input:
           value = []
           if row[column1] != '' and row[column2] != '':
               value.append(float(row[column1]))
               value.append(float(row[column2]))
               dataset.append(value)
       data = vstack(dataset)
       result1=[]
       result2=[]
       result3=[]
       centroids, distortion = kmeans(data, k)
       print(centroids)
       result1.append(centroids)
       distance=[]
       for i in range(1,len(centroids)+1):
           for j in range(i+1,len(centroids)+1):
               print(i,j)
               dvalue = []
               a=centroids[i-1]
               b=centroids[j-1]
               print(a,b)
               dvalue.append(str(i) +"-"+ str(j))
               print(dvalue)
               dist=math.sqrt(abs(((a[0]-a[1])**2)-((b[0]-b[1])**2)))
               print(dist)
               dvalue.append(dist)
               distance.append(dvalue)
       print(distance)
       result2.append(distance)
       indexdata, distance = vq(data, centroids)
       label=collections.Counter(indexdata)
       print(label)
       labels = [(k, v) for k, v in label.items()]
       result3.append(labels)
       mark = ['o']

       for i in range(0, k):
           pyplot.plot(data[indexdata == i, 0], data[indexdata == i, 1], marker=mark[0], ls='none')
       pyplot.plot(centroids[:, 0], centroids[:, 1], 'sm', markersize=8)

       pyplot.savefig('output1.png')
       return render_template('result1.html',msg1=result1,msg2=result2,msg3=result3)

# MEthod to find clusters,total number of points, number of clusters centroid locations, distances for mixed values (Eg:Cabin)
@app.route('/clusterchar', methods=['POST', 'GET'])
def cluster_char():
   if request.method == 'POST':
       column1='age'
       column2='cabin'
       k = str(request.form['cluster'])
       k = int(k)
       dataset = []
       input = csv.reader(open('titanic3.csv', "r"), delimiter=",")
       headers = next(input)
       column1 = headers.index(column1)
       column2 = headers.index(column2)
       for row in input:
           value = []
           if row[column1] != '' and row[column2] != '':
               value.append(float(row[column1]))
               l=list(row[column2])
               #print(l)
               z=0
               for item in l:
                   #print(ord(item))
                   z = z + ord(item)
               #print(z)
               value.append(float(z))
               dataset.append(value)
       data = vstack(dataset)
       result1=[]
       result2=[]
       result3=[]
       centroids, distortion = kmeans(data, k)
       print(centroids)
       result1.append(centroids)
       distance=[]
       for i in range(1,len(centroids)+1):
           for j in range(i+1,len(centroids)+1):
               print(i,j)
               dvalue = []
               a=centroids[i-1]
               b=centroids[j-1]
               print(a,b)
               dvalue.append(str(i) +"-"+ str(j))
               print(dvalue)
               dist=math.sqrt(abs(((a[0]-a[1])**2)-((b[0]-b[1])**2)))
               print(dist)
               dvalue.append(dist)
               distance.append(dvalue)
       print(distance)
       result2.append(distance)
       indexdata, distance = vq(data, centroids)
       label=collections.Counter(indexdata)
       print(label)
       labels=[(k, v) for k, v in label.items()]
       print(labels)
       result3.append(labels)
       mark = ['o']

       for i in range(0, k):
           pyplot.plot(data[indexdata == i, 0], data[indexdata == i, 1], marker=mark[0], ls='none')
       pyplot.plot(centroids[:, 0], centroids[:, 1], 'sm', markersize=8)

       pyplot.savefig('output2.png')
       print (result1,result2,result3)
       return render_template('result1.html', msg1=result1, msg2=result2, msg3=result3)



if __name__ == '__main__':
    app.run(debug = True)