import random
from flask import Flask, render_template

app = Flask(__name__)

textlist = [
        {'text':'Logic will get you from A to B. Imagination will take you everywhere.'},
        {'text':"There are 10 kinds of people. Those who know binary and those who don't."},
        {'text':"There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies."},
        {'text':"It's not that I'm so smart, it's just that I stay with problems longer."},
        {'text':"It is pitch dark. You are likely to be eaten by a grue."}
        ]


@app.route("/")
def template_test():
    dynamic_text = random.choice(textlist)
    return render_template('template.html', dynamic_text=dynamic_text['text'])


if __name__ == '__main__':
    app.run(debug=True)
