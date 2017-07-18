from behave import *
import requests

@when('we visit /form')
def visit_form(context):
  context.res = requests.get('https://localhost:8000/form')

@then('we load valid html')
def load_form(context):
  assert context.res