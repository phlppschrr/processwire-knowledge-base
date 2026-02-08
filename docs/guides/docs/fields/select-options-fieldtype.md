# Select Options Fieldtype in ProcessWire CMS

Source: https://processwire.com/docs/fields/select-options-fieldtype/

# Select Options Fieldtype (FieldtypeOptions) 

The Options Fieldtype provides single and multi choice selectable options in ProcessWire, as an alternative to using Page fields.

For features and highlights see our [post on the Options Fieldtype](/blog/posts/new-options-fieldtype-processwire-2.5.17/) or continue reading here to learn more about how to use it.
- [About the Options Fieldtype](#about-the-options-fieldtype)
- [Creating an Options field](#creating-an-options-field)
- [Defining options](#defining-options)
- [Adding New Options](#adding-new-options)
- [Moving or Sorting Options](#moving-or-sorting-options)
- [Editing or Renaming Options](#editing-or-renaming-options)
- [Deleting Options](#deleting-options)
- [Multi-Language: Translating Options](#multi-language-translating-options)
- [Separate Option Values](#separate-option-values)
- [Outputting selected options on a page](#outputting-selected-options-on-a-page)
- [Checking if an option is selected](#checking-if-an-option-is-selected)
- [Manipulating options on a page from the API](#manipulating-options-on-a-page-from-the-api)
- [Manipulating available options for all pages](#manipulating-available-options-for-all-pages)

---
[](#)

### About the Options Fieldtype

While we usually recommend using the Page Fieldtype for selectable options, this Options Fieldtype provides a convenient alternative for when the selectable options will not benefit from being pages, or when a speedy definition process outweighs the benefits of using pages. Like with the Page Fieldtype, you can define what type of input should be used with the field settings. The input type can be any core or 3rd party Inputfield that extends ProcessWire's *InputfieldSelect* module. For core Inputfields, this includes: Single Select, Multiple Select, Checkboxes, Radio Buttons, and AsmSelect (a sortable multi-select).

Options are stored in a relational database normalized manner, ensuring that changes to existing options apply across existing selections.

The Options Fieldtype was added to the core in ProcessWire 2.5.17.

---

## Options Administration

[](#)

### Creating an Options field

1. Confim that you are running ProcessWire 2.5.17 or newer.
2. Install the Select Options Fieldtype module, if it is not already installed. Do this by going to Modules > Core > Fieldtype > Select Options (or from the drop-down menus: Modules > Install > FieldtypeOptions). If you don't see it, you may need to first click on Modules > Refresh, and try again.
3. Create a new field (Setup > Fields > Add New) and choose "Options" as the type.
4. After creating the field, click to the *Details* tab, where you can define your options.

[](#)

### Defining options

You can define options on the *Details* tab when editing an Options field (Setup > Fields > your field). Options are defined in a multi-line text box, where each line represents one option. You may type or paste in a list of options (like a list of countries for example, 1 per line) and save.

Once an option exists in the database, it is assigned an ID number. When selected options are saved on a page, the ID number [for each option] is stored rather than the option title or value. This enables you to go back and later modify options without breaking existing selections on a page. However, it does require that that the assigned ID number always remain with the option.

In addition, these ID numbers enable mutli-language support by connecting an option in one language with a translation in another language. Please note that these ID numbers need not symbolize anything about your option title or value, and are not typically used for anything on the front-end of your site.[](#)

### Adding New Options

Enter the text of each new option on a new line anywhere in the existing options. You may omit the ID number as one will be automatically assigned after you save. Once assigned, you should never change this ID number, but you can change the title (or value) as much as you like.

While we recommend letting the Options Fieldtype assign unique ID numbers for you, you may optionally assign your own. To do this, specify `123=title` when adding a new option, where `123` is the ID number you wish to assign and `title` is the title text for your option. If you need separate "value" and "title" properties for each option, see the last section in these notes.[](#)

### Moving or Sorting Options

Copy entire line(s), including ID number, and paste wherever you want them to go.[](#)

### Editing or Renaming Options

Modify the option title or value as you would like, ensuring that the original ID number remains connected with the option.[](#)

### Deleting Options

Delete the entire lines containing the options that you want to delete. You will be asked to confirm the deletion after you submit the form. The option will not be deleted until you click the box to confirm and submit the form again. Note that this also deletes any selections for that option in the database.

If using multi-language options, deleting the option in the default language deletes it for all languages, and deleting an option in a non-default language only deletes the translation.[](#)

### Multi-Language: Translating Options

Multi-language support with options requires that you have the LanguageSupportFields module installed (Modules > Core > Language > Language Support Fields).

Define your options in the default language and save, before defining them in other languages. Copy the options you want to translate from the default language tab to the other language tab. Paste in and translate the titles (and/or values). Untranslated options inherit the default language title and value. If using separate option values (as described in the next section) your translation does not need to include the "value" portion unless you want it to.[](#)

### Separate Option Values

By default only titles are kept with each option. If you want to maintain a separate value and title, enter your option in the format `value|title` (for new options) or `123=value|title` (for existing options that already have an ID assigned). The text for `value` and `title` will be kept as separate `$option->value` and `$option->title` properties from the API. These properties can also be independently queried to find pages from the API.

---

## Options API

[](#)

### Outputting selected options on a page

You output options in exactly the same way that you would page titles. For our example, lets assume you created an Options field called "countries" and you wanted to output an HTML list of those countries:

```
foreach($page->countries as $country) {
  echo "<li>$country->title</li>";
}
```

If Options field only supports 1 selection, the above example would still work. However, you can also do this:

```
echo $page->countries->title;
```

There is no distinction between single-value and multi-value options at the API level. You can simply choose to treat it as a single or multi-value field as you see fit. This works because when you access the title (or other) property from the field, it simply gives you the value for that property from the first item.[](#)

### Checking if an option is selected

**If you are working with a single-selection options field**, then you can simply compare the option title (or value if used) to the value you want to check. Below, we'll assume we have a single-selection in a field named "country":

```
if($page->country->title === 'Finland') {
  // Finland is selected
}
```

If using [separate titles and values](#separate-option-values), and you were using country codes for the values, like "us", "mx", "de", "fi", etc., then you you could compare the option value rather than the title. This is probably what you'd want to do in a multi-language environment, where the title will vary according to language, but the value will not.

```
if($page->country->value === 'fi') {
  // Finland is selected
}
```

**If you are working with a multiple-selection options field**, then there are hasTitle() and hasValue() helper methods that you can use. In the example below, we'll return to our "countries" options field that supports multiple country selections:

```
if($page->countries->hasTitle('Finland')) {
  // Finland is selected
}
```

...or if using [separate titles and values](#separate-option-values), you may want to compare the option values instead:

```
if($page->countries->hasValue('fi')) {
  // Finland is selected
}
```

All selectable options also have numeric IDs which you can use in comparisons as well. For example: `$page->country->id == 123` or `$page->countries->hasID(123);` But using IDs doesn't make for very easy-to-read code, so we'd suggest sticking with using the titles or values instead.[](#)

### Manipulating options on a page from the API

The value of your Options field (i.e.` $page->countries`) is a WireArray, and can be manipulated using any of the methods supported by WireArray. Once manipulated, you would either save the page they live on, or save the page field, i.e. `$page->save('countries');`

Before manipulation options on a page, always make sure that output formatting is OFF first:

```
$page->of(false); // set output formatting off
```

If working with an Options field that supports a single selected value, you can set it directly as the title:

```
$page->countries = 'Finland';
```

For a multi-value Options field, set it as an array…

```
$page->countries = array('Finland', 'Sweden', 'Norway');
```

…or a pipe "|" separated string:

```
$page->countries = 'Finland|Sweden|Norway';
```

The above examples demonstrate setting the value by the option's *title* property. You can also set it from the option's *id* property, the *value* property, or directly with SelectableOption or SelectableOptionArray objects. If setting with the *value* property, note that the *title* property is considered before the *value* property (if there are any conflicts).

**A note about numeric titles: **Any time you set from a numeric value, it is assumed to be the *id* property. If your situation involves options that have a numeric *title*, this is someting to consider, as you'll likely want to stick to setting the options by *id* in order to avoid confusion. Or, you can use one of the methods described below to retrieve all options and determine which ones you need. In particular, see the "Getting the *id* property of an option when you only know the *title*" section below.

#### Getting all possible options

This retrieves all possible options for the field, regardless of whether they are selected or not (there is no page involved here).

```
$field = $fields->get('countries');
$all_options = $field->type->getOptions($field);
```

#### Getting the *id* property of an option when you only know the *title*:

The following code examples build upon the previous example (getting all possible options), so make sure to include that first.

```
$option = $all_options->get("title=Finland"); 
echo "The id for $option->title is: $option->id";
```

If you need to pull multiple options out of a set:

```
$options = $all_options->find("title=Finland|Sweden|Norway");
foreach($options as $option) {
  echo "<li>The id for $option->title is: $option->id</li>";
}
```

You can use these values (objects) you pulled from `$all_options` to set the value of your options field:

```
$options = $all_options->find("title=Finland|Sweden|Norway");
$page->countries = $options;
```

[](#)

### Manipulating available options for all pages

This section coming soon. For additional info now, see the bottom of the /wire/modules/Fieldtype/FieldtypeOptions/FieldtypeOptions.module file, which contains all the public API methods for adding, updating and deleting available options at the API level.
- [Fields, types, input](/docs/fields/)
- [Introduction to fields](/docs/start/structure/fields/)
- [Field dependencies](/docs/fields/dependencies/)
- [Repeaters](/docs/fields/repeaters/)
- [Textarea](/docs/fields/textarea-fieldtype/)
- [Select options](/docs/fields/select-options-fieldtype/)
- [Images](/docs/fields/images/)
- [Multi-language fields](/docs/multi-language-support/multi-language-fields/)
- [CKEditor](/docs/fields/ckeditor/)

- [Docs](/docs/)
- [API reference](/api/ref/)
- [Getting started](/docs/start/)
- [Front-end](/docs/front-end/)
- [Tutorials](/docs/tutorials/)
- [Selectors](/docs/selectors/)
- [Modules & hooks](/docs/modules/)
- [Fields, types, input](/docs/fields/)
- [Access control](/docs/user-access/)
- [Security](/docs/security/)
- [Multi-language](/docs/multi-language-support/)
- [More topics](/docs/more/)
