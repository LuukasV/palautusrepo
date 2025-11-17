*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jussi  salasana123
    Output Should Contain  New user registered
  
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  mikko123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  kek  mikko123
    Output Should Contain  Selected username is not long enough

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  m1kko  mikko123
    Output Should Contain  Selected username is in incorrect format

Register With Valid Username And Too Short Password
    Input Credentials  mikko  k
    Output Should Contain  Selected password is not long enough

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  mikko  mikko
    Output Should Contain  Selected password must have both numbers and letters

*** Keywords ***
Input New Command and Create User
    Create User  kalle  kalle123
    Input New Command