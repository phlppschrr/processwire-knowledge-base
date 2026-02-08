# NullPage

Source: `wire/core/NullPage.php`

ProcessWire NullPage

NullPage is a type of Page object returned by many API methods to indicate a non-match.
The simplest way to detect a NullPage is typically by checking the value of the `$page->id` property.
If it happens to be 0 then for most practical purposes, you have a NullPage. A NullPage object
has all of the same methods and properties as a regular `Page` but there's not much point in
calling upon them since they will always be empty.
~~~~~
$item = $pages->get("featured=1");

if(!$item->id) {
  // this is a NullPage
}

if($item instanceof NullPage) {
  // this is a NullPage
}
~~~~~

Placeholder class for non-existant and non-saveable Page.
Many API functions return a NullPage to indicate no match.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@property int $id The id property will always be 0 for a NullPage.
