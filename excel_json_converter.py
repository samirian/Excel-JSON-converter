import argparse
import time
from excel2json import convert_from_file


def main():
    parser = argparse.ArgumentParser(description='Converts given excel file to JSON format, where each sheet is converted in a separate file.', usage='python3 ExcelJsonConverte.py <excel_file_path> <output_directory>')
    parser.add_argument('excel_file_path', help='the path to the excel file to be converted.')
    parser.add_argument('output_dir', help='the path to the directory that will contain the output JSON files.')

    args = parser.parse_args()
    start = time.time()
    convert_from_file(args.excel_file_path, args.output_dir)
    end = time.time()
    print('Execution time:', (end - start)/60, 'mins.')


if __name__ == "__main__":
    main()