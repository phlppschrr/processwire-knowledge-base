# ProcessWire updates and new field types

Source: https://processwire.com/blog/posts/processwire-updates-and-new-field-types/

## Sections


## ProcessWire updates and new field types

30 June 2017 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-updates-and-new-field-types/#comments)

[Last week](/blog/posts/processwire-3.0.65-core-updates/) we released a new [multi-language URL fieldtype](https://modules.processwire.com/modules/fieldtype-urllanguage/) module, and there was also a request for a multi-language email module. That's now available in the [modules directory](http://modules.processwire.com), and GitHub repo, as [FieldtypeEmailLanguage](https://github.com/ryancramerdesign/FieldtypeEmailLanguage).

While there have been a few small posted updates to the core this week, most of the more major updates are still very much work-in-progress, and thus not yet pushed to GitHub. Given that, I'll wait till next week before bumping the version number up on the dev branch.


### How to implement file/image fields as multi-language

Last week there were requests for a multi-language file/image fieldtypes. Currently the file/image fieldtypes support multi-language descriptions for any file/image, but not a separate file or image per language. Such a feature would be useful if you are dealing with files in different languages (like PDFs), or with images that have text in them in different languages. So that kind of multi-language support is not currently available for file/image fields… or is it?

Actually they do support it in a way that's not immediately obvious or as straightforward as other multi-language types, but still quite useful and worthwhile when you need the capability. To give you a hint, this is one of the reasons why tags support was added to files/images. Below is how you can use tags to support separate files per language:

```
$image = $page->images->getTag($user->language->name); 
if($image) {
  echo "<img src='$image->url' alt=''>";
}
```

The above will output the image in the user’s correct language. Lets say that you think sometimes you'll have a multi-language image for a field, and sometimes you won't. So you want it to fall-back to the default language image if one for the user's language isn't available. Furthermore, if no image has the default language tag, then just pull the first image, whatever it may be:

```
$image = $page->images->getTag($user->language->name); 
if(!$image) $image = $page->images->getTag('default');
if(!$image) $image = $page->images->first();
if($image) {
  echo "<img src='$image->url' alt=''>";
}
```

That's how you can use the current files/images field to support multiple languages. It's pretty easy, and I've used this strategy consistently on multi-language sites–it works very well. Since there seems to be interest in it, we'll likely add some shortcuts to make all of this even simpler. For instance, we could support an option for predefined tags, where you select them rather than enter them. Or better yet, we could add a language select option to each file/image, independently of tags. Going further, we could do some nice things on the API side to make the formatted value of an images field be reduced to just the image (or images) specific to the language. I'll continue looking at this more in the weeks ahead. But since the topic came up last week, I did want to demonstrate how you can already support it pretty easily with the current file/image fields.


### New ProFields module: FieldtypeStaticFields

I'm getting close to wrapping up a new ProFields module here and wanted to tell you more about it. It's pretty different from the others, yet like the other ProFields modules, shares the common goal of reducing the number of fields necessary in your ProcessWire installations. This new Fieldtype actually has a lot in common with ProcessWire's language translation tools and API, and even has some crossover with it. It does not require that you have multi-language support installed however.

The Fieldtype originates as a result of a recent site I was developing where there were a lot of various text labels in various parts of the markup. The client needed the ability to be able to edit everything, so static text phrases in the template files were not an option. I didn't want to manage dozens of fields just for this purpose either. It seemed like a perfect job for ProcessWire's language translation functions (even on a single language site). I liked the convenience of being able to make something editable and translatable by wrapping it in a translation function like `__('text')` or `$this->_('text')`, but I needed them to be editable per-page. This new Fieldtype enables just that.

**Here's how it works.** When you create a new “static field” and add it to a template, any pages using that template may modify static text defined in the template file. You can define the text using the existing language functions with $this:

```php
html<a class='more' href='#'>
  <?php echo $this->_('Read More'); ?>
</a>
```

That “Read More” text above becomes editable with any page using that template. If we wanted to personalize that text a bit, we might edit the page and change it to “Read more about Monarch butterflys”, and that text would appear in the output, rather than the static “Read More” text we have in our template file.

If we didn't override the value on our page (via the page editor) then the existing “Read More” value would stay, or the language-translated version of it would be used (if multi-language support installed). In addition, if multi-language support is installed, then it becomes editable per-language as well (tabbed), directly in the page editor. This is a basic example, but I hope it gives you a sense of what's in store.

The nice thing about this Fieldtype is that it takes ALL of the static text marked up this way in your template file and makes it editable in the page editor. So if you are building out some kind of complex attraction map for a theme park with a hundred different labels that need to be editable, you can now do it all with just one static field. It takes care of generating all the inputs and storing the data. All you have to do is wrap the editable text in function calls like the example above. That's all that is necessary in order to make it editable like any other field on the page.

I used the `$this->_('text');` call above because it's something that's already familiar to many reading this (per multi-language support). But in addition to that, this module comes with its own function calls you can use, and perhaps are more likely to use:

```
__text('foo');
__textarea('bar');
__richtext('<p>foo bar baz</p>');
```

As you might guess, the `__text()` function is for single line text, the `__textarea()` is for multi-line text, and the `__richtext()` is for CKEditor. So you can use any of these in your markup, and get the right kind of input to edit that text in your page editor.

Back to our “Read More” text from before. Lets say we've got several spots where we are using that phrase, and we don't want to type out our default value “Read More” more than once. We can give it the name “more”, by using the second argument:

```
html<a class='more' href='#'>
  <?= __text('Read More', 'more') ?>
</a>
```

Now, anywhere else that we want to use that “Read More” label again, we can, just by referring to the name we gave it:

```
echo "<a href='#'>" . __text('more') . "</a>";
```

This is just a brief introduction to this new Fieldtype, but I hope it's enough to point out where it might come in useful. There's actually more to it, but I'll save that for another post when the module is ready to release.


### Nominate ProcessWire at CMS Critic

If you get a chance, please nominate ProcessWire for CMS Critic’s annual CMS awards via their [nomination form](https://www.cmscritic.com/awards/2017-web-nominations/). We think ProcessWire probably fits best in one of the 3 categories below, but you decide what category you think is best (it only lets you choose one per nomination). Thanks for your support!

- Best open source CMS
- Best free CMS
- Best small business CMS

Thanks for reading and I hope that you all have a great weekend. Check in at the [ProcessWire Weekly](http://weekly.pw) this weekend as well.
