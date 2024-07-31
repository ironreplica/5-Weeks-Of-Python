from datetime import datetime
def write():
    f = open('notes.txt', 'a')
    f.write(f'\nTrevor Childs | {datetime.today().strftime('%Y-%m-%d')}\n{input('Note: ')}')
    write()
write()