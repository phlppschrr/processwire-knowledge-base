# $functions->wireClassName($className, $withNamespace = false, $verbose = false): string|null

Source: `wire/core/Functions.php`

Normalize a class name with or without namespace, or get namespace of class

Default behavior is to return class name without namespace.

## Usage

~~~~~
// basic usage
$string = $functions->wireClassName($className);

// usage with all arguments
$string = $functions->wireClassName($className, $withNamespace = false, $verbose = false);
~~~~~

## Arguments

- `$className` `string|object` Class name or object instance
- `$withNamespace` (optional) `bool|int|string` Should return value include namespace? (default=false) - `false` (bool): Return only class name without namespace (default). - `true` (bool): Yes include namespace in returned value. - `1` (int): Return only namespace (i.e. “ProcessWire”, with no backslashes unless $verbose argument is true)
- `$verbose` (optional) `bool` When namespace argument is true or 1, use verbose return value (added 3.0.143). This does the following: - If returning class name with namespace, this makes it include a leading backslash, i.e. `\ProcessWire\Wire` - If returning namespace only, adds leading backslash, plus trailing backslash if namespace is not root, i.e. `\ProcessWire\`

## Return value

- `string|null` Returns string or NULL if namespace-only requested and unable to determine
