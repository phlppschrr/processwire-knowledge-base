# $markupQA->wakeupLinks(&$value): array

Source: `wire/core/MarkupQA.php`

Wakeup href attributes, using the data-pwid attribute to update the href attribute as necessary

Should be used BEFORE wakeupUrls() is called so that href attributes are relative to "/" rather than
a potential "/subdir/" that wouldn't be recognized as a page path.

## Usage

~~~~~
// basic usage
$array = $markupQA->wakeupLinks($value);

// usage with all arguments
$array = $markupQA->wakeupLinks(&$value);
~~~~~

## Arguments

- $value

## Return value

- `array` Returns array of replacements that were made (3.0.184+)
