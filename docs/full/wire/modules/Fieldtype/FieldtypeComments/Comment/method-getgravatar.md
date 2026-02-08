# Comment::getGravatar()

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Returns a URL to this user's gravatar image (static version, use non-static gravatar() function unless you specifically need static)

@param string $email

@param string $rating Gravatar rating, one of [ g | pg | r | x ], default is g.

@param string $imageset Gravatar default imageset, one of [ 404 | mm | identicon | monsterid | wavatar | retro | blank ], default is mm.

@param int $size Gravatar image size, default is 80.

@return string
