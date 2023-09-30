from selene.support.shared import browser
from selene import be, have

import os


def test_submit_student_registration_form():
    # ARRANGE
    browser.open('/automation-practice-form').wait_until(have.title('DEMOQA'))  # noqa

    # ACTIONS
    browser.element('[id="firstName"]').should(have.attribute('placeholder').value('First Name')).type('Some')
    browser.element('[id="lastName"]').should(have.attribute('placeholder').value('Last Name')).type('User')
    browser.element('[id="userEmail"]').should(have.attribute('placeholder').value('name@example.com')).type(
        'some@user.io')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(have.attribute('placeholder').value('Mobile Number')).type(
        '8800008800')

    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('option[value="1939"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('option[value="9"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--020"]').click()

    browser.element('[id="subjectsInput"]').should(be.blank).click().type('maths').press_enter().type(
        'hindi').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()

    # browser.element('#uploadPicture').click().with_(timeout=browser.config.timeout * 2).send_keys(os.path.abspath('image/test.png'))
    # browser.element('[for="uploadPicture"]').click().with_(timeout=browser.config.timeout * 2).send_keys(os.path.abspath('image/test.png'))

    browser.element('[id="currentAddress"]').should(have.attribute('placeholder').value('Current Address')).type(
        'Far far away')

    browser.element('#react-select-3-input').type('rajasthan').press_enter()
    browser.element('#react-select-4-input').type('jaipur').press_enter()

    browser.element('[id="submit"]').click()

    # ASSERT
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
        (
        'Some User',
        'some@user.io',
        'Male',
        '8800008800',
        '20 October,1939',
        'Maths, Hindi',
        'Sports, Reading',
        '',
        'Far far away',
        'Rajasthan Jaipur'
    ))
