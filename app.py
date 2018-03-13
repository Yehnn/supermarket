from flask import Flask,render_template
from flask import request,make_response

app=Flask(__name__)

app.config.update({
    'SECRET_KEY':'a random string'
    })

@app.route('/')
def index():
    username=request.cookies.get('username')
    return render_template('index.html',username=username)

@app.route('/user/<username>')
def user_index(username):
    resp=make_response(render_template('user_index.html',username=username))
    resp.set_cookie('username',username)
    return resp

@app.route('/product/<int:product_id>')
def product_index(product_id):
    return render_template('product.html',product_id=product_id)


if __name__=='__main__':
    app.run()
