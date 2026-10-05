# Imports
import argparse
import yaml

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, help='Name of YAML file that contains resume contents.')
parser.add_argument('--template', type=str, help='RenderCV template to use to build the generated YAML file.')
parser.add_argument('--destination', type=str, help='Path to save generated YAML file for RenderCV to use.')

# Main
def main():
    ARGS = parser.parse_args()

    ## Load files
    print(f'[INFO]: Loading contents from {ARGS.source} & {ARGS.template}...')
    data = None
    with open(ARGS.source, 'r') as file:
        data = yaml.safe_load(file)
    template = None
    with open(ARGS.template, 'r') as file:
        template = yaml.safe_load(file)

    ## Convert
    print('[INFO]: Generating ResumeCV format config...')
    ### General
    template['cv']['name'] = data['general']['name']
    template['cv']['headline'] = data['general']['title']
    template['cv']['location'] = data['general']['location']
    template['cv']['email'] = data['general']['contact']['email']
    template['cv']['website'] = data['general']['contact']['website']
    template['cv']['social_networks'] = [
        {
            'network': 'LinkedIn',
            'username': data['general']['contact']['linkedin']
        },
        {
            'network': 'GitHub',
            'username': data['general']['contact']['github']
        }
    ]
    ### Sections
    template['cv']['sections'] = {
        'Summary': None,
        'skills': [],
        'experience': [],
        'projects': [],
        'education': []
    }
    #### Summary
    template['cv']['sections']['Summary'] = data['general']['summary']
    #### Skills
    for skill in data['skills']:
        template['cv']['sections']['skills'].append({
            'label': skill['category'],
            'details': ', '.join([x['name'] for x in skill['list']])
        })
    #### Experience
    for experience in data['experiences']:
        template['cv']['sections']['experience'].append({
            'company': experience['company'],
            'position': ', '.join(experience['roles']),
            'date': experience['start'],
            'end_date': experience['end'],
            'location': experience['location'],
            'highlights': experience['highlights']
        })
    #### Projects
    for project in data['projects']:
        template['cv']['sections']['projects'].append({
            'name': project['name'],
            'date': project['date'] if 'date' in project else None,
            'start_date': project['start_date'] if 'start_date' in project else None,
            'end_date': project['end_date'] if 'end_date' in project else None,
            'summary': project['summary']
        })
    #### Education
    for education in data['education']:
        template['cv']['sections']['education'].append({
            'institution': education['name'],
            'area': education['degree'],
            'degree': education['level'],
            'end_date': education['graduated'] if 'graduated' in education else None
        })

    ## Save converted file
    print(f'[INFO]: Saving generated content to {ARGS.destination}...')
    yaml.safe_dump(template, stream=open(ARGS.destination, 'w'))

    print('[INFO]: Done!')

if __name__ == '__main__':
    main()
