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

## Methods
- [`_wirePagesAPI($_apiVar, $selector): null|NullPage|Page|PageArray|Pages|PagesType`](method-_wirepagesapi.md) Common helper for API functions dealing with pages
- [`_wireDataAPI($_apiVar, $key, $value): mixed|null|WireData|Page`](method-_wiredataapi.md) Common helper for API functions dealing with WireData objects
- [`wirePages(string|array $selector = ''): Pages|PageArray|Page|NullPage`](method-wirepages.md) Access the `$pages` API variable as a function
- [`wirePage(string $key = '', null $value = null): Page|mixed`](method-wirepage.md) Access the `$page` API variable as a function
- [`wirePageId(Page|mixed $value): int|false`](method-wirepageid.md) Return id for given page or false if it’s not a page
- [`wireConfig(string $key = '', null $value = null): Config|mixed`](method-wireconfig.md) Access the `$config` API variable as a function
- [`wireModules(string $name = ''): Modules|Module|ConfigurableModule|null`](method-wiremodules.md) Access the `$modules` API variable as a function
- [`wireUser(string $key = '', null $value = null): User|mixed`](method-wireuser.md) Access the `$user` API variable as a function
- [`wireUsers(string|array $selector = ''): Users|PageArray|User|NullPage|mixed`](method-wireusers.md) Access the `$users` API variable as a function
- [`wireSession(string $key = '', null $value = null): Session|mixed`](method-wiresession.md) Access the `$session` API variable as a function
- [`wireFields(string $name = ''): Fields|Field|null`](method-wirefields.md) Access the `$fields` API variable as a function
- [`wireTemplates(string $name = ''): Templates|Template|null`](method-wiretemplates.md) Access the `$templates` API variable as a function
- [`wireDatabase(): WireDatabasePDO`](method-wiredatabase.md) Access the `$database` API variable as a function
- [`wirePermissions(string $selector = ''): Permissions|Permission|PageArray|null|NullPage`](method-wirepermissions.md) Access the `$permissions` API varaible as a function
- [`wireRoles(string $selector = ''): Roles|Role|PageArray|null|NullPage`](method-wireroles.md) Access the `$roles` API varaible as a function
- [`wireSanitizer(string $name = '', string $value = ''): Sanitizer|string|int|array|null|mixed`](method-wiresanitizer.md) Access the `$sanitizer` API variable as a function
- [`wireDatetime(string $format = '', string|int $value = ''): WireDateTime|string|int`](method-wiredatetime.md) Access the `$datetime` API variable as a function
- [`wireFiles(): WireFileTools`](method-wirefiles.md) Access the `$files` API variable as a function
- [`wireCache(string $name = '', callable|int|string|null $expire = null, callable|int|string|null $func = null): WireCache|string|array|PageArray|null`](method-wirecache.md) Access the `$cache` API variable as a function
- [`wireLanguages(string|int $name = ''): Languages|Language|NullPage|null`](method-wirelanguages.md) Access the `$languages` API variable as a function
- [`wireInput(string $type = '', string $key = '', string $sanitizer = null, mixed $fallback = null): WireInput|WireInputData|array|string|int|null`](method-wireinput.md) Access the `$input` API variable as a function
- [`wireInputGet(string $key = '', string $sanitizer = null, mixed $fallback = null): WireInputData|string|int|array|null`](method-wireinputget.md) Access the `$input->get` API variable as a function
- [`wireInputPost(string $key = '', string $sanitizer = null, mixed $fallback = null): WireInputData|string|int|array|null`](method-wireinputpost.md) Access the `$input->post` API variable as a function
- [`wireInputCookie(string $key = '', string $sanitizer = null, mixed $fallback = null): WireInputData|string|int|array|null`](method-wireinputcookie.md) Access the `$input->cookie` API variable as a function
- [`wireLog(string $logName = '', string $message = ''): WireLog|bool`](method-wirelog.md) Access the `$log` API variable as a function
- [`wireProfiler(string|array|object|null $name = null, null|object|string $source = null, array $data = array()): null|array|object`](method-wireprofiler.md) Start or stop a profiler event or return WireProfilerInterface instance
- [`wireUrls(string $key = ''): null|Paths|string`](method-wireurls.md) Function that returns a `$config->urls`->[name] value o
- [`wirePaths(string $key = ''): null|Paths|string`](method-wirepaths.md) Function that returns a `$config->paths`->[name] value o
- [`wireSetting(string|array $name = '', string|int|array|float|mixed $value = null): array|string|int|bool|mixed|null`](method-wiresetting.md) Get or set a runtime site setting
- [`_wireFunctionsAPI(): array`](method-_wirefunctionsapi.md) Return array of functions available from the functions API
