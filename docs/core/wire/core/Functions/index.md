# Functions

Source: `wire/core/Functions.php`

ProcessWire Functions

Common API functions useful outside of class scope


These shortcuts for creating WireArray types are available in ProcessWire 3.0.123 and newer.
These file system functions are procedural versions of some of those provided by the `$files` API variable.

Methods:
- [`wire(string $name = 'wire'): null|ProcessWire|Wire|Session|Page|Pages|Modules|User|Users|Roles|Permissions|Templates|Fields|Fieldtypes|Sanitizer|Config|Notices|WireDatabasePDO|WireHooks|WireDateTime|WireFileTools|WireMailTools|WireInput|string|mixed`](method-wire.md)
- [`wireInstance(?Wire $wire = null): ProcessWire`](method-wireinstance.md)
- [`wireMkdir(string $path, bool $recursive = false, string $chmod = null): bool`](method-wiremkdir.md)
- [`wireRmdir(string $path, bool $recursive = false): bool`](method-wirermdir.md)
- [`wireChmod(string $path, bool $recursive = false, string $chmod = null): bool`](method-wirechmod.md)
- [`wireCopy(string $src, string $dst, $options = array()): bool`](method-wirecopy.md)
- [`wireUnzipFile(string $file, string $dst, array $options = []): array`](method-wireunzipfile.md)
- [`wireZipFile(string $zipfile, array|string $files, array $options = array()): array`](method-wirezipfile.md)
- [`wireSendFile(string $filename, array $options = array(), array $headers = array())`](method-wiresendfile.md)
- [`wireRelativeTimeStr(int|string $ts, bool|int|array $abbreviate = false, bool $useTense = true): string`](method-wirerelativetimestr.md)
- [`wireMail(string|array $to = '', string $from = '', string $subject = '', string|array $body = '', array|string $options = array()): int|WireMail`](method-wiremail.md)
- [`wirePopulateStringTags(string $str, WireData|object|array $vars, array $options = array()): string`](method-wirepopulatestringtags.md)
- [`wireTempDir(Object|string $name, array|int $options = array()): WireTempDir`](method-wiretempdir.md)
- [`wireRenderFile(string $filename, array $vars = array(), array $options = array()): string|bool`](method-wirerenderfile.md)
- [`wireIncludeFile(string $filename, array $vars = array(), array $options = array()): bool`](method-wireincludefile.md)
- [`wireDate(string|int $format = '', int|string|null $ts = null): string|bool`](method-wiredate.md)
- [`wireIconMarkup(string $icon, string $class = ''): string`](method-wireiconmarkup.md)
- [`wireIconMarkupFile(string $filename, string|bool $class = ''): string`](method-wireiconmarkupfile.md)
- [`wireBytesStr(int $bytes, bool|int|array $small = false, array|int $options = array()): string`](method-wirebytesstr.md)
- [`wireClassName(string|object $className, bool|int|string $withNamespace = false, bool $verbose = false): string|null`](method-wireclassname.md)
- [`wireClassNamespace(string|object $className, bool $withClass = false, bool $strict = false): string|array`](method-wireclassnamespace.md)
- [`wireClassExists(string $className, bool $autoload = true): bool`](method-wireclassexists.md)
- [`wireMethodExists(string $className, string $method, bool $hookable = false): bool`](method-wiremethodexists.md)
- [`wireClassImplements(string|object $className, bool $autoload = true): array`](method-wireclassimplements.md)
- [`wireClassParents(string|object $className, bool $autoload = true): array`](method-wireclassparents.md)
- [`wireInstanceOf(object|string $instance, string|array $className, bool $autoload = true): bool|string`](method-wireinstanceof.md)
- [`wireIsCallable(string|callable $var, bool $syntaxOnly = false, &$callableName = ''): bool`](method-wireiscallable.md)
- [`wireCount(mixed $value): int`](method-wirecount.md)
- [`wireLength(string|array|object|int|bool|null $value, bool $mb = true): int`](method-wirelength.md)
- [`wireLen(string|array|object|int|bool|null $value): int`](method-wirelen.md)
- [`wireEmpty(mixed $value): bool`](method-wireempty.md)
- [`wire404(string $message = '')`](method-wire404.md)
- [`WireArray(array|WireArray|mixed $items = array()): WireArray`](method-wirearray.md)
- [`WireData(array|\Traversable $data = array()): WireData`](method-wiredata.md)
- [`PageArray(array|PageArray $items = array()): PageArray`](method-pagearray.md)
