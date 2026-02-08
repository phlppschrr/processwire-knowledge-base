# $markupQA->sleepLinks(&$value)

Source: `wire/core/MarkupQA.php`

Sleep href attributes, adding a data-pwid attribute to <a> tags that resolve to a Page

Should be used AFTER sleepUrls() has already been called, so that any URLs are already
relative to "/" rather than potential "/subdir/".

## Usage

~~~~~
// basic usage
$result = $markupQA->sleepLinks($value);

// usage with all arguments
$result = $markupQA->sleepLinks(&$value);
~~~~~

## Arguments

- `$value` `string`
