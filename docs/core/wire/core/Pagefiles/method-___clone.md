# $pagefiles->___clone(Pagefile $item, array $options = array()): Pagefile|bool

Source: `wire/core/Pagefiles.php`

Duplicate the Pagefile and add to this Pagefiles instance

After duplicating a file, you must follow up with a save of the page containing it.
Otherwise the file is marked for deletion.

## Usage

~~~~~
// basic usage
$pagefile = $pagefiles->___clone($item);

// usage with all arguments
$pagefile = $pagefiles->___clone(Pagefile $item, array $options = array());
~~~~~

## Arguments

- `$item` `Pagefile` Pagefile item to duplicate
- `$options` (optional) `array` Options to modify default behavior: - `action` (string): Specify "append", "prepend", "after", "before" or blank to only return Pagefile. (default="after") - `pagefiles` (Pagefiles): Pagefiles instance file should be duplicated to. (default=$this)

## Return value

- `Pagefile|bool` Returns new Pagefile or boolean false on fail
