# $commentField->updateComment(Page $page, Comment $comment, array $properties): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Update specific properties for a comment

## Usage

~~~~~
// basic usage
$bool = $commentField->updateComment($page, $comment, $properties);

// usage with all arguments
$bool = $commentField->updateComment(Page $page, Comment $comment, array $properties);
~~~~~

## Arguments

- `$page` `Page`
- `$comment` `Comment`
- `$properties` `array` Associative array of properties to update

## Return value

- `bool`
