from selene.support.shared import browser
from selene import have


def test_submit_student_registration_form():
    # ARRANGE
    browser.open('/automation-practice-form').wait_until(have.title('DEMOQA'))  # noqa

    # ACTIONS
    browser.element('[id="firstName"]').type('Some')
    browser.element('[id="lastName"]').type('User')
    browser.element('[id="userEmail"]').type('some@user.io')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('8800008800')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('option[value="1939"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('option[value="9"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--020"]').click()
    browser.element('[id="subjectsInput"]').click().type('maths').press_enter().type('hindi').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[class="form-control-file"]').send_keys('/home/sun/my_edu/qa_guru/g8_l5/image/test.png')
    browser.element('[id="currentAddress"]').type('Far far away')
    browser.element('[id="react-select-3-input"]').type('rajasthan').press_enter()
    browser.element('[id="react-select-4-input"]').type('jaipur').press_enter()
    browser.element('[id="submit"]').click()

    # ASSERT
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').all(
        'tr td:nth-child(2)').should(have.texts
        (
        'Some User',
        'some@user.io',
        'Male',
        '8800008800',
        '20 October,1939',
        'Maths, Hindi',
        'Sports, Reading',
        'test.png',
        'Far far away',
        'Rajasthan Jaipur'
    ))

