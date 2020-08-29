


import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox 
from tkinter.ttk import Progressbar

# import main_code_ as main_code
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import platform
import sys
import time
import math
from datetime import datetime
from time import sleep 
import warnings
from shutil import copyfile
import os

# from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.firefox.options import Options







def get_digits(str1):
    c  =  ""
    for i in str1:
        if i.isdigit():
            c +=  i
    return c


 

def inputs_to_ieee(progress,status,tk_,driver,Year1,Year2,Journal_name,Keyword,Sort_print):
    
    
    
    # global flgg
    
    TT=1
    while TT==1:
        
        global dt_string
        
        # global tk_
       
            
            
        # class PrintLogger(): # create file like object
        #     def __init__(self, textbox): # pass reference to text widget
        #         self.textbox = textbox # keep ref
                  
        #     def write(self, text):
        #         self.textbox.insert(tk_.END, text) # write text to textbox
        #         # could also scroll to end of textbox here to make sure always visible
        #     #Auto Scroll
        #         self.textbox.yview(tk_.END)
            
        #     def flush(self): # needed for file like object
        #         pass
        
        # make progress bar
        progress.place(x = x0+30, y = y0+130) 
        progress.update()   
        
        
        tk_.title('Processing....') 
        
    
        # root.mainloop(1)
                 
        
        url = 'https://ieeexplore.ieee.org/Xplore/home.jsp'
        
        text_status="Opened IEEE"
        status.config(text=text_status) 
        status.update()
        
        # root.update_idletasks()
       
        driver.get(url) 
        sleep(2)
    
        
    
        
        ther = 3
        
        Journal_name = Journal_name
        Year_from = Year1
        Year_to = Year2
        KEYWORD = Keyword
        SELECt_order = Sort_print
    
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
    
        try_ = 0
        while ( try_<ther):
            try:
                Type_bar = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[4]/div/xpl-root/xpl-header/div/div[4]/xpl-search-bar-migr/div/form/div[2]/div/div/xpl-typeahead-migr/div/input") 
                Type_bar.clear()
                Type_bar.send_keys(KEYWORD) 
                
                text_status="Keyword entered"
                status.config(text=text_status) 
                status.update()
                progress['value'] = 10
                progress.update() 
                time.sleep(.2) 
                
                # root.update()
                search_but = driver.find_element_by_class_name("search-icon")
                search_but.click()
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                # root.update()
                sleep(3)
                try_ += 1
    
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
    
    
   
        try_ = 0
        while ( try_<ther):
            try:
                driver.find_element_by_id("refinement-ContentType:Journals").click()
                sleep(5)
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                sleep(3)
                try_ += 1
                
            
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
        

        try_ = 0
        while ( try_<ther):
            try:
                driver.find_element_by_class_name("facet-ctype-apply-container").click()
    
                text_status = "Journals has been Selected"
                status.config(text=text_status) 
                status.update()
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                sleep(3)
                try_ += 1
        progress['value'] = 20
        progress.update() 
        time.sleep(.2) 
                
        
        
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
        
        
        
        
        
        try_ = 0
        while ( try_<ther):
            try:
                driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(1) > section > div.js-content.refinement-content.u-mt-1 > xpl-nouislider-facet > span > span:nth-child(3) > span:nth-child(2) > span:nth-child(1) > input").clear()
                driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(1) > section > div.js-content.refinement-content.u-mt-1 > xpl-nouislider-facet > span > span:nth-child(3) > span:nth-child(2) > span:nth-child(2) > input").clear()
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                
                sleep(3)
                try_ += 1
    
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
        
        
        
        try_ = 0
        while ( try_<ther):
            try:
                # Send Year Fromand To
                driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(1) > section > div.js-content.refinement-content.u-mt-1 > xpl-nouislider-facet > span > span:nth-child(3) > span:nth-child(2) > span:nth-child(1) > input").send_keys(Year_from)
                driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(1) > section > div.js-content.refinement-content.u-mt-1 > xpl-nouislider-facet > span > span:nth-child(3) > span:nth-child(2) > span:nth-child(2) > input").send_keys(Year_to)
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                
                sleep(3)
                try_ += 1
    
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break        
        progress['value'] = 30
        progress.update() 
        time.sleep(.2) 
                
    
        try_ = 0
        while ( try_<ther):
            try:
                year_aply = driver.find_element_by_id("Year-apply-btn")
                year_aply.click()
     
                text_status = "Year range has been applied"
                status.config(text=text_status) 
                status.update()
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                
                sleep(3)
                try_ += 1

        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break        


        sleep(4)
    
        try_ = 0
        while ( try_<ther):
            try:
                driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(4) > section > header > h1 > span").click()
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status)
                status.update()
                
                sleep(3)
                try_ += 1
        
        
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
        progress['value'] = 40
        progress.update() 
        time.sleep(.2) 
    
        try_ = 0
        while ( try_<ther):
            try:
                driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(4) > section > div.js-content.refinement-content.u-mt-1 > xpl-dimension-search-facet > div > div:nth-child(1) > form > xpl-typeahead-migr > div > input").send_keys(Journal_name)
                
                text_status = 'Specific Journal name entered'
                status.config(text=text_status) 
                status.update()
                
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                
                sleep(3)
                try_ += 1
        
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
        progress['value'] = 50
        progress.update() 
        time.sleep(.2) 
                
        sleep(4)
    
        
        try_ = 0
        while ( try_ < ther):
            try:
                  driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(4) > section > div.js-content.refinement-content.u-mt-1 > xpl-dimension-search-facet > div > div > form > xpl-typeahead-migr > div > ul > li > label > input").click()
                  
                  text_status = 'Specific Journal selected'
                  status.config(text=text_status) 
                  status.update()
                  
                  break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                
                sleep(3)
                try_ += 1
      
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break

        progress['value'] = 60
        progress.update() 
        time.sleep(.2)     
        
       
    
        try_1 = 0
        while ( try_1<ther):
            try:
                sleep(2)
                journal_aply = driver.find_element_by_id("Publication Title-apply-btn")
                journal_aply.click()
                
                text_status = "Specific journal has been applied"
                status.config(text=text_status) 
                status.update()
                
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                
                if try_1 == 3:
                    break
                else:
                    try_1 += 1

    
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
        
        if try_1==3 :
            text_status = "There is no Jounal withe entered name on IEEE Explore"
            status.config(text=text_status) 
            status.update()
            sleep(2)
            
            text_status = "please check the Journal name and select from"
            status.config(text=text_status) 
            status.update()
            sleep(2)
            
            text_status = "https://ieeexplore.ieee.org/browse/periodicals/title?refinements=ContentType:Journals"
            status.config(text=text_status) 
            status.update()
            sleep(2)
            return()
            
 
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            break
        progress['value'] = 70
        progress.update() 
        time.sleep(.2) 
                
    
        sleep(2)
    
       
        if SELECt_order == 'Relevence': 
            #It's default of IEEE  
            pass
        elif SELECt_order == 'Most Cited [By Papers]':
            driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div.main-section > xpl-results-list > div.results-actions.hide-mobile > xpl-select-dropdown > button > a").click()
            driver.find_element_by_css_selector("#ngb-tooltip-173 > div.tooltip-inner > ul > li:nth-child(4) > div.filter-popover-opt-text").click()
        else: # 'Newsest First'
            driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div.main-section > xpl-results-list > div.results-actions.hide-mobile > xpl-select-dropdown > button > a").click()
            driver.find_element_by_css_selector("#ngb-tooltip-173 > div.tooltip-inner > ul > li:nth-child(2) > div.filter-popover-opt-text").click()
           
        
        text_status = "Sorting has been selected as " + SELECt_order
        status.config(text=text_status) 
        status.update()
        
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
        sleep(6)
        
        progress['value'] = 80
        progress.update() 
        time.sleep(.2) 
                
        
        # if results >2000, IEEE wouldn't generate CSV file ! 
        while int(driver.find_element_by_css_selector("#xplMainContent > div.ng-Dashboard > div.col > xpl-search-dashboard > section > div > div.Dashboard-header.col-12 > span:nth-child(1) > span:nth-child(2)").text.replace(',', '')) >2000 :
            #clear From
            driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(1) > section > div.js-content.refinement-content.u-mt-1 > xpl-nouislider-facet > span > span:nth-child(3) > span:nth-child(2) > span:nth-child(1) > input").clear()
            # Send (From+To)/2  
            Year_from= math.ceil((int(Year_from)+int(Year_to))/2)
            
            
            text_status = "The results size was too large so the Beginning Year is modified by  " +  str(Year_from)
            status.config(text=text_status) 
            status.update()
            
            driver.find_element_by_css_selector("#xplMainContent > div.ng-SearchResults.row > div:nth-child(1) > xpl-facets > section > ul > li:nth-child(1) > section > div.js-content.refinement-content.u-mt-1 > xpl-nouislider-facet > span > span:nth-child(3) > span:nth-child(2) > span:nth-child(1) > input").send_keys(Year_from)
            driver.find_element_by_id("Year-apply-btn").click()
            sleep(8)
            total_number_result=driver.find_element_by_css_selector("#xplMainContent > div.ng-Dashboard > div.col > xpl-search-dashboard > section > div > div.Dashboard-header.col-12 > span:nth-child(1) > span:nth-child(2)").text
            
            text_status = "The total number of " + total_number_result + " resualts has been found for the begining year " + str(Year_from)
            status.config(text=text_status) 
            status.update()
            
        total_number_result=driver.find_element_by_css_selector("#xplMainContent > div.ng-Dashboard > div.col > xpl-search-dashboard > section > div > div.Dashboard-header.col-12 > span:nth-child(1) > span:nth-child(2)").text
        
        text_status = "The total number of " + total_number_result + " resualts has been found for the begining year " + str(Year_from)
        status.config(text=text_status)      
        status.update()
            
        try_ = 0
        while ( try_<ther):
            try:
                # Collecting results
                Export_key = driver.find_element_by_css_selector("#xplMainContent > div.ng-Dashboard > div.col-12.action-bar.hide-mobile > ul > li.Menu-item.inline-flexed.export-filter > xpl-export-search-results > button")
                Export_key.click()
                Hot_k=1
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                
                sleep(3)
                try_ += 1
                
 
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        progress['value'] = 90
        progress.update() 
        time.sleep(.2) 
                
        
        text_status = "We are collecting the results, Please Wait ! "
        status.config(text=text_status) 
        status.update()
        
        sleep(8)    
        try_ = 0
        while ( try_<ther):
            try:
                down_key = driver.find_element_by_css_selector("#ngb-tab-2-panel > div > div > form > div > button")
                sleep(10)
                down_key.click()
                if Hot_k==1:
                    now = datetime.now()
                    dt_string = now.strftime("%Y.%m.%d-%H.%M.%S")
                else: 
                    dt_string="1"
                break
            except:
                text_status = "Wait ..."
                status.config(text=text_status) 
                status.update()
                
                sleep(3)
                try_ += 1
 
        progress['value'] = 100
        progress.update() 
        time.sleep(1) 
        
        
        try_ = 0
        
        try:
            progress.destroy()
        except:
            pass
            
            
            
 
        if lol() == False :
            if not sys.warnoptions:
                warnings.simplefilter("ignore")
            driver.quit()
            progress.destroy()
            break
        
        
                
        
        text_status = "The total number of found papers is " + total_number_result + " from the range between " +str(Year_from) +"  to  "  + str(Year_to)
        status.config(text=text_status) 
        status.update()
        sleep(2)
        
        text_status = "The downloded file name is in your Selected Folder"
        status.config(text=text_status) 
        status.update()
        sleep(2)
        
        
        text_status = "with the name of export_"+ dt_string+".csv"
        status.config(text=text_status) 
        status.update()
        sleep(2)
        
        TT = 0
        
        
        # root.update()
        # root.after(100, root.destroy())
        
    if lol() == False:
        dt_string = '0'
        
    
        
    return(dt_string)
    


