import selenium
import random
from bs4 import BeautifulSoup as Bs
from time import sleep
from selenium import webdriver
import csv
import datetime as dt
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


#binary = FirefoxBinary("C:/User/user/Mozilla Firefox/firefox.exe")
#browser = webdriver.Firefox(firefox_binary=binary)
#browser = webdriver.Firefox(executable_path="C:/Mozilla Firefox/firefox.exe")
browser = webdriver.Firefox()
browser.implicitly_wait(10)


class Bot:


    def __init__(self):
        # browser.maximize_window()
        return browser


    def InstagramBot():

        browser.get('https://www.instagram.com/')
        sleep(5)
        try:
            username_input = browser.find_element_by_css_selector("input[name='username']")

            password_input = browser.find_element_by_css_selector("input[name='password']")


            username_input.send_keys("07082109611")
            sleep(3)

            password_input.send_keys("Joseph247$")

            sleep(3)

            try:
                login_link = browser.find_element_by_xpath("//button[@type='submit']")

                login_link.click()

                sleep(10)

            except:
                print("Connection Error")

        except:
            pass
        thumb = []
        count = 0
        hashtags = open("searchs.txt",'r')
        #iterate through the objects
        for tags in hashtags:

            if tags.startswith("#"):
                tags= tags.replace("#","/")

                #search for the tags
                browser.get(f'https://www.instagram.com/explore/tags{tags}/')   
                
                sleep(5)
                top_thumbnail_result =  browser.find_elements_by_css_selector('[class="v1Nh3 kIKUG  _bz0w"]')
                #loop through the list of thumbnails
                for content in top_thumbnail_result:
                    # sleep(5)
                    thum =content.find_elements_by_tag_name("a")

                    #Gathered all the links in the thumbnail in a list
                    for i in thum:                      
                        thumb.append(i.get_attribute('href'))
                        

                for x in thumb:
                                    
                        # x.click()
                    browser.get(x)
                    sleep(5)
                                
                            
                    follow = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button")
                    username_followed = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a").text
                                
                    usr =[]
                    with open('follow.csv','r+') as csvfile:
                        read = csv.reader(csvfile)
                        for line in read:
                            if username_followed not in line:
                                usr.append(username_followed)
                                append = csv.writer(csvfile)
                                append.writerow(usr)
                                    
                    if follow.text =="Follow":
                        follow.click()
                                
                        sleep(5)
                                    
                    else:
                        pass

                        sleep(2)

                    like = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
                    sleep(5)

                                # comments_box
                    try:
                        com = open("comment.txt",'r')
                        comment_symbol=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button").click()
                                # try:
                        comment = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                            # browser.find_element_by_css_selector(".Ypffh")
                        for i in com:
                            comment.send_keys(i)
                            sleep(5)
                                    #Post comment
                            browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").click()
                            sleep(5)
                                    
                        sleep(5)
                    except:
                        pass            
                                #trying if it is possible to message
                
                    click_username_message = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a")
                    click_username_message.click()
                    
                    sleep(5)
                    message_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
                    message_button.click()
                    sleep(5)
                    try:
                        browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    except:
                        pass
                    sleep(5)
                    mess = open("message.txt",'r')
                    text_box_selected = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                    # text_box_selected.click()
                    sleep(5)
                    for b in mess:
                        text_box_selected.send_keys(b)
                        sleep(5)
                        send_message = browser.find_elements_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div")
        
                        sleep(5)
                    sleep(15)
                # except:
                #     pass

                    
               
            elif tags.startswith("@"):
                tags= tags.replace("#","/")
                browser.get(f'https://www.instagram.com{tags}/')
                try:
                    message_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
                    message_button.click()
                    sleep(5)
                    try:
                        browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    except:
                        pass
                    sleep(5)
                    mess = open("message.txt",'r')
                    text_box_selected = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                    # text_box_selected.click()
                    sleep(5)
                    for b in mess:
                        text_box_selected.send_keys(b)
                        sleep(5)
                        send_message = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                        sleep(5)
                    sleep(5)
                except:
                    pass
                sleep(5)
                top_thumbnail_result =  browser.find_elements_by_css_selector('[class="v1Nh3 kIKUG  _bz0w"]')
                for content in top_thumbnail_result:
                    
                    content.click()
                    sleep(10)

                    follow = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
                    username_followed = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").text
                    

                    usr =[]
                    with open('follow.csv','r+') as csvfile:
                        read = csv.reader(csvfile)
                        for line in read:
                            if username_followed not in line:
                                usr.append(username_followed)
                                append = csv.writer(csvfile)
                                append.writerow(usr)
                    if follow.text =="Follow":
                        follow.click()
                        # print(follow.text)
                        sleep(5)
                       
                    else:
                        pass

                        sleep(2)

                    like = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
                    sleep(5)
                    com = open("comment.txt",'r')
                    comment_symbol=browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button").click()
                    try:
                        browser.find_element_by_css_selector(".Ypffh")
                        for i in com:
                            comment.send_keys(i)
                            sleep(5)

                            send_comments = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()
                            sleep(5)
                        # browser.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
                        # sleep(2)
                    except:
                        pass

                    click_username_message = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a")
                    click_username_message.click()
                    
                    sleep(5)
                    message_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
                    message_button.click()
                    sleep(5)
                    try:
                        browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    except:
                        pass
                    sleep(5)
                    mess = open("message.txt",'r')
                    text_box_selected = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                    # text_box_selected.click()
                    sleep(5)
                    for b in mess:
                        text_box_selected.send_keys(b)
                        sleep(5)
                        send_message = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                        sleep(5)
                    sleep(5)

                    
            
            else:
                browser.get(f'https://www.instagram.com/explore/locations/{tags}/')
                sleep(5)
                cities = browser.find_elements_by_css_selector('[class="aMwHK"]')
                for city in cities:
                    city.click()
                    sleep(5)
                    area = browser.find_elements_by_css_selector('[class="aMwHK"]')
                    for a in area:
                        a.click()
                        sleep(5)

                        top_thumbnail_result =  browser.find_elements_by_css_selector('[class="v1Nh3 kIKUG  _bz0w"]')
                        for content in top_thumbnail_result:
                            
                            content.click()
                            sleep(10)

                            follow = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
                            username_followed = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").text
                            

                            usr =[]
                            with open('follow.csv','r+') as csvfile:
                                read = csv.reader(csvfile)
                                for line in read:
                                    if username_followed not in line:
                                        usr.append(username_followed)
                                        append = csv.writer(csvfile)
                                        append.writerow(usr)


                            if follow.text =="Follow":
                                follow.click()
                                # print(follow.text)
                                sleep(5)
                                

                            else:
                                pass

                                sleep(2)

                            like = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
                            sleep(5)
                            # comments_box = 'nice one dude'
                            com = open("comment.txt",'r')
                            comment_symbol=browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button").click()
                            try:
                                browser.find_element_by_css_selector(".Ypffh")
                                for i in com:
                                    comment.send_keys(i)
                                    sleep(5)

                                    send_comments = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()
                                    sleep(5)
                                # browser.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
                                # sleep(2)
                            except:
                                pass

                            browser.get(f'https://www.instagram.com/{username_followed}/')
                            sleep(5)
                            click_username_message = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a")
                            click_username_message.click()
                    
                            sleep(5)
                            message_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
                            message_button.click()
                            sleep(5)
                            try:
                                browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                            except:
                                pass
                            sleep(5)
                            mess = open("message.txt",'r')
                            text_box_selected = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                            # text_box_selected.click()
                            sleep(5)
                            for b in mess:
                                text_box_selected.send_keys(b)
                                sleep(5)
                                send_message = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                                sleep(5)
                            sleep(5)                    




    def Block():
        browser.get('https://www.instagram.com/')
        sleep(5)
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys("07082109611")
        sleep(3)
        password_input.send_keys("Joseph247$")
        sleep(3)

        try:
            login_link = browser.find_element_by_xpath("//button[@type='submit']")

            login_link.click()

            sleep(5)

        except:
            print("Connection Error")

        sleep(3)
        Users = []
        DM = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]")
        print("Button Found")
        DM.click()
        print("processing DM")
        sleep(5)
        try:
            not_now = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
            not_now.click()
            sleep(2)
        except:
            pass

        sleep(5)
        All_DM = browser.find_elements_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div")
        
        for DM in All_DM :
            one_dm =DM.find_elements_by_tag_name("a")
            
            for dim in one_dm:
                Users.append(dim)

           
            sleep(2)

        for i in Users:
            WebDriverWait(browser,10)
            browser.execute_script("arguments[0].click();", i)
            
            
            print(Users)
            sleep(5)
        



    # def Block():
    
    #     browser.get('https://www.instagram.com/')
    #     sleep(5)
        
    #     try:
    #         username_input = browser.find_element_by_css_selector("input[name='username']")

    #         password_input = browser.find_element_by_css_selector("input[name='password']")


    #         username_input.send_keys("07082109611")
    #         sleep(3)

    #         password_input.send_keys("Joseph247$")

    #         sleep(3)

    #         try:
    #             login_link = browser.find_element_by_xpath("//button[@type='submit']")

    #             login_link.click()

    #             sleep(10)

    #         except:
    #             print("Connection Error")

    #     except:
    #         print("unable to connect")
    #         pass
        

    #     direct_message =[]
    #     try:
    #         Direct_message =browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]")
    #         Direct_message.click()
    #         sleep(5)
    #     except:
    #         print("unable to connect")
    #         pass
                   
    #     try:
    #         not_now = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
    #         not_now.click()
    #         sleep(5)
    #     except:
    #         pass
    #     sleep(5)  
    #             #loop through the list of thumbnails
    #     All_DM = browser.find_elements_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div")
    #     for content in All_DM:
    #         thum =content.find_elements_by_tag_name("a")

    #                     #Gathered all the links in the thumbnail in a list
    #         for i in thum:                      
    #             direct_message.append(i)
    #             sleep(2)

    #         sleep(2)
                            

    #     for x in direct_message:
    #         print(x)
    #         sleep(3)
    #         browser.execute_script("arguments[0].click();", x)
    #             #ActionChains(browser).move_to_element(x).click().perform()
                                        
    #             # x.click()
    #             #browser.get(x)
    #         sleep(2)
    #         message_time = browser.find_element_by_css_selector("div._7UhW9.PIoXz.MMzan._0PwGv.fDxYl").text
    #         print(message_time)

                     
                            
    #     # sleep(5)
    #     # Direct_message =browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]")
    #     # Direct_message.click()
    #     # sleep(5)
    #     # try:
    #     #     not_now = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
    #     #     not_now.click()
    #     #     sleep(5)
    #     # except:
    #     #     pass
    #     # sleep(5)
        
    #     # direct_message = []
    #     # All_DM = browser.find_elements_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div")
    #     # for message in All_DM:
    #     #     #links = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
    #     #     links =message.find_elements_by_tag_name("a")
    #     #     #WebDriverWait(browser,10)
    #     #     # print(mes)
    #     #     for i in links:
    #     #         direct_message.append(i)
    #     #         sleep(5)
            

    #     # for a in direct_message:
    #     #     a.click()
    #     #     sleep(5)
            

    #         # browser.execute_script("window.open('" + x +"');")
    #         # sleep(5)


    #         for elem in elems:
    #     print(elem)
    # elem.click()
    # driver.back() //to go back the previous page and continue over the links

            
            # try:
            #     browser.get(i)
            #     sleep(5)
            
            # except:
            #     pass
            # sleep(5)
        # sleep(5)
        # print(thing)
        #         sleep(5)
                
        # print(thing)
        # for x in thing:
        #     print(x)
        #     x.click()        
                            
        #     sleep(5)

























        #         thing.append(i.get_attribute('href'))
        #         # print(thing)                        
        #     # print(thing)
        # for x in thing:
           # #print(x)               
          #  #x.click()
            
            # browser.get(x)
            # sleep(10)
            # message_time = browser.find_element_by_css_selector("div._7UhW9.PIoXz.MMzan._0PwGv.fDxYl").text
            # print(message_time)
            #time /// html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.DT7qQ div.t30g8.L1C6I div.Igw0E.IwRSH.eGOV_._4EzTm div.oYYFH div.pV7Qt._6Rvw2.Igw0E.IwRSH.YBx95.ybXk5._4EzTm.i0EQd div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk div.uueGX div.JiVIq._0NM_B div.Igw0E.IwRSH.hLiUi.vwCYk div.frMpI.-sxBV div.VUU41 div.Igw0E.IwRSH.eGOV_._4EzTm
            #my mes/  html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.DT7qQ div.t30g8.L1C6I div.Igw0E.IwRSH.eGOV_._4EzTm div.oYYFH div.pV7Qt._6Rvw2.Igw0E.IwRSH.YBx95.ybXk5._4EzTm.i0EQd div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk div.uueGX div.JiVIq._0NM_B div.Igw0E.IwRSH.hLiUi.vwCYk div.frMpI.-sxBV div.VUU41 div.Igw0E.Xf6Yq.eGOV_.ybXk5._4EzTm
            #reciver  html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.DT7qQ div.t30g8.L1C6I div.Igw0E.IwRSH.eGOV_._4EzTm div.oYYFH div.pV7Qt._6Rvw2.Igw0E.IwRSH.YBx95.ybXk5._4EzTm.i0EQd div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk div.uueGX div.JiVIq._0NM_B div.Igw0E.IwRSH.hLiUi.vwCYk div.frMpI.-sxBV div.VUU41 div.Igw0E.Xf6Yq.eGOV_.ybXk5._4EzTm
        #     try:
        #         My_message = browser.find_element_by_css_selector('div.VdURK.e9_tN.JRTzd')
        #         try:
        #             Receivers_message = browser.find_element_by_css_selector('div.e9_tN.JRTzd')
        #         except:
        #             message_time = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/di/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div/divv/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div").text
        #             print(message_time)
        #             hour = dt.datetime.now().hour
        #             minute = dt.datetime.now().minute
        #             ("This account is ready to be blocked")

        #             #Messsage_area = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[4]")
        #             sleep(5)    

        #     except:
        #         pass

    def close():
        browser.quit()


if __name__ == '__main__':
    Bot()
    






