def create(files):
    try:
        with open(files, 'r', encoding='utf-8') as file:
            file.read()
    except:
        with open(files, 'w', encoding='utf-8') as file:
            file.write('')
            print(f'The file {file} was successfully created!')


def write(files, msg):
    from datetime import datetime
    try:
        with open(files, 'a') as file:
            file.write(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> {msg}\n')
    except:
        with open(files, 'a') as file:
            print('ERROR! Skipped line!')
            file.write(f'{str(datetime.today())[0:str(datetime.today()).find(".")]} -> ERROR! Skipped line!\n')
