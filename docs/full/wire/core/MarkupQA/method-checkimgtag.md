# $markupQA->checkImgTag(&$value, $img, array $options = array())

Source: `wire/core/MarkupQA.php`

Quality assurance for one <img> tag

## Arguments

- `$value` `string` Entire markup
- `$img` `string` Just the found <img> tag
- `$options` (optional) `array` What actions should be performed: - replaceBlankAlt (bool): Replace blank alt attributes with file description? (default=true) - removeNoExists (bool): Remove references to images that don't exist (or re-create images when possible) (default=true) - removeNoAccess (bool): Remove references to images user doesn't have view permission to (default=true)
