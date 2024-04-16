def criar_dicionario_musicos():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    dicionario_musicos = {}
    for musico, ano in d:
        if ano in dicionario_musicos:
            dicionario_musicos[ano] += ' ' + musico
        else:
            dicionario_musicos[ano] = musico
    return dicionario_musicos


def mostrar_dicionario(dicionario):
    for ano, musicos in sorted(dicionario.items()):
        print("{} : {}".format(ano, musicos))


if __name__ == "__main__":
    dicionario_musicos = criar_dicionario_musicos()
    mostrar_dicionario(dicionario_musicos)