# Creating tkinter window 
window = tk.Tk() 
window.resizable(False, False)
window.title('IEEE Xplore Paper Search Refiner') 
window.geometry('650x190') 
  
# label text for title 
y0=10
x0=0
# tk.Label(window, text = "This app helps you to refine your search on IEEE Xplore",  
#           font = ("Times New Roman", 25)).place(x = x0, 
                                           # y = y0) 
Ins_text= "Instruction: To have a better result, copy and paste the name of the jounal"
Intruc=tk.Label(window, text = Ins_text,
         fg="red", font = ("Times New Roman", 12))
Intruc.place(x = 5, y = 0) 



tk.Label(window, text = "Kiarash Aryankia Ver 1.1",  
          fg="gray",font = ("Times New Roman", 10)).place(x = x0+490, 
                                           y = y0+135) 
                                                          
  # Status Bar Set to Ready
text_status="Status: Ready"
statusbar = tk.Label(window, text =text_status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)
                                                          
# label 
tk.Label(window, text = "Select The Sorting :", 
          font = ("Times New Roman", 10)).place(x = x0+390, 
                                           y =y0+53) 
  
# Combobox creation 
n = tk.StringVar() 
Sorting_choose = ttk.Combobox(window, width = 13, textvariable = n) 
  
# Adding combobox drop down list 
Sorting_choose['values'] = ('Relevence',  
                          'Most Cited [By Papers]', 
                          'Newsest First')

