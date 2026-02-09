# $wireArray->first(): Wire|mixed|bool

Source: `wire/core/WireArray.php`

Returns the first item in the WireArray or boolean false if empty.

Note that this resets the internal WireArray pointer, which would affect other active iterations.

## Example

~~~~~
$item = $items->first();
~~~~~

## Usage

~~~~~
// basic usage
$wire = $wireArray->first();
~~~~~

## Return value

- `Wire|mixed|bool`
