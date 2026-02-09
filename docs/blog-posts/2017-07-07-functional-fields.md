# Functional Fields

Source: https://processwire.com/blog/posts/functional-fields/

## Sections


## Functional Fields

7 July 2017 by Ryan Cramer [ 7 Comments](/blog/posts/functional-fields/#comments)

The “Functional Fields” module lets you make text translatable in your template files, much in the same way that you do with multi-language support in ProcessWire.

Updated 7 June 2024

When editing your site template files, you simply wrap the text you want to output in a function call. Hence the name “Functional”. By doing this, you make that *apparently* static text become *dynamic* text, editable in ProcessWire. Functional fields are ideal for text fields that you provide a default value for (in your template file) that the user can then change if they want to.

When used in a multi-language environment, Functional fields can be edited in any of your languages, just like regular multi-language text fields in ProcessWire. The module takes care of making sure the right language is shown on the front-end.


### A convenient time saver

Functional fields are an entirely different way to define fields in ProcessWire, and they are really quite a convenient time saver for many cases. It's perfect for all of those text phrases and blocks you might be using in your template files that don't quite fit a traditional field. Things like postal addresses, copyright lines, phone numbers, action links like “Read More”, button text, disclaimers, table headings, alt tags for static images, and literally anything that you might use text for in your template files. You could just as easily use it for more traditional things like headlines, bodycopy or sidebar text, but we think it's better to stick to traditional ProcessWire fields for those kinds of things.

You can define as many fields of text as you like in your template files, and they will become editable from a single Functional field in ProcessWire. All that's required is that you have one Functional field added to your page template, and then any text declarations in your template file become editable, just like any other field in ProcessWire.


### Functional functions

Functional fields come in 3 flavors: text (single line), textarea (multi-line), and rich text (HTML via TinyMCE or CKEditor). These are defined in your template files via these three functions shown below, though we suspect the first will be the most commonly used one:

```
__text('your text'); 
__textarea('your text');
__richtext('<p>your text</p>');
```

**Why the two leading underscores on these function calls?** Because standard “gettext” language translation functions start with an underscore, and it's consistent with ProcessWire's primary multi-language translation function: `__('text')`. (WordPress also uses the same notation). However, the main reason is that we think it's helpful for all text translation functions to be prefixed in a similar manner, making them easy to identify in markup/code.


### Two ways of configuring Functional fields

Functional fields can be configured to focus in on whatever template file is used by the current page, but they can also focus in on specific files that you choose. When focused on specific file(s) of your choice, you would just add the Functional field to one template, and make it editable on just one page. An example of that might be text you've made editable in a _main.php file … bits of copy like a site tagline, footer text and links, copyright, disclaimer and so on.

On the other hand, when a Functional field is configured to use a page's template file, it can appear on as many pages as you'd like, and the values can be changed for every instance of the page. This makes it very flexible.


### Using Functional fields

Functional fields are defined via function calls that resemble ProcessWire's multi-language translation functions, but are focused on different types of text. This includes single-line text, multi-line textarea, and multi-line rich text. These are defined via the three functions mentioned earlier, in your template file(s). All of these functions return the edited/translated value defined with the page. Or if the value has not been changed, they return the original/default value defined in the function call.

Lets start with something simple, like the text for a button, somewhere on our homepage. Here's how we might have done it in the past, somewhere in our /site/templates/home.php file:

```
<button type='submit'>
  Subscribe Now
</button>
```

That's just a simple button with static text in it. Now lets say we've created a new Functional field called “**mytext**” ($page->mytext) and added it to the homepage template. Lets edit that homepage template and then wrap that button text from above in a `__text()` function call, which makes it editable in the page editor:

```
<button>
  <?= __text('Subscribe Now') ?>
</button>
```

What we've got above is a `__text()` function surrounded by PHP tags, in this case we use the `<?=` PHP open tag, which outputs the value returned from the function. It's the same as doing a `<?php echo __text('…'); ?>`, but I always prefer the shorter syntax when possible, and it's universally present all recent PHP versions.

Now when I edit my homepage in the ProcessWire admin, I have a new editable field with the text “Subscribe Now” in it. I can change that text, and my changes are shown in the button whenever the page is viewed.


### Naming text

We can optionally specify a second argument to the `__text()` function, which defines a name for that text. By giving it a name, the text can be referred to again elsewhere if we need it. When you name text like this, it also means you can change the default text without discarding a page-edited version of it (which could be a benefit or a drawback, depending on your need). In this case, we'll give our “Subscribe Now” text phrase the name “subscribe”:

```
<button>
  <?= __text('Subscribe Now', 'subscribe') ?>
</button>
```

Now we can re-use that text somewhere else, whether it remains as the original “Subscribe Now” or if it is edited to be something else, like “Join for free”, or something like that. Here's another place where I want to use the text, because I'm linking to the subscribe form, so I just refer to the name of it that I defined earlier:

```
<a href='#subform'>
  <?= __text('subscribe') ?>
</a>
```

Another way I could do the same thing is by referring to the field name I defined earlier (“mytext”), and access its subfield called “subscribe”. This might look familiar to many ProcessWire users:

```
<a href='#subform'>
  <?= $page->mytext->subscribe ?>
</a>
```

What’s kind of nice about the above syntax is that it may be already familiar to you, as it looks a lot like using a page reference field. In fact, I can use it exactly like a page reference field, from anywhere else in my site…


### Using text defined on one page from another

Continuing from above, since I know I have this “mytext” field on my homepage, lets say that I wanted to pull in that subscribe text on my “Contact Us” page, which uses a different template. I could do it like this:

```php
<button> <?= $pages->get('/')->mytext->subscribe ?> </button>
```

What I'm doing above is getting the homepage (via its path “/”), accessing the “mytext” field, and getting the “subscribe” property. This would return value “Subscribe Now”, or some other text, like “Join Today”, if I had modified it when editing the homepage.


### Labels and more

The above examples define a “subscribe” property in our “mytext” field. But when we edit it in the page editor, the Inputfield has no label. We just see the original text, “Subscribe Now” in an input, which we can modify as needed. Lets say that we wanted to have a label in the page editor to better describe what the text is for. We can do that with a 3rd argument to our `__text()` function call:

```
__text('Subscribe Now', 'subscribe', 'Submit button');
```

Now when we edit our page, we see “Submit button” as the field label. We can actually specify *any* Inputfield property in this function call if we want to, by using a traditional ProcessWire selector string:

```
__text('Subscribe Now', 'subscribe', 'label=Submit button, notes=Test');
```

This line is also equivalent, but moves the selector string to the 2nd argument, should you prefer it:

```
__text('Subscribe Now', 'name=subscribe, label=Submit button, notes=Test');
```

I mentioned above you an specify *any* Inputfield property, so the above are just examples. Properties you might find useful might include label, description, notes, columnWidth, collapsed, required, and others. Though I'm guessing most of the time, people will stick with simply defining just “text”, “text and name”, or “text, name and label”. That's why our `__text()` functions operate on those 3 arguments by default, with the name and label being optional. If you want to get deep into Inputfield customization, you can do a lot here, but chances are you'll be better off using a regular ProcessWire field when that is your need.


### Other functions

We've talked exclusively about the `__text()` function above, because it is probably the most common one used with this Fieldtype. However, you can also use these two other functions as well, which work exactly the same, and use the same exact arguments as the text function:

`__textarea('multi-line text')` Works just like the __text() function, except that it displays a multi-line textarea field in the page editor, rather than single-line text field.

`__richtext('<p>HTML multi-line text</p>')` This is similar to the __textarea() function except that it shows a CKEditor field in the page editor, enabling you to make a block of HTML in your template file editable.


### Multi-language

On multi-language installations of ProcessWire, all defined Functional fields become multi-language. Meaning, when you see them in the page editor, you have a tab for each language, and can edit the text independently for each language. In typical usage, it's pretty much identical to other multi-language text fields in ProcessWire.

From the front-end, accessing text from your Functional field is in the user's language, whether accessing it from a function call like `__text()` or directly as a property like `$page->field->property`. If a value isn't defined for a given language, it falls back to whatever value is specified in the template file where the field is defined. To say it another way, it does not fall-back to the default language translation, it falls back to whatever the original text is in the functional call.


### Using fieldsets

If you've defined a lot of `__text('phrases')` for a Functional field in your template file, you may find groups of fields in your page editor would benefit from some arrangement via fieldsets. These can be grouped and ordered into fieldsets in your page editor by using `__fieldset()` function calls in your template file. It works like this:

```
__fieldset('foo,bar,baz', 'myName', 'My Label');
```

What the above call tells ProcessWire is that you want the fields named “foo”, “bar” and “baz” to be grouped in a fieldset, in that order. The fieldset is named “myName” and has the label “My Label”. The name and label arguments are optional, but recommended. Like with the other Functional fields, you can replace those 2nd or 3rd arguments with a selector string to specify other Inputfield options, should you need to.


### Other considerations

**How they are stored and when to use them** Functional fields are stored in the database just like any other fields in ProcessWire. However, they are only stored if a value differs from the one defined in the PHP/template file where it was defined. This is a matter of efficiency, but also one of practicality. For instance, if you change your original “Click for more” phrase in your template file to instead be just “More”, then chances are you don't want to continue seeing “Click for more” anymore. For this reason, Functional fields only store values that differ from the original definition. Given that, Functional fields are not likely what you want to use as fields for a site search engine. Stick to regular text fields when that is your need.

**Namespace** The functions provided by Functional fields are in the ProcessWire namespace. As a result, we recommend having a `<?php namespace ProcessWire; ?>` at the top of PHP files where you are using Functional fields. OR, if not using the ProcessWire namespace, the template compiler will take care of it for you (so long as you haven't disabled it).

**Restoring original value** When editing a page, if you want to force a field in a Functional field to return to its original default value, simply make it blank. This will remove the edited version, returning to the original static value in the template file.

**Blank text** Functional fields are not designed to store blank text, in the same way that ProcessWire language translation functions not designed to produce blank text. However, if for some reason you have a field where you need to override the value defined in the template with a literal blank, you can enter just a period “.” as the value in the page editor, and it will force a blank.

**Variables in text** Functional field text defined in calls like `__text('phrase')` cannot contain PHP variables in the “phrase” portion (or any of the arguments), for the same reasons that you cannot in multi-language translation functions. However, you can use placeholders that are replaced with variables. See the [Placeholders](/docs/multi-language-support/code-i18n/#placeholders) section of the ProcessWire multi-language [code internationalization](/docs/multi-language-support/code-i18n/) documentation for details on how to do this.

**Requirements** The Functional fields module requires some features that are only available in ProcessWire 3.0.66 or newer, so that is the only significant requirement to mention at present.

**Multi-language translation functions** In last week's post I used ProcessWire's multi-language function calls like `$this->_('text')` to introduce these fields. Previously, the `$this->_()` function could be used as an alternative to `__text()`. However, I decided to remove that integration with multi-language functions, so as to reduce confusion and number of levels of translation and places where one could override values. I may add it back in later as an option, but for now I think it's better for it to be clear when we are wanting to use a Functional field, and when we are wanting to use a multi-language translation function. Granted they do have a lot of crossover, especially with regard to multi-language, but they are also very different animals.


### Download Functional Fields

This module is now available for download in the modules directory here: [Functional Fields](/modules/fieldtype-functional/)
