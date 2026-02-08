# $markupQA->error($text, $flags = 0): $this

Source: `wire/core/MarkupQA.php`

Record error message to image-errors log

## Usage

~~~~~
// basic usage
$result = $markupQA->error($text);

// usage with all arguments
$result = $markupQA->error($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string`
- `$flags` (optional) `int`

## Return value

- `$this`
