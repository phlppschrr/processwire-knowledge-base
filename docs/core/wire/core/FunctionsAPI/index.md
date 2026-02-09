# FunctionsAPI

Source: `wire/core/FunctionsAPI.php`

ProcessWire functions API maps function names to common API variables

=
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
- [`pages(string|array|int $selector = ''): Pages|PageArray|Page|NullPage`](method-pages.md)
- [`page(string $key = '', null $value = null): Page|mixed`](method-page.md)
- [`pageId(Page|mixed $value): int|false`](method-pageid.md)
- [`config(string $key = '', null $value = null): Config|mixed`](method-config.md)
- [`modules(string $name = ''): Modules|Module|ConfigurableModule|null`](method-modules.md)
- [`user(string $key = '', null $value = null): User|mixed`](method-user.md)
- [`users(string|array|int $selector = ''): Users|PageArray|User|mixed`](method-users.md)
- [`session(string $key = '', null $value = null): Session|null|string|array|int|float`](method-session.md)
- [`fields(string $name = ''): Fields|Field|null`](method-fields.md)
- [`templates(string $name = ''): Templates|Template|null`](method-templates.md)
- [`database(): WireDatabasePDO`](method-database.md)
- [`permissions(string|int $selector = ''): Permissions|Permission|PageArray|null|NullPage`](method-permissions.md)
- [`roles(string|int $selector = ''): Roles|Role|PageArray|null|NullPage`](method-roles.md)
- [`sanitizer(string $name = '', string $value = ''): Sanitizer|string|int|array|null|mixed`](method-sanitizer.md)
- [`datetime(string $format = '', string|int $value = ''): WireDateTime|string|int`](method-datetime.md)
- [`files(): WireFileTools`](method-files.md)
- [`cache(string $name = '', callable|int|string|null $expire = null, callable|int|string|null $func = null): WireCache|string|array|PageArray|null`](method-cache.md)
- [`languages(string|int $name = ''): Languages|Language|NullPage|null`](method-languages.md)
- [`input(string $type = '', string $key = '', string $sanitizer = null, string|int|null $fallback = null): WireInput|WireInputData|array|string|int|null`](method-input.md)
- [`urls(string $key = ''): null|Paths|string`](method-urls.md)
- [`paths(string $key = ''): null|Paths|string`](method-paths.md)
- [`region(string $key = '', null|string $value = null): string|null|bool|array`](method-region.md)
- [`setting(string|array $name = '', string|int|array|float|mixed $value = null): array|string|int|bool|mixed|null`](method-setting.md)
