# $markupQA->checkUrls(&$value, $sleep = false)

Source: `wire/core/MarkupQA.php`

Wake URLs for wakeup or sleep, converting root URLs as necessary

## Usage

~~~~~
// basic usage
$result = $markupQA->checkUrls($value);

// usage with all arguments
$result = $markupQA->checkUrls(&$value, $sleep = false);
~~~~~

## Arguments

- `$value` `string`
- `$sleep` (optional) `bool`
