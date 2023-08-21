from load_data import load_data
from output import out_result


def main():
    path_datafile: str = 'operations.json'
    out_result(load_data(path_datafile))


if __name__ == '__main__':
    main()