from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('01.index.html')

@app.route('/menu', methods=['GET','POST'])
def menu():
    if request.method == 'GET':
        languages = [
            {'disp':'영어', 'val':'en'},
            {'disp':'일어', 'val':'jp'},
            {'disp':'중국어', 'val':'cn'},
            {'disp':'프랑스어', 'val':'fr'},
            {'disp':'스페인어', 'val':'es'}
        ]
        return render_template('02.Menu.html', options=languages)   # 서버에서 클라이언트로 정보 전달
    else:
        # 사용자가 입력한 정보를 서버가 읽음
        index = request.form['index']
        lang = request.form['lang']
        lyrics = request.form['lyrics']
        print(lang, '\n', index, '\n', lyrics, sep='')
        return render_template('03.Menu_res.html')

if __name__ == '__main__':
    app.run(debug=True)