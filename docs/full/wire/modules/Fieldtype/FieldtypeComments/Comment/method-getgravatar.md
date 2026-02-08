# Comment::getGravatar($email, $rating = 'g', $imageset = 'mm', $size = 80): string

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Returns a URL to this user's gravatar image (static version, use non-static gravatar() function unless you specifically need static)

## Arguments

- string $email
- string $rating Gravatar rating, one of [ g | pg | r | x ], default is g.
- string $imageset Gravatar default imageset, one of [ 404 | mm | identicon | monsterid | wavatar | retro | blank ], default is mm.
- int $size Gravatar image size, default is 80.

## Return value

string