Sorting_choose.place(x = x0+490, y = y0+50) 
Sorting_choose.current(0) 

int_Y1=2000
int_Y2=2020
Init_J="IET Control Theory & Applications"
Init_key="Multi-agent systems"

# Inisitalization and insering initial values
Year_bgn=tk.IntVar()
Year_end=tk.IntVar() 
Year_bgn.set(int_Y1)
Year_end.set(int_Y2)
J_name=tk.StringVar() 
J_name.set(Init_J)
keyword_j=tk.StringVar() 
keyword_j.set(Init_key)

# defining a function that will 
# print them on the screen 
from tkinter import filedialog

def file_path():
        download_path = filedialog.askdirectory()
        return download_path
    
    
def submit():
    
    path = ''
    path = file_path() + '/'

    if path == '/':
        dt_string = ''
        
    else:    
        global driver,flgg
        dt_string = '1'
        flgg = 1
        if platform.system() == "Windows":
            options = Options()
            #options.add_argument("--headless") # Runs Chrome in headless mode.
           
            # driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
            driver = webdriver.Firefox(options=options, executable_path='./geckodriver.exe')
            
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.manager.showWhenStarting", False)
            options.set_preference("browser.download.dir", path)
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
            options = webdriver.Firefox(options=options)
        else:
            options =  Options()
            #options.add_argument("--headless")
            # driver = webdriver.Firefox()
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.manager.showWhenStarting", False)
            options.set_preference("browser.download.dir", path+'/')
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
            driver = webdriver.Firefox(options=options)
            
            # driver = webdriver.Chrome(options=options)
    
        
     
        # Progress bar widget 
        progress = Progressbar(window,length = 400, mode = 'determinate') 
        # Creating green loading bar 
        
        # flgg=1
      
        Year1=Year_bgn.get() 
        Year2=Year_end.get() 
        Journal_name=J_name.get()
        Keyword=keyword_j.get()
        Sort_print=Sorting_choose.get()
        #satus Bar
        text_status="Status: Please wait"
        statusbar.config(text=text_status) 
        statusbar.update()
        
        Intruc.config(text="") 
         # Send to Function
    
        dt_string = inputs_to_ieee(progress,statusbar,window,driver,Year1,Year2,Journal_name,Keyword,Sort_print)
        
        window.title('IEEE Xplore Paper Search Refiner') 
         #satus Bar
    
    
    
    
    try:
        a = os.listdir(path)
        # print(a)
        # print(path)
        for i in range(len(a)):
            # print(a[i]) 
            if '.csv' in a[i]:
                   
                copyfile(path + a[i], path + 'export_'+dt_string + '.csv')
                break
    except:
        print('eee')
        pass   
    
    
    
    
    
    
    
    if str(dt_string) == '0':
        text_status="Status: Stoped by User"
        statusbar.config(text=text_status) 
        statusbar.update()
        time.sleep(1)
        
        messagebox.showinfo("Status => Stoped ", "Program has stoped by the user") 
    elif str(dt_string) > "1" : 
        text_status="Status: Completed ! Please check your Selected Folder"
        statusbar.config(text=text_status) 
        statusbar.update()
        time.sleep(1)
        
        messagebox.showinfo("Status => Completed ", "Go to Selected Folder => [ export_" +  dt_string +  ".csv]") 
          
        driver.quit()
        Year_bgn.set(int_Y1) 
        Year_end.set(int_Y2) 
        J_name.set(Init_J)
        keyword_j.set(Init_key)
        Sorting_choose.current(0)
        text_status="Status: Ready"
        Intruc.config(text=Ins_text)
        statusbar.config(text=text_status) 
    else:
        messagebox.showwarning("Status => Error","There is an error, please try again") 
        try:
            progress.destroy()
        except:
            pass
        Year_bgn.set(int_Y1) 
        Year_end.set(int_Y2) 
        J_name.set(Init_J)
        keyword_j.set(Init_key)
        Sorting_choose.current(0)
        text_status="Status: Ready"
        Intruc.config(text=Ins_text)
        statusbar.config(text=text_status) 
    
    
   
    

