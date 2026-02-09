# $wireTextTools->diffArray(array $oldArray, array $newArray): array

Source: `wire/core/WireTextTools.php`

Given two arrays, return array of the changes with 'ins' and 'del' keys

Based upon Paul Butler’s Simple Diff Algorithm v0.1 © 2007 (zlib/libpng) https://paulbutler.org

## Usage

~~~~~
// basic usage
$array = $wireTextTools->diffArray($oldArray, $newArray);

// usage with all arguments
$array = $wireTextTools->diffArray(array $oldArray, array $newArray);
~~~~~

## Arguments

- `$oldArray` `array`
- `$newArray` `array`

## Return value

- `array`

## Since

3.0.144
