Feature: User Authentication and File Upload

  Background:
    Given I open the application

  # ---------- Signup ----------
  Scenario: User signs up with valid credentials
    When I sign up with valid username and password
    Then I should see a signup success message

  # ---------- Login ----------
  Scenario: User tries to login with invalid credentials
    When I login with invalid username and password
    Then I should see an invalid login message

  Scenario: User logs in with valid credentials
    When I login with valid username and password
    Then I should see a login success message

  # ---------- File Upload ----------
  Scenario Outline: Upload a file lesser than 5MB
    When I login with valid username and password
    Then I should see a login success message
    When I upload a file "<file_path>"
    Then I should see a file upload success message
    Examples:
      | file_path |
      | E:\\Example\\Notes\\Indee\QA Lead Take Home Assignment\\Automation\\screenshots\\login_page_failure_20250818-211913.png |
      | E:\\Example\\Notes\\Indee\\QA Lead Take Home Assignment\\Automation\\screenshots\\new_employee_failuress_20250818-230752.png |
      | E:\\Example\\Notes\\Indee\\QA Lead Take Home Assignment\\Automation\\screenshots\\new_employee_failuress_20250819-000929.png |

  Scenario Outline: Upload a file larger than 5MB
    When I login with valid username and password
    Then I should see a login success message
    When I upload a file "<file_path>"
    Then I should see a file too large error

    Examples:
      | file_path                                                                 |
      | E:\\Example\\Notes\\Indee\\QA Lead Take Home Assignment\\Automation\\screenshots\\Submission_1.jpeg |
      | E:\\Example\\Notes\\Indee\\QA Lead Take Home Assignment\\Automation\\screenshots\\NIK_0051.JPG |