from _ast import arg

import translators
import argparse


def translator(file1, to_lang, from_lang='auto', provider='google'):
    with open(file1) as f:
        s = f.read()
    engine = getattr(translators, provider)
    return engine(s, from_lang,to_lang)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='for translate')
    parser.add_argument('file_path', nargs='?', action='store', metavar='FILE_PATH', default=None)
    parser.add_argument('-t', '--to_lang', action='store', metavar='TO_LANG', default='fa', help='destination language')
    parser.add_argument('-f', '--from_lang', action='store', metavar='FROM_LANG', default='auto', help='origin language')
    parser.add_argument('-p', '--provider', action='store', metavar='PROVIDER', default='google', help='select provider')
    parser.add_argument('-s', '--save', action='store', metavar='SAVE_PATH', default='./', help='select a path to save result')
    args = parser.parse_args()
    if args.file_path==None:
        try:
            while True:
                s=input('>> ')
                print(translators.bing(s,to_language='fa'))
        except KeyboardInterrupt:
            print("finished")
    else:
        print(translator(args.file_path, args.to_lang, args.from_lang, args.provider))
    print(args)