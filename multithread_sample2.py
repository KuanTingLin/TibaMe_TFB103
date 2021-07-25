from util.jieba_test import paddle_cut, correct_cut, full_cut
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import time

def get_title_with_href(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    print(soup.select("a"))


def main():
    # datas = ["NIKON D780 單機身 公司貨",
    #          "3M 瞬涼5度抑螨可水洗烘乾涼夏兩用被-星空藍(180x210cm)",
    #          "【madd capp】I AM 拼圖 我是小熊貓 - 100 系列 極限逼真動物 不規則切邊 適合多人挑戰"]
    start = time.time()
    uri = "https://www.ptt.cc/bbs/CFantasy/index{}.html"
    with ThreadPoolExecutor(max_workers=30) as executor:
        for page in range(2000, 3300):
            executor.map(get_title_with_href, (uri.format(page),))
            # get_title_with_href(uri.format(page))
    end = time.time()
    print("time costed: ", end - start)


    # with ThreadPoolExecutor(max_workers=10) as executor:
        # for data in datas:
        #     executor.map(lambda x: print(correct_cut(x)), (data,))
            # print(data)


if __name__ == "__main__":
    main()



