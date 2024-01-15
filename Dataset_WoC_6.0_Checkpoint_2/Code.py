import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import click

#cService = webdriver.ChromeService(executable_path="C:\\Users\\rishi\\OneDrive\\Documents\\SELENIUM\\chromedriver.exe")
#driver = webdriver.Chrome(service = cService)

#PATH = "C:\\Users\\rishi\\OneDrive\\Documents\\SELENIUM\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

wd = webdriver.Chrome(options=options)

def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd): 
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?q=beagle&sca_esv=597261711&rlz=1C1GCEA_enIN1032IN1032&hl=en-GB&tbm=isch&sxsrf=ACQVn0_uKhLXzqdo0H8iSe_rTZU4o3WByw:1704908251252&source=lnms&sa=X&ved=2ahUKEwjn28KVrtODAxX3oa8BHRnXBLsQ_AUoAXoECAIQAw&biw=1536&bih=695&dpr=1.25"
    wd.get(url)

    image_urls = set()
    skip = 0

    while len(image_urls)+skip < max_images:
        scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

        for img in thumbnails[len(image_urls):max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue

            images = wd.find_elements(By.CLASS_NAME, "sFlh5c")
            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skip += 1
                    break

                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")
    wd.quit()
    return image_urls



def download_image(download_path, url , file_name):
    try: 
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f,"JPEG")
    except Exception as e:
        print("FAILED - ",e)
    
    print("Success")


urls = get_images_from_google(wd,0.5,100)

for i, url in enumerate(urls):
    download_image("Dog_breeds/Beagle/Img",url, str(i) + ".jpg")


