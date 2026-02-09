# $commentField->getCommentsByID(array $ids, $page = null): CommentArray

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Get multiple comments by ID

## Usage

~~~~~
// basic usage
$commentArray = $commentField->getCommentsByID($ids);

// usage with all arguments
$commentArray = $commentField->getCommentsByID(array $ids, $page = null);
~~~~~

## Arguments

- `$ids` `int[]` Comment IDs
- `$page` (optional) `Page|null` Optionally limit comments to this page

## Return value

- `CommentArray`

## Since

3.0.255
