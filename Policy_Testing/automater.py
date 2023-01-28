import json
import requests
from msgraph.core import GraphClient
import msgraph.core
from azure.identity import ClientSecretCredential

users_url = 'https://graph.microsoft.com/v1.0/users'
ca_url = 'https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies'
test_ca_url = ['https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/testCA.json', 'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/testCA2.json', 'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/testCA3.json']
base_url = 'https://github.com/y0uf0ol/MS_CA_Automater/blob/main/Policy_Testing/Base%20Protection/Links.md' # Base Protection Policies

# Create a ServicePrincipalCredentials object
credentials = ClientSecretCredential(
    client_id='ff20e021-d49f-4532-ab17-47dbf72181e4',
    client_secret='cNX8Q~SuxVeAD.y9gveP6IIlVX8jCY2tsDbTdbKv',
    tenant_id='e0c0089e-139c-46e7-a82f-231cd621849e'
)
# Create a Graph client
graph_client = GraphClient(credential=credentials)


# Collect all Base Protection Policies
print('Collecting Base Protection Policies')



#Create a new policy
print('Creating new policy')
for cap in test_ca_url:
    re = requests.get(cap).json()
    new_policy = graph_client.post(ca_url, json=re)