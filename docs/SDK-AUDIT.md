# Аудит Python SDK

## Статус исправлений — 2026-09-07

Все перечисленные ниже SDK-находки исправлены. Каноническая публичная схема
перегенерирована: **81 операция, 129 схем**. Все три SDK используют побайтово
одинаковую копию; SHA-256 и коммит источника закреплены в `openapi/source.json`.
Сгенерировано **79 поддерживаемых операций / 17 ресурсов**: две отключённые
sessions-management операции исключены по согласованному решению, без удаления
sticky-параметров генерации прокси и без изменения маршрутов бэкенда.

| Находка | Исправление |
| --- | --- |
| PY-01 | Добавлены verify_otp и union TokenPairResponse и OTPChallenge для sync/async login. |
| PY-02 | Invoice корректно разбирает null в package/coupon/country для create/get/list. |
| PY-03 | Поддержаны оба режима User и обе формы Invoice/InvoiceShort. |
| PY-04 | Добавлены тела MFA setup/disable с первичным фактором. |
| PY-05 | Платёжные поля актуализированы; расширяемые enum сохранены. |
| PY-06 | HTTP-ошибки классифицируются до декодирования; ошибки успешного ответа сохраняют status/body/headers/cause/idempotency key. |
| PY-07 | Удалены фиксированные ограничения размера контракта; покрытие и manifest проверяются динамически. |
| BE-01 | Исправлены pk-сигнатуры invoice PDF/pay-link и coupon redeems; добавлены router-регрессии. |
| BE-02 | Удалены публичный sessions-ресурс, его методы и отдельные сгенерированные модели/документы из SDK. |

Проверки SDK: `make quality generate-check` (44 теста, Ruff, mypy, воспроизводимая генерация), сборка wheel/sdist и `twine check`.
Фикстуры форм User/Invoice получены из реальных сериализаторов бэкенда на
синтетических объектах; серверный тест проверяет их соответствие текущему коду.
Тесты SDK проверяют MFA, платежи, вариативные ответы и регрессионные сценарии.
Это локальная проверка, не подтверждение развёртывания в production.

Версии пакетов не изменялись; релизы, теги и публикации пакетов не создавались.
Примеры миграции и MFA: `docs/backend-compatibility.md` внутри репозитория SDK.

## Исходный аудит (до исправлений)

Ссылки на SDK закреплены на исходном коммите. Пути и номера строк бэкенда
сохранены как исторические ориентиры: его исходное рабочее состояние содержало
незакоммиченные изменения.

Далее сохранён исторический отчёт. Его выводы, счётчики, матрица и номера строк
относятся к исходному состоянию и не являются описанием обновлённой SDK.


SDK: `proxyrequest-sdk` 1.0.0, каталог `python-sdk`, HEAD `3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7`.

**Вывод:** синхронные и асинхронные обёртки покрывают старый контракт, но реальные ответы MFA и nullable/вариативные модели вызывают ошибки декодирования. Наиболее опасный сценарий — операция на сервере завершилась, а SDK не смогла разобрать ответ и не сохранила необходимые данные для восстановления.

## Границы и методика

Аудит выполнен 2026-09-07 по рабочим файлам. Бэкенд: `/home/yuri/Projects/papaproxy/api`, HEAD `f10464717b19f98916b45cc25e7405610865957d`, с существующими незакоммиченными изменениями. Выводы относятся к этому рабочему состоянию, а не только к коммиту и не к проверенному production-развёртыванию.

Проверены публичная OpenAPI-схема (`api/openapi.yml`), состав публичного schema URLConf (`api/apps/routing/infrastructure/django/schema.py:35`), router, существенные serializers/viewsets, сгенерированные операции, клиентский транспорт, пагинация, ошибки, подписи webhook и процесс синхронизации схемы. Внутренние/admin API и входящие callback-маршруты платёжных провайдеров не считаются обязательными методами клиентской SDK.

Сохранённый публичный контракт содержит **81 операцию и 127 схем**. Независимая генерация публичной схемы в тестовом окружении также дала 81 операцию и 127 схем. Отдельно проверены оба значения `SITE_PACKAGE_BASED_AUTH`: формы ответов действительно зависят от настройки. Различия числовых ограничений при генерации под SQLite не объявлялись дефектами production-контракта.

