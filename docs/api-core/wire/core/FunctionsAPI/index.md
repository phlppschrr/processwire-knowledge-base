# FunctionsAPI

Source: `wire/core/FunctionsAPI.php`

ProcessWire functions API maps function names to common API variables
Provides an alternative to the API variables by providing functions of the same
name, with these benefits:

- They are always in scope whether inside a function or outside of it.
- They are self documenting with your IDE, unlike API $variables.
- They cannot be accidentally overwritten the way variables can be.
- They provider greater contrast between what are API-calls and variables.
- In some cases it makes for shorter API calls.
- Some of the functions provide arguments for useful shortcuts.

These functions always refer to the current ProcessWire instance, so are intended
primarily for front-end usage in template files (not for modules).

If these functions are not working for you, you can enable them by setting
`$config->useFunctionsAPI=true;` in your /site/config.php file.

Regardless of whether the Functions API is enabled or not, you can also access
any of these functions by prefixing the word `wire` to them and using the format
`wireFunction()` i.e. `wirePages()`, `wireUser()`, etc.
Or, if you do not

Methods:
- [`pages(string|array|int $selector = ''): Pages|PageArray|Page|NullPage`](method-pages.md) Retrieve or save pages ($pages API variable as a function)
- [`page(string $key = '', null $value = null): Page|mixed`](method-page.md) Returns the current Page being viewed ($page API variable as a function)
- [`pageId(Page|mixed $value): int|false`](method-pageid.md) Return id for given page or false if it’s not a page
- [`config(string $key = '', null $value = null): Config|mixed`](method-config.md) Access a ProcessWire configuration setting ($config API variable as a function)
- [`modules(string $name = ''): Modules|Module|ConfigurableModule|null`](method-modules.md) Get a module, get module information, and much more ($modules API variable as a function)
- [`user(string $key = '', null $value = null): User|mixed`](method-user.md) Get the currently logged in user ($user API variable as a function)
- [`users(string|array|int $selector = ''): Users|PageArray|User|mixed`](method-users.md) Get, find or save users ($users API variable as a function)
- [`session(string $key = '', null $value = null): Session|null|string|array|int|float`](method-session.md) Get or set values in the current user session ($session API variable as a function)
- [`fields(string $name = ''): Fields|Field|null`](method-fields.md) Get or save fields independent of templates ($fields API variable as as function)
- [`templates(string $name = ''): Templates|Template|null`](method-templates.md) Get or save templates ($templates API variable as a function)
- [`database(): WireDatabasePDO`](method-database.md) Create and execute PDO database queries ($database API variable as a function)
- [`permissions(string|int $selector = ''): Permissions|Permission|PageArray|null|NullPage`](method-permissions.md) Get, find or save permissions ($permissions API variable as a function)
- [`roles(string|int $selector = ''): Roles|Role|PageArray|null|NullPage`](method-roles.md) Get, find or save roles ($roles API variable as a function)
- [`sanitizer(string $name = '', string $value = ''): Sanitizer|string|int|array|null|mixed`](method-sanitizer.md) Sanitize variables and related string functions ($sanitizer API variable as a function)
- [`datetime(string $format = '', string|int $value = ''): WireDateTime|string|int`](method-datetime.md) Access date and time related tools ($datetime API variable as a function)
- [`files(): WireFileTools`](method-files.md) Access tools for working on the file system ($files API variable as a function)
- [`cache(string $name = '', callable|int|string|null $expire = null, callable|int|string|null $func = null): WireCache|string|array|PageArray|null`](method-cache.md) Get and save caches ($cache API variable as a function)
- [`languages(string|int $name = ''): Languages|Language|NullPage|null`](method-languages.md) Access all installed languages in multi-language environment ($languages API variable as a function)
- [`input(string $type = '', string $key = '', string $sanitizer = null, string|int|null $fallback = null): WireInput|WireInputData|array|string|int|null`](method-input.md) Access GET, POST or COOKIE input variables and more ($input API variable as a function)
- [`urls(string $key = ''): null|Paths|string`](method-urls.md) Get one of any named system URLs (shortcut to the $config API variable “urls” property)
- [`paths(string $key = ''): null|Paths|string`](method-paths.md) Get one of any named server disk paths (shortcut to the $config API variable “paths” property)
- [`region(string $key = '', null|string $value = null): string|null|bool|array`](method-region.md) Get or set an output region (primarily for front-end output usage)
- [`setting(string|array $name = '', string|int|array|float|mixed $value = null): array|string|int|bool|mixed|null`](method-setting.md) Get or set a runtime site setting
