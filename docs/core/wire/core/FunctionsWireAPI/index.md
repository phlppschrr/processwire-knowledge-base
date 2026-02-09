# FunctionsWireAPI

Source: `wire/core/FunctionsWireAPI.php`

ProcessWire functions API maps function names to common API variables

Provides an alternative to the API variables by providing functions of the same
name, with these benefits:

- They are always in scope
- Makes life simpler in an IDE that recognizes phpdoc, as it can more easily
  recognize the types an return values.
- In some cases it makes for shorter API calls.

The primary drawback is that the function calls are not mapped to a specific
instance, so in a multi-instance environment it's possible these function calls
may not be referring to the correct ProcessWire instance. For this reason, we
think these functions are primarily useful for front-end/website usages, and
not as useful for back-end and module development.

Shorter versions of these functions (without the leading "wire") can be found in
FunctionsAPI.php file, which is used only if $config->useFunctionsAPI is true.
The functions in this file are always available regardless of that setting.

Methods:
- [`_wirePagesAPI($_apiVar, $selector): null|NullPage|Page|PageArray|Pages|PagesType`](method-_wirepagesapi.md)
- [`_wireDataAPI($_apiVar, $key, $value): mixed|null|WireData|Page`](method-_wiredataapi.md)
- [`wirePages(string|array $selector = ''): Pages|PageArray|Page|NullPage`](method-wirepages.md)
- [`wirePage(string $key = '', null $value = null): Page|mixed`](method-wirepage.md)
- [`wirePageId(Page|mixed $value): int|false`](method-wirepageid.md)
- [`wireConfig(string $key = '', null $value = null): Config|mixed`](method-wireconfig.md)
- [`wireModules(string $name = ''): Modules|Module|ConfigurableModule|null`](method-wiremodules.md)
- [`wireUser(string $key = '', null $value = null): User|mixed`](method-wireuser.md)
- [`wireUsers(string|array $selector = ''): Users|PageArray|User|NullPage|mixed`](method-wireusers.md)
- [`wireSession(string $key = '', null $value = null): Session|mixed`](method-wiresession.md)
- [`wireFields(string $name = ''): Fields|Field|null`](method-wirefields.md)
- [`wireTemplates(string $name = ''): Templates|Template|null`](method-wiretemplates.md)
- [`wireDatabase(): WireDatabasePDO`](method-wiredatabase.md)
- [`wirePermissions(string $selector = ''): Permissions|Permission|PageArray|null|NullPage`](method-wirepermissions.md)
- [`wireRoles(string $selector = ''): Roles|Role|PageArray|null|NullPage`](method-wireroles.md)
- [`wireSanitizer(string $name = '', string $value = ''): Sanitizer|string|int|array|null|mixed`](method-wiresanitizer.md)
- [`wireDatetime(string $format = '', string|int $value = ''): WireDateTime|string|int`](method-wiredatetime.md)
- [`wireFiles(): WireFileTools`](method-wirefiles.md)
- [`wireCache(string $name = '', callable|int|string|null $expire = null, callable|int|string|null $func = null): WireCache|string|array|PageArray|null`](method-wirecache.md)
- [`wireLanguages(string|int $name = ''): Languages|Language|NullPage|null`](method-wirelanguages.md)
- [`wireInput(string $type = '', string $key = '', string $sanitizer = null, mixed $fallback = null): WireInput|WireInputData|array|string|int|null`](method-wireinput.md)
- [`wireInputGet(string $key = '', string $sanitizer = null, mixed $fallback = null): WireInputData|string|int|array|null`](method-wireinputget.md)
- [`wireInputPost(string $key = '', string $sanitizer = null, mixed $fallback = null): WireInputData|string|int|array|null`](method-wireinputpost.md)
- [`wireInputCookie(string $key = '', string $sanitizer = null, mixed $fallback = null): WireInputData|string|int|array|null`](method-wireinputcookie.md)
- [`wireLog(string $logName = '', string $message = ''): WireLog|bool`](method-wirelog.md)
- [`wireProfiler(string|array|object|null $name = null, null|object|string $source = null, array $data = array()): null|array|object`](method-wireprofiler.md)
- [`wireUrls(string $key = ''): null|Paths|string`](method-wireurls.md)
- [`wirePaths(string $key = ''): null|Paths|string`](method-wirepaths.md)
- [`wireSetting(string|array $name = '', string|int|array|float|mixed $value = null): array|string|int|bool|mixed|null`](method-wiresetting.md)
- [`_wireFunctionsAPI(): array`](method-_wirefunctionsapi.md)
