from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
#Pre Test
@app.route("/pretest")
def pretest():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSf4xuCCLBd29LkQQX-6Ny-xXl_SoD5SoWOuXxwS4YQXC4qaFA/viewform")
#Week 1 Day 3
@app.route("/khan")
def khan():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:rational-functions/e/linear_equations_4")
@app.route("/khan1")
def khan1():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:rational-functions/e/linear_equations_4")
@app.route("/khan2")
def khan2():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:rational-functions/e/solving_rational_equations_2")
@app.route("/khan3")
def khan3():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:rational-functions/e/rational-equations-3")
@app.route("/khan4")
def khan4():
    return redirect("https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:exp-model/x2ec2f6f830c9fb89:interpret-exp/a/exponential-models-faq")
#Week 1 Day 4
@app.route("/khan5")
def khan5():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:rational-functions/e/graphs-of-rational-functions")
@app.route("/khan6")
def khan6():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:rational-functions/v/discontinuities-of-rational-functions")
@app.route("/khan7")
def khan7():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:rational-functions/e/points-of-discontinuity-of-rational-functions")
@app.route("/khan8")
def khan8():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:rational-functions/v/analyzing-vertical-asymptotes-of-rational-functions")
@app.route("/khan9")
def khan9():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/exponential-growth-functions")
#Week 2 Day 1
@app.route("/khan10")
def khan10():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/exponential-growth-functions")
@app.route("/khan11")
def khan11():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/linear-exponential-models")
@app.route("/khan12")
def khan12():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/understanding-linear-and-exponential-models")
#Week 2 Day 2
@app.route("/khan13")
def khan13():
    return redirect("https://www.khanacademy.org/math/als-k-to-12-math/x54b4346ef80b5dcc:performance-standard-e/x54b4346ef80b5dcc:polynomials/e/evaluating-expressions-3")
@app.route("/khan14")
def khan14():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/exponential-expressions-word-problems-numerical")
@app.route("/khan15")
def khan15():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/exponential-expressions-word-problems")
@app.route("/khan16")
def khan16():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/exponential-expressions-word-problems-algebraic")
@app.route("/khan17")
def khan17():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/exponential-expressions-word-problems-algebraic")
#Week 2 Day 3
@app.route("/khan18")
def khan18():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/interpreting-exponential-expression-word-problem")
@app.route("/khan19")
def khan19():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/interpret-exponential-expressions-word-problems")
@app.route("/khan20")
def khan20():
    return redirect("https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:exp-model/x2ec2f6f830c9fb89:exp-change/e/modeling-with-exponential-functions")
@app.route("/khan21")
def khan21():
    return redirect("https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:exp-model/x2ec2f6f830c9fb89:exp-change/e/rewriting-and-interpreting-exponential-functions")
#Week 3 Day 1
@app.route("/khan22")
def khan22():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/constructing-exponential-models")
@app.route("/khan23")
def khan23():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/constructing-exponential-models-percent-change")
@app.route("/khan24")
def khan24():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/construct-exponential-models-according-to-rate-of-change")
#Week 3 Day 2
@app.route("/khan25")
def khan25():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/sat-math-p1-easier")
@app.route("/khan26")
def khan26():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/determine-and-represent-domain-and-range-of-exponential-functions-inequalities")
@app.route("/khan27")
def khan27():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/writing-functions-exponential-decay")
@app.route("/khan28")
def khan28():    
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/writing-functions-with-exponential-decay")
#Week 3 Day 3
@app.route("/khan29")
def khan29():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/initial-value-and-common-ratio-of-exponential-functions")
@app.route("/khan30")
def khan30():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/solving-for-a-fractional-exponent")
@app.route("/khan31")
def khan31():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/solving-exponential-equations-with-exponent-properties")
@app.route("/khan32")
def khan32():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/solve-exponential-equations-using-properties-of-exponents--basic-")
#Week 4 Day 1
@app.route("/khan33")
def khan33():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/solving-exponential-equations-with-exponent-properties-advanced")
@app.route("/khan34")
def khan34():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/solve-exponential-equations-using-properties-of-exponents-advanced")
@app.route("/khan35")
def khan35(): 
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/exponential-equations")
#Week 4 Day 2
@app.route("/khan36")
def khan36():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/writing-exponential-functions")
@app.route("/khan37")
def khan37():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/constructing-linear-and-exponential-functions-from-data")
@app.route("/khan38")
def khan38():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/construct-basic-exponential-functions-from-table-or-graph")
@app.route("/khan39")
def khan39():
    return redirect("https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:exp-model/x2ec2f6f830c9fb89:interpret-exp/e/interpret-rate-of-change-of-exponential-models-with-manipulation")
@app.route("/khan40")
def khan40():
    return redirect("https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:exp-model/x2ec2f6f830c9fb89:interpret-exp/e/interpret-rate-of-change-of-exponential-models-for-a-different-unit")
#Week 4 Day 3
@app.route("/khan41")
def khan41():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/constructing-linear-and-exponential-functions-from-graph")
@app.route("/khan42")
def khan42():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/analyzing-tables-of-exponential-functions")
#Week 5 Day 1
@app.route("/khan43")
def khan43():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/analyzing-graph-of-exponential-function")
@app.route("/khan44")
def khan44():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/analyzing-exponential-graph-with-negative-initial-value")
@app.route("/khan45")
def khan45():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/exponential-vs-linear-growth")
#Week 5 Day 2
@app.route("/khan46")
def khan46():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/a/warmup-exponential-vs-linear-growth")
@app.route("/khan47")
def khan47():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/exponential-vs-linear-growth")
#Week 5 Day 3
@app.route("/khan48")
def khan48():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/graphing-exponential-functions")
@app.route("/khan49")
def khan49():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/graphs-of-exponential-growth")
@app.route("/khan50")
def khan50():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/graphing-exponential-growth-intro")
@app.route("/khan51")
def khan51():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/v/exponential-decay-intro")
@app.route("/khan52")
def khan52():
    return redirect("https://www.khanacademy.org/math/senior-high-school-general-math/xc1934d16446a5789:unit-1/xc1934d16446a5789:exponential-functions/e/exponential-growth-vs-decay")
#Post Test
@app.route("/posttest")
def posttest():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSf-_kmnfeNS5ogEWVjR1a800gnOBaq8x_61bxYUESif1qpR5w/viewform")

if __name__ == "__main__":
    app.run()