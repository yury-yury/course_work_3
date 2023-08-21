from load_data import load_data
from output import out_result


def main() -> None:
    """
    The main function is the entry point to the application. Doesn't take parameters.
    It coordinates the work of various elements of the application.
    """
    path_datafile: str = 'operations.json'
    out_result(load_data(path_datafile))


if __name__ == '__main__':
    main()