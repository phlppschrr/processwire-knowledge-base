# $pageimages->add($item): Pageimages|Pagefiles

Source: `wire/core/Pageimages.php`

Add a new Pageimage item, or create one from given filename and add it.

## Usage

~~~~~
// basic usage
$pageimages = $pageimages->add($item);
~~~~~

## Arguments

- `$item` `Pageimage|string` If item is a string (filename) then the Pageimage instance will be created automatically.

## Return value

- `Pageimages|Pagefiles`
