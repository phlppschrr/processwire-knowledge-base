# RepeaterPage::getAccessTemplate()

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterPage.php`

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
