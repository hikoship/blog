f = open('test.txt')

games = []

while True:
    game = []
    if f.readline():
        for i in range(6):
            c = f.readline()
            c = c.replace('    ', '')
            c = c.replace('</td>', '')
            c = c.replace('<td>', '')
            c = c.replace('\n', '')
            game.append(c)
        f.readline()
        games.append(game)
    else:
        break

f2 = open('output.txt', 'w')
for g in games:
    f2.write('<p>\n')
    f2.write('    <b>' + g[1] + '</b><br>\n')
    f2.write('    ' + g[0] + ' · ' + g[3] + ' · ' + g[4] + '<br>\n')
    f2.write('    ' + g[5] + '<br>\n')
    f2.write('</p>\n')

f2.close()
