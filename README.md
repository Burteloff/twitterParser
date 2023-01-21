Short Description of the project:

This code creates a "Twitter" class that uses Selenium and webdriver to automate the login and navigation to the Twitter home page. It allows easy login to your account and browsing the home page without the need for manual input of login credentials.

Этот код создает класс "Twitter", который использует Selenium и webdriver для автоматизации входа и перехода на домашнюю страницу Twitter. Он позволяет легко войти в свой аккаунт и просматривать домашнюю страницу без необходимости ручного ввода логина и пароля.

Instructions for use:

Install Selenium and webdriver.
Download and install the webdriver for your browser (in this case Edge).
Open the code file and specify the path to the webdriver in the executable_path variable.
Enter your login and password in the login and password variables respectively.
Run the code.
Note:

The project uses Edge webdriver, if you want to use another browser you need to replace Edge with the desired browser in the line self.driver = webdriver.Edge(executable_path=executable_path)
The project currently works with the Twitter interface version, in case of interface changes the code may stop working and it will need to be updated.


На русском
Инструкции по использованию:

Установите Selenium и webdriver.
Скачайте и установите webdriver для вашего браузера (в данном случае Edge)
Откройте файл с кодом и укажите путь к webdriver в переменной executable_path.
Введите свой логин и пароль в переменные login и password соответственно.
Запустите код.
Примечание:

Проект использует Edge webdriver, если вы хотите использовать другой браузер, то нужно заменить Edge на нужный браузер в строке self.driver = webdriver.Edge(executable_path=executable_path)
Проект работает на данный момент с версией интерфейса Twitter, в случае изменения интерфейса код может перестать работать и его необходимо будет обновить.
