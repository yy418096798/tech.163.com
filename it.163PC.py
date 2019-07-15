import requests
from lxml import etree


def get_img(url):
    r = requests.get(url)
    tree = etree.HTML(r.text)
    src_list = tree.xpath('//*[@id="news-flow-content"]/li/div[2]/a/img/@src')
    return src_list

def get_title(url):
    r = requests.get(url)
    tree = etree.HTML(r.text)
    title_list = tree.xpath('//*[@id="news-flow-content"]/li/div/h3/a/text()')
    return title_list

def get_url(i):
    if i ==1:
        url = "http://tech.163.com/gd/"
    elif i < 10:
        url = f"http://tech.163.com/special/gd2016_0{i}/"
    else:
        url = f"http://tech.163.com/special/gd2016_{i}/"
    return url

def main():
    a = 0
    title = []
    img = []
    for i in range(1,21):
        url = get_url(i)
        title_list = get_title(url)
        img_list = get_img(url)
        title += title_list
        img += img_list
    # 查找发现“风向标—中国创新”没有图片
    img.insert(257, "无图片")
    for dic in zip(title, img):
        print(dic)

if __name__ == '__main__':
    main()