Во всех SDK сохранена одна и та же старая схема: **80 операций и 124 схемы**. Сопоставление HTTP-методов, шаблонов путей и публичных обёрток не выявило пропущенных операций из этой старой схемы. Единственная отсутствующая операция относительно текущего публичного списка — `POST /login/otp`. Это номинальное покрытие методов, а не оценка фактической совместимости.

SHA-256 схем:

- текущая API: `423fc57ebe9406a9a1a80ee7acfd8e0827f6196b317af90b0c24f64172e16b03`;
- сохранённая SDK: `0ed69e781aa752ac8e9c9b1974cd82810adbf1fd99a461724bd73432740d8737`.

Поиск выполнен через knowledge graph с проверкой покрытия и чтением исходников. Частично разобранные TypeScript re-export строки проверены непосредственно. Проигрывались синтетические ответы и локальные вызовы serializers/router; обращений к рабочему API, создания пользователей/счетов и изменений реализаций SDK/бэкенда не выполнялось.

Приоритеты: **P1** — блокирует основной сценарий при указанных условиях; **P2** — ограничивает часть API, искажает данные или ухудшает диагностику/сопровождение. Порядок внутри приоритета отражает рекомендуемую последовательность исправлений.


## Находки в SDK

### PY-01 · P1 · HTTP 202 при входе превращается в ошибку и теряет OTP challenge

Парсеры `login_create` и `login_google_create` не имеют ветки 202. При `otp_required` они возвращают `parsed=None`; затем `_response_value()` отклоняет непустой успешный ответ. Обёртка объявляет исключительно `TokenPairResponse`. Метода `POST /login/otp` нет.

Воспроизведено для `Client` и `AsyncClient`:

```text
ApiError: ProxyRequest returned an unreadable HTTP 202 response.
status_code=None
raw_body=b''
```

Challenge недоступен даже из ошибки: она создаётся без HTTP-метаданных. Таким образом, штатный вход аккаунта с включённой MFA остановится после проверки пароля/Google credential.

