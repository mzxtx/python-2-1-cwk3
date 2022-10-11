import csv
import matplotlib.pyplot as plt
import numpy as np

def generate_summary_for_web(csvfile, html_title, html_filename, show_barchart_gender=True):
    hd = ["Attributes", "Positive-yes", "Positive-no", "Negative-Yes", "Negative-No"]
    da = [hd]
    dia_data = []

    with open(csvfile) as c:
        cr = csv.reader(c)
        for r in cr:
            dia_data.append(r)

    dia_data = np.array(dia_data)
    dia_b = np.transpose(dia_data)
    new_len = len(dia_b) - 3

    for i in range(new_len):
        la = dia_b[-1].tolist()
        d1 = dia_b[i + 2].tolist()
        pno = 0
        nye = 0
        pye = 0
        nno = 0
        for l1 in range(len(d1)):
            if la[l1] == 'Negative':
                if d1[l1] == 'No':
                    nno += 1
                else:
                    if d1[l1] == 'Yes':
                        nye += 1
            else:
                if d1[l1] == 'No':
                    pno += 1
                else:
                    if d1[l1] == 'Yes':
                        pye += 1
        res = [d1[0], str(pye), str(pno), str(nye), str(nno)]
        da.append(res)
    print(da)
    h2 = open('result.csv', 'w', newline='')
    w1 = csv.writer(h2)
    for i in da:
        w1.writerow(i)
    h2.close()
    if show_barchart_gender is True:
        for n in range(new_len):
            la = dia_b[-1].tolist()
            n1 = dia_b[n + 1].tolist()
            pf = 0
            nm = 0
            pm = 0
            nf = 0
            for l1 in range(len(n1)):
                if la[l1] == 'Negative':
                    if n1[l1] == 'Female':
                        nf += 1
                    else:
                        if n1[l1] == 'Male':
                            nm += 1
                else:
                    if n1[l1] == 'Female':
                        pf += 1
                    else:
                        if n1[l1] == 'Male':
                            pm += 1
            res = [str(pm), str(pf), str(nm), str(nf)]
            wd = 0.35
            da.append(res)
            y = [pm, nm]
            x = np.arange(2)
            y1 = [pf, nf]
            tl = ["Positive", "Negative"]
            plt.bar(x + wd, y1, wd, color="b", align="center", label="Female", alpha=0.5)
            plt.bar(x, y, wd, align="center", color="c", label="Male", alpha=0.5)
            plt.ylabel("Gender")
            plt.xlabel("class")
            plt.xticks(x + wd / 2, tl)
            plt.title('Gender of Positive vs Negative case')
            plt.legend(["Male", "Female"], loc="upper right")
            plt.savefig("a.png")

    with open(html_filename, "w") as html:
        html.write("<html>\n")
        html.write("<head>\n")
        html.write("<meta charset=\"UTF-8\">\n")
        html.write("<style>\n")
        html.write("table, th, td {\n")
        html.write("border: 1px solid black;\n")
        html.write("border-collapse: collapse;\n")
        html.write("}\n")
        html.write("</style>\n")
        html.write("<title>"+html_title+"</title>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write("<table id=tab cellpadding=1 cellspacing=1 border=1>\n")

        with open('result.csv', "r") as f:
            f.readline()
            html.write("<tr>\n")
            html.write("<th rowspan=3> Attributes</th>\n")
            html.write("<th colspan=4> Class</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th colspan=2> Positive</th>\n")
            html.write("<th colspan=2> Negative</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th> Yes</th>\n")
            html.write("<th> No</th>\n")
            html.write("<th> Yes</th>\n")
            html.write("<th> No</th>\n")
            html.write("</tr>\n")

            r2 = csv.reader(f)

            for r in r2:
                html.write("<tr>\n")
                for m2 in r:
                    html.write("<td>"+m2+"</td>\n")
                html.write("</tr>\n")

        html.write("</table>\n")
        html.write("<img src='a.png'>\n")
        html.write("</body>\n")
        html.write("</html>\n")
generate_summary_for_web('diabetes_data.csv', 'htm', 'html.html', show_barchart_gender=True)