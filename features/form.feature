Feature: main form page

  Scenario: load a page
    when we visit /form 
    then we get a successful http response
    and we load valid html
    and we see a react component