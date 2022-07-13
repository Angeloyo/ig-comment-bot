# bot-instagram-comment
Simple python script working with selenium driver to spam comments on an instagram post

## Steps

The full guide to get started with selenium: https://www.selenium.dev/documentation/webdriver/getting_started/

1. Install selenium library for pyhton

```bash
pip install selenium
```

2. Install selenium web driver

Official download link: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

The script is coded for firefox browser, so I recommend you to use it too. If you want to use a different one, you will need to edit the code.
Really useful page of selenium-pyhton if you want to work on your own and learn more: https://selenium-python.readthedocs.io/getting-started.html#

3. Change your username and password from IgCommentBot.py

```pyhton
name = "your username"
passw = "your password"
```
Make sure you don't use your main account and 2FA is not activated.

4. Change the url of the post you want

```python
url = "https://www.instagram.com/p/blablabla/"
```
5. Change the comment you want to spam

```python
yourcomment = "sample comment"
```
6. Define the waiting time in seconds between each comment
```python
waitingtime = 10
```
7. Have your browser saved instagram cookies?

if so, set this variable to true.
```python
savedcookies = false
```
8. No more config. Run the script
```bash
python3 IgCommentBot.py
```
9. It's highly probable you will get errors in the future because instagram changed their config. Try to find the new path to the elements.

10. Use ctrl + c to stop the script


[^note]:
    Only for learning purposes :)
