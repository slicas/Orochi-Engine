import pyray as pr
import webview



def open_url(url):
    pr.open_url(url)


def web_view(title,file):
    webview.create_window(title,file)
    webview.start()