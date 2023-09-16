# TicketPriceSMS
## ابتدا کتابخانه های زیر را نصب کنید
``` pip install selenium ```  
``` pip install farsi_tools ```

### نکته: برای اجرای درست برنامه نیاز دارید chrome webdriver را [دانلود](https://chromedriver.chromium.org/downloads) کنید. دقت کنید نسخه مروگر کروم و **chrome webdriver** باید همگام باشند.

---
### با فراخوانی متد **()get_info_from_alibaba**  و فرستادن *url1* به عنوان پارامتر می توانید اطلاعات ارزان ترین پرواز تهران به استانبول و با فرستادن *url2* می توانید اطلاعات ارزان ترین پرواز استانبول به تهران را را دریافت کنید. 
```
  get_info_from_alibaba(url1) # Tehran to Istanbul

  get_info_from_alibaba(url2) # Istanbul to Theran

```






