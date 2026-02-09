# WireClassLoader

Source: `wire/core/WireClassLoader.php`

ProcessWire class autoloader

Similar to a PSR-4 autoloader but with knowledge of modules.

The ProcessWire $classLoader API variable handles autoloading of classes and modules.
This class loader is similar to a PSR-4 autoloader but with knowledge of modules.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
Method: [__construct()](method-__construct.md)
Method: [path()](method-path.md)
Method: [addExtension()](method-addextension.md)
Method: [addSuffix()](method-addsuffix.md)
Method: [addPrefix()](method-addprefix.md)
Method: [addNamespace()](method-addnamespace.md)
Method: [getNamespace()](method-getnamespace.md)
Method: [hasNamespace()](method-hasnamespace.md)
Method: [removeNamespace()](method-removenamespace.md)
Method: [findClassFile()](method-findclassfile.md)
Method: [loadClass()](method-loadclass.md)
Method: [findClassInPaths()](method-findclassinpaths.md)
Method: [findInPrefixSuffixPaths()](method-findinprefixsuffixpaths.md)
