import logging


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s')
    print("choose level: 0 - debug, 1 - info, 2 - warning")
    try:
        x = input()
        which_one = int(x)
    except:
        logging.warning("this is not a number!")
        which_one = 3

    if which_one == 0:
        logging.debug('debug level')
    elif which_one == 1:
        logging.info('info level')
    elif which_one == 2:
        logging.warning('warning level')
    else:
        logging.warning("number out of bounds")
