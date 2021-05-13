import time
from plyer import notification
while True:
    notification.notify(
    title="please drink water now!!",
    message=" The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
    timeout=10,
    app_icon='C:\\Users\\muskan\\Desktop\\DS_101\\Iconsmind-Outline-Glass-Water.ico'
        
    )
    time.sleep(60*60)