# Imports
import argparse
import yaml

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, help='Name of YAML file that contains resume contents.')
parser.add_argument('--destination', type=str, help='Path to save generated YAML file.')

# Main
def main():
    ARGS = parser.parse_args()

    ## Load files
    data = None
    with open(ARGS.source, 'r') as file:
        data = yaml.safe_load(file)

    ## Generate authors content
    authors = {
        data['general']['name'].split(' ')[0].lower(): {
            'name': data['general']['name'],
            'title': data['general']['title'],
            'url': data['general']['contact']['website'],
            'image_url': '/img/logo.png',
            'page': True,
            'socials': {
                'github': data['general']['contact']['github']
            }
        }
    }

    ## Save generated content
    yaml.safe_dump(authors, stream=open(ARGS.destination, 'w'))

if __name__ == '__main__':
    main()
