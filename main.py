from selenium import webdriver as wd;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import time;

wiki = wd.Chrome("./chromedriver-win64/chromedriver");
wiki.get("https://en.wikipedia.org/wiki/List_of_legendary_creatures_by_type");

pdf = wd.Chrome("./chromedriver-win64/chromedriver"); 
pdf.get("https://drive.google.com/file/d/1Q8TBnHlJ9Rpybmg3ioXwqJPtaizZty6V/view");

wait = input("hi")