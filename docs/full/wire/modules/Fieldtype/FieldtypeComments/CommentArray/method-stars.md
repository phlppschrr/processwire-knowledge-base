# $commentArray->stars($allowPartial = true, $getCount = false): int|float|false|array

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Get an average of all star ratings for all comments in this CommentsArray

## Arguments

- bool $allowPartial Allow partial stars? If true, returns a float. If false, returns int.
- bool $getCount If true, this method returns an array(stars, count) where count is number of ratings.

## Return value

int|float|false|array Returns false for stars value if no ratings yet.
