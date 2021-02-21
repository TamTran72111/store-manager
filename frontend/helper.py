def add_static_for_links():
    with open('dist/index.html') as f:
        data = f.read()

    data = data.replace('href="/', 'href="/static/')
    data = data.replace('src="/', 'src="/static/')

    with open('dist/index.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    add_static_for_links()
