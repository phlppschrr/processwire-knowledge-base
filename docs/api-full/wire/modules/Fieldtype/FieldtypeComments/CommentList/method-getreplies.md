# $commentList->getReplies($commentID): array

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Get replies to the given comment ID, or 0 for root level comments

## Usage

~~~~~
// basic usage
$array = $commentList->getReplies($commentID);
~~~~~

## Arguments

- `$commentID` `int|Comment`

## Return value

- `array`
