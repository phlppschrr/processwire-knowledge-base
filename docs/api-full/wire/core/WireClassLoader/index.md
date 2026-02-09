# WireClassLoader

Source: `wire/core/WireClassLoader.php`

## Summary

ProcessWire class autoloader

Common methods:
- [`path()`](method-path.md)
- [`addExtension()`](method-addextension.md)
- [`addSuffix()`](method-addsuffix.md)
- [`addPrefix()`](method-addprefix.md)
- [`addNamespace()`](method-addnamespace.md)

Similar to a PSR-4 autoloader but with knowledge of modules.

The ProcessWire `$classLoader` API variable handles autoloading of classes and modules.
This class loader is similar to a PSR-4 autoloader but with knowledge of modules.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## Methods
- [`__construct(ProcessWire $wire = null)`](method-__construct.md)
- [`path(string $path): string`](method-path.md) Normalize a path
- [`addExtension(string $ext)`](method-addextension.md) Add a recognized file extension for PHP files
- [`addSuffix(string $suffix, string $path)`](method-addsuffix.md) Map a class suffix to a path
- [`addPrefix(string $prefix, string $path)`](method-addprefix.md) Map a class prefix to a path
- [`addNamespace(string $namespace, string $path)`](method-addnamespace.md) Add a namespace to point to a path root
- [`getNamespace(string $namespace): array`](method-getnamespace.md) Return array of paths for the given namespace, or empty array if none found
- [`hasNamespace(string $namespace): bool`](method-hasnamespace.md) Return true if namespace is defined with paths or false if not
- [`removeNamespace(string $namespace, string $path = '')`](method-removenamespace.md) Remove defined paths (or single path) for given namespace
- [`findClassFile(string $className): bool|string`](method-findclassfile.md) Find filename for given class name (primarily for API testing/debugging purposes)
- [`loadClass(string $className)`](method-loadclass.md) Load the file for the given class
- [`findClassInPaths(string $name, string|array $paths, string $dir = ''): string|bool`](method-findclassinpaths.md) Find class file among given paths and return full pathname to file if found
- [`findInPrefixSuffixPaths(string $name): bool|string`](method-findinprefixsuffixpaths.md) Check prefix and suffix definition paths for given class name and return file if found
