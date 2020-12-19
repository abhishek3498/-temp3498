from flask import Flask, request, render_template
import pandas as pd
df = pd.read_excel("new.xlsx")
df1 = df['name']
df2 = df['price']
df3 = df['cost']
d =[]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')




@app.route('/predict', methods=['POST'])
def predict():
    for x in request.form.values():
    	print(x)
    return render_template('index.html')







@app.route('/dropdown', methods=['POST'])
def dropdown():
	if(request.method=='POST'):
		name = request.form.get('cars')

		c=0

		for i in df1:
			if i == name:
				d.append([df2[c],df3[c]])
			c += 1

		return render_template('index.html',prediction_text1=d[0][0],prediction=d[0][1])


app.run(debug=True)