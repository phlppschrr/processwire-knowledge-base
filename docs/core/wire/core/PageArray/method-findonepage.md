# $pageArray->findOnePage($selector): Page|NullPage

Source: `wire/core/PageArray.php`

Same as find() or findOne() methods, but always returns a Page (whether Page or NullPage)

## Usage

~~~~~
// basic usage
$page = $pageArray->findOnePage($selector);
~~~~~

## Arguments

- `$selector` `string`

## Return value

- `Page|NullPage`

## Since

3.0.162
