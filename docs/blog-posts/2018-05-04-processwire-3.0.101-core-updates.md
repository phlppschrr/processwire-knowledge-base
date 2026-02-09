# ProcessWire 3.0.101 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.101-core-updates/

## Sections


## ProcessWire 3.0.101 core updates

4 May 2018 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-3.0.101-core-updates/#comments)


## ProcessWire 3.0.101

This week's version of ProcessWire on the dev branch continues resolution of GitHub issue reports, and it also adds a new text truncation function to our $sanitizer API, something requested from our requests repository. We didn't have a blog post for last week's version 3.0.100—see the core updates section in [ProcessWire Weekly #207](https://weekly.pw/issue/207/) for more details on that version.


### New $sanitizer->truncate() method

This particular feature was [requested by Adrian](https://github.com/processwire/processwire-requests/issues/163) in our processwire-requests repository. Teppo also [replied](https://github.com/processwire/processwire-requests/issues/163#issuecomment-372028057) to the request, “This is something that I've needed on every ProcessWire site I've built so far, more or less. Makes sense not to reinvent the wheel every single time.” I agree, the same is true for me—I've needed this feature on every site I've built. And I can't tell you how many times I've built text truncation functions, reinventing the wheel. It seemed like something that really belonged in our API.

There are a lot of uses for text truncation, but a universally common one in ProcessWire is for generating a short summary from body copy, like for search results, featured pages or the like. Truncated text is not just a shorter copy of a string. Instead, it needs to be smarter than that, making sure to truncate in places that don't break words.

I thought it would be a fairly simple addition. But in order to be worth having in the core, it had to be more flexible and powerful than all the single-purpose truncate functions I've built for sites in the past. Nevertheless, I thought it would still be relatively simple, as truncating text isn't such a complex thing. But as I got going with it, I realized it's really not such a simple thing, once accounting for all the various needs I've come across with text truncation over the years.

It started as a small function in our Sanitizer class, but as I started thinking about the various places where it might be used, the scope changed to where it really belonged in its own class with related support functions. The resulting class is called WireTextTools, though the end result is accessible via `$sanitizer`. I think the resulting function is quite useful, flexible, and powerful, at least for the cases I'm familiar with. Let's take a closer look.

The `$sanitizer->truncate()` method accepts the string you want to truncate (like $page->body), the max-length you want to truncate it to, a truncation type (word, sentence, punctuation, paragraph), and other various options you can use to modify its behavior. Here are a few examples:

```
// Truncate string to closest word within 150 characters;
// this is the most basic, but also likely the most common usage.
$s = $sanitizer->truncate($str, 150);

// Truncate string to closest sentence within 300 characters
$s = $sanitizer->truncate($str, 300, 'sentence');

// Truncate with options
$s = $sanitizer->truncate($str, [
  'type' => 'sentence',
  'maxLength' => 300,
  'visible' => true,
  'keepFormatTags' => true,
  'more' => '…'
]);
```

The default behavior of the truncate() method is to truncate to the closest word within the max length that you specify. The method can accept plain text or HTML. If given HTML, it still truncates to plain text, though if you want to retain HTML, there are options available for that. If using HTML, and you don't want it to count characters used by markup tags or entities towards your max length, an option is available for that too.

The truncate method truncates to the closest word by default. But the `type` option lets you adjust that so that you can truncate to the closest punctuation, sentence, or paragraph (block). For instance, if you were using the "sentence" type of truncation, and specified 500 as your max-length, then it would include as many sentences as possible in 500 characters, omitting any partial sentences.


### Truncate options

Below are a list of options that can be specified to the truncate() function:

`type` (STRING) Preferred truncation type of closest "word", "punctuation", "sentence", or "block" (like a paragraph). The default value is "word". This is a “preferred type”, not an absolute one, because it will adjust to match what it can within your maxLength. For instance, if it can't match a complete sentence in your requested maxLength, then it will then attempt to match to the closest punctuation (like a comma). And if it still can't match that, then it will match to the closest word.

`maximize` (BOOLEAN) Include as much as possible within specified type and max-length? The default value is true. However, if you specify false, then it will include as little as possible of your specified type. For instance, if your type is "sentence" and there are 3 sentences within your max-length, then it'll include only the first sentence. If your type of "block" then it would include only the first paragraph, even if it could match 3 paragraphs in your max-length.

`visible` (BOOLEAN) When true, invisible text (markup, entities, etc.) does not count towards string length. The default is false. This is useful when your max-length has more to do with optics than something technical. This option is more likely to be useful when combined with the keepTags or keepFormatTags options, which allow for markup to remain in the truncated string.

`trim` (STRING) Characters to trim from returned string. The default is ",;/ ". These are the characters that aren't great to end a truncated string with since they are really only contextual to the text that follows the truncated version.

`noTrim` (STRING) Characters that, if present at the end of the string, should be included when possible. These are characters that close something that was opened in the truncated text. Things like quotes, parenthesis, brackets, etc. The default value is: ')]}”»'

`more` (STRING) A string that is appended to truncated strings that do not end with sentence punctuation. For instance, if the returned value doesn't end with a period, question mark or exclamation point, then you've likely truncated in the middle of a sentence, so this string indicates that. The default value is an ellipsis "…".

`keepTags` (ARRAY) These are HTML tag names that you want to remain in the truncated string. For instance a value of ['em','strong'] will ensure those tags remain. Though you might prefer to use the next option, which ensures all text formatting inline tags remain.

`keepFormatTags` (BOOLEAN) When true, this keeps all HTML text formatting tags in the returned string, stripping only the block level ones. The tags it leaves are: abbr, acronym, b, big, cite, code, em, i, kbd, q, samp, small, span, strong, sub, sup, time, and var.

`collapseLinesWith` (STRING) In a truncated string, multiple lines are are collapsed to a single line by default. If converting HTML for instance, there might be a headline followed by a paragraph. When those are collapsed, it might break readability since it will look like a run-on sentence (since headlines don't typically end with punctuation). So this collapseLinesWith option lets you specify what should separate a non-punctuated line from whatever follows it. The default value is an ellipsis surrounded by a space on either side, " … ".

`convertEntities` (BOOLEAN) By default, entity-encoded characters in the source string remain remain in the truncated string. If you want it to convert them to non-entity encoded characters, like &amp; to &, then specify true for this option. The default is false.

`noEndSentence` (STRING) When using a truncation of type "sentence", there are some words that are punctuated like the end of a sentence, but don't actually represent the end of a sentence (at least in English). Truncating them as a sentence will provide an unintended result. But it's pretty much impossible for a computer to know that, without knowing the words that apply to that context. This option provides that list of those words. The default value is "Mr. Mrs. Ms. Dr. Hon. PhD. i.e. e.g.".

To summarize, there are a lot of options available for affecting the behavior of this new truncate() function, but it remains very simple to use. I've focused in on the types of truncate options I've needed in my own projects, and chances are there will be more options added as I learn more about what others need here too. Because it is new code, please also keep an eye out for any bugs in it and let me know if you come across any.


### Related methods

Some other methods were built to support the truncate() function, but they could be useful on their own too. Below are the other methods added to the WireTextTools class. To access these methods, you have to create a new instance of WireTextTools, or obtain one from `$sanitizer->getTextTools();`

`markupToText()` Convert markup to plain text in a manner that maintains the readability and formatting (where possible) of the original HTML. We're probably going to make use of this one in our WireMail class to handle the default HTML-to-plaintext conversion.

`fixUnclosedTags()` Given a string of HTML, remove or close any unclosed tags. This function also knows about tags that require no closing tag, and it ignores them. For the truncate() function, this solves the issue of text getting truncated in the middle of a tag, like "This is <em>emphasis text</em>" getting truncated to "This is <em>emphasis", which would leave an unclosed <em> if we didn't have this fixUnclosedTags() function.

`collapse()` Collapse a string of text all down to a single long line, maintaining readability, without mangling any words or punctuation.

`getVisibleLength()` Gets the visible length of the string, rather than the actual length that you'd get from strlen(). The visible length means the number of visible characters that the user would see on screen. Meaning an entity like &amp; would count for 1 character rather than 5, and some HTML like <em>hi</em> would count as 2 characters rather than 11.

That's all for this week. Have a great weekend and enjoy reading the [ProcessWire Weekly](http://weekly.pw)!
