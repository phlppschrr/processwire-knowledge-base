# Input dependencies (or field dependencies)

Source: https://processwire.com/docs/fields/dependencies/

## Summary

Input and field dependencies enable you to specify the conditions under which a particular field in the page editor is shown or required.

## Key Points

- Input and field dependencies enable you to specify the conditions under which a particular field in the page editor is shown or required.
- Beyond the page editor, Inputfield dependencies may also be used with any other form based upon Inputfields. This includes ProcessWire Form Builder and configuration screens for ProcessWire modules.
- This is an old video and shows a much older version of ProcessWire, but still does a good job of visually demonstrating how input/field dependencies work.

## Sections


### Video: dependencies in action

This is an old video and shows a much older version of ProcessWire, but still does a good job of visually demonstrating how input/field dependencies work.


## Types of field dependencies

show-if dependencies enable you to specify a selector string of conditions that must match in order for a field to be shown.


### Where you can configure show-if dependencies

1. From any field edit screen in the ProcessWire admin. (Setup > Fields > [edit a field] > Input > Visibility > Show field if...).


### Where you can configure require-if dependencies

1. From any field edit screen in the ProcessWire admin. (Setup > Fields > [edit a field] > Input > Required [checked] > Required if…). Please note: the required checkbox must be checked first.


## Selector string format

The expected format for selector strings is: field=value, where "field" is the name of the field you want to check, "=" is the operator you want to use for comparison, and "value" is the value you want to compare. The "field" may be the name of any field in your form. The operator may be any one of the allowed operators (see below). The "value" may be any string or integer value (though see limitations section below). You may specify multiple conditions by separating each field=value condition with a comma, i.e.


### Allowed operators


## Limitations

When using selector strings with Inputfield dependencies, the format is largely the same as regular selector strings except that not as many options are yet supported.


## Examples
