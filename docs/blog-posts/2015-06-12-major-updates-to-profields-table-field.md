# Major updates to ProFields Table field

Source: https://processwire.com/blog/posts/major-updates-to-profields-table-field/

## Sections


## Major updates to ProFields Table field

12 June 2015 by Ryan Cramer [ 3 Comments](/blog/posts/major-updates-to-profields-table-field/#comments)

This week the core additions/changes were mostly geared at supporting updates we've made to the ProFields Table field. In fact, today we released a major update to ProFields Table, and that's what we'll be covering in this post.

[ProFields](https://processwire.com/talk/store/product/10-profields/) was released in stable fashion just about 1-year ago, and we wanted to get some really special upgrades in place for the [ProFields Table](https://processwire.com/api/modules/profields/table/) field, which many see as the flagship of the ProFields modules.

The latest beta version of ProFields Table was posted today in the ProFields download thread, and can be downloaded now by registered users. Though keep in mind this is still beta, so use it for testing or development, and maybe wait a bit before using it in production. This new version requires ProcessWire 2.6.0 or newer (or this week's 2.6.4 if you want to use CKEditor fields in it). Here's what's been added:


### New support for single and multi Page-reference fields

Previously, Table supported built-in single and multi-select fields, but didn't support Page reference fields. Now it does, and they can be queried from the API just like any other Page fields.

Supported input types for single page selection include radio buttons and select boxes. Supported input types for multi-page selection include checkboxes, select multiple and asmSelect (which provides a sortable select multiple). We also plan to support autocomplete in the near future, but that's not ready quite yet.

When it comes to configuring your page reference fields, you get a nicer interface than you do with regular PW Page fields. InputfieldSelector is used to handle the configuration of selectable pages, which provides a nice interactive interface and preview. If you've used Lister or ListerPro, then you are already familiar with InputfieldSelector.

For the labels of your selectable pages, you can specify just a field name, like `title`, you can specify a field name stack, like `title|name`, which uses "title" if populated, or "name" if not. Or you can specify your own format, like `{id}: {title|name}, {path}` which would display the page ID, title or name, and path. We'll no doubt be bringing some of these new configuration options and improvements to the regular PW page field in upcoming core updates.

From the API side, the new Page reference fields in Table work just like their regular PW counterparts. Single page fields have a value that is a Page object, or a NullPage object if not yet set (i.e. `$page->table_field->page_field->id == 0`). Multi-page reference fields are always a PageArray.


### New support for unlimited table columns

Previously in Table fields, you could support as many columns as you wanted, but couldn't practically use more than 5-6 or so, because you were limited to what you could see and edit in a single table row. So you were pretty limited when it came to more complex data types. Though even with with only a few columns, you might have been really limited on how much space you had for input.

In the latest version of Table we added support for supporting more columns that you could visually fit in a table. Here's how it works: when your combined width of fields exceeds 100%, it creates another row within your main row. At this point, your table row and columns become more like a fieldset than a table, so the output in the page editor likewise changes layout by getting rid of the column headers and instead placing the column labels above each input.

Meanwhile, your row remains in tact as a sortable element in your table. But think of them more like sortable fieldsets at this stage. This enables you to support far more diverse and complex data types than you could before with Table. You can create as many groups of columns that add up to 100% width as you'd like, within a single row.


### New support for rich text (CKEditor) fields

One of the top requests for Table over the last year has been support for rich text fields. This week we added it! Since CKEditor fields have potentially a lot of settings to configure, you simply specify what regular PW field you want your CKEditor field to pull settings from. Though you can also manually override any of them within your column settings as you see fit.

Use of CKEditor fields requires ProcessWire 2.6.4 or newer (this week's latest core dev branch), since we had to modify our core InputfieldCKEditor slightly to support dynamic insertion of CKEditor fields into the document.


### New support for multi-language text fields

Previously, Table had no multi-language support built in, and it never seemed particularly feasible, so hadn't been on the roadmap. After all, tables are like spreadsheets, and who's ever heard of a multi-language spreadsheet? But it's something that people have asked for, and our goal is to provide the best multi-language support with everything we do. It also makes a lot of sense to have support for it in Table. So now we've got great multi-language support in Table!

The built-in multi-language fields in Table include: Text, Textarea, and CKEditor. The way they work is just like other multi-language fields in PW, in that you get tabs above the field for each of your languages.

You'll need to have the core *LanguageSupport* module installed before you'll see the options available. We also recommend you have the core *LanguageSupportFields* and *LanguageTabs* modules installed, as these usually get installed as a group.

From the API side, multi-language text fields work exactly the same as they do outside of Table. Accessing the value of a multi-language text field outputs the value in the current user's language. It's as simple as that. The multi-language fields in Table also support the standardized `getLanguageValue($language);` and `setLanguageValue($language, $value);` methods you might have seen with other multi-language fields in ProcessWire. For instance, if we wanted to set the multi-language value of a "desc" field in our first row of a "beers" table:

```
$beer = $page->beers->first();
$beer->desc->setLanguageValue('default', 'Good Beer');
$beer->desc->setLanguageValue('spanish', 'Bueno Cerveza');
$page->save('beers');
```


### Even more additions to the Table field…

- New support for multi-language table column labels.
- New help text for most column settings properties.
- New support for select-multiple options field (as alternative to checkboxes).
- Expanded support for selection of Table properties in Lister/ListerPro.
