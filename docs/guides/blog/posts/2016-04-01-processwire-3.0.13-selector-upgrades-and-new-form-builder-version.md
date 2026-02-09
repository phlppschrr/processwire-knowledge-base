# ProcessWire 3.0.13, selector upgrades, and new Form Builder version

Source: https://processwire.com/blog/posts/processwire-3.0.13-selector-upgrades-and-new-form-builder-version/

## Sections


## ProcessWire 3.0.13, selector upgrades, and new Form Builder version

1 April 2016 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-3.0.13-selector-upgrades-and-new-form-builder-version/#comments)


### ProcessWire 3.0.13

This week we've got major upgrades to ProcessWire's selector engine, a great new version of Form Builder, and a few other core updates as well!


## Core updates


### Enhancements to dropdown submit buttons

A few weeks ago we introduced dropdown menus that appear for submit buttons, like in the page editor. These let you choose what action you want to perform after the submit, like exiting the editor, adding a new page, etc. There were a few requests for more visual two-part buttons rather than dropdowns that appear after a delay. This is a more familiar UI convention to many, so we have gone ahead and added support for this.

These dropdown submit actions also now have a [couple of simple API methods](https://github.com/ryancramerdesign/ProcessWire/blob/devns/wire/modules/Inputfield/InputfieldSubmit/InputfieldSubmit.module#L148) where you can add actions to any InputfieldSubmit button… something that may come in useful for other modules.


### Option to collapse PageList tree

Clicking the root "Home" link in your PageList navigation now collapses all open branches in the tree. This has a good use case now that the PageList tree always remembers where you last left it. So if you've got a bunch of open PageList branches that you want to collapse quickly, just click the "Home" item at the top!

The biggest core update this week was to our selector engine, so we'll give that a section of its own…


## Selector engine array support

Most of you reading this are probably familiar with ProcessWire selectors. Such selectors are strings that you use to perform a query in ProcessWire, most often to get a page, find pages, filter them, etc. They are the basis of getting or finding things in ProcessWire, and they can be very convenient and easy to use. But they aren't necessarily ideal in every situation…


### When selector strings aren’t ideal

It comes down largely to cases where you are constructing a selector string from user input, or other situations where you may be building a selector string programatically.


### Building a selector string with user input (example)

Lets build an example that uses selector strings to find pages containing user-specified terms in the title or body fields of pages using the basic-page or product template, that also match one or more user-specified categories, with the results sorted newest to oldest.

```php
$results = $pages->find(
  "template=basic-page|product, " .
  "title|body%=" .
    $sanitizer->selectorValue($input->get('q')) . ", " .
  "categories=" .
    implode('|', $sanitizer->intArray($input->get('categories')) . ", " .
  "sort=-created"
);
```

While selector strings are most often incredibly handy, the above example is one of those cases where I wish I could just send an array to `$pages->find()` … or any other function that accepts a selector string. No doubt, it's still quite concise given what it is accomplishing, but it's still not ideal. Especially when it comes to dealing with user input, constructing a selector string can be more tedious than it needs to be, and need double checking to make sure values are sanitized before going into the string, that everything is comma separated and concatenated correctly, etc. How else might we approach this…


### New: selectors as associative arrays

For the reasons above, we've been looking to make ProcessWire support arrays as an alternative to selector strings for quite some time, and ProcessWire 3.0.13 adds this capability. To demonstrate, here's the same selector as above, but using an array instead of a string:

```php
$results = $pages->find([
  'template' => ['basic-page', 'product'],
  'title|body%=' => $sanitizer->text($input->get('q')),
  'categories' => $sanitizer->intArray($input->get('categories')),
  'sort' => '-created'
]);
```


### A few things to note about the above:


### New: selectors as regular arrays

You can also specify selectors using a regular/non-associative array format that opens up a few more options. We'll use the same exact selector as in the previous two examples, but using the regular/non-associative array format.

```php
$results = $pages->find([
  ['template', ['basic-page', 'product']],
  ['title|body', '%=', $input->get('q'), 'text'],
  ['categories', '=', $input->get('categories'), 'int'],
  ['sort', '-created']
]);
```

The array you specify here has each selector item specified as an array as well, each of those arrays can use any of the following formats:

- [field, value]
- [field, operator, value]
- [field, operator, value, sanitizer]
- [field, operator, value, whitelist]

Consider the above to each be PHP arrays. Here's an explanation of what each part indicates:

You can mix and match array formats (associative and non-associative). We've shown you two different array formats you can use above (associative and regular), and you can use both in the same selector if you'd like. Though to reduce confusion, it may be best to stick with one or the other for each selector that you use.


### Wrapping up selectors and arrays

Array selectors also support OR-groups and sub-selectors, which we'll cover in more detail soon in the Selectors documentation for ProcessWire 3.x.

While most of us will still be using string selectors most of the time, I think having the option of using selector arrays like this is a genuinely useful addition to ProcessWire, is helpful for security, and I hope that many will find find a place for it in their development workflow.


## New Form Builder version released

After months in development, we released new version of Form Builder this week (0.3.0), which is a major upgrade in terms of features. It is available for download now by registered users in the Form Builder support board. Here's what's new:


### New embed method D: Custom Embed + Custom Markup

This new embed method essentially exports a copy of the entire form markup to a PHP file that you can edit and modify as you see fit. Form Builder will use your modified version rather than one that it generates at runtime. Like embed method C, the form outputs directly in your page with the rest of your markup (embed methods C and D do not use iframes).


### When to use embed method D?

This new embed method is good for people that need 100% control over the form markup. The drawback is that future changes to the form (if needed) have to be manually reflected in the markup, since it's the developer controlling the markup rather than FormBuilder. But many forms rarely need changes after being launched, so this new embed method might be just the right solution for some.

Screenshot of the Embed tab with embed method D instructions open.


### New “Basic” Form Builder framework

Form Builder 0.2.5 introduced CSS framework support to the software, enabling Form Builder to output markup native to Bootstrap, Uikit, and Foundation CSS frameworks, as well as the ability to create your own frameworks. It also included the "Admin" framework as an option, which uses the ProcessWire admin framework to output the form.

Form Builder 0.3.0 introduces a new "Basic" framework, which is ideal for sites that aren't using a CSS framework, or are using something other than those mentioned. It outputs simpler markup than the other frameworks, and likewise presents a more minimal form output, and is easier for you to modify or add your own styles to it. All while still supporting all of the Form Builder and ProcessWire features for forms. It's ideal for pairing with the new embed method D as well. This new Basic framework is the new default framework used by Form Builder, and it's the one we'll likely be using the most from now on.

Screenshot of the Preview tab using the Basic framework


### Improvements to the field editor

You can now edit fields in Form Builder without leaving the form editor. Field editing now occurs in modal windows, rather than moving your browser from one screen to the next. This results in faster edits, since Form Builder doesn't have to re-load the main form editor every time a change is saved to a field.

We've also spiffed up the field editor quite a bit. It now separates the field editing into two tabs, "Basics" and "Details" (just like the PW field editor). This makes field editing a lot more organized and and simpler.

Screenshot of the field editor


### Other Form Builder improvements

FormBuilder 0.3.0 also includes months worth of bug fixes and optimizations. Furthermore, there has been a major code refactoring in several areas–pretty much every file has had updates, some major. For those working with Form Builder from the API side, almost everything has been updated with comprehensive phpdoc documentation. While Form Builder was originally coded in 2012, it's now up-to-date for 2016 and fully supports ProcessWire 2.7.x and 3.0.x!

Screenshot of the entry editor

If you are already a registered user of Form Builder with a current support plan, you can [download the latest version](/talk/topic/1844-form-builder-download-and-updates-030/) of Form Builder in the support board download thread (login required). As with any upgrade, please test existing forms thoroughly and note that we are considering this version beta for the next week or so. If you don't have Form Builder but would like to get it, please visit the [ProcessWire store](/store/).

That's all for this week. Hope you all have a great weekend and remember to read the latest [ProcessWire Weekly](http://weekly.pw) this weekend!
