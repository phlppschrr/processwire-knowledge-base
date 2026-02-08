# Multi-language URLs in ProcessWire CMS

Source: https://processwire.com/docs/multi-language-support/multi-language-urls/

## Summary

Multi-language URLs and page names enable you to maintain different/translated URLs for each page, based on the language. It also lets you produce your site easily, as the language is determined automatically by the URL.

## Key Points

- [Overview](#overview)
- [Example](#example)
- [Getting started](#getting-started)
- [Going further](#going-further)
- [Implementing a language switcher](#language-switcher)

## Sections


## Multi-language URLs and page names

Multi-language URLs and page names enable you to maintain different/translated URLs for each page, based on the language. It also lets you produce your site easily, as the language is determined automatically by the URL.

ProcessWire takes care of all the work behind the scenes, and everything just works. Combined with multi-language fields, you can have a multi-language website with only a few clicks.

- [Overview](#overview)
- [Example](#example)
- [Getting started](#getting-started)
- [Going further](#going-further)
- [Implementing a language switcher](#language-switcher)
- [API additions and enhancements](#api)
- [Working with pagination and/or URL segments](#url-segments)
- [Improving the multi-language UI](#ui)
- [Language Field Tabs](#language-field-tabs)
- [Questions and support](#support)
- [FormBuilder and ProCache](#formbuilder-procache)


## Overview

As of ProcessWire 2.3.2 and newer (currently the *dev* branch on GitHub), we recommend installing the *Language Support Page Names* module, included with ProcessWire's core. This enables you to deliver a single page at different URLs, consistent with the language. Since the module can determine the language from the URL, that also means it can take care of determining and setting the language automatically. The end result is that you can write your site's template files without consideration of getting or setting the language. ProcessWire takes care of all the work behind the scenes, and everything "just works."


### Example

[Tripsite](http://www.tripsite.com) is an excellent example of a large multi-language website (in 5 languages) using ProcessWire with multi-language page names and multi-language fields. For example, these URLs reflect the same page in ProcessWire, but are accessed at different language-specific URLs, and output content specific to the language represented by the URL:

- English: [www.tripsite.com/bike-boat/](http://www.tripsite.com/bike-boat/)
- Spanish: [www.tripsite.com/es/bici-barco/](http://www.tripsite.com/es/bici-barco/)

We encourage you to browse this site further to see some of the possibilities with multi-language support.


### Getting started

Multi-language URLs / page names are best paired with [multi-language fields](/docs/multi-language-support/multi-language-fields/). Meaning, we recommend installing both the *Language Support Fields* and *Language Support Page Names* modules together. In order to test things out properly, start with at least one multi-language text field (i.e. field of type: *TextLanguage*, *TextareaLanguage* or *PageTitleLanguage*), edit a page using it, and populate it with the same text in multiple languages. This probably goes without saying, but you should also have more than one language installed in your system before proceeding further.

Once the *Language Support Page Names* module is installed, go and edit your homepage and click on the *settings* tab. For the *URL Name*, you should see multiple inputs, one for each language. These will represent the starting point of page URLs in each language. We recommend populating these with the same value as your language name (i.e. "es" for Spanish, "de" for German, "en" for English, etc.), though there is no requirement that they match up wit your language names. Some prefer to leave the "default" language page name blank, so that the URLs have no language segment at the beginning. Check the *Active* checkbox next to each language, so that the page is considered viewable in that language.

Once you have populated these names for your homepage, *save* and *view* the page. Now access the page in your web browser at one of the other language names you populated, like /de/ or /es/. Your translated multi-language fields should reflect the text in the language you expect. Likewise, any [static translations](/docs/multi-language-support/code-i18n/) (if you are using them) should reflect the proper language as well. The value of $user->language has been set automatically by ProcessWire.

**That is literally all there is to it.** Note that you didn't have to change anything about the code in your site's template files. Just a few clicks and you have a multi-language website.

*Please note that the URL for the default-language homepage is always your site's root URL, regardless of what you specify in the homepage name. This is intentional, as it's not desirable to have a homepage that produces a 404 or immediately performs a redirect to another URL. If populated, your homepage name for the default language is still applicable for the rest of the pages in your site. *


### Going further

The strategy that we used above to specify the page name at the homepage can be applied to any page in your site. But it's also optional from this point forward. You can translate the name of every (or any) page, but you don't have to. If you leave the non-default page names blank, then the default-language value is used instead. However, you will need to have the *Active* checkbox checked for any pages that you want to be visible in other languages.

One of the nice things about multi-language page names is that you don't have to do anything from the template-file side in order to detect or set the language. So there isn't really a lot to say about it until your needs get more specific. Below we try to cover some of the specific needs you may run into when building a multi-language site with multi-language page URLs/names.


### Implementing a language switcher

When visiting [Tripsite](http://www.tripsite.com), note that every page has one or more language switchers, enabling the user to view the same page in other languages. Here are a couple of approaches you can use to do the same.

First lets say you wanted to generate a list that linked to the page in all other languages it is available in (excluding the current language). Here's what the end result might look like (taken from [this page](http://www.tripsite.com/bike-boat/tours/provence-a-la-van-gogh/)):

And here's the code to implement it:

```
// remember what language is set to
$savedLanguage = $user->language;

foreach($languages as $language) {

  // if user is already viewing the page in this language, skip it
  if($language->id == $savedLanguage->id) continue;

  // if this page isn't viewable (active) for the language, skip it
  if(!$page->viewable($language)) continue;

  // set the user's language, so that the $page->url and any other
  // fields we access from it will be reflective of the $language
  $user->language = $language;

  // output a link to this page in the other language
  echo "<li><a href='$page->url'>$language->title: $page->title</a></li>";
}
// restore the original language setting
$user->language = $savedLanguage;
```

As an alternative, lets say that you wanted a <select> box language switcher that showed the current language while enabling the user to select the page in another. We'll also take this opportunity to demonstrate how you can retrieve the URL of another page using the $page->localUrl($language); function, which is an alternative to saving and changing the $user->language like we did in the previous example. Here is our desired output:

And here is the code to produce it:

```php
<select onchange='window.location=$(this).val();'><?php
foreach($languages as $language) {
  $selected = '';

  // if this page isn't viewable (active) for the language, skip it
  if(!$page->viewable($language)) continue;

  // if language is current user's language, make it selected
  if($user->language->id == $language->id) $selected = " selected=selected";

  // determine the "local" URL for this language
  $url = $page->localUrl($language);

  // output the option tag
  echo "<option$selected value='$url'>$language->title</option>";
}
?>
</select>
```

Using either one of these strategies, we can easily provide links for the user to switch to viewing the same page in another language.


### API additions and enhancements that accompany multi-language page names

In the example above for the language switcher you might have noticed the localUrl($language) function that we used. This is a function that was added by *Language Support Page Names*, for your convenience. Here is a list of all the functions that are enhanced or added, should you ever find them helpful:

Of course, these functions work on any Page object, we just use $page as an example.


### Working with pagination and/or URL segments

Page numbers (pagination) and URL segments are fully supported by multi-language page names. You don't have to do anything other than you would without multi-language support. Meaning, you can simply enable these features from your template settings, and you are good to go.

Multi-language page names does however add one nice feature for pagination: translated pagination URLs. Meaning, you can translate the keyword that signifies the current page number in the URL. Typically it is "page$n", where "$n" represents the current page number. But you can translate it specific to each language as needed. This is done in the *Language Support Page Names* module settings screen:


## Improving the multi-language UI


### Language Field Tabs

You might appreciate the UI improvements offered by the [Language Field Tabs](http://modules.processwire.com/modules/language-field-tabs/) module, which places your multi-language fields in tabs, like shown in the screenshot below:


## Questions and support

Please stop by our [multi-langage support board](/talk/forum/14-multi-language-support/) in the ProcessWire forums and we'll be glad to help!


### Can multi-language page URLs be used with Form Builder and/or ProCache?

Yes, both [FormBuilder](/store/form-builder/) and [ProCache](/store/pro-cache/) are designed to work nicely with multi-language page URLs and multi-language support in general. All of your multi-language URLs are cachable by ProCache, except those requiring GET or POST form submissions. When creating multi-language forms with Form Builder, it will display the form in the appropriate language consistent with the language identified by the URL. Both ProCache and Form Builder are great additions to your multi-language site.
