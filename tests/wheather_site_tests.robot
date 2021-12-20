*** Settings ***
Library    ../custom_libraries/CustomKeywords.py

Test Template   Verify city name on the page after city input

*** Test Cases ***                                          CITY_NAME
Verify city name on the page after city input - Moscow      Moscow
Verify city name on the page after city input - Minsk       Minsk
Verify city name on the page after city input - Belgrade    Belgrade

*** Keywords ***
Verify city name on the page after city input
    [Arguments]    ${city_name}
    verify city name after change   ${city_name}