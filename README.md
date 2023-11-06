# SPA-ПРИЛОЖЕНИЕ LMS-СИСТЕМЫ

## ОПИСАНИЕ ПРОЕКТА

Проект представляет собой мощную и гибкую систему, разработанную с помощью **DJANGO REST FRAMEWORK** для создания
современных онлайн-образовательных
платформ. Внимание к деталям и учет лучших практик веб-разработки позволили предоставить широкий спектр
функциональных возможностей, делающих этот проект идеальным выбором для образовательных учреждений, учителей и учеников.
Преподаватели могут загружать свои уроки, создавать курсы, а покупатели могут приобретать их. Модераторы имеют
возможность проверять курсы на ошибки, и учителя могут управлять своими собственными курсами. Кроме того, в проекте
реализована оплата через Stripe.

> Проект разработан в учебных целях с помощью DJANGO REST FRAMEWORK и не рекомендуется для коммерческого использования,
> характеризуется
> возможностью оптимизации кода.

## ОСОБЕННОСТИ ПРОЕКТА

1. **Аутентификация и Авторизация**: Проект обеспечивает надежную аутентификацию и авторизацию пользователей.
   Регистрация, вход и управление учетными записями пользователя выполняются с использованием современных механизмов
   безопасности, включая токены доступа (JWT).
2. **Учителя и Уроки**: Учителя могут загружать образовательные материалы, делая процесс обучения интерактивным и
   максимально привлекательным для учеников. Учителя также могут
   создавать курсы, предоставляя детальное описание, список уроков и установив цену за доступ.
3. **Покупатели и Оплата**: Для покупателей предоставлен удобный механизм приобретения доступа к интересующим их
   курсам или урокам. Интеграция с Stripe гарантирует безопасную и надежную оплату, позволяя
   пользователям совершать
   транзакции с минимальными усилиями.
4. **Модерация Курсов**: Система предоставляет модераторам возможность тщательной проверки созданных курсов на
   соответствие стандартам качества и безопасности. Это обеспечивает высокий стандарт контента, предоставляемого в
   рамках проекта, и обеспечивает качественное обучение.
5. **Детализированная Документация**: Проект сопровождается подробной документацией API, которая доступна в реальном
   времени через интерфейс **Swagger(OpenAPI)** по адресу **http://127.0.0.1:8000/redoc/**. Это обеспечивает
   прозрачность и
   понятность
   использования API и делает проект доступным для разработчиков.
6. **Расширяемость**: Проект разработан с учетом модульной архитектуры, позволяющей легко расширять функциональность и
   добавлять новые возможности. Вы можете интегрировать дополнительные инструменты, модули и API в соответствии с вашими
   потребностями.

## ТРЕБОВАНИЯ К НАСТРОЙКЕ И ЗАПУСКУ ПРОЕКТА

### Настройка

1. **Активация виртуального окружения**: Создайте и активируйте виртуальное окружение с помощью команды в вашем
   терминале. Пример для
   **macOS/Linux**:

   ```commandline
   source venv/Scripts/activate
   ```

2. **Создание файла .env**: Создайте файл с именем **.env** в корневой директории вашего проекта. В файле **.env**
   заполните
   все нижепредставленные переменные окружения:

   ```text
   SECRET_KEY=
   DEBUG=
   POSTGRES_DB=
   POSTGRES_USER=
   POSTGRES_PASSWORD=
   POSTGRES_HOST=
   POSTGRES_PORT=
   PGDATA=
   LANGUAGE_CODE=
   TIME_ZONE=
   MEDIA_URL=
   MEDIA_ROOT=
   STRIPE_PK=
   STRIPE_SK=
   CELERY_BROKER=
   EMAIL_PORT=
   EMAIL_USE_SSL=
   EMAIL_HOST_USER=
   EMAIL_HOST_PASSWORD=
   ```

### ЗАПУСК ПРОЕКТА

1. **Запуск проекта**: Для запуска Django проекта необходимо собрать Docker-контейнер, выполнив комманду:
   ```commandline
   docker-compose build
   ```
   Следующим шагом является запуск ранее созданного контейнера. Для этого выполните команду:
   ```commandline
   docker-compose up
   ``` 
