import requests
import re


# 获取每篇文章的url
def Get_url_list():
    s = 0
    url_list = []
    while True:
        url = f"https://3g.163.com/touch/reconstruct/article/list/BA8D4A3Rwangning/{s}-10.html"
        url_list.append(url)
        if len(Get_response(url)) == 0:
            break
        else:
            s = s + 10
    url_list = url_list[:-1]
    return url_list

# 用来判断
def Get_response(url):
    response = requests.get(url)
    txt = response.text
    return txt

# 获取源代码
def Get_html(url_list):
    html = ''
    for url in url_list:
        try:
            response = requests.get(url)
            html += response.text
        except:
            continue
    return html

# 清洗数据
def clean_html(html):
    title = []
    png_list = []
    title_list = re.findall('"title":"(.*?)","priority',html)
    for i in title_list:
        info = i.replace("\\", "")
        title.append(info)
    img_url_list = re.findall('"imgsrc":"(.*?)","ptime"',html)
    for i in img_url_list:
        i = re.findall(r'(http://cms-bucket.*?png|http://cms-bucket.*?jpeg)', i)
        png_list.append(i)
    for dict in zip(title, png_list):
        print(dict)

if __name__ == '__main__':
    url_list = Get_url_list()
    html = Get_html(url_list)
    clean_html(html)
