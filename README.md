# PWAF (Python Webdriver Automation Framework)

## _Prerequisite:_

1. Python
2. pip
3. Selenium/WebDriver
4. nosetests & nose-html-reporting
5. Browsers (Firefox, Chrome, IE)
6. Respective Browser drivers
7. Pycharm

### How to run?

**Test scripts can be executed by nosetests:**

>nosetests -s -v --nologcapture <test-script.py>

>e.g.: `nosetests -s -v --nologcapture checkbox_page_test.py`

**Get Test-reports:**

>nosetests -s -v --nologcapture --with-html --html-report=<test-report-file-path> <test-script.py>

>e.g.: `nosetests -s -v --nologcapture --with-html --html-report=test_report.html checkbox_page_test.py`


