# $template->urlSegments($value = '~'): array|int

Source: `wire/core/Template.php`

Get or set allowed URL segments

## Usage

~~~~~
// basic usage
$array = $template->urlSegments();

// usage with all arguments
$array = $template->urlSegments($value = '~');
~~~~~

## Arguments

- `$value` (optional) `array|int|bool|string` Omit to return current value, or to set value: - Specify array of allowed URL segments, may include 'segment', 'segment/path' or 'regex:your-regex'. - Or specify boolean true or 1 to enable all URL segments. - Or specify integer 0, boolean false, or blank array to disable all URL segments.

## Return value

- `array|int` Returns array of allowed URL segments, or 0 if disabled, or 1 if any allowed.
