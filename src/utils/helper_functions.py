import yaml


def load_key(path):
    with open(path, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)['key']


if __name__ == '__main__':
    print(load_key(r'/home/omrijsharon/PycharmProjects/setitfree/credentials/key.yaml'))