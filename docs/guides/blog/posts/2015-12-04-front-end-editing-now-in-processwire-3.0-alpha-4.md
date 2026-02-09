# Front-end editing now in ProcessWire 3.0 alpha-4

Source: https://processwire.com/blog/posts/front-end-editing-now-in-processwire-3.0-alpha-4/

## Sections


## Front-end editing now in ProcessWire 3.0 alpha-4

4 December 2015 by Ryan Cramer [ 15 Comments](/blog/posts/front-end-editing-now-in-processwire-3.0-alpha-4/#comments)


## ProcessWire 3.0.1 (alpha-4)

Last week we talked about the [new front-end editing features](/blog/posts/three-new-processwire-versions-and-surprises/) coming in ProcessWire 3.0. This week we've got them now available for download and testing in version 3.0.1, aka alpha-4. We've also taken them quite a bit farther than what was introduced last week, and this post will be focused on covering all that you can do with it and how to use them.


### Now all fields can be front-end editable

In our post last week, we talked about how just text and rich text fields could be editable on the front end. But for those that really wanted to use front-end editing, I worried that might not be enough, and that we needed a more complete/overall ability to make any field editable on the front-end.

ProcessWire isn't a markup generator, and that's a great thing. It means you are in full control over the front-end of your site. But since ProcessWire doesn't control the front-end, there are very few assumptions that can be made from an editing perspective. Given that, making everything editable on the front-end means putting the user in a partial editing environment while still keeping them on the front-end. Taking much inspiration from Antti Peisa's [Fredi](http://modules.processwire.com/modules/fredi/), this is exactly what ProcessWire now does when you are editing some non-text field.

When you are editing a text-based field (like this one you are reading) the editor will be inline, directly in the page, like you saw last week. When editing some other type of field, whether it be an *Page Reference, Image, PageTable, Repeater,* or any complex type, ProcessWire opens a dialog on top of your front-end where you can make edits specific to that field. To make an edit to a field on the front-end, you just double-click it. You can identify editable regions because the mouse cursor changes to a context pointer rather than just a pointer. When you save, the window closes, and the page updates with the newly-edited content, with no reloading necessary.

So we now have a much more full front-end editing capability built into PW 3.0 (relative to last week) that can cover any field.


## Making fields front-end editable

ProcessWire provides a few different options for you here, which we'll cover in detail below. Regardless of which option you choose, front-end editing will only appear when the user has appropriate permissions to the page and field. Required permissions are *page-edit* and *page-edit-front*. When a field is editable, hovering it shows a context mouse pointer rather than a regular pointer. To edit the field on the front-end, you must double click it.


### Option A: Automatic editing

When the formatted value of the field is retrieved from a $page, it will be editable without you having to write any markup/code for it. This is a good option for fields like a "body" copy or "sidebar" field, that you might only output once on the page. The main benefit here is that you can make the field editable just by checking a box in the admin. It becomes editable wherever and however you are outputting it. It doesn't matter if it's coming from another page or not, as PW keeps track of it.

The drawback is that the field is editable wherever you output it (to a user with permission to edit), so it's not ideal for fields like "title" that might be great in an editable headline, but could be problematic if it also makes appearances in a `<title>` tag or in a breadcrumb trail. Though you can do this:

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


### Option B: API method call

As you probably know, you can pull the value of any field on a page with `$page->field_name;` or `$page->get('field_name');` – If you want to pull an editable version of that field, you can instead use `$page->edit('field_name');` for example:

```php
<?php echo $page->edit('body'); ?>
```

Note that $page can be any Page object, it doesn't necessarily have to be the current $page.

This API method call option is good for fields that need no manipulation before output. Meaning, it's good for text fields, number fields, dates, and so on. But not worthwhile for things like *Files/Images, PageTables, Repeaters* or any field that you iterate to output or access object properties from. For those you will want to use `<edit>` tags or edit attributes, per options C and D.


### Option C: HTML edit tags

HTML `<edit>` tags enable you to create editable regions in your markup. Make the `<edit>...</edit>` tags wrap any markup that you wish, and double clicking whatever is contained within it will open up an editor to that field. For example, here is how you might make an image field named "photo" editable:

```
<edit photo>
  <img src="<?=$page->image->url?>" />
</edit>
```

Or lets say you wanted to make a *Repeater, PageTable* or *Table* field editable:

```php
<edit events>
  <?php foreach($page->events as $event): ?>
    <div class="event">
      <h3><?=$event->title?></h3>
      <p class="date"><?=$event->date?></p>
      <p><?=$event->summary?></p>
    </div>
  <?php endforeach; ?>
</edit>
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


## How do you enable front-end editing?

All of the front-end editing features are provided by a module included with the ProcessWire 3.0 core called *PageFrontEdit*. Once this module is installed, you can use any of the above options. The module is not installed by default.

Any time you edit a field in the admin (Setup > Fields) you'll see a "Front-end editing" section on the "Input" tab (at the bottom). If you don't have *PageFrontEdit* installed, it gives you a button you can click to automatically install it. When the module is installed, the "Front-end editing" section in your field editor shows you all of the options mentioned above but within the context of the field you are editing. If the field does not support one of the options, it is disabled in the copy/paste examples it gives you.

By the way, the *PageFrontEdit* module has a configuration screen that lists all of the fields that you can enable for option A (automatic editing), with checkboxes for each to enable. These checkboxes are not applicable to options B through D mentioned above, just option A.


### Screenshot Examples


### Inline editor on a headline field:


### Inline editor on a body copy field:


### Dialog editor on an images field:


### Field settings options (in Setup > Fields > [field] > Input):

Hope that you all enjoy these new front-end editing features and please let us know how they work for you. This is all brand new code to PW, so I'm sure we will still have some issues to work out. As a result (like the rest of PW 3.0) use this for testing, not production, and please let us know of any issues you come across. Remember to visit the [ProcessWire Weekly](http://weekly.pw) this weekend!
