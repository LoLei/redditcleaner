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
    # Newlines (replaced with space to preserve cases like word1\nword2)
    if newline:
        text = re.sub(r'\n+', ' ', text)

        # Remove surrounding ' '
        text = text.strip()
    # > Quotes
    if quote:
        text = re.sub(r'\"?\\?&?gt;?', '', text)

    # Bullet points/asterisk (bold/italic)
    if bullet_point:
        text = re.sub(r'\*', '', text)
        text = re.sub('&amp;#x200B;', '', text)

    # []() Link (Also removes the hyperlink)
    if link:
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)

    # Strikethrough
    if strikethrough:
        text = re.sub('~', '', text)

    # Spoiler, which is used with < less-than (Preserves the text)
    if spoiler:
        text = re.sub('&lt;', '', text)
        text = re.sub(r'!(.*?)!', r'\1', text)

    # Code, inline and block
    if code:
        text = re.sub('`', '', text)

    # Superscript (Preserves the text)
    if superscript:
        text = re.sub(r'\^\((.*?)\)', r'\1', text)

    # Table
    if table:
        text = re.sub(r'\|', ' ', text)
        text = re.sub(':-', '', text)

    # Heading
    if heading:
        text = re.sub('#', '', text)

    return text
