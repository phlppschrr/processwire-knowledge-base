# Multi-language URLs and page names

Source: https://processwire.com/docs/multi-language-support/multi-language-urls/

## Summary

Multi-language URLs and page names enable you to maintain different/translated URLs for each page, based on the language. It also lets you produce your site easily, as the language is determined automatically by the URL.

## Key Points

- Multi-language URLs and page names enable you to maintain different/translated URLs for each page, based on the language. It also lets you produce your site easily, as the language is determined automatically by the URL.
- ProcessWire takes care of all the work behind the scenes, and everything just works. Combined with multi-language fields, you can have a multi-language website with only a few clicks.
- As of ProcessWire 2.3.2 and newer (currently the dev branch on GitHub), we recommend installing the Language Support Page Names module, included with ProcessWire's core. This enables you to deliver a single page at different URLs, consistent with the language. Since the module can determine the language from the URL, that also means it can take care of determining and setting the language automatically. The end result is that you can write your site's template files without consideration of getting or setting the language. ProcessWire takes care of all the work behind the scenes, and everything "just works."

## Sections


## Overview

As of ProcessWire 2.3.2 and newer (currently the dev branch on GitHub), we recommend installing the Language Support Page Names module, included with ProcessWire's core. This enables you to deliver a single page at different URLs, consistent with the language. Since the module can determine the language from the URL, that also means it can take care of determining and setting the language automatically. The end result is that you can write your site's template files without consideration of getting or setting the language. ProcessWire takes care of all the work behind the scenes, and everything "just works."


### Example

Tripsite is an excellent example of a large multi-language website (in 5 languages) using ProcessWire with multi-language page names and multi-language fields. For example, these URLs reflect the same page in ProcessWire, but are accessed at different language-specific URLs, and output content specific to the language represented by the URL:


### Getting started

Multi-language URLs / page names are best paired with multi-language fields. Meaning, we recommend installing both the Language Support Fields and Language Support Page Names modules together. In order to test things out properly, start with at least one multi-language text field (i.e. field of type: TextLanguage, TextareaLanguage or PageTitleLanguage), edit a page using it, and populate it with the same text in multiple languages. This probably goes without saying, but you should also have more than one language installed in your system before proceeding further.


### Going further

The strategy that we used above to specify the page name at the homepage can be applied to any page in your site. But it's also optional from this point forward. You can translate the name of every (or any) page, but you don't have to. If you leave the non-default page names blank, then the default-language value is used instead. However, you will need to have the Active checkbox checked for any pages that you want to be visible in other languages.


### Implementing a language switcher

When visiting Tripsite, note that every page has one or more language switchers, enabling the user to view the same page in other languages. Here are a couple of approaches you can use to do the same.


### API additions and enhancements that accompany multi-language page names

In the example above for the language switcher you might have noticed the localUrl($language) function that we used. This is a function that was added by Language Support Page Names, for your convenience. Here is a list of all the functions that are enhanced or added, should you ever find them helpful:


### Working with pagination and/or URL segments

Page numbers (pagination) and URL segments are fully supported by multi-language page names. You don't have to do anything other than you would without multi-language support. Meaning, you can simply enable these features from your template settings, and you are good to go.


## Improving the multi-language UI
