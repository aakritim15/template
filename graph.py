
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():

	
	labels = [
		'0-10',
		'10-20',
		'20-30',
		'30-40',
		'40-50',
		'50-60',
		'60-70',
		'70-80',
		'80-90',
		'90-100'
	]

	data = [0, 10, 15, 8, 22, 18, 25, 45, 60, 30]

	
	return render_template(
		template_name_or_list='graph.html',
		data=data,
		labels=labels,
	)



if __name__ == '__main__':
	
	app.run(debug=True)
