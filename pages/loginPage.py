from utils.reusableMethods import *

def enterUserName(data):
    return enterById("txtUsername", data)

def enterPassword(data):
    return enterById("txtPassword", data)

def clickLoginButton():
    return clickById("btnLogin")

def VerifyHomePage(data):
    verifyText("welcome", data)