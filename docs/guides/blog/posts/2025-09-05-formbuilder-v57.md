# ProcessWire Form Builder Version 57

Source: https://processwire.com/blog/posts/formbuilder-v57/

## Sections


## Form Builder Version 57

5 September 2025 by Ryan Cramer [ 0 Comments](/blog/posts/formbuilder-v57/#comments)

This week we’ve got a new version of [FormBuilder](/store/form-builder/) released, version 57. This new version of FormBuilder adds a lot, including…

**New spam-blocking timer:** This feature lets you configure the minimum amount of seconds required to fill out a form. If the form is submitted faster than a human could fill it out, then it is considered spam.

**Updated Uikit 3 and Bootstrap 5 frameworks** that use the latest versions of the libraries as of today. As always, use of these CSS frameworks is completely optional. FormBuilder also makes it easy to add other frameworks, should it suit your need.

**Support for preview edit links:** When previewing a form, you now have the option of clicking a link in any field header in order to directly edit a field. This is handy, especially for large forms.

**New dedicated FormBuilder hook files:**

- `/site/templates/FormBuilder/hooks.php`
- `/site/templates/FormBuilder/hooks-formName.php`

This is a nice alternative to using /site/ready.php, as these files are only loaded when the applicable form(s) will be rendered or processed. There were also countless other additions, optimizations, fixes and updates in this version, but perhaps my favorite new addition is that FormBuilder now has a new and comprehensive FormBuilder API reference…


### Official Form Builder API reference

The new [FormBuilder API reference](/api/ref/form-builder/) includes coverage of not just the FormBuilder module but many of its components including the FormBuilder [Processor](/api/ref/form-builder-processor/), [Email](/api/ref/form-builder-email/), [Entries](/api/ref/form-builder-entries/), [Form](/api/ref/form-builder-form/), and even a [page dedicated to building FormBuilder plugins](/api/ref/form-builder-processor-action/).

FormBuilder originally started as a module that was intended to enable you to create, edit and use forms without having to code anything. But over time it became clear that people really wanted to get into the code, so numerous API methods and hooks were added incrementally. But there was no official API reference, until now.

FormBuilder continues its original mission of being a tool where no code is necessary, but for those that do want to get into the code, it now offers a lot more. If FormBuilder users find this helpful, we’ll likely take a similar approach with some of the other Pro modules as well.

**For the first week or two, please consider v57 as a development/beta version.** If you opt to try out this new version, please test in a development environment before a production environment, as most of the testing of this version has been on my own sites so far. It’s working very nicely for me, and has been very stable in my use, but please let me know if you run into any issues.

Next week we’ll likely be back to the core, working towards our next main/master version. Thanks for reading and have a great weekend!
