# $wire->className($options = null): string

Source: `wire/core/Wire.php`

Return this object’s class name

By default, this method returns the class name without namespace. To include the namespace, call it
with boolean true as the first argument.

## Example

~~~~~
echo $page->className(); // outputs: Page
echo $page->className(true); // outputs: ProcessWire\Page
~~~~~

## Usage

~~~~~
// basic usage
$string = $wire->className();

// usage with all arguments
$string = $wire->className($options = null);
~~~~~

## Arguments

- `$options` (optional) `array|bool|null` Specify boolean `true` to return class name with namespace, or specify an array of one or more options: - `lowercase` (bool): Specify true to make it return hyphenated lowercase version of class name (default=false). - `namespace` (bool): Specify true to include namespace from returned class name (default=false). - *Note: The lowercase and namespace options may not both be true at the same time.*

## Return value

- `string` String with class name
