from flask import Flask, render_template
from flask import request
from main import use_total, total, DB
app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route('/query', methods=['POST','GET'])
def index():
    use = use_total.use()
    all = total.get_all()
    #db = DB.conndb(use, all)
    #db.db_insert()
    return render_template('index.html', data=[use, all])
@app.route('/history', methods=['GET', 'POST'])
def history():
    #db = DB.conndb()
    #query_data = db.query_db() # 查询结果列表
    return render_template('history.html',data=['暂时关闭功能'])
if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0')
#root@cc:/home/web#uwsgi -s /tmp/webapp.sock --manage-script-name --mount /home/web=webapp:app --daemonize=True

