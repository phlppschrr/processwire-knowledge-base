# $comment->getFormatted($key, array $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Same as get() but with output formatting applied

Note that we won't apply this to get() when $page->outputFormatting is active
in order for backwards compatibility with older installations.

## Usage

~~~~~
// basic usage
$string = $comment->getFormatted($key);

// usage with all arguments
$string = $comment->getFormatted($key, array $options = array());
~~~~~

## Arguments

- `$key` `string` One of: text, cite, email, user_agent, website
- `$options` (optional) `array`

## Return value

- `string`
