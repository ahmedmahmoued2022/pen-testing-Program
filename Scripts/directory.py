import sys
from sys import platform
import requests
import os
import threading
import concurrent.futures


def brute_force(Url, v, name):
    if platform == "linux" or platform == "linux2":
        urls = open(fr"Results_{Url.replace(':', '')}/urls_{name}.txt", 'a')
    else:
        urls = open(fr"Results_{Url.replace(':', '')}\urls_{name}.txt", 'a')
    try:
        url_subdomain = (Url+v).strip()
        req = requests.get(url_subdomain)
        if req.status_code == 200:
            print("200 ok :" + url_subdomain)
            urls.write(url_subdomain + "\n")
            urls.close()
        else:
            print(f"{req.status_code}  {url_subdomain}")
    except:
        pass


def check_brute_force(type_brute_force: list, Url: str, name):
    try:
     os.makedirs(fr"Results_{Url.replace(':', '')}", exist_ok=True)
    except:
        pass
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for i, v in enumerate(type_brute_force):
            executor.submit(brute_force, Url,  v, name)


def choose_list(n: int) -> list:
    search_type = list()
    name_type = None
    if n == 1:
        search_type = open("Dirctories.txt", 'r').readlines()
        name_type = "Directories"
    elif n == 2:
        search_type = open("PHP.txt", 'r').readlines()
        name_type = "PHP"
    elif n == 3:
        search_type = open("js.txt", 'r').readlines()
        name_type = "JS"
    elif n == 4:
        search_type = open("asp.txt", 'r').readlines()
        name_type = "ASP.net"
    elif n == 5:
        search_type = open("HTML.txt", 'r').readlines()
        name_type = "HTML"
    elif n == 6:
        search_type = open("XML.txt", 'r').readlines()
        name_type = "XML"
    elif n == 7:
        # there is work ask where to get path you to brute force
        path = input("Enter your path:")
        search_type = open(path, 'r').readlines()
        name_type = "SELF"
    else:
        print("error")

    return search_type, name_type


def proccess():
    url = input("Enter target url Example https://target.com: ")  # first put in lineEdit
    print("""
          Choose brute force wordlist:
            1-Directories wordlist
            2-Php files wordlist
            3-JS files wordlist
            4-Asp.net files wordlist
            5-HTML files wordlist
            6-XML files wordlist
            7-Self wordlist
        
         """)  # Combo box
    num = input("Enter :")
    print(num)
    choose, name = choose_list(int(num))  # choose file to brute force on it.
    check_brute_force(choose, url, name)


if __name__ == '__main__':
    proccess()