2. **Использование проекта**: Откройте веб-браузер и перейдите по адресу, указанному в консоли
   (обычно **http://127.0.0.1:8000/**).
   > Проведите тестирование различных функциональностей вашего проекта, чтобы удостовериться, что они работают как
   ожидалось.

## РАСПРЕДЕЛЕНИЕ РОЛЕЙ

1. **Покупатель (г. user)**: роль, предназначенная для учеников и всех, кто ищет образовательные возможности. Покупатели
   могут
   искать и просматривать доступные курсы и уроки, приобретать курсы, включая доступ к видеоурокам и учебным материалам.
   > Группа **user** присваивается пользователю после регистрации
2. **Модератор (г. moderator)**: роль, обеспечивающая контроль и качество контента на платформе. Модераторы имеют
   возможность проверять созданные курсы на соответствие стандартам и требованиям, а также управлять процессом
   модерации. Эта роль позволяет поддерживать высокий стандарт образовательных материалов и обеспечивать безопасность
   для всех пользователей платформы.
   > Группу **moderator** необходимо устанавливать через административную панель Django
3. **Учитель  (г. teacher)**: роль для образовательных экспертов, которые создают и предоставляют уроки и курсы. Учителя
   могут загружать образовательные материалы, включая видеоуроки, делая процесс обучения
   интерактивным и привлекательным. Они также могут создавать курсы, предоставляя подробные описания, список уроков и
   установив цену за доступ к своим материалам. Учителя могут управлять своими курсами и следить за успехами своих
   учеников.
   > Группу **teacher** необходимо устанавливать через административную панель Django

#### УСТАНОВКА РОЛИ ПОЛЬЗОВАТЕЛЮ

1. **Авторизация в административной панели**: Войдите в административную панель вашего Django проекта,
   перейдя по URL-адресу, обычно **http://127.0.0.1:8000/admin/**, и введите свои учетные данные администратора.
2. **Навигация к пользователям**: В административной панели найдите раздел, связанный с управлением пользователями.
3. **Выбор пользователя:** Найдите пользователя, которому вы хотите присвоить определенную группу, и выберите его,
   нажав на его данные.
4. **Редактирование пользователя**: В открывшейся странице редактирования пользователя вы должны найти раздел "Группы"
   который позволяет управлять группами пользователя.
5. **Выбор группы**: В этом разделе вы увидите список доступных групп. Выберите группу, которую вы хотите присвоить
   пользователю.
6. **Сохранение изменений**: После выбора группы, убедитесь, что сохраните изменения, нажав на соответствующую кнопку
   "Сохранить".

## ТЕХНОЛОГИИ

1. **Python 3.x**: Проект основан на языке программирования Python, что обеспечивает чистоту и читаемость кода, а также
   широкие возможности для расширения.
2. **Django**: В качестве фреймворка для разработки веб-приложения используется Django, что обеспечивает
   структурированный и масштабируемый подход к веб-разработке.
3. **Django Rest Framework (DRF)**: DRF применяется для построения API проекта, обеспечивая простоту и гибкость
   взаимодействия с данными.
4. **Stripe API**: Интеграция с Stripe API обеспечивает безопасную и удобную оплату курсов, что делает платформу
   идеальным выбором для онлайн-продажи образовательных материалов.
5. **Celery**: Для выполнения асинхронных задач и улучшения производительности проекта активируется Celery Worker. Это
   позволяет обрабатывать фоновые задачи, такие как отправка уведомлений и обработка длительных операций.
6. **Swagger(OpenAPI)**: Документация API предоставляется с использованием интерфейса Swagger, что упрощает понимание и
   использование API для разработчиков.
7. **Docker**: Для упрощения развертывания и управления приложением в среде контейнеров используется Docker. Docker
   обеспечивает изоляцию и переносимость приложения, что делает процесс развертывания более удобным и надежным.

## СВЯЗЬ

Если у вас возникли вопросы, предложения или потребность в поддержке, не стесняйтесь связаться со мной. Я готов помочь
Вам с вашим проектом и ответить на все Ваши вопросы. Вы можете связаться со мной по следующим контактам:

- Электронная почта: **dima.captan@yandex.ru**
- Telegram: **@Kaverz1n**

> Проект разработан в учебных целях с помощью DJANGO REST FRAMEWORK и не рекомендуется для коммерческого использования,
> характеризуется
> возможностью оптимизации кода.
