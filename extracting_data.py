from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import time
from PIL import Image
import time
import math
from io import BytesIO

fieldId = "027b53e7-b46c-47bf-9c84-e4d648e83fd5"
ids=['81692d7d-8cbb-502c-a756-b6c283abed7d','9c037684-381a-59e3-a9cc-9062e6cddb83','85ad12af-132d-5eee-9f96-76d9e10b8a13','dec1b77c-038b-50ce-9f0d-1324442f7319','519bcef5-f704-5d39-af2f-92e040ca6f95','7afc460a-2a02-58dd-80bc-3363f033d2a3','7cf7eb85-2907-5f6f-bd0b-cf4790aa892c','aa3fea4b-1d8b-585b-82cd-f9794181246e','db8e9cee-9009-50cf-b094-a9f14018960e','00c38251-2beb-52c2-80a7-ec2ea30f1aa9','12042d5d-c0b5-56a0-9748-2ab7b2223851','f0939fe6-cd7d-594f-9b2c-bd9125f50b17','eae1e63d-3f3d-5cde-82f4-93712221f74a','a2f8a856-94b8-59f0-9688-2ac53a8744e8','1cc38e2b-f5e4-5225-8968-a918bc38daae','6c6e6247-2484-5f39-bd59-1b44c3de3a6d','242d7da2-28d1-5d22-92d6-a63eae757bd7','8c284ee6-b47b-5e86-98c4-287cb4f4dca2','2de8a24d-be32-5d70-a1b5-9e41b7e716a9','3cbf8f67-a7aa-5fe5-a9d5-746c81691bd7','4bbd1d47-9d52-58b1-9afa-11e482590cd3','9702270b-ccbd-53e6-ad63-52257b0aa323','f67e1a68-8208-5047-97cd-98a99d15b4ec','d5677cdb-3b0e-5ddd-9f6e-536913d3442c','7bc9f553-e1ec-551e-a40c-39b10e23eafd','30711405-ff9e-53e8-9bd9-4db3b7a58147','2281d9ee-76db-50a9-aba1-202234dce629','ecb3d0fb-42e7-5874-81d1-f62f6ae615f4','566ff112-f83d-5165-9144-67a5f82a34ca','dcb0f040-5347-5cec-b09c-077aee3cc4f2','9eea3e84-5302-5bab-bd95-6286162848ea','3a833235-297a-5a11-8fd8-177196770617','939830a6-055f-5381-8352-cca6db9a97ed','63602845-b04a-59ef-8034-1d59627843f2','25ef8b5a-91ba-5a91-9413-9385d7c85349','9f1ffc41-ba09-5bcf-adcb-7234686b9fe0','44acea1c-4878-5856-bcb1-e94ef1c375fb','b2b198f2-77c3-53b8-aeae-9a5eae5846c5','e8cd7339-e6b2-5d68-a40d-dee1fabe6cc5','60b7d2f6-496d-51dd-a9a0-8df5e912741f','f2c299a4-e344-520b-8dcf-a56bfea3232b','75298a81-f533-50d3-8b7d-b069a030f30e','816bba71-6d98-5dab-ae3a-dae67ed2a48e','2cab77ab-d5a6-5c09-8eb7-ac04f99d08de','fd4b09be-f7c4-5608-b3f5-77c3054a0245','7cf90b6e-94be-572c-8cb6-d62dc1a128ec','f69c8d5d-aaf5-50ea-ad28-5c164d49f29b','c04aae89-62eb-5bcc-b945-832442a84462','5ab481ef-a379-59e2-b117-a7100c77cb08','272f9cfb-9c21-5d85-ba76-dce2099b2219','61b8f256-6cb8-51c3-aa69-7959b9108c5d','bd2da52e-76ff-55ac-b3a5-5ad97248d75b','90531613-bf3f-56e8-930e-a44ebf2342d4','c2e81661-6f27-594f-9d8a-10358625aa47','cb6147fc-78b3-5260-8ba7-f8ba474f524e','651d048f-0d57-54df-a3d3-a090a695433a','99b6ce54-bf9b-581a-b2f1-8084b92efce0','222157f2-ec29-587b-9e16-09b083060bb5','e7b2756b-a0af-5572-9c05-a08ab6c15fda','c36cf048-66a0-530b-a568-cb2ce5d1aa33','90d426c3-7008-5a49-9555-a594ede8fc58','b4a98c7d-f34f-544d-9600-a0611a6c25ce','d51bcf61-9a54-5c83-91b3-0ecf271a89ad','da4a34b4-fc71-5143-b1b8-0cbdbf0a4a84','6e7f95ba-1186-5180-be3c-8875bf362019','fb6f66ae-6ce9-551e-8083-590698a94871','3be33bcc-e553-515d-9ff1-62831a7bb821','8c4468bf-ace1-5c32-ac53-d31104dad292','d851c933-e82c-5f40-89e7-375d70b6ddba','42780150-5748-5871-ae40-72518aeffe3e','aed80b1a-0d77-5221-a3e6-cbe4a1273491','4ca7645b-8003-58e9-b82e-6a21e352398e','8d85c781-c87c-5a8b-a0ea-4fb923fbd3b1','be05fea4-b97c-5ec7-91f7-af30b0f1fd03','8bc0efaa-2aeb-5949-bfe0-679601d2758d','f80763e1-c4e2-5ad0-a796-c95380fa1c39','34e51dc8-fa95-56f8-9b73-b2e6556938bb','887386b7-6327-564d-8eb8-c1044dccb54a','cb540040-7ae4-5784-9361-8ce0ff8d62a3','2b35744a-bab5-563b-af00-1af2bdde0cf7','1e22359a-73c7-5e8d-900a-d5eba161a13d','3388ecf6-327e-52be-acd9-7da49f6017a8','d768f7c2-1d2c-5e12-8261-e632e1ed122c','8551044c-8c6f-56d9-8a43-3926487dffad','8440ec2d-38e6-5ad2-bbc5-4409de88c466','36cb94ee-bdb7-5b9d-833a-e9b51c7dc265','d24ad14a-f5ac-5301-8453-350d00989854','8d29c699-1e62-5831-9b83-40d3966f0f8b','c9522b48-9364-5250-a7ea-841ad6bf713f','9d2fbf65-be9d-5a0b-80db-10c64cec88c9','31c5aa11-4c25-5152-9848-5ee028770aac','8faa4de2-fe51-5211-874f-6de8e70e00c7','d025a4b4-6ffb-5d9b-8157-a6ce8ca62edb','78cbcfc3-204c-5ae5-96d3-9409e381227a']
def get_token():
    url = "https://authenticate.oneatlas.geoapi-airbusds.com/auth/realms/IDP/protocol/openid-connect/token"
    response = requests.post(url, data={"apikey": "6cIPO5_tz7eK1CrnZe6qROZZZ3lp8U3qImy_jJKRAh04X1xIhhPbV9yjOp42XFHf_i0gxLgvOrD7G_EQUVWfew==",
    "grant_type": "api_key",
    "client_id": "IDP"})
    return response.json()

