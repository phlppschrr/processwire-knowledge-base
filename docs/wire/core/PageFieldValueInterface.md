# PageFieldValueInterface

Source: `wire/core/Interfaces.php`

Interface for objects that carry a Field value for a Page

Optional, but enables Page to do some of the work rather than the Fieldtype

## formatted()

Get or set formatted state

@param bool|null $set Specify bool to set formatted state or omit to retrieve formatted state

@return bool

## setPage()

Set the Page

@param Page $page

## setField()

Set the Field

@param Field $field

## getPage()

Get the page or null if not set

@return Page|null

## getField()

Get the field or null if not set

@return Field|null
