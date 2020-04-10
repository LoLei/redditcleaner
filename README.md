# redditcleaner

Cleans Reddit Text Data 📜 🧹 🧼 🧽

## Installation
[`pip install redditcleaner`](https://pypi.org/project/redditcleaner/)

## About

Reddit uses some characters in the raw text of comments and submission selftexts that may need to be removed if just the plain natural text is required for NLP/Data Science tasks. This Python module cleans this text data.

## Usage

```python
import redditcleaner
text_raw = <Reddit text>
text_cleaned = redditcleaner.clean(text_raw)
```

### Input

If Reddit's or Pushshift's API is used to retrieve comments or submissions, the raw comment bodies or submission self texts may look like this:
```
Normal text\n\n**Bold**\n\n*Italic*\n\n[Link](https://fsf.org)\n\n
~~Strike-through~~\n\n`Code`\n\n^(Superscript)
\n\n&gt;!Spoiler!&lt;\n\n# Heading\n\nBullet list:\n\n* Item 1\n* Item 2
\n\nNumbered list:\n\n1. Item 1\n2. Item 2\n\n&gt;Quote\n\n 
Code block\n\nTable:\n\n|Cell 1.1|Cell 1.2|\n|:-|:-|\n|Cell 2.1|Cell 2.2|

\n * Find &amp;#x200B; &gt; "\&gt; the "&gt; hidden\ntext [fsf](http://fsf.org)...
This & that in a normal sentence. "manual quote"
```

These characters stem from (Reddit-specific) Markdown formatting.

### Output

This Python module removes these characters and returns the cleaned text. Using the example above, the output would be:
```
Normal text Bold Italic
Strike-through Code Superscript
Spoiler Heading Bullet list: Item 1 Item 2 
Numbered list: 1. Item 1 2. Item 2 Quote
Code block Table: Cell 1.1 Cell 1.2 Cell 2.1 Cell 2.2

Find the hidden text ... This & that in a normal sentence. "manual quote"
```

:warning: **Common punctuation, numbers, parentheses, quotation marks etc. are deliberately not removed**, as this data cleaning task pertains to Reddit-specific characters only. An additional round of data cleaning can be applied manually to clean these common items or apply lowercasing, or whatever else is needed.

### Advanced Usage
The `clean` function supports optional arguments and it can be used as a lambda to be applied on e.g. Pandas DataFrames.

#### Optional Arguments
Specific removals of characters can be disabled with optional arguments passed to the `clean` function. Everything is on by default, but setting one to `False` disables it.

```python
def clean(text, newline=True, quote=True, bullet_point=True, 
          link=True, strikethrough=True, spoiler=True,
          code=True, superscript=True, table=True, heading=True)
```
E.g.
```python
redditcleaner.clean(text, heading=False)
```

#### Pandas Usages
This simulates a common format used when retrieving this type of data via the Reddit API:
```python

# Put "retrieved" text into Pandas Dataframe
test_body_1 = "\n * Find &amp;#x200B; &gt; \"\\&gt; the \"&gt; hidden\ntext [fsf](http://fsf.org)... This & that in a normal sentence. \"manual quote\""
test_body_2 = "Normal text\n\n**Bold**\n\n*Italic*\n\n[Link](https://fsf.org)\n\n~~Strike-through~~\n\n`Code`\n\n^(Superscript)\n\n&gt;!Spoiler!&lt;\n\n# Heading\n\nBullet list:\n\n* Item 1\n* Item 2\n\nNumbered list:\n\n1. Item 1\n2. Item 2\n\n&gt;Quote\n\n    Code block\n\nTable:\n\n|Cell 1.1|Cell 1.2|\n|:-|:-|\n|Cell 2.1|Cell 2.2|"

import pandas as pd
df = pd.DataFrame([['asdf', 'test_a', test_body_1],
                   ['fdsa', 'test_b', test_body_2]],
                   columns=list(['id', 'author', 'body']))
                           
# Prepare redditcleaner
import redditcleaner
clean_reddit = lambda x: redditcleaner.clean(x)

# Apply (map) the function on all body columns
df['body'] = df['body'].map(clean_reddit)
df
```
|    | id   | author   | body                                                                                                                                                                                                                             |
|---:|:-----|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | asdf | testa    | Find    the  hidden text ... This & that in a normal sentence. "manual quote"                                                                                                                                                    |
|  1 | fdsa | testb    | Normal text  Bold  Italic    Strike-through  Code  Superscript  Spoiler   Heading  Bullet list:   Item 1  Item 2  Numbered list:  1. Item 1 2. Item 2  Quote      Code block  Table:   Cell 1.1 Cell 1.2       Cell 2.1 Cell 2.2 |

## Contributing
If I missed any characters that should also be removed, please let me know or feel free to create a PR yourself! :heart:
