from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time
import os

# 페이지를 아래로 스크롤하는 함수
def scroll_down():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # 페이지 맨 아래로 스크롤
        driver.find_element(By.XPATH, '//body').send_keys(Keys.END)
        time.sleep(3)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        try:
            # '더보기' 버튼이 보이면 클릭
            load_more_button = driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input')
            if load_more_button.is_displayed():
                load_more_button.click()
                time.sleep(3)  # 버튼 클릭 후 잠시 대기
        except:
            pass

if __name__ == "__main__":
    query = input("검색어 : ") 
    image_cnt = int(input("수집할 이미지 개수 : ")) 

    save_dir = "saved_image"  # 저장할 디렉토리 이름
    os.makedirs(save_dir, exist_ok=True)  # 디렉토리 생성 (이미 존재하면 무시)
    os.chdir(save_dir)  # 작업 디렉토리 변경

    driver = webdriver.Chrome()  # Chrome 웹 드라이버 실행
    URL = 'https://www.google.com/search?tbm=isch&q='
    driver.get(URL + query)  # 검색어를 포함한 URL로 이동

    scroll_down()  # 페이지 스크롤 함수 호출

    print('=== 이미지 수집 시작 ===')

    images = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i')

    download_cnt = 0
    for img in images:
        if download_cnt == image_cnt:
            break
        try:
            img.click()
            time.sleep(3)  # 이미지 클릭 후 잠시 대기
            actual_images = driver.find_elements(By.CSS_SELECTOR, 'img.n3VNCb')
            for actual_img in actual_images:
                src = actual_img.get_attribute('src')
                if src and 'http' in src:
                    image_path = os.path.join(query.replace(' ', '_') + '_' + str(download_cnt) + '.jpg')
                    urllib.request.urlretrieve(src, image_path)
                    download_cnt += 1
                    if download_cnt == image_cnt:
                        break
        except Exception as e:
            print(f"Error downloading image {download_cnt}: {e}")

    print('=== 이미지 수집 종료 ===')
    driver.close()  # 브라우저 닫기
