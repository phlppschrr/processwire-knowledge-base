# Custom Fields Module

Source: https://processwire.com/blog/posts/custom-fields-module/

## Sections


## ProFields: Custom Fields

30 August 2024 by Ryan Cramer [ 0 Comments](/blog/posts/custom-fields-module/#comments)

This week we introduce a new ProFields module named Custom Fields. This module provides a way to rapidly build out ProcessWire fields that contain any number of subfields/properties within them.

No matter how simple or complex your needs are, Custom Fields makes your job faster and easier. Not only does this post introduce Custom Fields, but also documents how to use them and includes numerous examples.


## What are Custom Fields? (and why?)

This module set (Fieldtype and Inputfield) was built to answer a need that came up in a recent client project. This particular need involved a few different fields that needed to have 40+ subfields (or properties) within them. They would regularly change in the short term too, and likely grow larger. ProFields [Combo](/store/pro-fields/combo/) could do it, but that's a lot of subfields to manage interactively in any Combo field. I wished that I could just quickly define these subfields/properties in a text editor as a PHP array or JSON, as that would save me a lot of time in this particular case. So that's what I did.

Always looking for a good excuse to build a new module, I developed the proof-of-concept module very quickly: about as much time as it would have taken to create the fields using existing Fieldtypes in ProcessWire. It saved enough time and worked well enough that I thought I should take the time build it out fully, for this project, future projects, and for sharing with others.

After learning there was significant crossover with another module ([Mystique](/modules/mystique/)), I decided to instead develop Custom Fields as a [ProFields](/store/pro-fields/) module, so that it was not directly competitive with an existing excellent and supported module.

To make it worthwhile as a Pro module, Custom Fields aims to go a little further in several ways, focused more on findability, supporting more input types, and providing dedicated Pro module support. It fits right in with the concept of ProFields modules, taking a need that might traditionally require a lot of fields, and making it happen with just one field. Thereby saving you a lot of time.


## How do Custom Fields work?

Custom Fields are defined in a PHP or JSON file that returns an array of the fields within it. I'll refer to fields within a Custom Field as "properties", since they become properties of a Custom Field object. But you can also think of them as "subfields", "columns" or "inputs" for a ProcessWire field.

Whatever label we use, these properties are defined in the PHP or JSON file using ProcessWire’s Inputfields API. This API makes it simple to define inputs for forms and is used throughout ProcessWire and even in some 3rd party modules, including Mystique. These input definitions specify the properties (or subfields or inputs) of your Custom Field. The following example defines properties for "first name", "last name" and "email":

```php
<?php 
return [
  'first_name' => [
    'type' => 'text',
    'label' => 'First name'
  ],
  'last_name' => [
    'type' => 'text',
    'label' => 'Last name'
  ],
  'email' => [
    'type' => 'email',
    'label' => 'Email address'
  ]
];
```

As you can see from the above, each property typically needs at least 3 pieces of information:

- `name` The name of the property using `[_a-zA-Z0-9]`
- `type` The type of input that it will use
- `label` The text label the editor sees (optional but recommended)

Let's say that the above PHP array defines a Custom Field named "contact". You would place the PHP array (above) in the file: /site/templates/custom-fields/contact.php

Next, you'd add the "contact" field to a template, and edit a page using that template. It would look like this:

Once we have saved values for those properties in the page editor, we could output them from our template file like this:

```
<li>First name: <?= $page->contact->first_name ?>
<li>Last name: <?= $page->contact->last_name ?>
<li>Email: <?= $page->contact->email ?>
```


## Defining properties (aka subfields or inputs)

The above example demonstrates a very simple custom field. You might be wondering what other `type` values can be specified (for different property/input types), and what other settings each definition can have. We'll cover all the details here.


### Possible values for “type”

In our earlier example, we used 2 types, `text` and `email`. When we specify a "type" we are actually specifying a ProcessWire Inputfield module name, without the `Inputfield` prefix. Though if you prefer it, you can specify the entire Inputfield module name for the `type`. For instance, we used `text` as a type, which is a shortcut/synonym for `InputfieldText`.

Some Inputfield modules require a corresponding Fieldtype module, and these cannot be used in Custom Fields. For instance, `InputfieldRepeater` requires `FieldtypeRepeater`, so it can't be used in a Custom Field. Not to worry, the majority of Inputfield modules can be used on their own, and thus can be used in Custom Fields.

At this time, the following core Inputfield types (modules) are known to work with Custom Fields. Meaning, you can specify any of these for the `type` setting in your Custom Field properties:

- AsmSelect
- Checkbox
- Checkboxes
- Datetime
- Email
- Fieldset
- Float
- Hidden
- Icon
- Integer
- Markup
- Page
- Radios
- Select
- SelectMultiple
- Text
- Textarea
- TextTags
- TinyMCE
- Toggle
- URL

This list will likely continue to grow with each version. Whatever type you choose, it will likely have some of it's own custom settings that you can configure in your definition array too. More on that below.


### Other settings for property definition

In our earlier example that defined our "contact" field (with first name, last name, email) we only specified one setting for each, which was the "label". Below is a list of other common settings you might use or see (A-Z):

|  |  |
| --- | --- |
| `columnWidth` | The percent width of the input in the page editor (10-100), omit for 100%. |
| `description` | Text that appears above the input but under the label. |
| `detail` | Muted text that appears under the input (and under the notes, if present). |
| `icon` | Font-awesome 4.7 icon name to display with the label ("fa-" prefix optional). |
| `notes` | Highlighted text that appears under the input. |
| `options` | Array that defines selectable options for any single or multi-selection input type. |
| `placeholder` | Placeholder text for most text-based inputs. |
| `required` | Specify true to make the field required, omit otherwise. |
| `requiredIf` | Selector that denies conditions when input is required (required=true also needed). |
| `showIf` | Selector that defines the conditions necessary to show this input/property. |
| `useLanguages` | Specify true to make any text input multi-language (LanguageSupport modules required). |
| `value` | Default value to use or omit for empty/blank. |

Almost all types also have their own settings which can be found by looking in the phpdoc header of each corresponding Inputfield module [here](https://github.com/processwire/processwire/tree/master/wire/modules/Inputfield).

Given some of the additional properties we've learned about above, let's expand upon our original example:

```php
<?php 
return [
  'first_name' => [
    'type' => 'text',
    'label' => 'First name',
    'required' => true,
    'columnWidth' => 50,
  ],
  'last_name' => [
    'type' => 'text',
    'label' => 'Last name',
    'required' => true,
    'columnWidth' => 50
  ],
  'email' => [
    'type' => 'email',
    'label' => 'Email address',
    'icon' => 'envelope-o',
    'placeholder' => 'person@company.com'
  ],
  'bio' => [
    'type' => 'textarea',
    'label' => 'Biography',
    'rows' => 5,
    'value' => 'Enter biography (example of default value)'
  ]
];
```

And here is the result:


### Custom Fields examples

For real cases demonstrating almost all of the supported types with examples of more than 40 properties/inputs, see the files included with this module in /site/modules/FieldtypeCustom/examples/. These examples can also be viewed in in your admin at Setup > Fields > [your_custom_field] > Details [tab]. You may even want to use these examples as starting points when creating a new Custom Field. Below is a list of the included examples:

|  |  |
| --- | --- |
| `**example-basic.json**` | Demonstrates basic text inputs and a fieldset (JSON version). |
| `**example-basic.php**` | Same as the JSON version, but in PHP. Also demonstrate a "country" select. |
| `**example-basic2.php**` | Same as the above, but built out using Inputfield objects rather than arrays. This might be worthwhile for cases where you have an IDE like PhpStorm that can automatically identify the custom settings for each Inputfield type. |
| `**example-dates.php**` | Demonstrates several different kinds of date/time inputs that you can use. |
| `**example-dependencies.php**` | Demonstrates how you can use `$page` or showIf dependencies where the value in one field can affect the visibility or requirements of another. |
| `**example-languages.php**` | Demonstrates how to use multi-language inputs/properties as well as how to make your property labels and option labels translatable. |
| `**example-pagerefs.php**` | Shows you how to use various different kind of single-and-multiple Page selection types, including select, pageListSelect, pageListSelectMultiple, and pageAutocomplete. |
| `**example-selects.php**` | Demonstrates how to use radio button inputs, checkbox, checkboxes, select, asmSelect, toggle, and textTags. |
| `**example-tinymce.php**` | Demonstrates using TinyMCE inputs, as well as how you can make them inherit from existing TinyMCE fields. |
| `**example-profields.php**` | A couple of ProFields Inputfield modules can also be used in Custom Fields and this file demonstrates them. |
| `**example-kitchen-sink.php**` | This takes all of the examples above in a single file so that you can test them out all at once. |


### Using fieldsets

You can use fieldsets in Custom Fields to visually group inputs together. A fieldset is defined by specifying `"type" => "fieldset"` and then specifying a `children` array that defines the properties/inputs within the fieldset. If we wanted to expand the above example to include an "Address" fieldset, we could do so like this:

```php
<?php namespace ProcessWire;
return [
  'first_name' => [
    'type' => 'text',
    'label' => 'First name',
    'required' => true,
    'columnWidth' => 50,
  ],
  'last_name' => [
    'type' => 'text',
    'label' => 'Last name',
    'required' => true,
    'columnWidth' => 50
  ],
  'email' => [
    'type' => 'email',
    'label' => 'Email address',
    'icon' => 'envelope-o',
    'placeholder' => 'person@company.com'
  ],
  'bio' => [
    'type' => 'textarea',
    'label' => 'Biography',
    'rows' => 5,
    'value' => 'Enter biography here (this is an example of a default value)'
  ],
  'address' => [
    'type' => 'fieldset',
    'label' => 'Address (fieldset example)',
    'icon' => 'address-card-o',
    'children' => [
      'address_street' => [
        'type' => 'text',
        'label' => 'Street'
      ],
      'address_city' => [
        'type' => 'text',
        'label' => 'City',
        'columnWidth' => 50
      ],
      'address_state' => [
        'type' => 'text',
        'label' => 'State/province',
        'columnWidth' => 25
      ],
      'address_zip' => [
        'type' => 'text',
        'label' => 'Zip/post code',
        'columnWidth' => 25
      ],
      'address_country' => [
        'type' => 'select',
        'label' => 'Country',
        'options' => include(
          wire()->config->paths('FieldtypeCustom') . 'examples/countries.php'
        ),
        'value' => 'United States', // example of default value
      ]
    ]
  ]
];
```

The result looks like this:

When working with fieldsets, note that the fieldset defines a group that appears in the page editor, but does not define another layer of property hierarchy in the actual stored value or API. Meaning a property named "city" in a fieldset named "address" is still accessed by `$contact->city`, and not `$contact->address->city`. If you want your API access to reflect this hierarchy you may want to prefix your property names with the fieldset name, such as `address_city`, as we have done in the example above.


## Searching custom fields with selectors

You can find pages by any property in a Custom Field. All properties are searchable in Custom Fields, and you may use whatever operators are appropriate for the type you are trying to match.

```php
// matching text fields
$pages->find("contact.first_name=Hanna");
$pages->find("contact.bio*=expert");

// matching a select field
$pages->find("contact.address_country=United States");

// matching single or multi page fields
$category = $pages->get("/categories/some-category");
$pages->find("contact.categories=$category");

// matching number or date fields
$pages->find("contact.num_tours>3");
$pages->find("contact.date_from>2020-09-01");
```

Note that when matching a field using any single or multi-selection type, you should match the option value rather than the label. If you aren't using separate labels and values, then this distinction won't matter.

You can also perform text matches on the entire Custom Field, searching all properties at once:

```php
$pages->find("contact*=Atlanta"); 
```

All properties are also individually searchable from Lister/ListerPro with each property selectable by the core InputfieldSelector module. ListerPro can also individually output the value of any property in its own column. *(For any other Fieldtype developers out there, another way of saying this is that Custom Fields fully implement both the getSelectorInfo() and getMatchQuery() methods of the Fieldtype class.)*


## Outputting custom fields

Custom fields can be accessed from the API and output in a manner similar to any other Fieldtype that supports subfields/properties within it. They are all stored in a WireData (CustomWireData) object that enables you to access any property directly, or you can iterate through all of them at once.

Most text, number and single-selection properties can be output like this example below (replacing `custom_field` with the name of your custom field, and `property` with the name of the property within it):

```
echo $page->custom_field->property;
```

Multi-selection properties come as a PHP array and can be output like this:

```
foreach($page->custom_field->countries as $country) {
  echo "<li>$country</li>";
}
```

If your selection property has separate values and labels, note that the `$country` above will be the option `value` and not the option `label`. For instance, the value might be "US" and the label might be "United States". You can get the label like this:

```
// single selection 'country' field
$value = $page->custom_field->country;
$label = $page->custom_field->label('country', $value);

// multi-selection
foreach($page->custom_field->countries as $value) {
  $label = $page->custom_field->label('countries', $value);
  echo "<li>$value: $label</li>"; // i.e. "USA: United States"
}
```

Single page selection properties typically have a value of `Page` or `NullPage` (or false, if specified in your settings). So you could output the title of a selected page like this:

```
echo "Category: " . $page->custom_field->category->title;
```

Multi page selection fields come as a [PageArray](../api-full/wire/core/PageArray/index.md), which you could output like this:

```
foreach($page->custom_field->categories as $category) {
  echo "<li>$category->title</li>";
}
```

…or if you want to get fancy with it:

```
echo $page->custom_field->categories->each("<li>{title}</li>"); 
```

Multi-language text properties have an object value of [LanguagesPageFieldValue](../api-full/wire/modules/LanguageSupport/LanguagesPageFieldValue/index.md), just like multi-language values outside of a Custom Field. When output as a string, they output the text in the current user’s language:

```
echo $page->custom_field->terms_and_conditions;
```

Dates will output differently depending on whether the `$page` has [output formatting](/blog/posts/output-formatting/) on or off. When output formatting is off, populated dates display as `YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SS`. When output formatting is on, the dates display using the format specified with with your date property in this order: `dateOutputFormat`, `dateInputFormat`.

Single checkbox fields are integer `1` when selected and empty (blank) when not. Checkbox fields defined with a custom checked value will use that instead of integer 1.

TextTags fields have a space-separated string value of the selected tags.

Want to get the "label" of a custom field property? (and translated, if multilanguage). Here's how:

```
echo $page->custom_field->label('email'); // i.e. "Enter email address"
```


### Outputting all your properties at once

Here's a snippet of code that I've been using to output all of my Custom Field properties in an HTML table. It goes the appropriate template file and provides a quick reference of all the values and types that might be handy during development.

```php
<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Label</th>
      <th>Type</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody><?php
    $customValue = $page->your_custom_field;
    foreach($customValue as $property => $val):
      $label = $customValue->label($property);
      $type = is_object($val) ? wireClassName($val) : gettype($val);
      $val = $type === 'array' ? print_r($val, true) : "$val";
      ?>
      <tr>
        <td><?=$property?></td>
        <td><?=$label?></td>
        <td><?=$type?></td>
        <td><pre><?=htmlspecialchars($val)?></pre></td>
      </tr>
    <?php endforeach; ?>
  </tbody>
</table>
```


### A note about output formatting

When editing your Custom Field, the Settings fieldset has an option to "Entity encode text when $page output formatting is on". I strongly recommend having this enabled. This ensures that when you are outputting property values (as we did in the examples above) they are appropriate for HTML output, with characters like `<` and `>` getting converted to `<` and `>` and so on.


## Roadmap

Future versions are already being planned, with features such as:

- Support for making existing types repeatable, also including fieldsets.
- Support for file and image fields
- Support for MySQL 8.x multi-valued indexes

What else would you like to see in Custom Fields?


### Screenshots of example Custom Fields

All of these examples are included in the /site/modules/FieldtypeCustom/examples/ directory. What you see below can all be in a single Custom Field, or several of them, if you prefer. Custom Fields can be as simple or as complex as you need.


## Download

The first (beta) version of Custom Fields can be downloaded from the ProFields support board download thread (login required). If you don't have [ProFields](/store/pro-fields/), or if you want some similar capabilities in a more mature, widely tested and free module, or you want a module with a cooler name, be sure to check out [Mystique](/modules/mystique/).
