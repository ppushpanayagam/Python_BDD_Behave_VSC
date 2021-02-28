from behave import given
from pages.loginPage import *
 
@given('the user launch the application')
def step_function(context):  
    invokeApp()
    
@when('the user login with valid credentials')
def login_with_validDetails(context):
    enterUserName("Admin")
    enterPassword("admin123")
    clickLoginButton()
    
@then('user should be able to login successfully')
def login_Validation(context):
    VerifyHomePage("Welcome Paul")