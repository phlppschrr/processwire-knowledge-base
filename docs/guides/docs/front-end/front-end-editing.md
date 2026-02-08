# Front-end editing in ProcessWire CMS (PageFrontEdit module)

Source: https://processwire.com/docs/front-end/front-end-editing/

# Front-end editing (PageFrontEdit module) 

Edit pages on the front-end of your site with the core PageFrontEdit module.
- [Requirements](#requirements)
- [Enabling front-end editing](#enabling-front-end-editing)
  - [Option A: Automatic editing](#option-a-automatic-editing)
  - [Option B: API method call](#option-b-api-method-call)
  - [Option C: HTML edit tags](#option-c-html-edit-tags)
  - [Option D: HTML edit attributes](#option-d-html-edit-attributes)

- [Configuring front-end editing](#configuring-front-end-editing)

---
[](#)

### Requirements

- Front-end editing is available in ProcessWire 3.0 and newer.
- The *PageFrontEdit* module must be installed. It is included with the core and can be found at: Admin > Modules > Core > Page > Front-end page editor.
- Non-superusers must have [page-edit](/api/user-access/permissions/#page-edit) and [page-front-edit](/api/user-access/permissions/#page-edit-front) permission in order to make front-end page edits.

---
[](#)

## Enabling front-end editing

ProcessWire provides a few different options for you here, which we'll cover in detail below. Regardless of which option you choose, front-end editing will only appear when the user has appropriate permissions to the page and field. Required permissions are *page-edit* and *page-edit-front*. When a field is editable, hovering it shows a context mouse pointer rather than a regular pointer. To edit the field on the front-end, you must double click it.[](#)

### Option A: Automatic editing

When the formatted value of the field is retrieved from a $page, it will be editable without you having to write any markup/code for it. This is a good option for fields like a "body" copy or "sidebar" field, that you might only output once on the page. The main benefit here is that you can make the field editable just by checking a box in the admin. It becomes editable wherever and however you are outputting it. It doesn't matter if it's coming from another page or not, as PW keeps track of it.

#### Avoid using option A for your "title" field and similar

The drawback is that the field is editable wherever you output it (to a user with permission to edit), so it's not ideal for fields like "title" that might be great in an editable headline, but could be problematic if it also makes appearances in navigation, a `<title>` tag or in a breadcrumb trail. Though you can do this:

```
// non editable title
$page->edit(false);
echo "<title>$page->title</title>";
...
// editable title
$page->edit(true);
echo "<h1>$page->title</h1>";
```

...but once you are having to do that, it kind of defeats the purpose of using option A, since you are now making API calls to support it. So you'd want to consider if one of the other options might suit your needs better in those situations.

---
[](#)

### Option B: API method call

As you probably know, you can pull the value of any field on a page with `$page->field_name;` or `$page->get('field_name');` – If you want to pull an editable version of that field, you can instead use `$page->edit('field_name');` for example:

```
<?php echo $page->edit('body'); ?>
```

Note that $page can be any Page object, it doesn't necessarily have to be the current $page.

This API method call option is good for fields that need no manipulation before output. Meaning, it's good for text fields, number fields, dates, and so on. But not worthwhile for things like *Files/Images, PageTables, Repeaters* or any field that you iterate to output or access object properties from. For those you will want to use `<edit>` tags or edit attributes, per options C and D.

---
[](#)

### Option C: HTML edit tags

HTML `<edit>` tags enable you to create editable regions in your markup. Make the `<edit>...</edit>` tags wrap any markup that you wish, and double clicking whatever is contained within it will open up an editor to that field. For example, here is how you might make an image field named "photo" editable:

```
<edit photo>
  <img src="
```

Or lets say you wanted to make a *Repeater, PageTable* or *Table* field editable:

```
<edit events>
```

The only difference from the above and what you may already be doing is just the addition of the surrounding `<edit>` tags. The point I'm trying to get across with the above is that it really doesn't matter what is in the editable region. Surrounding it with the `<edit>` tags means that double clicking it with open an editor to the "events" field. After saving your events field, the editor will close and that region on your page will be automatically updated with the new updated markup.

The `<edit>` tags themselves never appear in the actual output of your site. They are stripped out during page rendering. If the user has no access to edit, then the edit tags are ignored and stripped out.

By the way, you can also use some more verbose but alternate syntax for the `<edit>` tags if you prefer. If your editor does syntax highlighting with your HTML, it may be more consistent (the "quotes" are optional of course):

```
<edit field="events"> ... </edit>
```

If your editable region contains multiple fields you want to be edited together, you can specify more than one:

```
<edit field="intro,image,events"> ... </edit>
```

If your field happens to be on some other page other than the one being rendered, you can also specify what page you want to be edited:

```
<edit field="events" page="1001"> ... </edit>
```

The 1001 can be any page ID or path. The above can also be shortened to this if you prefer:

```
<edit field="1001.events"> ... </edit>
```

Or this:

```
<edit 1001.events> ... </edit>
```

If you are using `<edit>` tags with a field that supports inline editing (like a text or CKEditor field), the inline editor will be used. Otherwise it will open a dialog to the editor.

---
[](#)

### Option D: HTML edit attributes

These work about the same as `<edit>` tags except they are an attribute you can add to an existing tag in your markup, such as `<div>`, `<span>` or whatever you'd like.

```
<div edit="events">
  <!-- code to output events -->
</div>
```

Or to specify a field from some other page (1001):

```
<div edit="1001.events"> ... </div>
```

Or to specify multiple fields:

```
<div edit="intro,image,events"> ... </div>
```

The "edit" attributes are stripped from the markup that gets output, so the only place you will see them is where you place them in your template file(s).

Worth noting about option D is that it always uses the dialog editor and does not use the inline editor.

---
[](#)

## Configuring front-end editing

All of the front-end editing features are provided by a module included with the ProcessWire 3.0 core called *PageFrontEdit*. Once this module is installed, you can use any of the above options. The module is not installed by default.

Any time you edit a field in the admin (Setup > Fields) you'll see a "Front-end editing" section on the "Input" tab (at the bottom). If you don't have *PageFrontEdit* installed, it gives you a button you can click to automatically install it. When the module is installed, the "Front-end editing" section in your field editor shows you all of the options mentioned above but within the context of the field you are editing. If the field does not support one of the options, it is disabled in the copy/paste examples it gives you.

By the way, the *PageFrontEdit* module has a configuration screen that lists all of the fields that you can enable for option A (automatic editing), with checkboxes for each to enable. These checkboxes are not applicable to options B through D mentioned above, just option A.
