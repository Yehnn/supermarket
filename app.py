from flask import Flask,render_template
from flask import request,make_response

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

app.config.update({
    'SECRET_KEY':'a random string'
    })



            
user={
            'id': 1,
            'uname': 'tom',
            'tel': '1841111111',
            'addr': 'tianfu',
            'time': '2018-3-26',
            'pay': 'weixin'
            }
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
    product={
            'id': 1,
            'pname': 'maidong',
            'price': 2.0,
            'stock': 5,
            'time': '2018-3-26',
            'category': 'water',
            'tags': ['water','summer','engine']
            }
    return render_template('product.html',product_id=product_id,product=product)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/login')
def login():
    return render_template('login.html')


if __name__=='__main__':
    app.run()
