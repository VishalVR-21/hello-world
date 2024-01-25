import time
import webbrowser
import subprocess
import platform

video_url = ["https://www.youtube.com/watch?v=7P0ApXLwsAg","https://www.youtube.com/watch?v=kPcQdmKBey4","https://www.youtube.com/watch?v=eTuH5sWtX_c","https://www.youtube.com/watch?v=uitvgimzxZA","https://www.youtube.com/watch?v=YatqIX7oyc8","https://www.youtube.com/watch?v=CCZlSC2xcm4","https://www.youtube.com/watch?v=UZW3Ekx0-hg"]

while True:
    for i in range(0,len(video_url)):
        webbrowser.open(video_url[i])
        time.sleep(200)  # Sleep for 20 seconds

        # Determine the operating system
        current_os = platform.system()

        # Platform-specific commands to close the browser window
        if current_os == "Windows":
            subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"])
        elif current_os == "Linux":
            subprocess.run(["pkill", "chrome"])
        elif current_os == "Darwin":  # macOS
            subprocess.run(["pkill", "Google Chrome"])
        else:
            print("Unsupported operating system. Please close the browser manually.")
# from selenium import webdriver
# import time

# video_url = "https://youtu.be/kPcQdmKBey4"

# # Create a new instance of the Chrome browser
# driver = webdriver.Chrome()
# while 1:

# # Open the URL in a new tab
#     driver.get(video_url)

#     # Wait for 20 seconds
#     time.sleep(20)

#     # Close the current tab
#     driver.close()

#     # Quit the browser
# driver.quit()