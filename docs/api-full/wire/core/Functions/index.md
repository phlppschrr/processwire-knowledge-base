# Functions

Source: `wire/core/Functions.php`

ProcessWire Functions

Common API functions useful outside of class scope


These shortcuts for creating WireArray types are available in ProcessWire 3.0.123 and newer.
These file system functions are procedural versions of some of those provided by the `$files` API variable.

## Methods
- [`wire(string $name = 'wire'): null|ProcessWire|Wire|Session|Page|Pages|Modules|User|Users|Roles|Permissions|Templates|Fields|Fieldtypes|Sanitizer|Config|Notices|WireDatabasePDO|WireHooks|WireDateTime|WireFileTools|WireMailTools|WireInput|string|mixed`](method-wire.md) Return an API variable, or return current ProcessWire instance if given no arguments
- [`wireInstance(?Wire $wire = null): ProcessWire`](method-wireinstance.md) Get or set the current ProcessWire instance
- [`wireMkdir(string $path, bool $recursive = false, string $chmod = null): bool`](method-wiremkdir.md) Create a directory (optionally recursively) that is writable to ProcessWire and uses the `$config` chmod settings
- [`wireRmdir(string $path, bool $recursive = false): bool`](method-wirermdir.md) Remove a directory (optionally recursively)
- [`wireChmod(string $path, bool $recursive = false, string $chmod = null): bool`](method-wirechmod.md) Change the mode of a file or directory (optionally recursive)
- [`wireCopy(string $src, string $dst, $options = array()): bool`](method-wirecopy.md) Copy all files recursively from one directory to another
- [`wireUnzipFile(string $file, string $dst, array $options = []): array`](method-wireunzipfile.md) Unzips the given ZIP file to the destination directory
- [`wireZipFile(string $zipfile, array|string $files, array $options = array()): array`](method-wirezipfile.md) Create a ZIP file from given files
- [`wireSendFile(string $filename, array $options = array(), array $headers = array())`](method-wiresendfile.md) Send the contents of the given filename via http
- [`wireRelativeTimeStr(int|string $ts, bool|int|array $abbreviate = false, bool $useTense = true): string`](method-wirerelativetimestr.md) Given a unix timestamp (or date string), returns a formatted string indicating the time relative to now
- [`wireMail(string|array $to = '', string $from = '', string $subject = '', string|array $body = '', array|string $options = array()): int|WireMail`](method-wiremail.md) Send an email or get a WireMail object to populate before send
- [`wirePopulateStringTags(string $str, WireData|object|array $vars, array $options = array()): string`](method-wirepopulatestringtags.md) Given a string (`$str`) and values (`$vars`), replace “{tags}” in the string with the values
- [`wireTempDir(Object|string $name, array|int $options = array()): WireTempDir`](method-wiretempdir.md) Return a new temporary directory/path ready to use for files
- [`wireRenderFile(string $filename, array $vars = array(), array $options = array()): string|bool`](method-wirerenderfile.md) Given a filename, render it as a ProcessWire template file
- [`wireIncludeFile(string $filename, array $vars = array(), array $options = array()): bool`](method-wireincludefile.md) Include a PHP file passing it all API variables and optionally your own specified variables
- [`wireDate(string|int $format = '', int|string|null $ts = null): string|bool`](method-wiredate.md) Format a date, using PHP date(), strftime() or other special strings (see arguments).
- [`wireIconMarkup(string $icon, string $class = ''): string`](method-wireiconmarkup.md) Render markup for a system icon
- [`wireIconMarkupFile(string $filename, string|bool $class = ''): string`](method-wireiconmarkupfile.md) Get the markup or class name for an icon that can represent the given filename
- [`wireBytesStr(int $bytes, bool|int|array $small = false, array|int $options = array()): string`](method-wirebytesstr.md) Given a quantity of bytes (int), return readable string that refers to quantity in bytes, kB, MB, GB and TB
- [`wireClassName(string|object $className, bool|int|string $withNamespace = false, bool $verbose = false): string|null`](method-wireclassname.md) Normalize a class name with or without namespace, or get namespace of class
- [`wireClassNamespace(string|object $className, bool $withClass = false, bool $strict = false): string|array`](method-wireclassnamespace.md) Get namespace for given class
- [`wireClassExists(string $className, bool $autoload = true): bool`](method-wireclassexists.md) Does the given class name exist?
- [`wireMethodExists(string $className, string $method, bool $hookable = false): bool`](method-wiremethodexists.md) Does the given class have the given method?
- [`wireClassImplements(string|object $className, bool $autoload = true): array`](method-wireclassimplements.md) Get an array of all the interfaces that the given class implements
- [`wireClassParents(string|object $className, bool $autoload = true): array`](method-wireclassparents.md) Return array of all parent classes for given class/object
- [`wireInstanceOf(object|string $instance, string|array $className, bool $autoload = true): bool|string`](method-wireinstanceof.md) Does given instance (or class) represent an instance of the given className (or class names)?
- [`wireIsCallable(string|callable $var, bool $syntaxOnly = false, &$callableName = ''): bool`](method-wireiscallable.md) Is the given `$var` callable as a function?
- [`wireCount(mixed $value): int`](method-wirecount.md) Return the count of item(s) present in the given value
- [`wireLength(string|array|object|int|bool|null $value, bool $mb = true): int`](method-wirelength.md) Returns string length of any type (string, array, object, bool, int, etc.)
- [`wireLen(string|array|object|int|bool|null $value): int`](method-wirelen.md) Returns string byte length of any type (string, array, object, bool, int, etc.)
- [`wireEmpty(mixed $value): bool`](method-wireempty.md) Is the given value empty according to ProcessWire standards?
- [`wire404(string $message = '')`](method-wire404.md) Stop execution with a 404 unless redirect URL available (for front-end use)
- [`WireArray(array|WireArray|mixed $items = array()): WireArray`](method-wirearray.md) Create new WireArray, add given `$items` to it, and return it
- [`WireData(array|\Traversable $data = array()): WireData`](method-wiredata.md) Create a new WireData instance and optionally add given associative array of data to it
- [`PageArray(array|PageArray $items = array()): PageArray`](method-pagearray.md) Create new PageArray, add given `$items` (pages) to it, and return it
