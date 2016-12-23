from flask import Flask,render_template,request,redirect

app = Flask(__name__)
file1=open("lists.txt","a")
@app.route('/',methods=['GET'])
def handle_root():
	return render_template('form.html')
	

@app.route('/responses',methods=['POST'])
def handle_data():
	l=''
	l+=request.form['roll_number']+','
	l+=request.form['rad1']
	l+=request.form['rad2']
	l+=request.form['rad5']
	l+=request.form['rad4']         #questions arranged in order of priority
	l+=request.form['rad3']
	file1.write(l)
	file1.write('\n')
	return redirect("http://localhost:8000/answer")

@app.route('/answer',methods=['GET'])
def handle_root1():
	diff=30000
	file1=open("lists.txt","r")
	# print file1.readlines()[0].split(',')[1]
	lines = file1.readlines()
	a=int(lines[0].split(',')[1])
	l=lines[0]
	for line in lines:
		b=int(line.split(',')[1])
		if abs(b-a)<diff:
			if abs(b-a)!=0:
				diff=abs(b-a)
				l=line
	rn=l.split(',')[0]
	return"""<html>
			<head> </head>
			<body><H1>Your Suitable Roommate is: """+str(rn)


app.run(debug=True, port=8000)