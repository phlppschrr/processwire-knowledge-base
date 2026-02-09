# ProcessWire 2.6.12 core updates, updates to several Pro modules and more

Source: https://processwire.com/blog/posts/processwire-2.6.12-core-updates-updates-to-several-pro-modules-and-more/

## Sections


## ProcessWire 2.6.12 core updates, updates to several Pro modules and more

7 August 2015 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-2.6.12-core-updates-updates-to-several-pro-modules-and-more/#comments)


## ProcessWire 2.6.12

Welcome back and thanks for reading! This week we've got a lot of core updates and Pro module updates for you:


### Continued improvements to AJAX editing in ProcessWire

I've spent much of this week using the new [AJAX editing feature](/blog/posts/new-ajax-driven-inputs-conditional-hooks-template-family-settings-and-more/) that we introduced to you last week. I've been testing this new feature out in every scenario and with every Fieldtype/Inputfield possible, making numerous improvements and resolving issues as they come up. You can even have AJAX-loaded fields within AJAX-loaded fields now (like an AJAX-loaded fieldset or tab that itself has additional AJAX-loaded fields within it).

In addition, all of the [ProFields](/api/modules/profields/) Fieldtype/Inputfield modules have been updated with full support of AJAX editing: [Table](/api/modules/profields/table/), [Multiplier](/api/modules/profields/multiplier/) and [Textareas](/api/modules/profields/textareas/). This is along with some other updates to to the ProFields, described further down in this post.

These AJAX-editing features came to the core in part by the work we did with the [ListerPro](/api/modules/lister-pro/) module in past weeks, and the editing features built into it. There is a lot of crossover between what's been added in the core and what was built into ListerPro. ListerPro lets you edit multiple pages at the same time in a table format. Imagine editing all your site pages at once in a spreadsheet, and you've got an idea of what we've been trying to get at with ListerPro. Since all of ProcessWire's core Fieldtypes/Inputfields now support AJAX-editing (and now the ProFields do too) there are major benefits to be found both in the core, and in ListerPro. We've found these features really useful over here, and hope that you do too.


### New Pages > Add New menu and landing page

A few major core versions back we added the "Add New" button that you see in the top right corner of ProcessWire's main Page List screen. Assuming you've configured some parent/child relationships between templates (in template Family settings), this lets you create new pages of a specific type, without having to drill-down in the Page List. It can be a real time saver, and I've come to rely on it quite a bit, especially on larger sites.

There's been only one problem with this feature though, and that's that you can't get to it unless you are on the main Page List screen. So if you are editing a page, and then want to go immediately to add another page, you first have to go back to the main Pages screen. Not anymore...

This week we added an "Add New" link in the top navigation of the ProcessWire admin. When you hover the "Pages" navigation item at the top, you'll now get an "Add New" option (in addition to the existing "Tree", "Find" and "Recent" options). Hover that "Add New" and you'll get a list of page types that you can add–click one to add immediately. Alternatively, you can click the "Add New" label, and it'll take you to another screen asking you what you want to add, and where (if there are multiple locations possible).

I've already found this to be a big time saver this week and hope that you find it useful too. Note however that if you don't have any predefined parent/child relationships with your templates (by way of the "Family" settings) you won't see this "Add New" option. If you do have parent/child relationships defined, then you should start seeing it immediately after upgrading to PW 2.6.12.


### Additional core tweaks

In addition to the above, there were also several tweaks and optimizations to the core this week.

**Improved cache busting with CSS and JS files used by modules.** Module asset links now use file modification times (determined at runtime) rather than just module version numbers. This helps to ensure you aren't ever getting non-current CSS/JS files in the admin.

**Improvements to the appearance of non-editable file and image fields (among others). **As you may know, it's possible to have fields in the page editor that aren't editable, whether due to field-level access control or a "locked" visibility mode in the field settings. We're working to make sure these fields still remain as useful as possible. For instance, file and image fields now look exactly like their editable counterparts (including lightbox and grid support), but of course without edit and upload controls.

**Optimizations to PW's module information caches.** We've shuffled around a few things in the modules information cache to make it use less memory and bypass loading of the more memory-intensive verbose cache, unless it is needed for something specific (like module installation). That's not particularly interesting is it? There were more core updates, but like this optimization, they are things you won't ever see, so I think I'll stop there. :)


## Updates to several Pro modules


### New ListerPro version 1.0.6

- Continued tweaks and improvements to inline page editing editing mode (AJAX).
- Some tweaks and optimizations to the ListerPro Config tab.
- Requires the latest PW dev version or newer (2.6.12+). Available for download now in the ListerPro support board.
- [More about ListerPro](/api/modules/lister-pro/)


### New ProFields Table Fieldtype/Inputfield version 9

- Adds support for autocomplete (single and multiple) Page reference fields. This is great for dealing with quantities of selectable pages that are larger than what you could make selectable with other types. Whether you are dealing with a few hundred selectable pages, or a million, this is the way to go.
- Adds support for AJAX editing of table fields (2.6.12+).
- Improved support for granular selection of Table properties for filtering in Lister/ListerPro.
- ProcessWire 2.6.12+ is recommended, though this version may also work with past PW versions. Though the autocomplete feature does require PW 2.6.12+. Available for download now in the ProFields support board.
- [More about Table](/api/modules/profields/table/)


### New ProFields Textareas Fieldtype/Inputfield version 6

- Adds support for searching individual properties from selectors.
- Adds support for ajax editing mode (PW 2.6.12+).
- Adds support for individual "notes" fields for each property.
- Adds support for display of individual properties from Lister/ListerPro.
- Adds support for filtering of individual properties from Lister/ListerPro.
- Adds support for markupValue (as used in Lister/ListerPro output).
- [More about Textareas](/api/modules/profields/textareas/)

As you may know, Textareas bundles all fields within it into one value stored in the database, so previously it wasn't possible to query those individual properties from selectors and $pages->find(), etc. This was mentioned as one of the drawbacks of using a Textareas field. That drawback no longer exists. You can now query properties in the Textareas field separately from one another, whether from a $pages->find() query (or anywhere you might use a database-driven selector), or interactively from ListerPro. This is a major improvement to Textareas and greatly expands the scenarios where you might consider using it. This version of Textareas is available for download now in the ProFields support board.


### New ProFields Multiplier Fieldtype/Inputfield version 9

- Adds support for AJAX-editing, whether using an AJAX visibility mode (PW 2.6.12+) or editing with ListerPro.
- Improvements to non-editing output (like when previewing in Lister/ListerPro and viewing non-editable fields in the page editor).
- ProcessWire 2.6.12+ is recommended. Available for download now in the ProFields support board.
- [More about Multiplier](/api/modules/profields/multiplier/)


### Have a great weekend + ProcessWire Weekly

Hope that you all have a great weekend and week ahead, and hope to see you at [ProcessWire Weekly](http://weekly.pw) on Saturday morning. Thanks so much for reading–we really appreciate your interest in ProcessWire!

We also recommend that you keep in touch by [subscribing to the ProcessWire weekly](/contact/subscribe/) and we will send the updates to you once per week.
