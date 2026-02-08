# $fields->___getTags($getFieldNames = false): array

Source: `wire/core/Fields.php`

Get list of all tags used by fields

- By default it returns an array of tag names where both keys and values are the tag names.
- If you specify true for the `$getFields` argument, it returns an array where the keys are
  tag names and the values are arrays of field names in the tag.
- If you specify "reset" for the `$getFields` argument it returns a blank array and resets
  internal tags cache.

## Arguments

- `$getFieldNames` (optional) `bool|string` Specify true to return associative array where keys are tags and values are field names …or specify the string "reset" to force getTags() to reset its cache, forcing it to reload on the next call.

## Return value

array Both keys and values are tags in return value

## Since

3.0.106 + made hookable in 3.0.179
