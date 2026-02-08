# InputfieldPageTableAjax

Source: `wire/modules/Inputfield/InputfieldPageTable/InputfieldPageTableAjax.php`

Ajax handler for FieldtypePageTable/InputfieldPageTable

Concept by Antti Peisa
Code by Ryan Cramer
Sponsored by Avoine

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method void checkAjax()

## __construct()

Construct

## ___checkAjax()

Check if current request is a valid ajax request and call renderAjax() if it is.

## renderAjax()

Render the ajax request output directly and halt execution

@param Page $page

@param Field $field

## addItem()

Handler for the InputfieldPageTableAdd ajax action

@param Page $page

@param Field $field

@param Page $item

@return bool

## sortItems()

Update items to make sure they are in same order specified in GET var InputfieldPageTableSort

@param Page $page

@param Field $field

@param string $sort CSV string
