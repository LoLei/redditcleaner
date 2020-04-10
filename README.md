# redditcleaner

Cleans Reddit Text Data 📜 🧹 🧼 🧽

## Installation
[`pip install redditcleaner`](https://pypi.org/project/redditcleaner/)

## About

Reddit uses some characters in the raw text of comments and submission selftexts that may need to be removed if just the plain natural text is required for NLP/Data Science tasks.

If Reddit's or Pushshift's API is used to retrieve comments or submissions, the comment bodies or submission self texts may look like this:
```
Normal text\n\n**Bold**\n\n*Italic*\n\n[Link](https://fsf.org)\n\n~~Strike-through~~\n\n`Code`\n\n^(Superscript)\n\n&gt;!Spoiler!&lt;\n\n# Heading\n\nBullet list:\n\n* Item 1\n* Item 2\n\nNumbered list:\n\n1. Item 1\n2. Item 2\n\n&gt;Quote\n\n Code block\n\nTable:\n\n|Cell 1.1|Cell 1.2|\n|:-|:-|\n|Cell 2.1|Cell 2.2|

\n * Find &amp;#x200B; &gt; "\&gt; the "&gt; hidden\ntext [fsf](http://fsf.org)... This & that in a normal sentence. "manual quote"
```

These characters stem from (Reddit-specific) Markdown formatting.

This Python module removes these characters and returns the cleaned text. Using the example above, the output would be:
```
Normal text Bold Italic Strike-through Code Superscript Spoiler Heading Bullet list: Item 1 Item 2 Numbered list: 1. Item 1 2. Item 2 Quote Code block Table: Cell 1.1 Cell 1.2 Cell 2.1 Cell 2.2

Find the hidden text ... This & that in a normal sentence. "manual quote"
```
