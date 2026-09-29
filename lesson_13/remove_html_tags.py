
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    switch = True
    chars = []

    for char in html:
        if char == '<':
            switch = False
        elif char == '>':
            switch = True
        elif switch:
            chars.append(char)
    html = ''.join(chars)

    lines = html.splitlines(keepends=True)
    text_list = []
    for line in lines:
        if line.strip():
            text_list.append(line.strip(" "))
    html = ''.join(text_list)

    with open(result_file, 'w', encoding='utf-8') as result:
        result.write(html)


delete_html_tags(html_file='draft.html')
