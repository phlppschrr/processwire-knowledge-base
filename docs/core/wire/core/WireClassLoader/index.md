# WireClassLoader

Source: `wire/core/WireClassLoader.php`

ProcessWire class autoloader

Similar to a PSR-4 autoloader but with knowledge of modules.

The ProcessWire $classLoader API variable handles autoloading of classes and modules.
This class loader is similar to a PSR-4 autoloader but with knowledge of modules.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`__construct(ProcessWire $wire = null)`](method-__construct.md)
- [`path(string $path): string`](method-path.md)
- [`addExtension(string $ext)`](method-addextension.md)
- [`addSuffix(string $suffix, string $path)`](method-addsuffix.md)
- [`addPrefix(string $prefix, string $path)`](method-addprefix.md)
- [`addNamespace(string $namespace, string $path)`](method-addnamespace.md)
- [`getNamespace(string $namespace): array`](method-getnamespace.md)
- [`hasNamespace(string $namespace): bool`](method-hasnamespace.md)
- [`removeNamespace(string $namespace, string $path = '')`](method-removenamespace.md)
- [`findClassFile(string $className): bool|string`](method-findclassfile.md)
- [`loadClass(string $className)`](method-loadclass.md)
- [`findClassInPaths(string $name, string|array $paths, string $dir = ''): string|bool`](method-findclassinpaths.md)
- [`findInPrefixSuffixPaths(string $name): bool|string`](method-findinprefixsuffixpaths.md)
