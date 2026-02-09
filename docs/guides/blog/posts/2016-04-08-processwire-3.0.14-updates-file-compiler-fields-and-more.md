# ProcessWire 3.0.14 updates file compiler, fields and more

Source: https://processwire.com/blog/posts/processwire-3.0.14-updates-file-compiler-fields-and-more/

## Sections


## ProcessWire 3.0.14 updates file compiler, fields and more

8 April 2016 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-3.0.14-updates-file-compiler-fields-and-more/#comments)


## ProcessWire 3.0.14

Getting closer to the ProcessWire 3.x stable release, version 3.0.14 focuses largely on updates and optimizations specific to recent GitHub issue reports. We also have optimizations and in-depth coverage of PW's file compiler, some new options for required fields, along with a review of some best practices when working with fields.

It's now Spring 2016 (Happy Spring!) so we're starting to focus on getting PW3 ready for it's stable release. As a result, we'll likely be shifting some attention away from adding new features, and more towards maximizing the stability of 3.0 in preparation for release. Most of our updates this week can be found in the [devns branch commit log](https://github.com/ryancramerdesign/ProcessWire/commits/devns), and we'll also cover some of the bigger ones below.


## File compiler updates

If you are using ProcessWire 3.x, you are likely familiar with the file compiler, which compiles template files and modules to make them work in ProcessWire 3.x's namespaced environment. This enables non-namespaced code written for ProcessWire 2.x to easily work with ProcessWire 3.x. It's a good solution for the transition of no-namespace to ProcessWire namespace.

In ProcessWire, compiling a file means moving it to another location (in /site/assets/cache/), making updates to it, and using the updated file rather than the original.

Once ProcessWire 3.x has been out for awhile, we expect that modules and template files will be coded specifically for 3.x more and more. By that, I mean they will use namespaced PHP code. That means simply having a `namespace ProcessWire;` (or some other namespace if preferred) at the top of each PHP file. Once a namespace is present, it's no longer necessary for the file to be compiled in order to work with ProcessWire 3.x.


### New compiler option for templates

ProcessWire 3.x already detects whether modules have a namespace or not. When they do, the modules are used as-is without compilation. When they don't, ProcessWire compiles the module for compatibility with 3.x.

This week we added that same option for template files. Meaning, you can now specify that ProcessWire should not compile your template file if it has a namespace present. We're calling this the *Auto* option:

This new *Auto* option is our new default (for newly added templates) and it enables the compiler to be automatically disabled whenever you add a namespace to your template, should you decide to sooner or later. Likewise, if you remove the namespace, it'll start compiling your template again.

Note that there are other uses for template compilation outside of just making 2.x template files compatible with 3.x, such as use of [FileCompiler modules](/blog/posts/processwire-3.0-alpha-2-and-2.6.22-rc1/#file-compiler-modules). So if you always want a compiled template then choose one of the "Yes" options rather than the "Auto" option.


### File compiler optimizations

The file compiler also received a few optimizations this week. One of the biggest optimizations is that it is now a little bit smarter about when a file needs compilation or not. Specifically, it doesn't need to use as many compiled files as before. If it determines that the original file can still be used (even if it lacks a namespace) it will use the original file rather than the compiled version. It will still compile the file so that it can keep track of things for comparison purposes, but it will use the non-compiled source file instead of the compiled version when it is possible to do so.


### Are there any drawbacks to using compiled files?

Since we're talking about ways to enable and disable the file compiler above, you might be wondering what are the drawbacks of file compilation. In an ideal world, we wouldn't need file compilation at all. That's because technically, it is overhead. ProcessWire has to keep track of both the source and target (compiled) files, and re-compile the source to target every time a change is made to the source file.

Keeping track of what needs to be compiled and when adds a little bit of overhead, though not overhead you are ever likely to notice. Whereas the actual compilation of a file can be slow, perhaps taking up to a second to compile a single file. Thankfully, once compiled, it continues using the compiled version until it's no longer current. Meaning, compiled files shouldn't affect the performance of your site since the compiled file should execute just as fast as the original.


### Keeping track of what needs to be compiled

For every compiled file, ProcessWire has to keep a hash of the source and target file contents and compare them to each other every time the file is used. This ensures a compiled file can never be of a version older than the source. It's quite fast actually, but it does add a little bit of overhead, especially if there are lots of compiled files to review on every request.

In reality, I haven't yet noticed any difference in performance between sites using compiled files and those not, except when the actual files need to get compiled (which you definitely notice). But the point I'm trying to get across here is that *there are more “moving parts” when the file compiler is involved*. So if you are starting a new site, or building a new module, you might consider making it PW3 native by using the ProcessWire namespace in your template file(s) and/or module (or another namespace if preferred). But of course, doing so will always be optional.


### Is it worth updating template files in existing sites to avoid compilation?

I'd say No, as this is exactly what the file compiler was originally intended for – to save you from having to modify your site during a PW2 to PW3 major site upgrade. ProcessWire is here to save you time, not cost you time. Though if you want to avoid compilation perhaps due to a complex application, then it's something to consider. But in my case, I've not updated templates in any of my PW2 to PW3 site upgrades, as I've not seen any reason to. But when creating new sites, I'm using the ProcessWire namespace in my template files so that compilation isn't necessary.


### Is it worth updating existing modules to to avoid compilation?

This is for module developers. The answer is Yes and No. But for now, No, unless you are creating a brand new module. After the stable PW3 has been out for awhile and use of PW2 is less common, then I would say Yes, we'll want to update our modules to be PW3 native by using a namespace.


### Fewer moving parts or more?

To conclude the question, fewer moving parts are always a good thing in any machine or application. But the moving parts are there for a reason, and are often more than worthwhile. Such is the case with compiled files. Yes there are some drawbacks to compiled files, but the drawbacks are relatively minimal (or non-existent) for many. The major point of the file compiler is to save you time, so use it when it will save you time. If it's not going to save you time–like when creating a new site in PW3–then you might consider bypassing the compiler unless you need FileCompiler modules (which is currently a rare need). If you've determined you don't need the file compiler, how do you bypass it? Read on…


### How to bypass the file compiler

If you want to globally disable compilation for all template files, add this in your /site/config.php file:

```
$config->templateCompile = false;
```

You can do the same to disable module compilation, though we don't recommend this at present since few modules are PW3 native.

**If you want to disable compilation for a single template file**, edit the template in Setup > Templates > your-template. Click the *Advanced* tab, and choose "No" or "Auto" for the "Use Compiled File?" setting. If you choose "Auto", you'll have to make sure your template has a `namespace ProcessWire;` at the top (or another namespace).

**You can disable the compiler for any module** just by declaring a namespace at the top, like mentioned in the previous item.

**You can disable the compiler for any individual file** (regardless of whether it's for a template or module) by adding the text `FileCompiler=0` somewhere within it. Presumably you'd put this in a PHP comment perhaps at the top of the file, but it doesn't matter, i.e.

```
// FileCompiler=0
```


### I don’t know what any of this compiler stuff is and I don’t care

This is why the file compiler exists. It's biggest purpose is to enable you to go about your business without caring about major version differences in your CMS. So if this is you, then you should continue using ProcessWire the way you always have. Most likely you can tune out whenever you hear the term "file compiler".


### I still don’t care

Good! That means the file compiler is working correctly. Carry on. But if you do start to care, or run into any issues you aren't sure about, come back here to learn more about the options available to control the file compiler.


## Required fields in ProcessWire

In ProcessWire, you can't publish a new page until all required fields are completed. But once that page is published, the "required" state of a field is not as strict. If a person editing intentionally makes a required field blank, it'll notify that user that they've missed something required (and continue to do so, so long as it's blank). But ProcessWire won't prevent the page from being saved, or block the edit they've made. So the required state for a field has always been more like a strong suggestion than a do-or-die rule, at least when it comes to already published pages.

Why? ProcessWire's schema is always flexible. You can add new fields to existing templates at any time (optionally making them required). You can modify the settings of existing fields, perhaps making a field required that wasn't before. Basically, it's always possible for required fields to exist as blank. It's the nature of the flexibility.

**Avoid writing code with ProcessWire's API that assumes a field will be always populated.** In most cases, the distinction may not matter. But for cases where it might matter, it's as simple as an `if()` statement to make sure something is there before you start building markup around it. We'll cover some examples and best practices in the next section.


### New required field options

There have been requests to provide more options in dealing with missing required fields on published pages, so this week we've added a couple that you may find useful. You can now specify how you want ProcessWire to handle missing required values on published pages, as part of your template configuration. When editing a template, click to the *Advanced* tab, and note the new "Required field action" field. Now you can specify whether you want ProcessWire to simply alert the user of the error (as it has always done), restore the previous value, or revert the page to an Unpublished state:

This is specified at the Template level because it's very likely you may prefer different behaviors depending on the template. For instance, you wouldn't want a missing required field to unpublish a top-level section of your site, but it might be perfectly fine for a product page in a large inventory of products.

Note that alerting the user of the error is the only solution that will work 100% of the time. That's because there may not be a previous value to restore (as would be the case on a newly added field), or the user may not have permission to unpublish a page. So just keep that in mind as you consider these options.

Also note that these new options do not relieve you of the responsibility to check that a value is populated when it comes to your own code, as blank values can exist on a Page regardless (for the reasons of flexibility stated earlier). We'll cover some best practices in this regard in the next section.


## Best practices with fields and values

When working with fields on a page in ProcessWire, it's never a good idea to assume that a given custom field is always going to have a value. Most of the time it doesn't matter that much, but in some cases it does. We'll cover some scenarios and things to consider here.


### Image and file fields

If you are outputting a photo gallery, you might first check that there are some photos before outputting a headline and list of photos:

```
if(count($page->photos)) {
  echo "<h3>Photo Gallery<h3>";
  echo $page->photos->each("<img src='{url}'>");
}
```

If the above code executed without that `if()` statement, it's hardly an error – it would just display a "Photo Gallery" headline with no photos below it. If you didn't need the headline, to accompany it, you could safely skip that `if()` statement if you wanted to. That's because the value is always a Pageimages object/array, which can contain 0 or more values.

*But suppose you instead have an images field where you've specified it can only contain 1 value. *You are now dealing with a single item (or no item) rather than an array of items. You've got to be more careful with that because if it has a value, it'll be a single image (Pageimage object). whereas if it doesn't, then it will be empty/nothing. If you try to treat it as a literal image object in your code without first checking that it's populated, that will result in a PHP error if it happens to be empty. Given that, note the following examples:

```
// Don't do this: if no image, then fatal error
echo "<img src='{$page->image->url}'>";

// Do this: if no image, no problem
if($page->image) {
  echo "<img src='{$page->image->url}'>";
}
```


### Single item Page fields

ProcessWire gives you some useful alternatives to work with when dealing with Page fields. You have control over whether the value will be an array of pages (PageArray) or a single page. If you choose a single page, then you can also choose what the blank value would be: boolean false or a NullPage.

**For these single item Page fields, it's safer to choose NullPage as your blank value** because a NullPage is just another type of Page (with id=0) so any code written to work with a Page will also work with a NullPage. That doesn't mean you shouldn't still check that it's populated, just that doing so isn't necessarily required.

```
// If Page field is type: Page or NullPage
// good to check that it has an "id", but not fatal if skipped
if($page->cat->id) {
  echo "<p>Category: {$page->cat->title}</p>";
}
```

**But lets say that you've instead chosen "Page or boolean false" for your Page field.** In that case, it's necessary to check that a value is present before treating it as a Page because trying to access an $object->property of a boolean false would be a fatal PHP error. This is just like the situation we described earlier with regard to a single Image field.

```
// Don't do this: fatal error if $page->cat is empty
echo "<p>Category: {$page->cat->title}</p>";

// Do this
if($page->cat) {
  echo "<p>Category: {$page->cat->title}</p>";
}
```


### Text fields

Most fields you work with in ProcessWire are probably text fields, and the blank value of a text field is just a blank string of text. Meaning, you don't need to use much care here. However, if you need to output related content (like a headline) based on whether a field is present or not, then it's a good idea to use an if() statement to check that there's a value before outputting that related content. Likewise, if you want to display alternative content if a value is not present an if() statement can be helpful here too:

```
if($page->headline) {
  echo "<h1>$page->headline</h1>";
} else {
  echo "<h1>$page->title</h1>";
}
```

There's also another way to handle this kind of if() statement above, by using fallbacks…


### Fallback fields

Another useful way to handle values that aren't present is to use fallbacks. When you ask a page for a field value, you can specify the alternatives that you'll accept if the one you requested isn't available. For instance, we might have 3 fields that we can output in the browser `<title>` tag: browser_title, headline or title, in that order:

```
<title><?=$page->get('browser_title|headline|title')?></title>
```

In the above example, ProcessWire will try to get the "browser_title" field. If not available, it'll try to get the "headline" field. And if that's not available, it'll use the "title" field.

The examples above are best practices to working with ProcessWire fields and translate to almost all ProcessWire Fieldtypes. That's all for this week! Hope that you all have a great weekend and week ahead. Remember to read the [ProcessWire Weekly](http://weekly.pw) this weekend.
