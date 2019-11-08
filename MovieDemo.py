from bs4 import BeautifulSoup
import requests
import os


def get_html(web_url):
    header = {
        "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
    html = requests.get(url=web_url, headers=header).text
    Soup = BeautifulSoup(html, "lxml")
    data = Soup.find("ol").find_all("li")
    return data


def get_info(all_move):
    f = open("E:\\PythonDemo\\dianying.txt", "a")

    for info in all_move:
        #    排名
        nums = info.find('em')
        num = nums.get_text()
        print(num)
        #    名字
        names = info.find("span")
        name = names.get_text()
        print(name)
        #    导演
        charactors = info.find("p")
        charactor = charactors.get_text().replace(" ", "").replace("\n", "")
        charactor = charactor.replace("\xa0", "").replace("\xee", "").replace("\xf6", "").replace("\u0161", "").replace(
            "\xf4", "").replace("\xfb", "").replace("\u2027", "").replace("\xe5", "")
        print(charactor)
        #    评语
        remarks = info.find_all("span", {"class": "inq"})
        if remarks:
            remark = remarks[0].get_text().replace("\u22ef", "")
        else:
            remark = "此影片没有评价"
        print(remark)

        # 评分
        scores = info.find_all("span", {"class": "rating_num"})
        score = scores[0].get_text()
        print(score)

        f.write(num + '、')
        f.write(name + "\n")
        f.write(charactor + "\n")
        f.write(remark + "\n")
        f.write(score)
        f.write("\n\n")

    f.close()


if __name__ == "__main__":
    if os.path.exists("E:\\PythonDemo") == False:
        os.mkdir("E:\\PythonDemo")
    if os.path.exists("E:\\PythonDemo\\dianying.txt") == True:
        os.remove("E:\\PythonDemo\\dianying.txt")

    page = 0
    while page <= 225:
        web_url = "https://movie.douban.com/top250?start=%s&filter=" % page
        all_move = get_html(web_url)
        get_info(all_move)
        page += 25