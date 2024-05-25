# Локаторы для тестов


name_input = ".//label[text()='Имя']/following-sibling::input"         # поле ввода "Имя"
email_input = ".//label[text()='Email']/following-sibling::input"      # поле ввода "Email"
password_input = ".//label[text()='Пароль']/following-sibling::input"  # поле ввода "Пароль"
registration_button = ".//button[text()='Зарегистрироваться']"         # кнопка "Зарегистрироваться"
pass_validation = ".//p[text()='Некорректный пароль']"                 # валидация поля "Пароль"
fillings_tab = ".//span[contains(text(),'Начинки')]"                   # вкладка "Начинки"
fillings_header = ".//h2[text()='Начинки']"                            # заголовок "Начинки" на вкладке "Начинки"
buns_tab = ".//span[contains(text(),'Булки')]"                         # вкладка "Булки"
buns_header = ".//h2[text()='Булки']"                                  # заголовок "Булки" на вкладке "Булки"
sauces_tab = ".//span[contains(text(),'Соусы')]"                       # вкладка "Соусы"
sauces_header = ".//h2[text()='Соусы']"                                # заголовок "Соусы" на вкладке "Соусы"
sign_in_account_button = ".//button[text()='Войти в аккаунт']"         # кнопка "Войти в аккаунт"
login_button = ".//button[text()='Войти']"                             # кнопка "Войти"
login_link = ".//a[text()='Войти']"                                    # ссылка "Войти"
logout_button = ".//button[text()='Выход']"                            # кнопка "Выход"
personal_account_button = ".//p[text()='Личный Кабинет']"              # кнопка "Личный кабинет"
name_info = ".//input[@value='Alina']"                                 # поле с именем
email_info = ".//input[@value='adementyeva8123@yandex.ru']"            # поле с email
password_info = ".//input[@value='*****']"                             # поле с паролем
constructor_button = ".//p[text()='Конструктор']"                      # кнопка "Конструктор"
make_an_order_button = ".//button[text()='Оформить заказ']"            # кнопка "Оформить заказ"


