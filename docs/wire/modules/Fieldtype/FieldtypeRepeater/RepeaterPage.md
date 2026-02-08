# RepeaterPage

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPage.php`

RepeaterPage represents an individual repeater page item

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@property-read int $depth

## setForPage()

Set the page that owns this repeater item

@param Page $forPage

@return $this

## getForPage()

Return the page that this repeater item is for

@return Page

## setForField()

Set the field that owns this repeater item

@param Field $forField

@return $this

## getForField()

Return the field that this repeater item belongs to

Returns null only if $forField has not been set and cannot be determined from any other
properties of this page. Meaning null return value is not likely.

@return Field|null

## getForRoot()

For nested repeaters, returns the root level forPage and forField in an array

@param string $get Specify 'page' or 'field' or omit for array of both

@return array|Page|Field

@since 3.0.132

## getForFieldRoot()

For nested repeaters, return the root-level field that this repeater item belongs to

@return Field

@since 3.0.132

## getForPageRoot()

For nested repeaters, return the root-level non-repeater page that this repeater item belongs to

@return Page

@since 3.0.132

## get()

Get property

@param string $key

@return int|mixed|null

## getDepth()

Get depth

@return int

## setDepth()

Set depth

@param int $depth

## isPublic()

Is this page public?

In this case, we delegate that decision to the owner page.

@return bool

## isReady()

Is this a ready page?

@return bool

## getAccessTemplate()

Track a change to a property in this object

The change will only be recorded if change tracking is enabled for this object instance.


@param string $what Name of property that changed

@param mixed $old Previous value before change

@param mixed $new New value

@return $this

public function trackChange($what, $old = null, $new = null) {
parent::trackChange($what, $old, $new);
if($this->trackChanges()) {
$forPage = $this->getForPage();
$forField = $this->getForField();
if($forPage->id && $forField) $forPage->trackChange($forField->name);
}
return $this;
}