# creating a label for  
# year from using widget Label 
Year_from_label = tk.Label(window,width = 9, text = 'Year From :', 
                      font=('Times New Roman', 
                            10, 'normal')).place(x = x0+390, 
                                           y = y0+20)  
   
# creating a entry for input 
# year from  using widget Entry 
Year_from = tk.Entry(window, width = 5,
                     textvariable = str(Year_bgn),
                     font=('Times New Roman',10,'normal')).place(x = x0+450, 
                                           y = y0+18) 

# creating a label for year to 
Year_to_label = tk.Label(window, width = 5,
                   text = 'To :', 
                   font = ('Times New Roman',10,'normal')).place(x = x0+500, 
                                           y = y0+20) 
   
# creating a entry for year to 
Year_to = tk.Entry(window, width = 5,
                     textvariable = str(Year_end), 
                     font = ('Times New Roman',10,'normal')).place(x = x0+540, 
                                           y = y0+18) 


# creating a label for Journal name 
J_name_label = tk.Label(window, width = 12,
                   text = 'Journal Name :', 
                   font = ('Times New Roman',10,'normal')).place(x = x0+10, 
                                           y = y0+20) 
   
# creating a entry for year to 
J_name_entry = tk.Entry(window, width =45,
                     textvariable = str(J_name), 
                     font = ('Times New Roman',10,'normal')).place(x = x0+90, 
                                           y = y0+18)                   
                                                                   
                                                                   
   
  # creating a label for Keyword                                                              # creating a label for Journal name 
