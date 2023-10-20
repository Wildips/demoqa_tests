import resource

from selene import have, command
from selene.support.shared import browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('[id="firstName"]')
        self.last_name = browser.element('[id="lastName"]')

    @staticmethod
    def open(page):
        browser.open(page).wait_until(have.title('DEMOQA'))

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    @staticmethod
    def fill_email(value):
        browser.element('[id="userEmail"]').type(value)

    @staticmethod
    def choose_gender(value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    @staticmethod
    def fill_mobile(value):
        browser.element('[id="userNumber"]').type(value)

    @staticmethod
    def fill_date_of_birth(year, month, day):
        if len(str(day)) == 1:
            day = f"00{str(day)}"
        else:
            day = f"0{str(day)}"
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('[class="react-datepicker__month-select"]').type(month)
        browser.element('[class="react-datepicker__year-select"]').type(year)
        browser.element(f'.react-datepicker__day--{day}:not(.react-datepicker__day--outside-month)').click()

    @staticmethod
    def fill_subjects(value):
        browser.element('[id="subjectsInput"]').click().type(value).press_enter()

    @staticmethod
    def choose_hobbies(value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    @staticmethod
    def should_registered_user_with(full_name, email, gender, phone_number, date_of_birth, subject, hobby, picture,
                                    address, state_and_city):
        browser.element('[class="table table-dark table-striped table-bordered table-hover"]').all(
            'tr td:nth-child(2)').should(
            have.texts(full_name, email, gender, phone_number, date_of_birth, subject, hobby, picture, address,
                       state_and_city))

    @staticmethod
    def upload_file(image_name):
        # browser.element('[id="uploadPicture"]').set_value(os.path.realpath(f'image/{image_name}'))
        browser.element('[id="uploadPicture"]').set_value(resource.path(image_name))

    @staticmethod
    def choose_state_and_city(state, city):
        browser.element('[id="react-select-3-input"]').type(state).press_enter()
        browser.element('[id="react-select-4-input"]').type(city).press_enter()

    @staticmethod
    def fill_current_address(value):
        browser.element('[id="currentAddress"]').type(value)

    @staticmethod
    def submit_form():
        browser.element('[id="submit"]').perform(command.js.click)
