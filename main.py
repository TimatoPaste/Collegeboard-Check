from selenium import webdriver as wd;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import time;

#maybe want to put the links and creds in text file
collegeboardLink = input("Enter collegeboard link\n").strip().replace(" ","");


studentportalLink = input("Enter student portal link\n").strip().replace(" ","");
 

cb = wd.Chrome("./chromedriver-win64/chromedriver");
cb.get(collegeboardLink);
pdf = wd.Chrome("./chromedriver-win64/chromedriver");
pdf.get(studentportalLink);

wait = input("Program finished running. Enter to end.")
print("Ending... Thank you for using this program :)")