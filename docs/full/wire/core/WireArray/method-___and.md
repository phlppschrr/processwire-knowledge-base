# WireArray::___and()

Source: `wire/core/WireArray.php`

Return a new copy of this WireArray with the given item(s) appended

Primarily for syntax convenience in fluent interfaces.

~~~~~
if($page->parents->and($page)->has($featured)) {
  // either $page or its parents has the $featured page
}
~~~~~

[Introduction of and method](https://processwire.com/talk/topic/5098-new-wirearray-api-additions-on-dev/)

@param Wire|WireArray $item Item(s) to append

@return WireArray New WireArray containing this one and the given item(s).
