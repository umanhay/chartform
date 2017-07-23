Feature: chart form app

  Scenario: load the form page
    when we visit the "form" page
    then we get a successful http response
    and we load valid html
    and we see a react component
    and we see the header Form

  Scenario: load the chart page
    when we visit the "chart" page
    then we get a successful http response
    and we load valid html
    and we see a react component
    and we see the header Chart