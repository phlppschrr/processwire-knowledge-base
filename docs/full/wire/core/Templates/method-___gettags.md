# $templates->getTags($getTemplateNames = false): array

Source: `wire/core/Templates.php`

Get all tags used by templates

## Usage

~~~~~
// basic usage
$array = $templates->getTags();

// usage with all arguments
$array = $templates->getTags($getTemplateNames = false);
~~~~~

## Hookable

- Hookable method name: `getTags`
- Implementation: `___getTags`
- Hook with: `$templates->getTags()`

## Arguments

- `$getTemplateNames` (optional) `bool` Get arrays of template names for each tag? (default=false)

## Return value

- `array` In return value both key and value are the tag

## Since

3.0.176 + hookable in 3.0.179
