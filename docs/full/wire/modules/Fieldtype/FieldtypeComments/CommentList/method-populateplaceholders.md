# $commentList->populatePlaceholders(Comment $comment, $out, $placeholders = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Populate comment {variable} placeholders

## Usage

~~~~~
// basic usage
$string = $commentList->populatePlaceholders($comment, $out);

// usage with all arguments
$string = $commentList->populatePlaceholders(Comment $comment, $out, $placeholders = array());
~~~~~

## Arguments

- `$comment` `Comment`
- `$out` `string`
- `$placeholders` (optional) `array` Additional placeholders to populate as name => value (exclude the brackets)

## Return value

- `string`