keyword_label=label = tk.Label(window, width = 9,
                   text = 'Keyword :', 
                   font = ('Times New Roman',10,'normal')).place(x = x0+10, 
                                           y = y0+55) 
   
# creating a entry for Keyword
keyword_entry = tk.Entry(window, width =45,
                     textvariable = str(keyword_j), 
                     font = ('Times New Roman',10,'normal')).place(x = x0+90, 
                                           y = y0+53) 
 
     
                                                                   


                                                                 
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(window,text = 'Search', command =  submit, width=10) 
                  #command =  lambda : [submit, bar()] )
                  #command =  combine_funcs(submit, bar)) 
                  #command =  submit) 
                  # 

sub_btn.place(x = x0+300, y = y0+100) 



# cancel button
# Button that will call the submit function  
# can_btn=tk.Button(window,text = 'Cancel', 
#                   command =  cancel) 


  


def stop():
    global flgg
    flgg = 0
    # print(flgg)
    
def lol():
    # global flgg
    if flgg != 1:
        text_status = "Stoped"
        statusbar.config(text=text_status) 
        statusbar.update() 
        
        
        return(False)
        
        
        
can_btn = tk.Button(window, text="Stop",width=10, command=stop)




can_btn.place(x = x0+190, y = y0+100) 



window.mainloop() 



