# FileCompiler

Source: `wire/core/FileCompiler.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

FileCompiler


@todo determine whether we should make storage in dedicated table rather than using wire('cache').

@todo handle race conditions for multiple requests attempting to compile the same file(s).

Methods:
- [`__construct(string $sourcePath, array $options = array())`](method-__construct.md) Construct
- [`wired()`](method-wired.md) Wired to instance
- [`init()`](method-init.md) Initialize paths
- [`mkdir(string $path, bool $recursive = true): bool`](method-mkdir.md) Make a directory with proper permissions
- [`chmod(string $filename): bool`](method-chmod.md) Change file to correct mode for FileCompiler
- [`initTargetPath()`](method-inittargetpath.md) Initialize the target path, making sure that it exists and creating it if not
- [`initRawPHP(string &$data)`](method-initrawphp.md) Populate the $this->rawPHP data which contains only raw php without quoted values
- [`allowCompile(string &$filename, string &$basename): bool`](method-allowcompile.md) Allow the given filename to be compiled?
- [`compile(string $sourceFile): string`](method-___compile.md) (hookable) Compile given source file and return compiled destination file
- [`compileData(string $data, string $sourceFile): string`](method-___compiledata.md) (hookable) Compile the given string of data
- [`compileComments(&$data)`](method-compilecomments.md) Compile comments so that they can be easily identified by other compiler methods
- [`compileIncludes(string &$data, string $sourceFile)`](method-compileincludes.md) Compile include(), require() (and variations) to refer to compiled files where possible
- [`compileIncludesValidLineOpen(string $open): bool`](method-compileincludesvalidlineopen.md) Test the given line $open preceding an include statement for validity
- [`compileIncludesFileMatchType(string $fileMatch, string $funcMatch): string|bool`](method-compileincludesfilematchtype.md) Returns fileMatch type of 'var', 'file', 'func' or boolean false if not valid
- [`compileNamespace(string &$data): bool`](method-compilenamespace.md) Compile global class/interface/function references to namespaced versions
- [`copyAllNewerFiles(string $source, string $target, bool $recursive = true): int`](method-copyallnewerfiles.md) Recursively copy all files from $source to $target, but only if $source file is $newer
- [`getNumCacheFiles(bool $all = false, string $targetPath = null): int`](method-getnumcachefiles.md) Get a count of how many files are in the cache
- [`clearCache(bool $all = false): bool`](method-clearcache.md) Clear all file compiler caches
- [`maintenance(int $interval = 86400): bool`](method-maintenance.md) Run maintenance on the FileCompiler cache
- [`_maintenance($sourcePath, $targetPath): bool`](method-_maintenance.md) Implementation for maintenance on a given path
- [`optionsToString(array $options): string`](method-optionstostring.md) Given an array of $options convert to an PHP-code array() string
- [`addExclusion(string $pathname)`](method-addexclusion.md) Exclude a file or path from compilation
- [`touch(string $filename, null|int $time = null): bool`](method-touch.md) Same as PHP touch() but with fallbacks for cases where touch() does not work
