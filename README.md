
>

      ______             _                 _      _                _       _____            _             _      _____ _               _             
     |  ____|           | |               | |    | |              | |     / ____|          | |           | |    / ____| |             | |            
     | |__ __ _  ___ ___| |__   ___   ___ | | __ | |     ___  __ _| | __ | |     ___  _ __ | |_ __ _  ___| |_  | |    | |__   ___  ___| | _____ _ __ 
     |  __/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ / | |    / _ \/ _` | |/ / | |    / _ \| '_ \| __/ _` |/ __| __| | |    | '_ \ / _ \/ __| |/ / _ \ '__|
     | | | (_| | (_|  __/ |_) | (_) | (_) |   <  | |___|  __/ (_| |   <  | |___| (_) | | | | || (_| | (__| |_  | |____| | | |  __/ (__|   <  __/ |   
     |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\ |______\___|\__,_|_|\_\  \_____\___/|_| |_|\__\__,_|\___|\__|  \_____|_| |_|\___|\___|_|\_\___|_|   
                                                                                                                                                 
                                                                                                                                                 
After the leak of 533 millions Facebook user data, I wanted to find out if any of my friends have been affected. I could not find an easy way to do it so I wrote this program to help me. All you have to do is import a vcard ('.vcf') and provide a file from the leak (you may find the files on your favorite torrent providers) and let the program do the rest.

# To use:

1- install dependency for parsing Vcards
----------------------------------------
> pip install vobject

2- use the program
----------------------------------------
> python main.py -i 'contact.vcf' -l 'Country.txt'

# How to export .vcf on Android:

[https://www.howtogeek.com/359081/how-to-manually-export-and-back-up-contacts-on-android/](https://www.howtogeek.com/359081/how-to-manually-export-and-back-up-contacts-on-android/)

# How to export .vcf on Apple

[https://trendblog.net/how-to-export-iphone-contacts-to-a-vcf-or-csv-file/](https://trendblog.net/how-to-export-iphone-contacts-to-a-vcf-or-csv-file/)



