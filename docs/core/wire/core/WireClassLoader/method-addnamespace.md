# WireClassLoader::addNamespace()

Source: `wire/core/WireClassLoader.php`

Add a namespace to point to a path root

Multiple root paths may be specified for a single namespace by calling this method more than once.

~~~~~
$classLoader->addNamespace('HelloWorld', '/path/to/that/');
~~~~~

@param string $namespace

@param string $path Full system path
