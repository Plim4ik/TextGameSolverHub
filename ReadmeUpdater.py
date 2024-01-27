import os
import chardet
from tabulate import tabulate
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def count_words(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as f:
        words = [line.strip() for line in f if line.strip()]
    return len(words)

def update_readme(directory):
    data = []

    for file_name in os.listdir(directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory, file_name)
            language_name = file_name.split('.')[0]

            logging.info(f'Processing {language_name}...')
            
            word_count = count_words(file_path)

            data.append({
                'Language Name': language_name,
                'Native Language Name': get_native_name(language_name),
                'Number of Words': word_count,
                'Word File': file_path,
            })

            logging.info(f'Word count for {language_name}: {word_count}')

    # Format data as table
    table = tabulate(data, headers='keys', tablefmt='github')

    # Update README.md
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_path, 'r') as f:
        readme_content = f.read()

    # Replace placeholder in README.md with the generated table
    updated_readme_content = readme_content.replace('<!-- TABLE_PLACEHOLDER -->', table)

    with open(readme_path, 'w') as f:
        f.write(updated_readme_content)

def get_native_name(language_name):
    # Add logic to map language names to their native names
    # This is a simplified example, you may need to expand it for all languages
    language_mapping = {
        'English': 'English',
        'French': 'Français',
        'Italian': 'Italiano',
        'Polish': 'Polski',
        'Portuguese': 'Português',
        'Russian': 'Русский язык',
        'Spanish': 'Español',
        'Swedish': 'Svenska',
        'Turkish': 'Türkçe',
    }
    return language_mapping.get(language_name, language_name)

if __name__ == '__main__':
    update_readme('dict')
    logging.info('Task completed successfully.')
