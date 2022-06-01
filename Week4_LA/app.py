from flask import Flask, render_template, request
from jinja2 import Template
import matplotlib

# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

app = Flask(__name__)
data = csv.reader(open('data.csv'), delimiter=',')
data = list(data)[1:]


@app.route('/')
def index():
    return render_template('index.html')


def plot(freqdist):
    plt.clf()
    # fig, ax = plt.subplots(figsize=(10, 5))
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    # print(freqdist)
    freqdist.sort()

    plt.hist(freqdist, bins=[20,40,60,80,100])

    plt.savefig('static/foo.png')


@app.route('/', methods=['POST'])
def s():
    if request.method == 'POST':
        id = str(request.form['id_value'])
        # print(id)
        flag = 0
        for x in data:
            if str(id) in x[0] and request.form.get('ID', None) == 'student_id':
                flag = 1

            if str(id) in x[1] and request.form.get('ID', None) == 'course_id':
                flag = 1

        if flag == 0:
            return render_template('wrong.html')
        if (request.form.get('ID', None)) == 'student_id':
            # print(11)
            stud1 = []
            tot = 0
            for x in data:
                # print(x)
                if id in x[0]:
                    tot += int(x[2])
                    stud1.append(x)
            # Template(stud2).stream(len=len(stud1), stud=stud1, total_=tot).dump('templates/output.html')
            # print(stud1,22)
            return render_template('stud.html', len=len(stud1), stud=stud1, total_=tot)
        elif (request.form.get('ID', None)) == 'course_id':
            total, count, max = 0, 0, 0
            freq = []
            for x in data:
                # print(x)
                if id in x[1]:
                    total += int(x[2])
                    count += 1
                    if int(x[2]) > max:
                        max = int(x[2])
                    freq.append(int(x[2]))
                    # print(total,count,max)


            # Template(crud2).stream(average=total / count, max=max).dump('output.html')

            # print(freqdist)
            plot(freq)
            return render_template('crud.html', average=total / count, max=max)


if __name__ == '__main__':
    app.run()
