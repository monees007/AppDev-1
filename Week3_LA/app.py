import csv
import sys
import matplotlib.pyplot as plt
# from jinja2 import Template
from jinja2 import Template

data = list(csv.reader(open('data.csv'), delimiter=','))

wrong = """
<!DOCTYPE html>
<html>
  <body>
    <h1> Wrong Inputs </h1>
    <p> Something went wrong </p>
  </body>
</html>
"""
stud2 = """
<!DOCTYPE html>
<html>
    <body>
        <h1> Student Details </h1>
        <table border="1px">
            <tr>
                <th>
                  Student id_
                </th>
                <th>
                  Course id_
                </th>
                <th>
                  Marks id_
                </th>
              </tr>
              {% for i in range(len) %}
              <tr>
                <td>
                  {{ stud[i][0] }}
                </td>
                <td>
                  {{ stud[i][1] }}
                </td>
                <td>
                  {{ stud[i][2] }}
                </td>
              </tr>
              {% endfor %}
              <tr>
                <td colspan="2">
                  <center>
                    Total Marks
                  </center>
                </td>
                <td>
                  {{ total_ }}
                </td>
              </tr>
        </table>
    </body>
</html>
"""
crud2 = """
<!DOCTYPE html>
<html>
    <body>
        <h1> Course Details </h1>
        <table border="1px">
            <tr>
                <th>
                  Average Marks
                </th>
                <th>
                  Maximum Marks
                </th>
              </tr>
              
              <tr>
                <td>
                  {{ average }}
                </td>
                <td>
                  {{ max_ }}
                </td>
              </tr>
              
              
        </table>
        <img src="foo.png"/>
    </body>
</html>
"""


def student(id_):
    stud1 = []
    tot = 0
    for x in list(data)[1:]:
        # print(x)
        if x[0] == id_:
            tot += int(x[2])
            stud1.append(x)
    Template(stud2).stream(len=len(stud1), stud=stud1, total_=tot).dump('output.html')


def course(id_):
    total, count, max_ = 0, 0, 0
    freqdist = []
    # print(list(data[1:]))
    for x in list(data)[1:]:
        # print(x[1])
        if id_ in x[1]:
            total += int(x[2])
            count += 1
            if int(x[2]) > max_:
                max_ = int(x[2])
            freqdist += [int(x[2])]
    if count == 0:
        count = 1
    Template(crud2).stream(average=total / count, max_=max_).dump('output.html')
    plt.clf()
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    freqdist.sort()
    plt.hist(freqdist, bins=[20, 40, 60, 80, 100])
    plt.savefig('foo.png')


def err():
    Template(wrong).stream().dump('output.html')


f = 0
print(len(sys.argv))
if 3 != len(sys.argv):
    err()
else:
    id_ = sys.argv[2]
    # print(id_)
    if sys.argv[1] == '-s':
        for x in list(data)[1:]:
            if id_ and id_ == str(x[0]).strip():
                student(id_)
                f = 1

    elif sys.argv[1] == '-c':
        for x in list(data)[1:]:
            if id_ and id_ == str(x[1]).strip():
                course(id_)
                f = 1

if not f:
    err()
