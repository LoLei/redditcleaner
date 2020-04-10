import re


def clean(text, newline=True, quote=True, bullet_point=True, 
          link=True, strikethrough=True, spoiler=True,
          code=True, superscript=True, table=True, heading=True):
    """
    Cleans text (string).
    Removes common Reddit special characters/symbols:
      * \n (newlines)
      * &gt; (> quotes)
      * * or &amp;#x200B; (bullet points)
      * []() (links)
      * etc (see below)
    Specific removals can be turned off, but everything is on by default.
    Standard punctuation etc is deliberately not removed, can be done in a
    second round manually, or may be preserved in any case.
    """
    if newline:
        text = re.sub('\n', ' ', text)                # Newlines
    if quote:
        text = re.sub(r'\"?\\?&?gt;?', '', text)      # > Quotes
    if bullet_point:
        text = re.sub(r'\*', '', text)                # Bullet points or asterisk in general (bold/italic)
        text = re.sub('&amp;#x200B;', '', text)       # Bullet points
    if link:
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)    # []() Links
    if strikethrough:
        text = re.sub('~', '', text)                  # Strike-through
    if spoiler:
        text = re.sub('&lt;', '', text)               # < Less-than (Used in spoiler-tag)
        text = re.sub(r'!(.*?)!', r'\1', text)        # Spoiler
    if code:
        text = re.sub('`', '', text)                  # Code
    if superscript:
        text = re.sub(r'\^\((.*?)\)', r'\1', text)    # Superscript
    if table:
        text = re.sub(r'\|', ' ', text)               # Table
        text = re.sub(':-', '', text)                 # Table
    if heading:
        text = re.sub('#', '', text)                  # Heading
    return text
