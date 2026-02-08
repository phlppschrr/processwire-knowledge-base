# PageAction

Source: `wire/core/PageAction.php`

PageAction

Base class for Page actions in ProcessWire

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## other

@method bool action(Page $item)

@method executeMultiple(PageArray $items)

## getItemType()

Return array of module information

@return array

public static function getModuleInfo() {
return array(
'title' => 'PageAction (abstract)',
'summary' => 'Base class for PageActions',
'version' => 0
);
}

## getItemType()

Return the string type (class name) of items that this action operates upon

@return string

## execute()

Execute the action for the given page

@param Page $item Item to operate upon

@return bool True if the item was successfully operated upon, false if not.
