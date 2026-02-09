# FileCompiler

Source: `wire/core/FileCompiler.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

FileCompiler


@todo determine whether we should make storage in dedicated table rather than using wire('cache').

@todo handle race conditions for multiple requests attempting to compile the same file(s).

Methods:
- [`__construct(string $sourcePath, array $options = array())`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`init()`](method-init.md)
- [`mkdir(string $path, bool $recursive = true): bool`](method-mkdir.md)
- [`chmod(string $filename): bool`](method-chmod.md)
- [`initTargetPath()`](method-inittargetpath.md)
- [`initRawPHP(string &$data)`](method-initrawphp.md)
- [`allowCompile(string &$filename, string &$basename): bool`](method-allowcompile.md)
- [`compile(string $sourceFile): string`](method-___compile.md) (hookable)
- [`compileData(string $data, string $sourceFile): string`](method-___compiledata.md) (hookable)
- [`compileComments(&$data)`](method-compilecomments.md)
- [`compileIncludes(string &$data, string $sourceFile)`](method-compileincludes.md)
- [`compileIncludesValidLineOpen(string $open): bool`](method-compileincludesvalidlineopen.md)
- [`compileIncludesFileMatchType(string $fileMatch, string $funcMatch): string|bool`](method-compileincludesfilematchtype.md)
- [`compileNamespace(string &$data): bool`](method-compilenamespace.md)
- [`copyAllNewerFiles(string $source, string $target, bool $recursive = true): int`](method-copyallnewerfiles.md)
- [`getNumCacheFiles(bool $all = false, string $targetPath = null): int`](method-getnumcachefiles.md)
- [`clearCache(bool $all = false): bool`](method-clearcache.md)
- [`maintenance(int $interval = 86400): bool`](method-maintenance.md)
- [`_maintenance($sourcePath, $targetPath): bool`](method-_maintenance.md)
- [`optionsToString(array $options): string`](method-optionstostring.md)
- [`addExclusion(string $pathname)`](method-addexclusion.md)
- [`touch(string $filename, null|int $time = null): bool`](method-touch.md)
