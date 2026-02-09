# $inputfieldWrapper->insert($item, $existingItem, $before = false): $this

Source: `wire/core/InputfieldWrapper.php`

Insert new or existing Inputfield before or after another

## Usage

~~~~~
// basic usage
$result = $inputfieldWrapper->insert($item, $existingItem);

// usage with all arguments
$result = $inputfieldWrapper->insert($item, $existingItem, $before = false);
~~~~~

## Arguments

- `$item` `Inputfield|array|string` New or existing item Inputfield, name, or new item array to insert.
- `$existingItem` `Inputfield|string` Existing item or item name you want to insert before.
- `$before` (optional) `bool` True to insert before, false to insert after (default=false).

## Return value

- `$this`

## Exceptions

- `WireException`

## Since

3.0.196
