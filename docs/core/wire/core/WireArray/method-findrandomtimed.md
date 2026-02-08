# $wireArray->findRandomTimed($num, $seed = 'Ymd'): WireArray

Source: `wire/core/WireArray.php`

Find a quantity of random elements from this WireArray based on a timed interval (or user provided seed).

If no `$seed` is provided, today's date (day) is used to seed the random number
generator, so you can use this function to rotate items on a daily basis.

_Idea and implementation provided by [mindplay.dk](https://twitter.com/mindplaydk)_

## Example

~~~~~
// Get same 3 random items per day
$randomItems = $items->findRandomTimed(3);

// Get same 3 random items per hour
$randomItems = $items->findRandomTimed('YmdH');
~~~~~

## Usage

~~~~~
// basic usage
$items = $wireArray->findRandomTimed($num);

// usage with all arguments
$items = $wireArray->findRandomTimed($num, $seed = 'Ymd');
~~~~~

## Arguments

- `$num` `int` The amount of items to extract from the given list
- `$seed` (optional) `int|string` Optionally provide one of the following: - A PHP [date()](http://php.net/manual/en/function.date.php) format string. - A number used to see the random number generator. - The default is the PHP date format "Ymd" which makes it randomize once daily.

## Return value

- `WireArray`

## See Also

- [WireArray::findRandom()](method-findrandom.md)
