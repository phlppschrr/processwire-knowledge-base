# FieldsetPage

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldsetPage.php`

FieldsetPage represents Page objects used by the FieldtypeFieldsetPage module

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## trackChange()

Track a change to a property in this object

The change will only be recorded if change tracking is enabled for this object instance.


@param string $what Name of property that changed

@param mixed $old Previous value before change

@param mixed $new New value

@return $this

## get()

Get a property

@param string $key

@return mixed

## getOf()

Get property in formatted (true) or unformatted (false) state

@param string $key

@param bool $of

@return mixed

@since 3.0.215

## getUnformatted()

Get the unformatted value of a field, regardless of current output formatting state

@param string $key Field or property name to retrieve

@return mixed

## getFormatted()

Get the formatted value of a field, regardless of output formatting state

@param string $key Field or property name to retrieve

@return mixed

## getForPage()

Return the page that this repeater item is for

@return Page

## getForField()

Return the field that this repeater item belongs to

@return Field
