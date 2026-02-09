# $inputfield->getSetting($key): mixed

Source: `wire/core/Inputfield.php`

Gets a setting (or API variable) from the Inputfield, while ignoring attributes.

This is good to use in cases where there are potential name conflicts, like when there is a field literally
named "collapsed" or "required".

## Usage

~~~~~
// basic usage
$result = $inputfield->getSetting($key);
~~~~~

## Arguments

- `$key` `string` Name of setting or API variable to retrieve.

## Return value

- `mixed` Value of setting or API variable, or NULL if not found.
