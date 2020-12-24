#### ленивый вариант ####
#
# from urllib import parse as ups
# def parse(url: str) -> dict:
#     return dict(ups.parse_qsl(ups.urlsplit(url).query))
#
#####
def parse(query: str) -> dict:
    _dict = {}
    if '?' not in query:
        return _dict
    else:
        for _ in query.split('?')[1].split('&'):
            if _ != '':
                i = _.split('=')
                _dict.update({i[0]: i[1]})
    return _dict

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://www.google.com/search?client=firefox-b-e&q=parser') == {'client': 'firefox-b-e', 'q': 'parser'}
    assert parse('http://example.com/?&') == {}
    assert parse('http://www.example.org/default.html?ct=32&op=92&item=98') == {'ct':'32', 'op':'92', 'item':'98'}
    print('Ok1')


def parse_cookie(query: str) -> dict:
    _dict = {}
    for _ in query.split(';'):
        if _ != '':
            i = _.split('=')
            _dict.update({i[0]: '='.join(i[1:])})
    return _dict

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User=Name;age=28;') == {'name': 'Dima=User=Name', 'age': '28'}
    assert parse_cookie('bday=01.01.1920') == {'bday': '01.01.1920'}
    assert parse_cookie('bday=01.01.1920;age=99;') == {'bday': '01.01.1920', 'age': '99'}
    assert parse_cookie('age=99;bday=01.01.1920;name=Name') == {'age': '99', 'bday': '01.01.1920', 'name': 'Name'}
    assert parse_cookie('email=name@mail.com;bday=01.01.1920;') == {'email': 'name@mail.com', 'bday': '01.01.1920'}
    print('Ok2')