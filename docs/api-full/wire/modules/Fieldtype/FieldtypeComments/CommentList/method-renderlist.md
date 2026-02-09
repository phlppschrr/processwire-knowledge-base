# $commentList->renderList($parent_id = 0, $depth = 0): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Render comment list

## Usage

~~~~~
// basic usage
$string = $commentList->renderList();

// usage with all arguments
$string = $commentList->renderList($parent_id = 0, $depth = 0);
~~~~~

## Arguments

- `$parent_id` (optional) `int`
- `$depth` (optional) `int`

## Return value

- `string`
