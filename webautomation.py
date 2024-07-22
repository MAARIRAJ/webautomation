import webbrowser as wb

def automation():
    copypath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    urls={
        "youtube.com",
        "spotify.com"   }
    for url in urls:
        wb.get(copypath).open(url)

automation()