def getRainAndET(date):
    currentDate = {"day": date[0], "month": date[1],"year":date[2]}
    dataUrl = "https://www.weatherlink.com/browse/9722cfc3-a4ef-47b9-befb-72f52592d6ed"
    loginUrl = "https://www.weatherlink.com/"
    agent = Options()
    agent.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
    driver = webdriver.Chrome(options=agent)
    driver.get(loginUrl)
    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys('BlueBell_IT123')
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys('bluebell123')
    password.send_keys(Keys.ENTER)
    # click data
    while (True):
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a/span").click()
            break
        except(Exception):
            time.sleep(1)
    while (True):
        try:
            dropdown = driver.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/a/span[1]")
            break
        except(Exception):
            time.sleep(1)
    while (True):
        try:
            dropdown.click()
            break
        except(Exception):
            time.sleep(1)
    while (True):
        try:
            yearClicker=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[1]/div/div[2]")
            monthClicker=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[1]/div/div[1]")
            break
        except(Exception):
            time.sleep(1)
    yearClicker.click()
    while (True):
        try:
            year = driver.find_element_by_xpath( "/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[2]/table/thead/tr[2]/th[2]")
            leftArrow_year=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[2]/table/thead/tr[2]/th[1]/i")
            rightArrow_year=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[2]/table/thead/tr[2]/th[3]/i")
            break
        except(Exception):
            time.sleep(1)
    while(True):
        if(year.text=="2019"):
            break
        else:
            leftArrow_year.click()
    while(True):
        if(year.text==currentDate["year"]):
            break
        else:
            rightArrow_year.click()
    monthClicker.click()
    while (True):
        try:
            date = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[1]/table/thead/tr[2]/th[2]")
            leftArrow = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[1]/table/thead/tr[2]/th[1]/i")
            rightArrow = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[1]/table/thead/tr[2]/th[3]/i")
            break
        except(Exception):
            time.sleep(1)
    while (True):
        for i in range(len(date.text)):
            if (date.text[i] == " "):
                month = date.text[:i]
        if (currentDate["month"] == month):
            break
        elif (date.text[:7] != "January"):
            leftArrow.click()
        else:
            rightArrow.click()
            break
    while (True):
        for i in range(len(date.text)):
            if (date.text[i] == " "):
                month = date.text[:i]
        if (currentDate["month"] == month):
            break
        else:
            rightArrow.click()
    time.sleep(1)
    temp=0
    for i in range(1, 8):
        sri = str(i)
        startDay = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[1]/table/tbody/tr[1]/td[" + sri + "]").text
        startDay2 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[1]/table/tbody/tr[2]/td[" + sri + "]").text
        if (startDay == "1"):
            startDayIndex = i
            break
        if(startDay2=="1"):
            startDayIndex= i
            temp=1
    while (True):
        row = str(math.floor((startDayIndex / 7) - 0.001) + 1+temp)
        if (startDayIndex % 7 == 0):
            column = "7"
        else:
            column = str((startDayIndex % 7))
        day = driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/form/div[1]/div/div[2]/div[1]/table/tbody/tr[" + row + "]/td[" + column + "]")
        if (day.text == currentDate["day"]):
            day.click()
            break
        startDayIndex += 1
    while (True):
        try:
            yAxisScroller = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div[4]/div[3]/div")
            break
        except(Exception):
            time.sleep(1)
    times = []
    rain = 0
    ET = 0
    for i in range(28):
        for j in range(1, 200):
            try:
                currentData = driver.find_element_by_xpath(
                    "/html/body/div[2]/div[1]/div[1]/div[3]/div/div[1]/div[4]/div/div/div/table/tbody/tr[" + str(
                        j) + "]/td").text
                if (currentData not in times) and (currentData != ''):
                    rain += (float(driver.find_element_by_xpath(
                        "/html/body/div[2]/div[1]/div[1]/div[3]/div/div[1]/div[1]/div/div/div/table/tbody/tr[" + str(
                            j) + "]/td[17]").text))
                    ET += (float(driver.find_element_by_xpath(
                        "/html/body/div[2]/div[1]/div[1]/div[3]/div/div[1]/div[1]/div/div/div/table/tbody/tr[" + str(
                            j) + "]/td[19]").text))
                    times.append(currentData)
            except(Exception):
                break
        try:
            yAxisScroller.send_keys(Keys.ARROW_DOWN)
        except(Exception):
            break
        time.sleep(0.2)
    return (rain,ET)

