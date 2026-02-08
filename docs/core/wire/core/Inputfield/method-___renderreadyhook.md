# $inputfield->___renderReadyHook(?Inputfield $parent = null, $renderValueMode = false)

Source: `wire/core/Inputfield.php`

Hookable version of renderReady(), not called unless 'renderReadyHook' is hooked

Hook this method instead if you want to hook renderReady().

## Usage

~~~~~
// basic usage
$result = $inputfield->___renderReadyHook();

// usage with all arguments
$result = $inputfield->___renderReadyHook(?Inputfield $parent = null, $renderValueMode = false);
~~~~~

## Arguments

- `$parent` (optional) `Inputfield|null`
- `$renderValueMode` (optional) `bool`
