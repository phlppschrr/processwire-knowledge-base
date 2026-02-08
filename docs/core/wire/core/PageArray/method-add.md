# $pageArray->add($item): $this

Source: `wire/core/PageArray.php`

Add one or more Page objects to this PageArray.

Please see the `WireArray::add()` method for more details.

~~~~~
// Add one page
$pageArray->add($page);

// Add multiple pages
$pageArray->add($pages->find("template=basic-page"));

// Add page by ID
$pageArray->add(1005);
~~~~~

## Arguments

- Page|PageArray|int $item Page object, PageArray object, or Page ID. - If given a `Page`, the Page will be added. - If given a `PageArray`, it will do the same thing as the `WireArray::import()` method and append all the pages. - If Page `ID`, the Page identified by that ID will be loaded and added to the PageArray.

## Return value

$this
