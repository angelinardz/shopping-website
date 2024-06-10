
from flask import Flask,render_template

images=['https://legendary-space-train-977pj7qv9vgv2xq9v-5000.app.github.dev/static/dog1.png','https://legendary-space-train-977pj7qv9vgv2xq9v-5000.app.github.dev/static/dog2.jpg' ,
        'https://legendary-space-train-977pj7qv9vgv2xq9v-5000.app.github.dev/static/dog3.jpg' ]

app= Flask(__name__)
DOGS=[ 

    { 
    'id':1 ,
    'Breed': 'Dog 1' ,
    'Age': ' 4 months ',
    'image': images[0] ,
    'Price': 'XXXX',
    }
,
    {
        'id':2,
       'Breed': 'Dog 2' ,
        'Age': ' X',
        'image':images[1],
        'Price': 'XXXX',

    }
    ,
    {
        'id':3,
        'Breed': 'Dog 3' ,
        'Age': ' X',
        'title':'Dog 3',
        'image': images[2],
        'Price': '$8000',
    }
    ]

@app.route("/")
def hello_world():
    return render_template('home.html',dogs=DOGS,company_name='Xquisute')

if __name__== '__main__':
    app.run( '0.0.0.0', debug=True)

