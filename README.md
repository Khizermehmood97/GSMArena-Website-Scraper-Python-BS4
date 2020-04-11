# GSMArena-Website-Scraper-Python-BS4

GSMArena Website Mobile Devices Scraper:
A tool for gathering all specifications data of each mobile device of each brand available on GSMArena website.
All this data is then exported to a json file named as GsmArena.json.

Software Requirements:
	Python 3.6
	List of pip packages needed:
		BeautifulSoup4
		selenium
	chromedriver (save the location of this file)


How to Run:
	1. In line-32 and line-64  of GSMArena_Scraper.py file, replace the number '3' with your desired number of brands you want to gather data of.
        2. In line-66 of GSMArena_Scraper.py file, replace the number '3' with your desired number of devices of each brand you want to gather data of.
	3. Run the program using : python3 Controller.py
	
Note
This tool is for research purposes only. Hence, the developers of this tool won't be responsible for any misuse of data collected using this tool.
