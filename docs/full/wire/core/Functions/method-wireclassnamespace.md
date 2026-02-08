# $functions->wireClassNamespace($className, $withClass = false, $strict = false): string|array

Source: `wire/core/Functions.php`

Get namespace for given class

~~~~~
echo wireClassNamespace('Page'); // returns: "\ProcessWire\"
echo wireClassNamespace('DirectoryIterator'); // returns: "\"
echo wireClassNamespace('UnknownClass'); // returns "" (blank)

// Specify true for 2nd argument to make it include class name
echo wireClassNamespace('Page', true); // outputs: \ProcessWire\Page

// Specify true for 3rd argument to find all matching classes
// and return array if more than 1 matches (or string if just 1):
$val = wireClassNamespace('Foo', true, true);
if(is_array($val)) {
  // 2+ classes found, so array value is returned
  // $val: [ '\Bar\Foo', '\Foo', '\Baz\Foo' ]
} else {
  // string value is returned when only one class matches
  // $val: '\Bar\Foo'
}
~~~~~

## Arguments

- string|object $className
- bool $withClass Include class name in returned namespace? (default=false)
- bool $strict Return array of namespaces if multiple match? (default=false)

## Return value

string|array Returns one of the following: - String of `\Namespace\` (leading+trailing backslashes) if namespace found. - String of `\` if class in root namespace. - Blank string if unable to find namespace for class. - Array of namespaces only if $strict option is true AND multiple namespaces were found for class. - If the $withClass option is true, then return value(s) have class, i.e. `\Namespace\ClassName`.

## Meta

- @since 3.0.150
