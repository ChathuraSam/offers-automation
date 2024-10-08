import os
from dotenv import load_dotenv
from twilio.rest import Client
import requests
import uuid
import schedule
import time

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

recipients = [
    {
      "name": "Chathura",
      "phone": "whatsapp:+94716301615"
    },
    {
      "name": "Ruwanthi",
      "phone": "whatsapp:+94769322212"
    }
]

products_url = "https://zebraliveback.keellssuper.com/2.0/Web/GetItemDetails"
all_products_url = "https://zebraliveback.keellssuper.com/2.0/AllPromotion/GetItemDetails"
login_url = "https://zebraliveback.keellssuper.com/1.0/Login/CredentialLogin"
all_nexus_deals = "https://zebraliveback.keellssuper.com/2.0/Web/GetItemDetails"

# Example REST API call
# response = requests.get('https://zebraliveback.keellssuper.com/1.0/AllPromotion/GetInitialDataCollectionForAllPromotion?locationCode=SCUP&subDeaprtmentCode=&subDepartmentsOnly=true')  # Replace with your actual API URL
# response = requests.get('https://zebraliveback.keellssuper.com/2.0/Web/GetItemDetails?fromCount=0&toCount=20&outletCode=SCDR%20%20%20%20%20%20%20%20&departmentId=&subDepartmentId=&categoryId=&itemDescription=%20%20%20%20%20%20%20%20&itemPricefrom=0&itemPriceTo=5000&isFeatured=0&isPromotionOnly=true%20%20%20%20%20%20%20%20&promotionCategory=2&sortBy=default&BrandId=&storeName=%20%20%20%20%20%20%20%20&subDeaprtmentCode=ALL&stockStatus=true&brandName=')  # Replace with your actual API URL
# all: https://zebraliveback.keellssuper.com/2.0/Web/GetItemDetails?fromCount=0&toCount=20&outletCode=SCDR%20%20%20%20%20%20%20%20&departmentId=&subDepartmentId=&categoryId=&itemDescription=%20%20%20%20%20%20%20%20&itemPricefrom=0&itemPriceTo=5000&isFeatured=0&isPromotionOnly=true%20%20%20%20%20%20%20%20&promotionCategory=2&sortBy=default&BrandId=&storeName=%20%20%20%20%20%20%20%20&subDeaprtmentCode=ALL&stockStatus=true&brandName=

# Return the login response
def login():
  headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': '_gcl_au=1.1.665450327.1727543550; _gid=GA1.2.676612484.1727543551; _fbp=fb.1.1727543550870.547033089227967214; _hjSessionUser_2566102=eyJpZCI6ImFlZTVmMmVlLWM2MmEtNWI0OS05NzdlLWU2N2ZkOWY3NDJiNyIsImNyZWF0ZWQiOjE3Mjc1NDM1NTEyMTksImV4aXN0aW5nIjp0cnVlfQ==; _clck=1qgoquq%7C2%7Cfpl%7C0%7C1732; ARRAffinity=34dc192faaa9d0b965caeb984296252404f91dd2795ce26d868945f67daac397; ARRAffinitySameSite=34dc192faaa9d0b965caeb984296252404f91dd2795ce26d868945f67daac397; ARRAffinity=34dc192faaa9d0b965caeb984296252404f91dd2795ce26d868945f67daac397; ARRAffinitySameSite=34dc192faaa9d0b965caeb984296252404f91dd2795ce26d868945f67daac397; __cf_bm=ysiqFNhtvJ7ZSnUfiMD5pYAY5R3gxeWkU0kBVgH40yI-1727635654-1.0.1.1-RfxqenNR6rL1IikP_MHG92kA_20sQkqT.BuGGYKbj9vgwuGOaFm6s5Ik32Ax7vxguSPD11I0tvS8cWvKsWVGvA; cf_clearance=kA6XUpUNP8PEBg000_fyFGT8S1JblaadXa0p9OnxFtA-1727635655-1.2.1.1-NHaZOZG4Go432MtC9lUSC93aZJEYkeWuCSX8TPEAr0u9CHPO4tgr4eGFNUGBhhKMa8Av1.bfukbltrtsafAtjQ1MdYP0SY4ai5nb6KXINqE.cyp__oHxOTzGtgw.fdKvKly07x9tykusmTuj1y2lOMjXDQS4k2dbAPVkmNxPp7lSca928ehwtlZ5HKa28PYsg_MwkV2vNtUiT.b.EIpkr9ot1Y8f19Iu5Ywr2hsdfikIhy7y4pdfw06fLo3g5iFXsBct2Yv0YwwbNGyT3HVQK8Ces5tERbH3e2Hhj4bfOwfVhrPTv4wTUPZ7pDEUIZT6qxsKne9LTbDdh3W9VROslJ_M8nyzVQ2Grcvn36Zt.4IWoBodgag6caG8uBy3ZOgshJKh0IwU8rBpsjAqm6s_bw; _hjSession_2566102=eyJpZCI6IjU0ZmQ2ZmI4LTgwZWQtNGU2Zi1hMWM4LWFhNzk3NWM1ZjE3NCIsImMiOjE3Mjc2MzU2NTYzOTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gat_UA-9750031-5=1; _ga=GA1.1.116328125.1727543551; _ga_B6EBGT7EZF=GS1.1.1727635654.6.1.1727636332.58.0.0; _ga_NHXL73BPBY=GS1.1.1727635654.6.1.1727636332.58.0.0; _clsk=1q9v4c8%7C1727636334336%7C4%7C1%7Cw.clarity.ms%2Fcollect',  # The full cookie value
    'origin': 'https://keellssuper.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://keellssuper.com/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'usersessionid': '',
    'x-frame-options': 'DENY'
  }

  login_payload = {
    "Username": "chathuras940@gmail.com",
    "Password": "G7u8#JGu"
  }

  response = requests.post(login_url, headers=headers, json=login_payload)

  if response.status_code == 200:
    print("Login successful!")
  else:
    print(f"Login failed with status code: {response.status_code}")
    print("Response:", response.text)
  return response

