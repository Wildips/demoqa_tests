from model.pages.registration_page import RegistrationPage


def test_submit_student_registration_form():
    # ARRANGE
    registration_page = RegistrationPage()
    registration_page.open('/automation-practice-form')

    # ACTIONS
    registration_page.fill_first_name('Some')
    registration_page.fill_last_name('User')
    registration_page.fill_email('some@user.io')
    registration_page.choose_gender('Female')
    registration_page.fill_mobile('8800008800')
    registration_page.fill_date_of_birth('1939', 'September', '1')
    registration_page.fill_subjects('hindi')
    registration_page.choose_hobbies('Reading')
    registration_page.upload_file('test.png')
    registration_page.fill_current_address('Far far away')
    registration_page.choose_state_and_city('rajasthan', 'jaipur')
    registration_page.submit_form()

    # ASSERT
    registration_page.should_registered_user_with('Some User', 'some@user.io', 'Female', '8800008800',
                                                  '01 September,1939', 'Hindi', 'Reading', 'test.png', 'Far far away',
                                                  'Rajasthan Jaipur')
