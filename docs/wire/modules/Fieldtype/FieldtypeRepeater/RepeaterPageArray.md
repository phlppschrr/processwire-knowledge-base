# RepeaterPageArray

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPageArray.php`

ProcessWire Repeater Page Array

Special PageArray for use by repeaters that includes a `getNewItem()` method
for adding new items to the repeater.

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Page $parent

@param Field $field

## setForPage()

Set page this RepeaterPageArray is for

@param Page $forPage

@since 3.0.188

## getForPage()

Get page this RepeaterPageArray is for

@return Page

@since 3.0.188

## setForField()

Set repeater field this RepeaterPageArray is for

@param RepeaterField $field

@since 3.0.188

## getForField()

Get repeater field this RepeaterPageArray is for

@return RepeaterField

@since 3.0.188

## getNewItem()

Return a new repeater item ready for use

This method differs from `FieldtypeRepeater::getBlankRepeaterPage()` in the following ways:

1. It returns an already existing readyPage, if it exists (otherwise it creates a new page)
2. The returned page is in a non-hidden published state, so will appear as soon as it is saved.
3. It appends the new item to this RepeaterPageArray.

Please note:

- This method has no relation/similarity to the `makeNew()` method.
- After making changes to the returned item, you must still `$item->save()` the item.
- When finished adding items you must `$page->save()` or `$page->save('repeater_field_name');`
  the page that has this repeater field.
- If previously added but unsaved items (aka "ready items") exist in the repeater, they will
  be recycled and returned by this method rather than creating a new item.

~~~~~
$item = $page->repeater_field->getNewItem(); // get new repeater item
$item->title = 'My new item'; // set field value(s) as needed
$item->save(); // save the item
$page->save('repeater_field'); // save the page that has the repeater
~~~~~

@return RepeaterPage

## trackAdd()

Track an item added

@param Wire|mixed $item

@param int|string $key

## trackRemove()

Track an item removed

@param Wire|mixed $item

@param int|string $key