# Return the deals for the day
def get_deals():
  
  params = {
    'fromCount': 0,
    'toCount': 20,
    'outletCode': 'SCDR',
    'departmentId': '',
    'subDepartmentId': '',
    'categoryId': '',
    'itemDescription': '',
    'itemPricefrom': 0,
    'itemPriceTo': 5000,
    'isFeatured': 0,
    'isPromotionOnly': 'true',
    'promotionCategory': 2,
    'sortBy': 'default',
    'BrandId': '',
    'storeName': '',
    'subDeaprtmentCode': 'ALL',
    'stockStatus': 'true',
    'brandName': ''
  }

  headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cookie': '_gcl_au=1.1.665450327.1727543550; _gid=GA1.2.676612484.1727543551; _fbp=fb.1.1727543550870.547033089227967214; _hjSessionUser_2566102=eyJpZCI6ImFlZTVmMmVlLWM2MmEtNWI0OS05NzdlLWU2N2ZkOWY3NDJiNyIsImNyZWF0ZWQiOjE3Mjc1NDM1NTEyMTksImV4aXN0aW5nIjp0cnVlfQ==; _clck=1qgoquq%7C2%7Cfpl%7C0%7C1732; ARRAffinity=34dc192faaa9d0b965caeb984296252404f91dd2795ce26d868945f67daac397; ARRAffinitySameSite=34dc192faaa9d0b965caeb984296252404f91dd2795ce26d868945f67daac397; _clsk=1q9v4c8%7C1727635653320%7C1%7C1%7Cw.clarity.ms%2Fcollect; __cf_bm=ysiqFNhtvJ7ZSnUfiMD5pYAY5R3gxeWkU0kBVgH40yI-1727635654-1.0.1.1-RfxqenNR6rL1IikP_MHG92kA_20sQkqT.BuGGYKbj9vgwuGOaFm6s5Ik32Ax7vxguSPD11I0tvS8cWvKsWVGvA; cf_clearance=kA6XUpUNP8PEBg000_fyFGT8S1JblaadXa0p9OnxFtA-1727635655-1.2.1.1-NHaZOZG4Go432MtC9lUSC93aZJEYkeWuCSX8TPEAr0u9CHPO4tgr4eGFNUGBhhKMa8Av1.bfukbltrtsafAtjQ1MdYP0SY4ai5nb6KXINqE.cyp__oHxOTzGtgw.fdKvKly07x9tykusmTuj1y2lOMjXDQS4k2dbAPVkmNxPp7lSca928ehwtlZ5HKa28PYsg_MwkV2vNtUiT.b.EIpkr9ot1Y8f19Iu5Ywr2hsdfikIhy7y4pdfw06fLo3g5iFXsBct2Yv0YwwbNGyT3HVQK8Ces5tERbH3e2Hhj4bfOwfVhrPTv4wTUPZ7pDEUIZT6qxsKne9LTbDdh3W9VROslJ_M8nyzVQ2Grcvn36Zt.4IWoBodgag6caG8uBy3ZOgshJKh0IwU8rBpsjAqm6s_bw; _ga_B6EBGT7EZF=GS1.1.1727635654.6.1.1727635655.59.0.0; _ga_NHXL73BPBY=GS1.1.1727635654.6.1.1727635655.59.0.0; _ga=GA1.2.116328125.1727543551; _gat_UA-9750031-5=1',
    'origin': 'https://keellssuper.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://keellssuper.com/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-frame-options': 'DENY'
  }

  response = requests.get(all_products_url, headers=headers, params=params)
  
  if response.status_code == 200:
    print("Deals retrieved successfully!")
    
    data = response.json()
    item_details_list = data["result"]["itemDetailsList"]
    deals = []
    for response in item_details_list:
      item_id = response['itemID']
      name = response['name']
      original_price = response['amount']
      discounted_price = original_price - response['promotionDiscountValue']

      deal = {
        "item_d": item_id, 
        "name": name, 
        "original_price": original_price, 
        "discounted_price": discounted_price
      }

      deals.append(deal)
    
  else:
    print(f"Failed to retrieve deals. Status code: {response.status_code}")
    print("Response:", response.text)
  
  
  return deals

# Return the templated message
def get_message_template(recipient, deals):
  message = f"🟩 Hello {recipient["name"]}. Today's Keels deals are as follows: \n"
  for deal in deals:
    message += f"✅ {deal['name']} - {deal['original_price']} -> {deal['discounted_price']} \n"
  return message

# Send the message to the recipients
def send_whatsapp_message(message, recipient):
  print(f'sending message: {message} to {recipient["name"]} at {recipient["phone"]}')
  client.messages.create(
    body=message,
    from_="whatsapp:+14155238886",
    to=recipient["phone"],
  )

def send_message():
  login()
  deals = get_deals()
  for recipient in recipients:
    message = get_message_template(recipient, deals)
    send_whatsapp_message(message, recipient)

def main():
  # Schedule the message to be sent every 24 hours
  schedule.every(24).hours.do(send_message)
  while True:
    schedule.run_pending()
    time.sleep(60*60)  # wait one hour
  

if __name__ == "__main__":
  main()

