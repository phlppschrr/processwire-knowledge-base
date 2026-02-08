# $pagesRawFinder->ids($csv = false): array|string

Source: `wire/core/PagesRaw.php`

Get or convert $this->ids to/from CSV

The point of this is just to minimize the quantity of copies of IDs we are keeping around.
In case the quantity gets to be huge, it'll be more memory friendly.

## Usage

~~~~~
// basic usage
$array = $pagesRawFinder->ids();

// usage with all arguments
$array = $pagesRawFinder->ids($csv = false);
~~~~~

## Arguments

- `$csv` (optional) `bool`

## Return value

- `array|string`
