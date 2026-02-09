# Output formatting in ProcessWire

Source: https://processwire.com/blog/posts/output-formatting/

## Sections


## All about output formatting in ProcessWire

28 July 2023 by Ryan Cramer [ 1 Comment](/blog/posts/output-formatting/#comments)

Pages have fields, fields have values, and those values can be either formatted or unformatted in ProcessWire. This post tells you everything you need to know about output formatting and how to use it to your benefit.

In a recent GitHub issue report, I was asked about output formatting in ProcessWire, and where more information could be found about it. I know I've written about it numerous times, and went to locate the documentation page, only to find we didn't have one! Output formatting is such an important topic, so here is everything you need to know. I hope you'll find it simple enough, but also useful and thorough.

Output formatting is one of those things that you don't necessarily need to think about in basic ProcessWire use and development. But as your needs and skills grow, it becomes more important to understand what it does and how to use it. There are also some important security factors to be aware of, whether you manipulate pages from the API or not, and we've covered them here too. Please feel free to comment and reply with any questions at the bottom of this post.


### What is output formatting?

When getting a field value from a page in ProcessWire, output formatting determines whether you receive a formatted or unformatted value. A formatted value is one that's prepared for use in output, while an unformatted value is one more appropriate for editing.

To add more detail, pages in ProcessWire are typically used for either output purposes or for editing purposes. When output formatting for a page is enabled (as it is by default in a ProcessWire powered website), field values retrieved from the page are assumed to be for output purposes, especially HTML. When output formatting is disabled, values retrieved from the page are assumed to be for editing and saving (or in some cases, for non-HTML output).

When developing a website in ProcessWire, every page you access from your template files will have output formatting enabled already. So you may not need to even consider output formatting until you need to modify the page from the API.** **But before we look at that further, let's take a closer look at how output formatting works.

If a page were a car with an automatic transmission, the page with output formatting ON would be a car in DRIVE, as the car is in a state to produce output: to spin the wheels and go. While a page with output formatting OFF would be a car in PARK, a state where it can be worked on.


### Why do we need output formatting?

When using ProcessWire to develop a website, the current `$page` variable (and any pages you load from [$pages](../api-full/wire/core/Pages/index.md)) will have output formatting enabled automatically. That’s because most of the time, you’ll be using a `$page` for output purposes, such as in this example below, where we output the `$page->title` in an `<h1>` tag:

```
<h1><?=$page->title?></h1>
```

The original purpose of output formatting was to make sure that we were outputting text that is valid and safe for HTML output. So if that `$page->title` example above outputs the text `This & That`, output formatting would ensure that it actually outputs `This & That` in the HTML source. That’s because HTML requires that some characters (like ampersands) are entity-encoded.

**What if ProcessWire didn't have output formatting?** In order to output text that is valid for HTML, you would have to entity encode it yourself using PHP’s [htmlentities()](https://www.php.net/manual/en/function.htmlentities.php), [htmlspecialchars()](https://www.php.net/manual/en/function.htmlspecialchars.php) or ProcessWire’s [$sanitizer->entities()](../api-full/wire/core/Sanitizer/method-entities.md) functions. Meaning every single time you output any text field value, you'd have to do something like this:

```
<h1><?=htmlspecialchars($page->title)?></h1>
```

That would be a pain, and easy to forget. And if someone did forget, they'd have at best, invalid HTML; and at worst, an open door for [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting), a security issue.

Output formatting exists to save us time, make our job simpler, make our HTML valid, and add security.


### When is output formatting disabled?

Output formatting is disabled (OFF) when booting ProcessWire manually, such as from another application or PHP file. That’s because in that context, ProcessWire is not handling a web request, and is instead acting as an API client.

ProcessWire doesn’t know what you’ll be using pages for in this instance, so there’s no reason for it to enable output formatting by default here. Even if using pages for output, maybe that output is for a JSON feed or something else where you wouldn’t want formatting like entity encoded text.

Another instance where output formatting is disabled is in ProcessWire's admin. Pages retrieved from the [$pages](../api-full/wire/core/Pages/index.md) API variable in the admin have output formatting disabled by default, since the admin is an environment intended for modifying pages.

Output formatting is also disabled if you manually disable it yourself, using methods outlined further in this post.


### Why must output formatting be OFF when modifying a page?

Take our earlier example where the formatted value of `$page->title` was `This & That`. If we modify the existing value, and then save it (with output formatting ON), we will have corrupted that value:

```
$page->title = "About $page->title";
$page->save('title');
echo $page->title; /* Output: About This &amp;amp; That */
```

We might think that we are saving the value `About This & That`, but in fact we are saving the value `About This & That`, with the entity-encoded ampersand. Since ampersands (and quotes and greater/less than signs) get entity encoded at output time, we will end up with the output `About This &amp; That` which the browser will then render literally as `About This & That` with a visible `&`. Not good!

If we turn off output formatting first, we can modify our value without corrupting it:

```
$page->of(false); /* turn off output formatting */
$page->title = "About $page->title";
$page->save('title');
echo $page->title; /* Output: About This & That */
```

We probably should have left that last echo line out! Because if we are going to also use the `$page` for additional output after the code above, we'd want to turn output formatting back on again:

```
$page->of(true); 
echo $page->title; /* Output: About This &amp; That */
```

This example with entity encoding in a text field is just the simplest case. As you'll read later, other Fieldtypes can return entirely different value types depending on the output formatting state of the `$page` they are accessed from.


## Output formatting by field type

While entity-encoding text for use in HTML output is the most basic reason for output formatting, it’s actually up to each field type (Fieldtype module) to decide what it considers a “formatted” value and what is considers an “unformatted” value. For some field types, there may be no difference at all. While other field types might return entirely different types of values depending on the output formatting state.

Each Fieldtype module contains a [formatValue()](../api-full/wire/core/Fieldtype/method-___formatvalue.md) method that handles creating the formatted value. When a page's output formatting is enabled (ON), that value is automatically routed through the Fieldtype's `formatValue()` method whenever you access `$page->field_name`. When output formatting is disabled (OFF), then that `formatValue()` method is skipped. This [Fieldtype::formatValue()](../api-full/wire/core/Fieldtype/method-___formatvalue.md) method is also a hookable method, enabling you to extend it to apply whatever additional formatting you'd like. (See the example at the bottom of this post).


### Text fields

In the case of FieldtypeText (the standard single-line text field type) the `formatValue()` method applies any "Textformatter" modules that were selected in the field configuration. Most commonly, the "Entity encoder" Textformatter is selected for text fields. But there might be others too, such as one that formats the text as Markdown, or another that manipulates the text in some other way.


### Textarea fields

FieldtypeTextarea is another field type that lets you select which Textformatter modules you want to apply when output formatting is enabled (ON). If working with a rich text (TinyMCE/CKEditor) textarea field, we don't want the "entity encoder" selected because TinyMCE/CKEditor store HTML with ampersands, quotes and greater/less than signs that are already entity encoded. Entity encoding HTML would make the browser show literal HTML tags to the user. So we don't need entity-encoding here, but we might instead want our formatted value to route through [TextformatterHannaCode](/modules/process-hanna-code/) to insert custom markup at runtime, or [TextformatterVideoEmbed](/modules/textformatter-video-embed/) to automatically convert YouTube URLs to embedded videos in our output. See more [Textformatter modules](/modules/category/textformatter/).


### File and image fields

File and image fields (FieldtypeFile and FieldtypeImage) use output formatting in a couple of different ways. Consider that file and image fields can hold any number of files or images. When configuring a file/image field, you can dictate that it should behave as a single file/image when output formatting is on, rather than behaving as an array of them. If using a file/image field to store just one single file/image, such as an employee profile photo, then it's very convenient to refer to `$page->image->url` rather than `$page->image->first()->url`. Output formatting makes this more output-friendly syntax possible.

Output formatting also enables you to automatically apply [Textformatter modules](/modules/category/textformatter/) to a file/image description text. Like with regular text fields, these are selectable in the field's configuration, and like with any text field, you should typically have at least the "entity encoder" selected.


### Date/time fields

Date/time fields (FieldtypeDatetime) enable us to use a date/time output format that applies only when output formatting is enabled (ON). For instance, when we output `$page->date` we might want it to render as `28 July 2023` rather than an unformatted unix timestamp (integer). The output format is controlled by the date/time field configuration.


### Page reference fields

In the case of Page reference fields (FieldtypePage) output formatting automatically removes any unpublished pages from the value before returning it to you, ensuring you don't output values for (or links to) unpublished pages in your output. If output formatting is disabled (OFF), it is likely you want any unpublished pages to remain in the value, ensuring they don't permanently disappear from the value when the page is saved. After all, an unpublished page today might become a published one tomorrow.

Note that allowing unpublished pages in a Page field is an option configurable within the Page field settings.


### Toggle fields

The Toggle field (FieldtypeToggle) is an interesting case in that stores no values other than integer 0, 1 and 2, which represent: No, Yes and Other. But output formatting enables you to translate those to be formatted values of strings like "Disabled", "Enabled", and "Neither", or some other words that apply to your intended meaning of the field.

*The point is that output formatting has a lot of uses, depending on the field type. But all are geared towards assisting you with obtaining an output-ready (formatted) field value, and making it as easy to use as possible.*


## How to work with output formatting

Unless you have manually turned it off, output formatting is always enabled (ON) in your site template files.

You can get or set the output formatting state for an entire $page by using the `$page->of()` method. If you call the `of()` method with no arguments, it simply returns the current output formatting state of true (ON) or false (OFF).

```
if($page->of()) {
  /* output formatting is ON */
} else {
  /* output formatting is OFF */
}
```

The `of()` method can also be used for setting the output formatting state. When you call `$page->of(true);` it enables (turns ON) output formatting. When you call `$page->of(false);` it disables (turns OFF) output formatting:

```
$page->of(false); /* set output formatting OFF */
$page->of(true); /* set output formatting ON */
```

When you call `$page->of(false);` any later calls to `$page->get('any_field')` or `$page->any_field` return unformatted values. Likewise, when you call `$page->of(true);` any later calls return formatted values. For this reason, if you change the formatting state, it's a good idea to restore it when you are done (see the section on best practices).

If you want to get an unformatted or formatted value without changing the formatting state of the `$page`, you can use the `getUnformatted()` or `getFormatted()` methods:

```
$value = $page->getUnformatted('title'); /* This & That */
$value = $page->getFormatted('title'); /* This &amp; That */
```

If you want to set and save a value, regardless of whether the page has output formatting ON or OFF, you can use the handy `setAndSave()` method:

```
$page->setAndSave('title', 'About This & That');
```

Just be sure that that the value you are setting and saving doesn't itself contain an already formatted value, such as one with an `&` in it.


## Security considerations


### Why is output formatting important for security?

Let's get back to our original example that demonstrated how output formatting in a text field converted an `&` to `&`.

Maybe it seems like not that big of a deal if we output `This & That` rather than `This & That`, as your browser is smart enough to still render it properly. But if you were to use an HTML validator on your document, it would fail. Who cares? Well, it really starts to matter when the page content can come from non trusted sources. Non trusted sources like a disgruntled employee with access to edit pages in the admin. Or perhaps content from pages created from user submitted forms on the front end.

If a page field value containing `&` is output as a literal `&` in HTML (rather than `&`) then that also means that characters like `<` and `>` won't be encoded to `<` and `>`, enabling them to create literal HTML like `<script>alert('gotcha!')</script>`.

And if an attacker can do that much, they can do much worse. If they can insert basic HTML and scripts, they can insert much more complex and malicious HTML or scripts. Perhaps even HTML and scripts that mimic a trusted login form that posts to the attacker's site, enabling them to capture a user's login and password.

The issue also arises with non-encoded quotes when they appear in text values. Consider an `<img src="…" alt="description">` where the `description` comes from non-trusted user input. If quotes are not encoded, then a description with a literal quote character `"` would close the alt attribute, opening the door for additional attributes or closing the `<img>` tag and starting new HTML tags. Consider a description like this…

```
description"><script>alert('gotcha')</script> 
```

…which would be possible without entity encoded quotes. Or consider a description value like this…

```
description" onclick="window.location.href='https://xxx.xxx'"
```

…which would also be possible without entity encoded quotes, and contains no HTML tags. If such a value came from a non trusted user, then that description could control what happens for any clicks on the image. Had the quotes just been entity-encoded to `"` these issues would not arise. This is one of many reasons why it's so important to ensure that text output is entity encoded.

For existing ProcessWire installations, consider reviewing all of your text fields (and fields that can use text, like file/image field descriptions), and verify that they have the "HTML entity encoder" selected for "Text formatters". This will ensure that when output formatting is enabled, your text values will be safe for output in HTML.


## Best practices


### Clean up after yourself

If you need to change the output formatting state of a `$page`, return it to its original state when you are done. This ensures that any later code accessing the same `$page` isn't given something unexpected.

```
$of = $page->of(); /* remember */
$page->of(false);
$page->body = str_replace('https://old.com', 'https://new.com', $page->body);
$page->save('body');
$page->of($of); /* restore */
```


### Turn off output formatting before making modifications

Often times I will see people call `$page->of(false)` right before a `$page->save()`, like this:

```
$page->title = "About $page->title";
$page->of(false); /* Oops */
$page->save();
```

This makes output formatting useless. The above can potentially corrupt the title value because it used the formatted value of `$page->title`, and turned off output formatting afterwards. Instead, we should turn off output formatting before we get or set any values to the page that will be used for manipulating the page:

```
$page->of(false);
$page->title = "About $page->title";
$page->save();
```

Even if we won't be using the existing field value in the new value, we should still turn off output formatting before populating any field values:

```
$page->of(false);
$page->title = "About This & That";
$page->save();
```


### How to get values without considering output formatting state

I already mentioned this one earlier, but it bears repeating. If it suits your purpose, consider using the `getFormatted()` and `getUnformatted()` methods when in an environment where the output formatting state isn't obvious. These always return the formatted or unformatted value, according to the method you use, without any need to call the `of()` method.

```
$value = $page->getUnformatted('title'); /* This & That */
$value = $page->getFormatted('title'); /* This &amp; That */
```


### Consider using a local copy of any value you will be re-using

Whenever you access `$page->field_name` or `$page->get('field_name')`, ProcessWire first gets the unformatted value behind-the-scenes. Then, if output formatting is enabled, it will route that value through the Fieldtype's `formatValue()` method, before returning it to you. Meaning, that `formatValue()` method will execute every time you access the field.

Note that there are exceptions to this. Some fields that use object values (like file and image fields) to keep track of whether their object value is already formatted or not, and thus don't re-do formatting on every call.

It works this way because ProcessWire doesn't know what will happen when the value is formatted. Perhaps the format involves some random or time-based element that must be unique on every call, or not. The point is, we don't know. So to be safe, ProcessWire caches the unformatted value and formats it before returning it to you, every time you ask for the field value. Given that, if your output involves repetitive calls to `$page->field_name`, it may be beneficial to keep a local copy to re-use:

```
$title = $page->get('title');
$body = $page->get('body');
$desc = $sanitizer->truncate($body, 260);

echo "
  <title id='html-title'>$title - CompanyName</title>
  <meta id='meta-description' name='description' content='$desc'>
  <meta property='og:description' content='$desc' pw-append='html-head'>
  <h1 id='headline'>$title</h1>
  <div pw-append='bodycopy'>$body</div>
";
```

If you are wondering how we can populate all those different parts of an HTML document in one small snippet, check out ProcessWire's [Markup Regions](/docs/front-end/output/markup-regions/).

This simple example reduced 2 calls each to title and body to just one call. In reality, I probably wouldn't bother keeping local copies of things like `$title` and `$body` unless I had selected some very time consuming text formatters for them (not likely). But I thought using familiar fields would help to communicate the idea best. Where I'd be more likely to keep local copies of field values like this is if I had to re-use values from more complex field types like repeaters or ProFields (Table, Combo, etc.) multiple times.


### Module developers: don't assume a particular output formatting state

Some modules may be active whether ProcessWire is rendering pages in HTML, an editor is editing pages in the admin, or ProcessWire has been booted from another application. This is particularly the case with autoload modules. The same can be true for hooks you might add in your /site/init.php or /site/ready.php files.

As we learned earlier, output formatting is ON most of the time, but will be OFF in the admin and when ProcessWire is booted from another application. In template files, we can safely assume output formatting is enabled. But your module or hook may still be active in other cases, so it should not assume a particular output formatting state.

If your module (or hook) needs to use a page for output, it should first make sure the page has output formatting enabled by checking `$page->of()` and turn it ON if necessary. On the other hand, if your module or hook needs to modify a page, it should also check `$page->of()` and turn it OFF if necessary. In either case, your module or hook should always clean up after itself, by restoring the page to the state it was received in.


### Avoid setting field values to pages with output formatting enabled

When you set a field value to a page with output formatting enabled, ProcessWire tests the value by formatting it and determining how it is affected. If ProcessWire determines that saving the page could cause corruption, it sets the page status to `Page::statusCorrupted`, which prevents it from ever being saved. If you try to save it, an exception will be thrown.

This is there to prevent accidents, but it's worth mentioning here because internally ProcessWire runs the formatters for any field values you set when output formatting is enabled for the page. For this reason, it's a best practice to avoid setting field values to a page with output formatting enabled. Even if you don't intend to save the page, it potentially increases overhead.

The solution of course it to turn off output formatting before setting field values to the page. But there's also a shortcut method that enables you to explicitly set a field value without turning off output formatting:

```
$page->setUnformatted('title', 'This & That');
```

If you are setting some value to a page that isn't for a field, then output formatting doesn't come into play at all, so it makes no difference, i.e. `$page->set('foo', 'bar');`


### Thoroughly test output formatting on fields

For any non-TinyMCE/CKEditor fields that contain text that will be placed directly in HTML markup, it's a good idea to test that the text is properly entity-encoded in output.

Maybe at some point you created the field and forgot to select "Entity encoder" as the Textformatter, or maybe you temporarily disabled it to check something and forgot to re-enable it. Recent versions of ProcessWire are more aggressive about alerting you to such issues, but all versions of ProcessWire do trust that you as the developer are configuring text fields in manner that is safe and appropriate for your needs. But still, nobody is perfect, so why not make sure?

I like to do this by creating a new "test" template that contains all of my text fields in it, also including any other fields that can contain text fields or subfields within them. These types include (but aren't limited to):

- Text and TextLanguage
- Textarea and TextareaLanguage
- PageTitle and PageTitleLanguage
- Repeater
- PageTable
- Options
- All of the ProFields
- Email (see notes)
- URL (see notes)

Once you have all fields of those types on a template, create a page using that template and for any text inputs, populate this:

```
<script>alert('field_name')</script>
```

Replace `field_name` with the name of the field.

In your template file, make it output values for all of the fields and then view the page. If you get a JS alert box with 'field_name' then you'll know that the field identified by that name needs work on its settings.


### Email fields

While less common in output, if you happen to use any email fields in output, consider enabling the "Entity Encoder" Textformatter by editing the email field and clicking on the Details tab. The danger with email addresses is that if the local-part starts and ends with a quote, the part between quotes can contain anything, even script tags, while still being a valid email address.

When used in output, email addresses are often placed within an HTML tag attribute, such as `<a href="mailto:addr@example.com">`. It's possible for a valid email address to contain a quote, and if not entity encoded, such a quote would close the `href` attribute and open the door for exploits.

Where you wouldn't want an email address entity encoded is if you are using the email address to actually send an email. Depending on the contents of the email address, entity encoding may take a valid email address and make it invalid. For this reason, another route is to avoid the Textformatter and instead manually entity encode an email address if and when you have to use it in output:

```
$email = $sanitizer->entities($user->email); 
echo "<a href='mailto:$email'>$email</a>";
```


### URL fields

You'll always want "Entity Encoder" selected for URL fields. Though our `<script>` test above may not be possible here. Test a URL such as `https://processwire.com?a=b&c=d`. When viewed in the page source output (raw HTML), the ampersand in the URL should be `&` rather than `&`. If it is `&` then you need to modify your URL field settings to enable the Entity Encoder Textformatter.


## Adding your own output formatting with hooks

The Fieldtype method that provides output formatting for each field is [Fieldtype::formatValue](../api-full/wire/core/Fieldtype/method-___formatvalue.md). That method is hookable, which enables us to very easily modify its return value however we'd like.

In this post, I needed a lot of `<code>` tags, but didn't feel like highlighting all of them in TinyMCE and selecting "Styles > Inline > Code". Instead, I wanted to be able to just wrap the words with backticks like `this` and have it convert to `<code>this</code>` automatically, like we do on GitHub and in markdown.

We could build a custom [Textformatter module](/modules/category/textformatter/) to do it, or we could just hook after the existing formatting, which is what this hook does below (added to my /site/ready.php file):

```
$wire->addHookAfter('FieldtypeTextarea::formatValue', function(HookEvent $e) {
  $value = $e->return; /* @var string $value */
  if(strpos($value, "`") === false || strpos($value, '<') === false) return; /* not HTML */
  if(!preg_match_all('/`([^`\n<>]+)`/', $value, $matches)) return; /* no matches */
  $a = [];
  foreach($matches[1] as $key => $code) {
    $find = $matches[0][$key];
    $replace = "<code>$code</code>";
    $a[$find] = $replace;
  }
  $e->return = str_replace(array_keys($a), array_values($a), $value);
});
```

This is just an example, as it could be any runtime text formatting or manipulation. Here's a much simpler example that adds "Copyright 2023" in a paragraph at the bottom of every "body" field:

```
$wire->addHookAfter('FieldtypeTextarea::formatValue', function(HookEvent $e) {
  $field = $e->arguments(1); /** @var Field $field */
  if($field->name == 'body') {
    $year = date('Y'); /* i.e. 2023 */
    $e->return .= "<p><small>Copyright $year</small></p>";
  }
});
```

Output formatting is a genuinely useful helper that opens the door to all sorts of possibilities, a few of which we've covered here. If you have any remaining questions about output formatting please feel free to post below and I'll be happy to reply.
