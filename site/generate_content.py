# Imports
import argparse
import yaml
import os

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, help='Name of YAML file that contains resume contents.')
parser.add_argument('--destination', type=str, help='Path to save generated YAML file for Hugo to use.')

# Main
def main():
    ARGS = parser.parse_args()

    ## Load files
    print(f'[INFO]: Loading contents from {ARGS.source}...')
    data = None
    with open(ARGS.source, 'r') as file:
        data = yaml.safe_load(file)

    ## Convert
    print('[INFO]: Generating Hugo data format config...')
    ### Author
    FILE_NAME = 'author.yml'
    template = {
        'author': {
            'name': data['general']['name'],
            'location': data['general']['location'],
            'description': data['general']['summary'][0],
            'github': f"https://github.com/{data['general']['contact']['github']}",
            'github_username': data['general']['contact']['github'],
            'email': data['general']['contact']['email'],
            'linkedin': f"https://www.linkedin.com/in/{data['general']['contact']['linkedin']}",
            'linkedin_username': data['general']['contact']['linkedin']
        }
    }
    print(f'[INFO]: Saving generated content to {ARGS.destination}/{FILE_NAME}...')
    yaml.safe_dump(template, stream=open(os.path.join(ARGS.destination, FILE_NAME), 'w'))
    
    ### Tech
    FILE_NAME = 'tech.yml'
    template = {
        'row1': [],
        'row2': []
    }
    for category in data['skills']:
        for tech in category['list']:
            if category['section'] == 1:
                template['row1'].append({
                    'name': tech['name'],
                    'icon': tech['icon']
                })
            elif category['section'] == 2:
                template['row2'].append({
                    'name': tech['name'],
                    'icon': tech['icon']
                })
    print(f'[INFO]: Saving generated content to {ARGS.destination}/{FILE_NAME}...')
    yaml.safe_dump(template, stream=open(os.path.join(ARGS.destination, FILE_NAME), 'w'))
    
    ### Experience
    FILE_NAME = 'experience.yml'
    template = {
        'experience': []
    }
    for experience in data['experiences']:
        to_add = {
            'company': experience['company'],
            'role': experience['roles'][0],
            'period': f"{experience['start']} - {experience['end']}",
            'logo': f"/images/company/{str(experience['company']).lower().replace(' ', '_').replace(',', '')}.png",
            'description': None, # TODO
            'responsibilities': experience['highlights']
        }
        template['experience'].append(to_add)
    print(f'[INFO]: Saving generated content to {ARGS.destination}/{FILE_NAME}...')
    yaml.safe_dump(template, stream=open(os.path.join(ARGS.destination, FILE_NAME), 'w'))
    
    ### Volunteering
    FILE_NAME = 'voluntary.yml'
    template = {
        'voluntary': []
    }
    for volunteer in data['volunteering']:
        to_add = {
            'organization': volunteer['organization'],
            'role': volunteer['role'],
            'period': volunteer['period'],
            'description': volunteer['description']
        }
        template['voluntary'].append(to_add)
    print(f'[INFO]: Saving generated content to {ARGS.destination}/{FILE_NAME}...')
    yaml.safe_dump(template, stream=open(os.path.join(ARGS.destination, FILE_NAME), 'w'))
    
    ### Projects
    FILE_NAME = 'projects.yml'
    template = {
        'projects': []
    }
    for project in data['projects']:
        to_add = {
            'title': project['name'],
            'description': project['summary'],
            'tech': project['tech'],
            'image': f"/images/projects/{project['name'].lower().replace(' ', '_')}.jpg",
            'link': project['link']
        }
        template['projects'].append(to_add)
    print(f'[INFO]: Saving generated content to {ARGS.destination}/{FILE_NAME}...')
    yaml.safe_dump(template, stream=open(os.path.join(ARGS.destination, FILE_NAME), 'w'))
    
    ### Honors
    FILE_NAME = 'honors.yml'
    template = {
        'honors': []
    }
    for honor in data['awards']:
        to_add = {
            'institution': honor['where'],
            'title': honor['name'],
            'date': honor['when']
        }
        template['honors'].append(to_add)
    print(f'[INFO]: Saving generated content to {ARGS.destination}/{FILE_NAME}...')
    yaml.safe_dump(template, stream=open(os.path.join(ARGS.destination, FILE_NAME), 'w'))
    
    ### Certifications
    FILE_NAME = 'certifications.yml'
    template = {
        'certifications': []
    }
    for certification in data['certifications']:
        to_add = {
            'title': certification['name'],
            'date': certification['when'],
            'url': certification['url']
        }
        template['certifications'].append(to_add)
    print(f'[INFO]: Saving generated content to {ARGS.destination}/{FILE_NAME}...')
    yaml.safe_dump(template, stream=open(os.path.join(ARGS.destination, FILE_NAME), 'w'))

    print('[INFO]: Done!')

if __name__ == '__main__':
    main()
