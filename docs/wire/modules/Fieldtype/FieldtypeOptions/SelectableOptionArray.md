# SelectableOptionArray

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

ProcessWire Selectable Option Array, for FieldtypeOptions

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## other

@property string $title

@property string $value

@property int $id

## setPage()

Set the these options live on

@param Page $page

## getPage()

Returns page these options are for, if applicable (NullPage otherwise)

@return NullPage|Page

## setField()

Set the field these options are for

@param Field $field

## getField()

Returns Field object these options are for

@return null|Field

## of()

Get or set output formatting mode

@param bool|null $of Omit to retrieve mode, or specify bool to set it

@return bool Current mode. If also setting mode, returns previous mode.

## render()

Provide a default string rendering of these selectable options

For debugging or basic usage

@return string

## __toString()

Return string value of these options (pipe separated IDs)

@return string

## getProperty()

Enables this WireArray to behave like the first item (for getting properties)

@param string $property

@return mixed|null

## setProperty()

Enables this WireArray to behave like the first item (for setting properties)

@param string $property

@param mixed $value

@return SelectableOption|SelectableOptionArray

## isIdentical()

Is the given WireArray identical to this one?

@param WireArray $items

@param bool|int $strict

@return bool

## getByProperty()

Get SelectableOption by $property matching $value, or boolean false if not found

@param string $property May be "title", "value" or "id"

@param string|int $value

@param bool|null $noValue Value to return if option not present (default=false)

@return bool|null|SelectableOption

## getOptionByProperty()

Alias of getByProperty

Was renamed to getByProperty() but old method name kept in case this class is extended anywhere

@param string $property

@param string|int $value

@return bool|SelectableOption

@deprecated

## addByProperty()

Add option by property (id, name, title)

@param string $property One of id, name or title

@param string|int $value Value to match for above property

@return SelectableOption|false Returns option added or false if not found

@throws WireException

## addByID()

Add by option ID

@param int $id

@return false|SelectableOption Returns option added on success or false on fail

@throws WireException

## addByValue()

Add by option value

@param string $value

@return false|SelectableOption Returns option added on success or false on fail

@throws WireException

## addByTitle()

Add by option title

@param string $title

@return false|SelectableOption Returns option added on success or false on fail

@throws WireException

## getByID()

Get option by ID

@param int $id

@return SelectableOption|null

@since 3.0.242

## getByValue()

Get option by value

@param string $value

@return SelectableOption|null

@since 3.0.242

## getByTitle()

Get option by title

@param string $title

@return SelectableOption|null

@since 3.0.242

## removeByProperty()

Remove item by property (value, title, id)

@param string $property

@param string|int $value

@return bool

@since 3.0.242

## removeByID()

Remove option by ID

@param int $id

@return bool

@since 3.0.242

## removeByValue()

Remove option by value

@param string $value

@return bool

@since 3.0.242

## removeByTitle()

Remove option by title

@param string $title

@return bool

@since 3.0.242

## hasValue()

Is the given value present in these selectable options?

@param string $value

@return SelectableOption|bool Returns SelectableOption if found, or boolean false if not

## hasTitle()

Is the given title present in these selectable options?

@param string $title

@return SelectableOption|bool Returns SelectableOption if found, or boolean false if not

## hasID()

Is the given id present in these selectable options?

@param int $id

@return SelectableOption|bool Returns SelectableOption if found, or boolean false if not
