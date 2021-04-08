# Facebook_Leak_Contact_Checker
After the leak of 533 millions Facebook user data, I wanted to find out if any of my friends have been affected. I could not find an easy way to do it so I wrote this program to help me. All you have to do is import a vcard ('.vcf') and provide a file from the leak (you may find the files on your favorite torrent providers) and let the program do the rest.

To use:

1- install dependency for parsing Vcards
  pip install vobject

2- use the program
  python main.py -i 'contact.vcf' -l 'Country.txt'
