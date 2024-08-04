import os.path

from selene import browser, have, command


def test_demoga_form():
    browser.open('/automation-practice-form')
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('footer').perform(command.js.remove)
    browser.element('#firstName').type('Sergei')
    browser.element('#lastName').type('Gorobets')
    browser.element('#userEmail').type('sergei.gorobets.vit@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('7985491026')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="9"]').click()
    browser.element('.react-datepicker__year-select option[value="1996"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--007').click()
    browser.element('#subjectsInput').type('Biology').press_tab()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('imeg.jpg'))
    browser.element('#currentAddress').type('Moscow')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()
    browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
        'Sergei Gorobets',
        'sergei.gorobets.vit@gmail.com',
        'Male',
        '7985491026',
        '07 October,1996',
        'Biology',
        'Music',
        'imeg.jpg',
        'Moscow',
        "Haryana Karnal"
    ))
