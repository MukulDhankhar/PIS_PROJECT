from boltiot import Bolt, Sms #Import Sms and Bolt class from boltiot libraryimport json, timefrom twilio.rest import Clientgarbage_full_limit = 30 # the distance between device and  garbage in dustbin in cmAPI_KEY = "d8adb078-fa6c-4c08-9f9a-4ebcd81bd6e2"DEVICE_ID  = "BOLT13167538"# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKENaccount_sid = 'AC587119d274919d3317b457a5cc873d2b'auth_token = '43f30e4100396d464395da8bee848a78'client = Client(account_sid, auth_token)# this is the Twilio sandbox testing numberfrom_whatsapp_number='whatsapp:+14155238886'# replace this number with your own WhatsApp Messaging numberto_whatsapp_number='whatsapp:+919810779810'mybolt = Bolt(API_KEY, DEVICE_ID) #Create object to fetch data##sms = Sms(SID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER) #Create object to send SMSresponse = mybolt.serialRead('10')print (response)while True:    response = mybolt.serialRead('10')  #Fetching the value from Arduino    data_1 = json.loads(response)    data_2 = dict(data_1)        print(data_2)    if (data_2['value']=='Device is offline'):        print('DEVICE IS OFFLINE, EXITING...')        exit()    elif (data_2['value'] =='') or (data_2['value']=='Command timed out'):        pass    else:        b=data_2['value'].strip()        a = b.split('/n')        garbage_value=a[0]        print(garbage_value)        print ("Garbage level is", garbage_value)        if int(garbage_value) <= 20:            response = client.messages.create(body="Hey there! Dustbin ID 13167538 is about to get full. Please collect it's trash. Navigate quickly through: https://goo.gl/maps/nqDYdJtE3hoRVuyx7",                           from_=from_whatsapp_number,                           to=to_whatsapp_number)            print('MESSAGE SENT')        time.sleep(10)## fill_percentage = (garbage_value/garbage_full_limit)*100## print('Dustbin ID 13167538 is' + str(fill_percentage) + ' % full!')    