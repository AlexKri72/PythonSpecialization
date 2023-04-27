# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil


def sort_files(dir_target: str, dir_video: str = 'Videos', dir_images: str = 'Images', dir_musics: str = 'Musics',
               dir_documents: str = 'Documents'):
    '''разносим файлы из целевой папки по другим, согласно их расширениям.'''

    if not os.path.isdir(dir_target):
        return 'Указанная цель не является папкой!'
    list_of_files = os.listdir(dir_target)
    video_ext = ['mov', 'mp4', 'mkv', 'avi']
    image_ext = ['png', 'jpeg', 'bmp']
    music_ext = ['mp3', 'wav']
    documents_ext = ['txt', 'doc', 'xls']
    all_ext = {dir_video: video_ext, dir_images: image_ext, dir_musics: music_ext, dir_documents: documents_ext}

    try:
        [os.mkdir(f'{os.getcwd()}/{dir_target}/{i}') for i in all_ext.keys()]
    except FileExistsError:
        print('Папки уже созданы.')

    def remove_file(current_file: str, target_dir: str, all_ext1: dict):
        cur_ext = current_file.split('.')[-1]
        for i in all_ext1.keys():
            if cur_ext in all_ext1.get(i):
                print(cur_ext)
                shutil.move(f'{os.getcwd()}/{current_file}', f'{os.getcwd()}/{i}')

    os.chdir(dir_target)
    [remove_file(cur_file, dir_target, all_ext) for cur_file in list_of_files]
    os.chdir('..')

    return f'Файлы в папке {dir_target} разнесены по типам.'


print(sort_files('Task07'))
