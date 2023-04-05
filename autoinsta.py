import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

chromedrive_path = 'C:/Users/pedro/Downloads/chromedriver_win32/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedrive_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/')
sleep(randint(3, 6))

usuario = webdriver.find_element(By.NAME, "username")
usuario.send_keys('user')
senha = webdriver.find_element(By.NAME, "password")
senha.send_keys('password')

button_login = webdriver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button')
button_login.click()
sleep(randint(4, 8))

hashtag_list = ['casadecampo', 'bookingbrasil', 'carnaval2023', 'rustico', 'flat', 'gravata', 'recife', 'pernambuco',
                'viagemcasal', 'hospedagem', 'natureza', 'nature', 'viajar', 'amoviajar', 'comida', 'boraviajar',
                'viagembarata', 'caruaru', 'festa', 'gravatape']

tag = -1
likes = 0
comentarios = 0
avancos = 0

choice_hashtag_list = random.choice(hashtag_list)
hashtag_list.remove(choice_hashtag_list)

for hashtag in hashtag_list:
    if avancos < 50:
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/' + random.choice(hashtag_list) + '/')
        sleep(6)
        thumb_recente = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/di'
                                                         'v[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div'
                                                         '[2]')
        thumb_recente.click()
        sleep(randint(8, 10))
        try:
            while avancos < 50:
                button_like = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div'
                                                               '[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/d'
                                                               'iv/div[2]/section[1]/span[1]/button')
                button_like.click()
                likes += 1
                sleep(randint(3, 6))

                webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/di'
                                                 'v/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]'
                                                 '/button').click()
                comment_box = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div'
                                                               '[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/'
                                                               'div/div[2]/section[3]/div/form/div/textarea')
                sleep(3)
                comentario_chance = randint(1, 10)

                if comentario_chance == 1:
                    comment_box.send_keys('Top!')
                    sleep(randint(4, 6))
                elif comentario_chance == 2:
                    comment_box.send_keys('Gostei')
                    sleep(randint(2, 7))
                elif comentario_chance == 3:
                    comment_box.send_keys('Parabéns!')
                    sleep(randint(4, 10))
                elif comentario_chance == 4:
                    comment_box.send_keys('Amei !')
                    sleep(randint(4, 7))
                elif comentario_chance == 5:
                    comment_box.send_keys('Show!')
                    sleep(randint(1, 3))
                elif comentario_chance == 6:
                    comment_box.send_keys('WOW!')
                    sleep(randint(1, 4))
                elif comentario_chance == 7:
                    comment_box.send_keys('Show de bola')
                    sleep(randint(3, 7))
                elif comentario_chance == 8:
                    comment_box.send_keys('Curti')
                    sleep(randint(6, 9))
                elif comentario_chance == 9:
                    comment_box.send_keys('boa ideia')
                    sleep(randint(1, 12))
                elif comentario_chance == 10:
                    comment_box.send_keys('muito bom')
                    sleep(randint(4, 12))
                comment_box.send_keys(Keys.ENTER)
                comentarios += 1
                sleep(randint(2, 10))

                if avancos == 0:
                    avancar_postagem = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div['
                                                                        '1]/div/div[3]/div/div/div/div/div[1]/div/div/d'
                                                                        'iv[2]/button')
                    avancar_postagem.click()
                    sleep(randint(5, 10))
                    avancos += 1
                elif avancos % 5 == 0:
                    avancos += 1
                    break
                else:
                    avancar_postagem = webdriver.find_element(By.XPATH,
                                                              '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div['
                                                              '3]/div/div/div/div/div[1]/div/div/div[2]/button')
                    avancar_postagem.click()
                    sleep(randint(5, 10))
                    avancos += 1
        except:
            continue
    else:
        print('Liked {} fotos'.format(likes))
        print('Comentários {} fotos'.format(comentarios))
