import csv

from django.core.management.base import BaseCommand

from core.models import FeiraLivre


class Command(BaseCommand):
    help = "Extrai dados de um arquivo CSV e adiciona no bando de dados"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        self.file_path = options['file_path'][0]
        self.csv_to_models()

    def csv_to_models(self):
        f = open(self.file_path, 'rt')
        try:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                feira_dict = {}
                for index, col_value in enumerate(row):
                    col_name = header[index].lower()
                    if col_name == 'lat':
                        col_name = 'latitude'
                    elif col_name == 'long':
                        col_name = 'longitude'
                    feira_dict[col_name] = col_value
                feira_dict.pop('id')
                try:
                    feira = FeiraLivre.objects.create(**feira_dict)
                    print("Feira '{}' cadastrada.".format(feira.nome_feira))
                except Exception as err:
                    print(err)
                    print("Erro ao cadastrar feira '{}'".format(
                        feira_dict['nome_feira']))
                    input('Pressione ENTER tecla para continuar...')
        finally:
            f.close()
