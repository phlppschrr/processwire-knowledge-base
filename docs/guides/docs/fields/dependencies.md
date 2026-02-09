# Field dependencies

Source: https://processwire.com/docs/fields/dependencies/

## Sections


## Input dependencies (or field dependencies)

Input and field dependencies enable you to specify the conditions under which a particular field in the page editor is shown or required.

Beyond the page editor, Inputfield dependencies may also be used with any other form based upon Inputfields. This includes ProcessWire Form Builder and configuration screens for ProcessWire modules.

- [Video: dependencies in action](#video)
- [Types of field dependencies](#types)
- [Selector string format](#selectors)
- [Allowed operators](#operators)
- [Limitations](#limitations)
- [Examples](#examples)
- [Matching a quantity of selected items](#example-quantity)
- [Matching blank or not-blank](#example-blank)
- [Matching a page in a page reference field](#example-page)
- [Matching a single checkbox field](#example-checkbox)


### Video: dependencies in action

This is an old video and shows a much older version of ProcessWire, but still does a good job of visually demonstrating how input/field dependencies work.


## Types of field dependencies


### Where you can configure *show-if* dependencies

**1. From any field edit screen in the ProcessWire admin. ** (Setup > Fields > [edit a field] > Input > Visibility > Show field if...).

**2. From any field-template context edit screen. ** (Setup > Templates > [edit a template] > [click a field] > Visibility > Show field if...).

**3. From the API on any Inputfield object/module: **

```
$inputfield->showIf = "field=value";
```

**4. From the **[Form Builder](/store/form-builder/)** module. ** ([edit a field] > Visibility > Show field if…)


### Where you can configure *require-if* dependencies

**1. From any field edit screen in the ProcessWire admin.** (Setup > Fields > [edit a field] > Input > Required [checked] > Required if…). *Please note: the required checkbox must be checked first. *

**2. From any field-template context edit screen.** (Setup > Templates > [edit a template] > [click a field] > Required [checked] > Required if…). *Please note: the required checkbox must be checked first. *

**3. From the API on any Inputfield object/module: **

```
$inputfield->required = 1; // must be set
$inputfield->requiredIf = "field=value";
```

**4. From the **[Form Builder](/store/form-builder/)** module. ** ([edit a field] > Required [checked] > Required if…)


## Selector string format

The expected format for selector strings is: **field=value**, where "field" is the name of the field you want to check, "=" is the operator you want to use for comparison, and "value" is the value you want to compare. The "field" may be the name of any field in your form. The operator may be any one of the allowed operators (see below). The "value" may be any string or integer value (though see *limitations* section below). You may specify multiple conditions by separating each field=value condition with a comma, i.e.

```
fullname!='', items>5
```


### Allowed operators

```
=   equal
!=  not equal
>   greater than
<   less than
>=  greater than or equal
<=  less than or equal
%=  contains phrase
*=  contains phrase (same as above) 
```


## Limitations

When using selector strings with Inputfield dependencies, the format is largely the same as [regular selector strings](/docs/selectors/) except that not as many options are yet supported.

- Currently, the "value" may not contain commas (as they are used to separate conditions) but that is only a short term limitation.
- While you can specify OR conditions with "|" in the field or value you cannot use [OR groups](../selectors.md#or-groups).
- The "~=" string matching operator is not supported.
- Subfields are not yet supported, except for "count", i.e. "field_name.count".
- Not all Inputfields will work with dependencies, though most should. We'll later update this page with a list of core Inputfields that are known not to work with dependencies.
- Field dependency selectors may not yet query the value of a multi-language field. However, they can show/hide multi-language fields according to the value of other fields.
- Field dependencies must be supported by the admin theme. All admin themes included with ProcessWire support them.


## Examples


### Matching a quantity of selected items

When attempting to match the value from a field containing multiple selections, you may match based on the quality of values selected by using the *count* subfield in your selector field. The format is "field.count=[number]", which is best demonstrated by example:

Matches if 1-2 items is selected from field "categories":

```
categories.count>0, categories.count<3
```

Matches only if no categories are selected:

```
categories.count=0
```


### Matching blank or not-blank

To match a blank value, specify an empty quoted string. Quotes may be double or single quotes, it does not matter. The following example would match if the *first_name* field was populated and the *last_name* field was blank.

```
first_name!='', last_name=''
```

To match a blank (or not blank) quantity of selected items, you can also use the "count" subfield described in the previous section.


### Matching a page in a page reference field

Most multiple selection fields in ProcessWire are based upon page reference fields. The values present in page reference fields are the selected page IDs. As a result, to match a specific page in a page reference field, you should match the ID. For instance, lets say that you wanted to match a "featured" category in your categories field. You'd determine the ID of the "featured" page by editing it and looking at the "id" variable in the address bar of your browser. Then you'd take that number and use it in your selector string. Lets say that the ID of the "featured" page was 1234. We would match it in the categories field like this:

```
categories=1234
```

That condition specifies that the "featured" page must be one of the selected categories. In a multiple-selection field, other categories may also be selected. If you wanted to specify that only the "featured" (id=1234) category may be selected, then you'd do this:

```
categories=1234, categories.count=1
```

*Note: we will soon support specification of page references by /path/to/page/ as well. *


### Matching a single checkbox field

The value of a checked checkbox field is 1 and the value of an unchecked checkbox field is blank or 0. While there are many ways to query the value, we recommend simply specifying a 1 for *checked* and a 0 for *unchecked*:

```
checkbox=1
checkbox=0
```