Источники: [login parser](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/api/authorization/login_create.py#L40), [Google parser](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/api/authorization/login_google_create.py#L41), [обработка parsed=None](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/client.py#L84), [AuthorizationResource](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/resources/authorization.py#L29), серверный OTP endpoint (`api/apps/core/authentication/api.py:57`).

Исправление: добавить `OTPChallenge`, `VerifyOTPRequest`, sync/async метод завершения входа и результат `TokenPairResponse | OTPChallenge`. Для неизвестного успешного статуса сохранять исходный ответ, даже если типизированная модель ещё отсутствует.

### PY-02 · P1 · Допустимые null в счёте ломают create/get/list invoices

`Invoice.from_dict()` без проверки вызывает:

```python
package = PackageShort.from_dict(d.pop("package"))
country = Country.from_dict(d.pop("country"))
coupon = CouponShort.from_dict(d.pop("coupon"))
```

На сервере все три связи nullable. `InvoiceSerializer` на несохранённом объекте обычного пополнения баланса реально вернул `package=null, country=null, coupon=null`. Отсутствие купона также является нормальным случаем покупки пакета.

Локальные проверки с валидной базовой моделью и поочерёдным `null` для каждой связи воспроизвели:

```text
ApiError: Unable to decode the ProxyRequest API response.
cause: TypeError("'NoneType' object is not iterable")
```

Затронуты создание, получение и весь список счетов, если хотя бы один элемент содержит такой `null`. В async используется тот же generated parser.

Особенно существенно для `invoices.create()`: сервер может уже создать счёт, но ошибка парсинга попадает в общий `except Exception`, который не прикрепляет ни тело ответа, ни автоматически созданный idempotency key. Повторный вызов без сохранённого явного ключа затрудняет безопасное восстановление и может повторить создание.

Источники: [Invoice.from_dict](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/models/invoice.py#L222), [обёртки invoice](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/resources/invoices.py#L32), [общая ветка ошибки](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/client.py#L240), InvoiceSerializer (`api/apps/billing/api/serializers.py:28`), серверная схема Invoice (`api/openapi.yml:16871`).

Исправление: обозначить nullable-связи в серверной схеме, регенерировать модели как `... | None`, сохранить HTTP-контекст и idempotency key при ошибках декодирования. Нужны тесты без купона, без страны, на balance invoice и на список со смешанными вариантами.

### PY-03 · P1 · Ни одна фиксированная пара User/Invoice не покрывает оба режима backend

| Настройка | Реальное поведение | Ошибка текущей SDK |
| --- | --- | --- |
| `SITE_PACKAGE_BASED_AUTH=True` | User содержит `orders`, не содержит пяти плоских полей данных/пароля | `User.from_dict()` требует `data` и остальные поля; `KeyError('data')` |
| `SITE_PACKAGE_BASED_AUTH=False` | чтение счетов использует `InvoiceShortSerializer`, без `package`, `user_id`, `type`, `payment_url` | `Invoice.from_dict()` требует полный счёт; `KeyError('package')` |

Проверены фактический набор полей `UserSerializer()` и `InvoicesViewSet.get_serializer_class()` под обоими флагами. Затем синтетические ответы этих форм пропущены через публичные методы SDK: обе ошибки воспроизведены. Контрольный User с плоскими полями успешно разобран.

При True затронуты `profile.get/update`, `users.get/list/create/update/reset_password` и другие ответы типа User. При False затронуты `invoices.get/list`. Создание invoice отдельно возвращает полный `InvoiceSerializer`, поэтому не следует переносить ошибку короткой формы на все действия без различия; для create действует PY-02.

Источники: динамические поля User (`api/apps/core/api/serializers/users.py:269`), выбор serializer счёта (`api/apps/billing/api/viewsets.py:121`), InvoiceShortSerializer (`api/apps/billing/api/serializers.py:101`), [обязательное чтение data](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/models/user.py#L320), [обязательное чтение package](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/models/invoice.py#L228).

Исправление: определить стабильный общий контракт либо явные варианты моделей для двух режимов; учитывать отсутствие поля отдельно от `null`. Простая синхронизация сохранённой серверной схемы недостаточна: в ней уже есть неотражённая конфигурационная вариативность.

### PY-04 · P1 · setup_two_factor не принимает body, disable-модель не описывает первичный фактор

`profile.setup_two_factor()` принимает только `accept_language` и посылает пустой POST. Сервер требует пароль либо Google credential, а при замене уже включённой MFA — также текущий код. Модель отключения описывает только `code`, поэтому обычный вызов из старого контракта не может отключить активную MFA.

Источники: [setup_two_factor](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/resources/profile.py#L168), [TwoFactorDisableRequest](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/models/two_factor_disable_request.py#L18), TwoFactorViewSet (`api/apps/core/api/viewsets.py:1522`), проверка первичного фактора (`api/apps/core/authentication/service.py:192`).

Для disable есть работающий низкоуровневый обход через `additional_properties`:

```python
body = TwoFactorDisableRequest(code="492031")
body["password"] = "current-password"
client.profile.disable_two_factor(body=body)
```

Для setup нужен `client.request("POST", "/profile/2fa/setup", json={...})`, поскольку фасад вовсе не принимает body. Исправление: добавить типизированные поля/модель setup и обновить обе sync/async обёртки. Подтверждение по коду остаётся доступным; после изменений MFA следует учитывать отзыв прежних JWT.

### PY-05 · P2 · Платёжные модели устарели, но новые enum-значения уже поддерживаются

Не хватает именованных вариантов gateway, поля `payment_currency` в конструкторе invoice request, полей `currency`, `payment_amount`, `payment_currency`, `provider_checkout_id`, `provider_payment_id`, `checkout_status`, `fx_*` в invoice response и `payment_gateways` в settings. Остались устаревшие `coinbase_charge_id` и `coingate_order_token`.

Однако `_missing_()` в generated enums специально принимает неизвестные строки. Утверждать, что Python отвергает `whitepay`, было бы неправильно. Воспроизведены успешные разбор нового gateway и сохранение новых response-полей в `additional_properties`, если остальные обязательные поля ответа корректны.

Рабочий обход запроса:

```python
body = InvoiceCreateRequest(
    gateway=InvoiceCreateRequestGatewayEnum("whitepay"),
    amount=500,
)
body["payment_currency"] = "UAH"
# to_dict(): {"payment_currency":"UAH","gateway":"whitepay","amount":500}
```

Источники: [InvoiceCreateRequest](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/models/invoice_create_request.py#L21), [расширяемый enum](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/models/invoice_create_request_gateway_enum.py#L4), [генератор enum](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/scripts/generate.py#L179), серверный запрос (`api/apps/billing/api/serializers.py:126`), новые платёжные метаданные (`api/openapi.yml:18607`).

Исправление: обновить модели/документацию, сохранив forward-compatible enum и additional properties. Не удалять уже полезное поведение ради закрытого набора значений.

### PY-06 · P2 · Ошибки декодирования маскируют HTTP-статус, тело и контекст операции

Generated endpoints разбирают тело до того, как клиент получает объект `Response`. Например, HTML вместо JSON на **документированном HTTP 400** вызывает `JSONDecodeError`; общий `except Exception` создаёт `ApiError(kind=unexpected)` с `status_code=None`, пустым `raw_body`, без request ID и idempotency key.

Это воспроизведено на login с `400 <html>bad request</html>`. Причина доступна как `__cause__`, но HTTP-контекст уже потерян. Аналогичный дефект усложняет восстановление после успешной серверной операции, ответ которой не соответствует старой модели.

Источники: [порядок build/parse response](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/_generated/api/authorization/login_create.py#L58), [sync обработка](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/client.py#L224), [async обработка](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/src/proxyrequest_sdk/client.py#L413).

Исправление: сначала сохранять транспортный ответ и классифицировать HTTP-ошибку, затем декодировать успешный payload; в decoding exception прикреплять исходные status/headers/body/key. Сам по себе неизвестный HTTP 502 уже корректно становится server ApiError с сохранённым payload — это проверено на ошибке checkout с `invoice_id` и `retryable`.

### PY-07 · P2 · Синхронизация схемы жёстко привязана к устаревшему числу методов

`scripts/sync_openapi.py` принимает только 80 операций и 124 схемы. Запуск на текущем серверном файле завершается до записи:

```text
Unexpected contract size: 81 operations and 127 schemas.
```

Контрактные тесты тоже проверяют собственную сохранённую схему и наличие 80 generated sync/async фасадов. Это полезная проверка целостности генерации, но она не обнаруживает отставание от бэкенда.

Источники: [validate](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/scripts/sync_openapi.py#L37), [contract tests](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/tests/test_contract.py#L27), [manifest](https://github.com/proxyrequest/python-sdk/blob/3424a4e62ac7b8d1d5309bd4d3c4109f90da16c7/openapi/source.json#L1).

В отличие от TypeScript SDK, hash и счётчики Python manifest соответствуют реально сохранённой старой схеме. Исправление: принимать эволюцию публичного контракта с проверкой его назначения, анализировать семантический diff и обновлять mapping/модели. Добавить проверки against выбранного backend snapshot, а не только собственной копии.

## Проблемы бэкенда, влияющие на эту SDK

### BE-01 · P1 · Три публичных detail-маршрута падают при передаче `pk`

| HTTP-маршрут | Обработчик |
| --- | --- |
| `GET /invoices/{id}/download/pdf` | `InvoicesViewSet.download_pdf(self, request)` |
| `GET /invoices/{id}/pay` | `InvoicesViewSet.pay_link(self, request)` |
| `GET /coupons/{id}/redeems` | `CouponsViewSet.redeems(self, request)` |

DRF router передаёт идентификатор как `pk`, но обработчики не принимают ни `pk`, ни `**kwargs`. Через настоящий `django.urls.resolve()` и вызов соответствующего view воспроизведены:

```text
TypeError: InvoicesViewSet.download_pdf() got an unexpected keyword argument 'pk'
TypeError: InvoicesViewSet.pay_link() got an unexpected keyword argument 'pk'
TypeError: CouponsViewSet.redeems() got an unexpected keyword argument 'pk'
```

При проверке были заменены только `initial()` и обработка исключения, чтобы изолировать диспетчеризацию от авторизации и БД. Это подтверждённая ошибка вызова обработчика, а не результат запроса к развёрнутому серверу. SDK формируют правильные HTTP-методы и пути; исправление требуется на стороне API.

Источники: InvoicesViewSet (`api/apps/billing/api/viewsets.py:197`), CouponsViewSet.redeems (`api/apps/marketing/api/viewsets.py:444`), регистрация router (`api/apps/routing/infrastructure/django/public.py:95`).

Исправление: принимать `pk=None` или `*args, **kwargs`; добавить HTTP-тесты всех трёх detail-action через router. После этого повторить интеграционные проверки SDK для платёжной ссылки, PDF и погашений купона.

### BE-02 · P2 · Управление sessions отключено, хотя SDK обещает успешные ответы

Авторизованные `GET /sessions` и `DELETE /sessions/{id}` безусловно вызывают `_unavailable()` и возвращают 403 с причиной `errors.proxy.session_ownership_unavailable`. Актуальная схема уже не содержит успешного ответа для этих операций; сохранённая схема SDK всё ещё содержит старые `SessionListResponse` / `SessionDeleteResponse`.

Это ограничение текущего API, а не неправильный ключ пользователя. Следует отметить методы как временно недоступные/deprecated и обновить документацию. Возвращать возможность управления сессиями нужно только после реализации проверки владельца на сервере.

Источник: SessionViewSet (`api/apps/core/api/viewsets.py:1622`).


## Минимальное локальное воспроизведение OTP

Из текущего каталога, без сетевого обращения:

```bash
python-sdk/.venv/bin/python - <<'PY'
import httpx
from proxyrequest_sdk import ApiError, Client
from proxyrequest_sdk.models import LoginRequest

transport = httpx.MockTransport(lambda request: httpx.Response(
    202,
    json={"status": "otp_required", "challenge": "audit", "expires_in": 300},
))
http = httpx.Client(
    base_url="https://api.proxyrequest.com/api/v1",
    transport=transport,
)
with Client.anonymous(http_client=http) as client:
    try:
        client.authorization.login(
            body=LoginRequest(email="audit@example.com", password="synthetic")
        )
    except ApiError as error:
        print(str(error), error.status_code, error.raw_body)
http.close()
PY
```

## Проверки и приоритет исправлений

`.venv/bin/python -m pytest -q`: **24 passed**. Дополнительно проверены sync/async OTP 202, пустой 204, JSON 502, HTML 400, каждый nullable invoice field, короткий Invoice, оба User-режима и новый gateway через enum.

Подтверждены корректные заголовки Static/Bearer, дополнительные JSON-поля, единый idempotency key на повторные попытки в штатных сценариях, ETag/If-Match, пагинация через offset, файлы и совместимость HMAC webhook с серверным алгоритмом (`api/apps/webhooks/management/commands/send_webhook_events.py:55`). Ошибка `id_path` в `users_orders_list` не обнаружена: это внутреннее переименование, которое корректно подставляется в `/users/{id}/orders`.

Порядок: исправить серверные detail-action и контракты моделей; устранить nullable/варианты User/Invoice и потерю HTTP-контекста; внедрить MFA; обновить платежи и schema sync. Проверить реальные успешные ответы создания пользователя/счёта, а не только mocked HTTP-ошибки и наличие методов.

## Полная матрица методов

Каждый указанный метод существует и у `Client`, и у `AsyncClient`; доступны варианты `*_with_response`. Наличие метода не отменяет перечисленных выше ограничений.

| HTTP | Путь | Метод SDK |
| --- | --- | --- |
| GET | `/affiliates` | `affiliates.list()` |
| GET | `/affiliates/rewards` | `affiliates.list_rewards()` |
| GET | `/affiliates/rewards/overall` | `affiliates.get_rewards_overall()` |
| GET | `/analytics/{id}/transactions` | `analytics.get_transactions()` |
| GET | `/analytics/connections` | `analytics.get_connections()` |
| GET | `/analytics/domains` | `analytics.list_domains()` |
| GET | `/analytics/feed` | `analytics.list_feed()` |
| GET | `/analytics/logs` | `analytics.list_logs()` |
| GET | `/analytics/overall` | `analytics.get_overall()` |
| GET | `/api-keys` | `api_keys.list()` |
| POST | `/api-keys` | `api_keys.create()` |
| DELETE | `/api-keys/{id}` | `api_keys.delete()` |
| GET | `/coupons` | `coupons.list()` |
| POST | `/coupons` | `coupons.create()` |
| GET | `/coupons/{id}` | `coupons.get()` |
| PUT | `/coupons/{id}` | `coupons.replace()` |
| PATCH | `/coupons/{id}` | `coupons.update()` |
| DELETE | `/coupons/{id}` | `coupons.delete()` |
| GET | `/coupons/{id}/redeems` | `coupons.list_redeems()` |
| POST | `/coupons/calculate-price` | `coupons.calculate_price()` |
| GET | `/integrations/telegram/connection` | `telegram.get_connection()` |
| PATCH | `/integrations/telegram/connection` | `telegram.update_connection()` |
| DELETE | `/integrations/telegram/connection` | `telegram.delete_connection()` |
| POST | `/integrations/telegram/link` | `telegram.create_link()` |
| GET | `/invoices` | `invoices.list()` |
| POST | `/invoices` | `invoices.create()` |
| GET | `/invoices/{id}` | `invoices.get()` |
| DELETE | `/invoices/{id}` | `invoices.delete()` |
| GET | `/invoices/{id}/download/pdf` | `invoices.download_pdf()` |
| GET | `/invoices/{id}/pay` | `invoices.get_payment_link()` |
| GET | `/locations/asn` | `locations.list_asns()` |
| GET | `/locations/cities` | `locations.list_cities()` |
| GET | `/locations/cities/{id}` | `locations.get_city()` |
| GET | `/locations/continents` | `locations.list_continents()` |
| GET | `/locations/continents/{id}` | `locations.get_continent()` |
| GET | `/locations/countries` | `locations.list_countries()` |
| GET | `/locations/countries/{id}` | `locations.get_country()` |
| GET | `/locations/isps` | `locations.list_isps()` |
| GET | `/locations/regions` | `locations.list_regions()` |
| GET | `/locations/regions/{id}` | `locations.get_region()` |
| POST | `/login` | `authorization.login()` |
| POST | `/login/google` | `authorization.login_with_google()` |
| POST | `/login/otp` | **Отсутствует — PY-01** |
| GET | `/news` | `news.list()` |
| GET | `/orders` | `orders.list()` |
| GET | `/orders/{id}` | `orders.get()` |
| PATCH | `/orders/{id}` | `orders.update_auto_renewal()` |
| DELETE | `/orders/{id}` | `orders.delete()` |
| GET | `/packages` | `packages.list()` |
| GET | `/packages/commissions` | `packages.list_commissions()` |
| GET | `/profile` | `profile.get()` |
| PATCH | `/profile` | `profile.update()` |
| DELETE | `/profile` | `profile.delete()` |
| POST | `/profile/2fa/confirm` | `profile.confirm_two_factor()` |
| POST | `/profile/2fa/disable` | `profile.disable_two_factor()` |
| POST | `/profile/2fa/setup` | `profile.setup_two_factor()` |
| GET | `/profile/2fa/status` | `profile.get_two_factor_status()` |
| POST | `/profile/change-password` | `profile.change_password()` |
| POST | `/proxies/generate` | `proxies.generate()` |
| POST | `/recover-password` | `authorization.recover_password()` |
| POST | `/refresh` | `authorization.refresh()` |
| POST | `/reset-password` | `orders.reset_password()` |
| GET | `/rewards` | `rewards.list()` |
| POST | `/rewards/claim` | `rewards.claim()` |
| GET | `/sessions` | `sessions.list()` |
| DELETE | `/sessions/{id}` | `sessions.delete()` |
| GET | `/settings` | `settings.get()` |
| POST | `/signup` | `authorization.signup()` |
| GET | `/users` | `users.list()` |
| POST | `/users` | `users.create()` |
| GET | `/users/{id}` | `users.get()` |
| PATCH | `/users/{id}` | `users.update()` |
| DELETE | `/users/{id}` | `users.delete()` |
| POST | `/users/{id}/data/add` | `users.add_data()` |
| POST | `/users/{id}/data/subtract` | `users.subtract_data()` |
| GET | `/users/{id}/orders` | `users.list_orders()` |
| POST | `/users/{id}/password` | `users.reset_password()` |
| GET | `/webhooks` | `webhooks.list()` |
| POST | `/webhooks` | `webhooks.create()` |
| GET | `/webhooks/{id}` | `webhooks.get()` |
| DELETE | `/webhooks/{id}` | `webhooks.delete()` |
