import io
from pickle import Pickler
import sys
from msgspec import json, MsgspecError
from structs import PreparedData

if __name__ == '__main__':
    try:
        with open('test_prepared_data.json', 'rb') as f:
            prepared_data = json.decode(f.read(), type=PreparedData)
    except (MsgspecError, FileNotFoundError):
        sys.exit(1)


    print('start pickling...')

    count = 99999
    while count > 0:            
        prepared_data.key = count

        with io.BytesIO() as buf:
            p = Pickler(buf)
            p.dump(prepared_data)

        count -= 1

    print('pickling done.')