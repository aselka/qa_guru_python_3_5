import os
from selene import have
from selene.support.shared import browser


def test_submit_form():
    browser.element('#firstName').type('Asel')
    browser.element('#lastName').type('Bisengalieva')
    browser.element('#userEmail').type('test@email.com')
    browser.element('[name=gender][value=Female]+label').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type("June")
    browser.element('.react-datepicker__year-select').type("1995")
    browser.element('[aria-label=Choose Saturday, June 24th, 1995]').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()
    
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'files/foto.jpg')))
    browser.element('#currentAddress').type('Saratov')
    
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    
    browser.element('#submit').press_enter()

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
         'Asel Bisengalieva',
         'test@email.com',
         'Female',
         '1234567890',
         '24 June,1995',
         'Computer Science',
         'Reading',
         'foto.jpg',
         'Saratov',
         'Haryana Panipat'))
