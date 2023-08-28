# Example 2: Format HTML Element

def create_html_element(tag, content, **attributes):
    attribute_str = ' '.join([f'{key}="{value}"' for key, value in attributes.items()])
    html_element = f'<{tag} {attribute_str}>{content}</{tag}>'
    return html_element


result = create_html_element('a', 'Click here', href='https://example.com', target='_blank')
print(result)  # Output: <a href="https://example.com" target="_blank">Click here</a>
