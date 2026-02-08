# Functions::wireIconMarkup()

Source: `wire/core/Functions.php`

Render markup for a system icon

It is NOT necessary to specify an icon prefix like “fa-” with the icon name.

Modifiers recognized in the class attribute:
lg, fw, 2x, 3x, 4x, 5x, spin, spinner, li, border, inverse,
rotate-90, rotate-180, rotate-270, flip-horizontal, flip-vertical,
stack, stack-1x, stack-2x

~~~~~
// Outputs: "<i class='fa fa-home'></i>"
echo wireIconMarkup('home');

// Outputs: "<i class='fa fa-home fa-fw fa-lg my-class'></i>"
echo wireIconMarkup('home', 'fw lg my-class');

// Outputs "<i class='fa fa-home fa-fw' id='root-icon'></i>" (3.0.229+ only)
echo wireIconMarkup('home', 'fw id=root-icon');
echo wireIconMarkup('home fw id=root-icon'); // same as above
~~~~~


@param string $icon Icon name (currently a font-awesome icon name)

@param string $class Any of the following:
 - Additional attributes for class (example: "fw" for fixed width)
 - Your own custom class(es) separated by spaces
 - Any additional attributes in format `key="val" key='val' or key=val` string (3.0.229+)
 - An optional trailing space to append an `&nbsp;` to the return icon markup (3.0.229+)
 - Any of the above may also be specified in the $icon argument in 3.0.229+.

@return string
