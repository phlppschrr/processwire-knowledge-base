# $inputfield->renderReadyHook(?Inputfield $parent = null, $renderValueMode = false)

Source: `wire/core/Inputfield.php`

Hookable version of renderReady(), not called unless 'renderReadyHook' is hooked

Hook this method instead if you want to hook renderReady().

## Usage

~~~~~
// basic usage
$result = $inputfield->renderReadyHook();

// usage with all arguments
$result = $inputfield->renderReadyHook(?Inputfield $parent = null, $renderValueMode = false);
~~~~~

## Hookable

- Hookable method name: `renderReadyHook`
- Implementation: `___renderReadyHook`
- Hook with: `$inputfield->renderReadyHook()`

## Arguments

- `$parent` (optional) `Inputfield|null`
- `$renderValueMode` (optional) `bool`
