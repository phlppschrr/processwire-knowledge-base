# $sanitizer->bracketTagsToHtml($str, array $options): string

Source: `wire/core/Sanitizer.php`

Convert HTML bracket tags [tag]...[/tag] to HTML - helper method for entitiesMarkdown()

## Usage

~~~~~
// basic usage
$string = $sanitizer->bracketTagsToHtml($str, $options);

// usage with all arguments
$string = $sanitizer->bracketTagsToHtml($str, array $options);
~~~~~

## Arguments

- `$str` `string` String containing bracket tags, should be entity encoded ahead of time
- `$options` `array`

## Return value

- `string`
