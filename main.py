from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def formPage():
    return render_template('page.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        tte = request.form['user2']
        tte2 = request.form['user3']
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https:pay.taipei/v2/CheckBill/Index/2")
        time.sleep(0.5)
        serc2 = driver.find_element("name", "parameter2")
        serc2.send_keys(tte2)
        time.sleep(0.5)
        serc3 = driver.find_element("xpath", '/html/body/article/main/form/div[3]/button')
        serc3.click()
        time.sleep(0.5)
        serc4 = driver.find_element("xpath", '/html/body/article/main/form/section/div[4]/button')
        serc4.click()
        time.sleep(0.5)
        serc12 = driver.find_element("xpath", '/html/body/article/main/form[1]/div[1]/div/span[2]')
        return redirect(url_for('success', name=user,serc6=tte,serc9=serc12.text))

@app.route('/success/<name>/<serc6>/<serc9>/')
def success(name,serc6,serc9):
    sst=int(serc9)
    return "<title>查詢網</title>"\
            f"<h2>{name}</h2>"\
           f"<h2>{serc6}</h2>"\
           f"<h2>{sst}元</h2>"\
           "<h2><input type='button' value='返回首頁' onclick='history.back()' style='width:90px;height:40px;'/></h2>"\

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
