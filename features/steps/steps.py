from behave import *
import requests

# This is how we use variables with Behave
@when('we visit the "{page}" page')
def visit_form(context, page):
  context.res = requests.get('http://localhost:8000/' + page)
  context.browser.get('http://localhost:8000/' + page)

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

@then('we see a react component')
def see_component(context):
  assert "id='react'" in context.res.text

@then('we see the header Form')
def see_header_form(context):
  assert '<h1>Form</h1>' in context.res.text

@then('we see the header Chart')
def see_header_chart(context):
  assert '<h1>Chart</h1>' in context.res.text