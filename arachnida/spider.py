# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 14:55:52 by fcanadas          #+#    #+#              #
#    Updated: 2023/05/01 09:42:55 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, argparse, requests
from bs4 import BeautifulSoup

urls = set()
imgs = set()

def pargs():
    parser = argparse.ArgumentParser(description='Web Image Scrapper')
    parser.add_argument("URL")
    parser.add_argument("-r", action="store_true", help="Set the image search to recursive")
    parser.add_argument("-l", default=5, help="Set the recursion level (dependent of -r)")
    parser.add_argument("-p", default="./data", help="Set the directory path for downloaded images")
    
    return parser.parse_args()

def get_urls(main_url, cur_lv):
    try:
        response = requests.get(main_url, timeout=0.5)
        if (response.status_code == 200):
            url_soup = BeautifulSoup(response.content, "html.parser")
            all_url = url_soup.find_all("a")
            for each_url in all_url:
                url = each_url.get("href")
                if url not in urls:
                    urls.add(url)
                    if (cur_lv < rec_lv):
                        get_urls(url, cur_lv + 1)
    except:
        print('Web not accessible at the moment. Try again.')

def get_imgs(main_url):
    try:
        response = requests.get(main_url, timeout=0.5)
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        if (response.status_code == 200):
            url_soup = BeautifulSoup(response.content, "html.parser")
            all_imgs = url_soup.find_all("img")
            for each_img in all_imgs:
                img = each_img.get("src")
                if img not in imgs:
                    for extension in valid_extensions:
                        if (img.endswith(extension)):
                            imgs.add(img)
    except:
        print('Image not accessible')
def download_imgs(imgs):
    for img in imgs:
        try:
            img_name = img.split('/')[-1]
            rel_path = os.path.join(args.p, img_name)
            file_req = requests.get(img, allow_redirects=True)
            if not os.path.isfile(rel_path):
                print('Downloading: ', img_name)
                open(rel_path, 'wb').write(file_req.content)
            else:
                print('Already in directory')
        except:
            print('Image could not be downloaded')
            continue

def spider():
    try:
        if is_rec and rec_lv:
            print("Getting all URLs...")
            get_urls(main_url, 0)
        elif not is_rec:
            print("Getting all URLs...")    
            urls.add(main_url)
        else:
            print("No levels of depth means 0 pictures :(")
        print("Getting all images...")
        for url in urls:
            get_imgs(url)
        if not os.path.exists(args.p):
            os.makedirs(args.p)
        download_imgs(imgs)
    except:
        print('Something went wrong.')

if __name__=='__main__':
    global rec_lv, is_rec

    args = pargs()
    main_url = args.URL
    is_rec = args.r
    rec_lv = int(args.l)
    spider()

