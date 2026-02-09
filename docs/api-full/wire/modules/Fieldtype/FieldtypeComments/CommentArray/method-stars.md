# $commentArray->stars($allowPartial = true, $getCount = false): int|float|false|array

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Get an average of all star ratings for all comments in this CommentsArray

## Usage

~~~~~
// basic usage
$int = $commentArray->stars();

// usage with all arguments
$int = $commentArray->stars($allowPartial = true, $getCount = false);
~~~~~

## Arguments

- `$allowPartial` (optional) `bool` Allow partial stars? If true, returns a float. If false, returns int.
- `$getCount` (optional) `bool` If true, this method returns an array(stars, count) where count is number of ratings.

## Return value

- `int|float|false|array` Returns false for stars value if no ratings yet.
