# $markupQA->checkImgTags(&$value, array $options = array())

Source: `wire/core/MarkupQA.php`

Quality assurance for <img> tags

## Usage

~~~~~
// basic usage
$result = $markupQA->checkImgTags($value);

// usage with all arguments
$result = $markupQA->checkImgTags(&$value, array $options = array());
~~~~~

## Arguments

- `$value` `string`
- `$options` (optional) `array` What actions should be performed: - replaceBlankAlt (bool): Replace blank alt attributes with file description? (default=true) - removeNoExists (bool): Remove references to images that don't exist (or re-create images when possible) (default=true) - removeNoAccess (bool): Remove references to images user doesn't have view permission to (default=true)
