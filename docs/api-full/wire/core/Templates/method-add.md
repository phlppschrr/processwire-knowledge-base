# $templates->add($name, array $properties = array()): Template

Source: `wire/core/Templates.php`

Add and save new template (and fieldgroup) with given name and return it

## Usage

~~~~~
// basic usage
$template = $templates->add($name);

// usage with all arguments
$template = $templates->add($name, array $properties = array());
~~~~~

## Arguments

- `$name` `string`
- `$properties` (optional) `array` Any additional properties to add to template

## Return value

- `Template`

## Exceptions

- `WireException` if given invalid template name or template already exists

## Since

3.0.170
