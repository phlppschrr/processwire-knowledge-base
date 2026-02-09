# $repeaterPage->getAccessTemplate($type = 'view'): $this

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPage.php`

Track a change to a property in this object

The change will only be recorded if change tracking is enabled for this object instance.






public function trackChange($what, $old = null, $new = null) {
parent::trackChange($what, $old, $new);
if($this->trackChanges()) {
$forPage = $this->getForPage();
$forField = $this->getForField();
if($forPage->id && $forField) $forPage->trackChange($forField->name);
}
return $this;
}

## Usage

~~~~~
// basic usage
$result = $repeaterPage->getAccessTemplate();

// usage with all arguments
$result = $repeaterPage->getAccessTemplate($type = 'view');
~~~~~

## Arguments

- `$what` `string` Name of property that changed
- `$old` `mixed` Previous value before change
- `$new` `mixed` New value

## Return value

- `$this`
