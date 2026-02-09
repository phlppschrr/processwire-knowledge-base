# Wire: api-helpers

Source: `wire/core/Wire.php`

Shortcuts to ProcessWire API variables. Access without any arguments returns the API variable. Some support arguments as shortcuts to methods in the API variable.

- [`cache($name = '', $expire = null, $func = null): WireCache|string|array|PageArray|null`](method-cache.md) Access the `$cache` API variable as a function.
- [`config($key = '', $value = null): Config|mixed`](method-config.md) Access the `$config` API variable as a function.
- [`database(): WireDatabasePDO`](method-database.md) Access the `$database` API variable as a function.
- [`datetime($format = '', $value = ''): WireDateTime|string|int`](method-datetime.md) Access the `$datetime` API variable as a function.
- [`fields($name = ''): Field|Fields|null`](method-fields.md) Access the `$fields` API variable as a function.
- [`files(): WireFileTools`](method-files.md) Access the `$files` API variable as a function.
- [`input($type = '', $key = '', $sanitizer = ''): WireInput|WireInputData|WireInputDataCookie|array|string|int|null`](method-input.md) Access the `$input` API variable as a function.
- [`inputCookie($key = '', $sanitizer = ''): WireInputDataCookie|string|int|array|null`](method-inputcookie.md) Access the `$input->cookie()` API variable as a function.
- [`inputGet($key = '', $sanitizer = ''): WireInputData|string|int|array|null`](method-inputget.md) Access the `$input->get()` API variable as a function.
- [`inputPost($key = '', $sanitizer = ''): WireInputData|string|int|array|null`](method-inputpost.md) Access the `$input->post()` API variable as a function.
- [`languages($name = ''): Languages|Language|NullPage|null`](method-languages.md) Access the `$languages` API variable as a function.
- [`modules($name = ''): Modules|Module|ConfigurableModule|null`](method-modules.md) Access the `$modules` API variable as a function.
- [`page($key = '', $value = null): Page|Mixed`](method-page.md) Access the `$page` API variable as a function.
- [`pages($selector = ''): Pages|PageArray|Page|NullPage`](method-pages.md) Access the `$pages` API variable as a function.
- [`permissions($selector = ''): Permissions|Permission|PageArray|null|NullPage`](method-permissions.md) Access the `$permissions` API variable as a function.
- [`roles($selector = ''): Roles|Role|PageArray|null|NullPage`](method-roles.md) Access the `$roles` API variable as a function.
- [`sanitizer($name = '', $value = ''): Sanitizer|string|int|array|null|mixed`](method-sanitizer.md) Access the `$sanitizer` API variable as a function.
- [`session($key = '', $value = null): Session|mixed`](method-session.md) Access the `$session` API variable as a function.
- [`templates($name = ''): Templates|Template|null`](method-templates.md) Access the `$templates` API variable as a function.
- [`user($key = '', $value = null): User|mixed`](method-user.md) Access the `$user` API variable as a function.
- [`users($selector = ''): Users|PageArray|User|mixed`](method-users.md) Access the `$users` API variable as a function.
