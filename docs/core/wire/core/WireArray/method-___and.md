# $wireArray->and($item): WireArray

Source: `wire/core/WireArray.php`

Return a new copy of this WireArray with the given item(s) appended

Primarily for syntax convenience in fluent interfaces.


[Introduction of and method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

## Example

~~~~~
if($page->parents->and($page)->has($featured)) {
  // either $page or its parents has the $featured page
}
~~~~~

## Usage

~~~~~
// basic usage
$items = $wireArray->and($item);
~~~~~

## Hookable

- Hookable method name: `and`
- Implementation: `___and`
- Hook with: `$wireArray->and()`

## Arguments

- `$item` `Wire|WireArray` Item(s) to append

## Return value

- `WireArray` New WireArray containing this one and the given item(s).
