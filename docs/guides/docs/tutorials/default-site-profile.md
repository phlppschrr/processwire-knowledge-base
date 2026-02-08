# Introduction to the default site profile

Source: https://processwire.com/docs/tutorials/default-site-profile/

## Summary

Just getting started with ProcessWire and aren't totally clear on what template files are? The good news is that template files aren't anything other than regular HTML or PHP files, and you can use them however you want!

## Key Points

- Just getting started with ProcessWire and aren't totally clear on what template files are? The good news is that template files aren't anything other than regular HTML or PHP files, and you can use them however you want!
- If you know enough to create an HTML or PHP document, then you already know how to use ProcessWire template files. The only difference is that ProcessWire provides your template files with certain variables that you may choose to use, or not use. Most notable is the $page variable, which contains all the fields of text or other information contained by the page being viewed.
- For instance, $page->title contains the text contained in the Title field of the current page, and $page->body contains the text for the Body field of the current page. You can choose to output those wherever you want. A really simple template file might look like a regular HTML document except for where you want to output the dynamic portions (like title and body). Here's an example:

## Sections


### Template file strategies

The default site profile uses a strategy called Delayed Output, but you should use whatever strategy you prefer (or make up your own). The two most popular strategies for template files are:


## Beginner / direct output version


### Why we have different versions of the same site profile

The default site profile comes in 3 different versions: beginner, intermediate, and multi-language. The truth is, they are all equally simple (and all for beginners), but we are anxious to get you working with ProcessWire as quickly and easily as possible, so wanted to show you a couple different ways of doing things. We've found that people just getting started with ProcessWire are more likely to catch on quickly with the beginner version of the default site profile. Not because it's necessarily simpler, but because it uses a strategy similar to what you may have seen elsewhere (like in WordPress).


### How the beginner version of the default site profile works

This beginner version of the default site profile uses the Direct Output strategy. When a page is viewed on your site, here's what happens:


### 1. The initialization file is loaded (_init.php)

This step is completely optional with direct output, but we find it handy to use this file to define our shared functions (if any). In the case of this profile, we define a single renderNavTree() function. It is useful to have this as a re-usable function since we use it to generate markup for more than one place (specifically, for sidebar navigation and for the sitemap). However, if you have any confusion about this, ignore it for now and focus on #2 below, as an initialization file is completely optional.


### 2. The template file is loaded (i.e. basic-page.php or another)

Next, ProcessWire loads the template file used by the page being viewed. For example, most pages here use basic-page.php.


### Files in the beginner default profile

Here is a summary of what is in each of the files in the /site/templates/ directory of the beginner default site profile. We also recommend reviewing them in this order:


## Intermediate / delayed output version
