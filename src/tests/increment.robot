*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
When button pressed it increments the right amount
    Go To  ${HOME_URL}
    Input Text  title  10
    Click Button  Aseta
    Page Should Contain  nappia painettu 10 kertaa