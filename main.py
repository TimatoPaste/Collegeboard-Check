from selenium import webdriver as wd;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import time;

wiki = wd.Chrome();
wiki.get("https://en.wikipedia.org/wiki/List_of_legendary_creatures_by_type");

pdf = wd.Chrome(); 
pdf.get("https://drive.google.com/file/d/1Q8TBnHlJ9Rpybmg3ioXwqJPtaizZty6V/view");

try:
    passwordBar = WebDriverWait(pdf, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"ndfHFb-c4YZDc-UmsTj-YPqjbf")))
except Exception as e:
    print(e)

try:
    pass #fix this a;dfj;sakdfjl;ajsdl;fj;asdj
    
except Exception as e:
    print(e)

creatures = wiki.find_elements(By.TAG_NAME,"li");

for li in creatures:
    children = li.find_elements(By.XPATH,".//*");
    for elements in children:
        text = elements.text
        if not text.isspace() and len(text) != 0:
            text = elements.text.upper().strip().replace("\n","");
            passwordBar.send_keys(text);
            submit.click()

input("done, enter to finish");