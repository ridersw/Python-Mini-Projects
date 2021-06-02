import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirects = "127.0.0.1"
websiteLists = ["www.facebook.com","facebook.com"]


while True:
	if dt.now().hour > 8 and dt.now().hour < 18:
		print("Working Hours")
		with open(hosts_path, "r+") as file:
			content = file.read()
			for website in websiteLists:
				if website in content:
					print(f"{website} in the List")
				else:
					print(f"Adding {website} in the list")
					file.write(redirects + " " + website + "\n")
	else:
		print("Fun Hours")
		with open(hosts_path, "r+") as file:
			content = file.readlines()
			file.seek(0)
			
			for line in content:
				if not any(website in line for website in websiteLists):
					file.write(line)
				else:
					print(f"Match found for {line}, Removing..")
					
			file.truncate()
				
	time.sleep(5)