def getPastIrragation():
    file=open("pastIrrgation.txt")
    PastIrragation=file.read()
    file.close()
    return (float(PastIrragation))

def putPastIrragation(pastIrragation):
    file = open("pastIrrgation.txt", "w")
    file.write(str(pastIrragation))
    file.close()


def showImage(image):
    array=list(image.getdata())
    maxx=max(array)
    for i in range (len(array)):
        array[i]=(array[i]/maxx)*255
    result=Image.new(image.mode,image.size)
    result.putdata(array)
    result.show()


def getLocation():
    path = __file__
    path=path[:-8]
    return (path)

def getImageAndDate(field,id):
    date=[]
    monthsDic = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June",
                 "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December", }
    token = get_token()
    headers = {}
    headers['Authorization'] = 'Bearer ' + str(token['access_token'])
    url = 'https://verde.oneatlas.airbus.com/projects/dced3cc6-a9a0-4cd7-b05f-7d0d05a7c519/fields/' + field + '/observations/'+ id
    response = requests.get(url, headers=headers)
    response=response.json()
    date.append(response["observation"]["acquisition"]['sensingDate'][5:7])
    date.append(monthsDic[response["observation"]["acquisition"]['sensingDate'][8:10]])
    date.append(response["observation"]["acquisition"]['sensingDate'][:4])
    url = 'https://verde.oneatlas.airbus.com/projects/dced3cc6-a9a0-4cd7-b05f-7d0d05a7c519/fields/' + field + '/observations/' + id + '/data?lk=FCOVER&ofk=ANALYTICS'
    response = requests.get(url, headers=headers)
    image=response.content
    if (date[0][0] == "0"):
        date[0] = date[0][1]
    return (date,image)



def calculateWaterNeed(rain,ET,FCimage,pastIrrigation,soilCapcity):
    currentImage = Image.open(BytesIO(FCimage))
    metaData = currentImage.tag
    tempList = list(currentImage.getdata())
    array=tempList.copy()
    for k in range(len(tempList)):
        if (tempList[k] >= 0):
            # claculate KC
            tempList[k] = (0.8565 * tempList[k] + 0.2122)  # 0.4 + ((0.3923 * tempList[k]) ** 0.74)
            # claculate water need
            tempList[k] = (tempList[k] * ET) - (rain + pastIrrigation + soilCapcity)
    waterImage = Image.new(currentImage.mode, currentImage.size)
    waterImage.putdata(tempList)
    myLocation=getLocation()
    location = myLocation + "waterImage.tiff"
    waterImage.save(location, tiffinfo=metaData)

    maxx = max(array)
    for i in range(len(array)):
        temp=round((array[i] / maxx) * 255)
        array[i] = (temp,temp,temp)
    waterImage = Image.new("RGB", currentImage.size)
    waterImage.putdata(array)
    location = myLocation + "waterImage.jpeg"
    waterImage.save(location, tiffinfo=metaData)




date, FCImage = getImageAndDate(fieldId, ids[0])
rain, ET = getRainAndET(date)
calculateWaterNeed(rain, ET, FCImage, 0, 0)
