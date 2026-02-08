# CommentStars::render()

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentStars.php`

Render stars

If given a float for $stars, it will render partial stars.
If given an int for $stars, it will only render whole stars.

@param int|float|null $stars Number of stars that are in active state

@param bool $allowInput Whether to allow input of stars

@return string
