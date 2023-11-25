from fastapi import FastAPI

#customize metadata configurations and define URLs for API documentation
app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi', redoc_url=None, title='EthiopianBanks', description='**EthiopianBanks** a *RESTful API* to provide a comprehensive list of banks in Ethiopia along with their contact information and other relevant details.', summary='Open-source project that aims at providing an overview of banks in Ethiopia.', version='0.0.1', contact={'name': 'EthiopianBanks', 'url': 'https://github.com/antenehbedilu/ethiopianbanks', 'email': 'hello@antenehbedilu.com'}, license_info={'name': 'MIT License', 'url': 'https://raw.githubusercontent.com/antenehbedilu/ethiopianbanks/main/LICENSE'})
