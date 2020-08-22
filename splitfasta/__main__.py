import argparse
import os


def check_extension(choices):
    class Act(argparse.Action):
        def __call__(self, parser, namespace, fname, option_string=None):
            ext = os.path.splitext(fname)[1][1:]
            if ext not in choices:
                parser.error(f"File doesn't end with one of {choices}")
            else:
                setattr(namespace, self.dest, fname)

    return Act


def main():

    parser = argparse.ArgumentParser()
    my_parser = argparse.ArgumentParser(prog='splitfasta', description='Splits the Fasta file with multiple sequences into individual Fasta files')

    my_parser.add_argument('File',
                           help='Name of the fasta file (.fa or .fasta)',
                           action=check_extension({'fasta', 'fa'}))

    args = my_parser.parse_args()
    input_file = args.File
    only_file_name = os.path.splitext(input_file)[0]

    # if not os.path.exists(f'{only_file_name}_split_files'):
    try:
        os.mkdir(f'{only_file_name}_split_files')
    except FileExistsError:
        pass

    DEST_DIR = f'{only_file_name}_split_files'

    with open(input_file, 'r') as f:
        data = f.read().split('>')

        for i, j in enumerate(data[1:], start=1):
            new_file_name = f'{only_file_name}_{i}.fasta'
            with open(os.path.join(DEST_DIR, new_file_name), 'w') as f:
                f.write('>' + j)


if __name__ == '__main__':
    main()
