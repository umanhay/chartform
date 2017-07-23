from behave import *
import requests


@when('we visit /form')
def visit_form(context):
  context.res = requests.get('http://localhost:8000/form')

@then('we get a successful http response')
def get_valid_response(context):
  assert context.res.status_code == 200

@then('we load valid html')
def load_form(context):
  assert '<!DOCTYPE html>' in context.res.text
  assert '</html>' in context.res.text

@then('we see a form')
def see_form(context):
  assert '<form>'in context.res.text
  assert '</form>' in context.res.text