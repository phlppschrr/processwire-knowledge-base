# $repeaterPageArray->getNewItem(): RepeaterPage

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPageArray.php`

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

## Return value

RepeaterPage
