import json
import requests
from msgraph.core import GraphClient
import msgraph.core
from azure.identity import ClientSecretCredential
import os

#Variables
users_url = 'https://graph.microsoft.com/v1.0/users'
ca_url = 'https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies'
grp_url = 'https://graph.microsoft.com/v1.0/groups'
test_ca_url = ['https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/testCA.json', 'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/testCA2.json', 'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/testCA3.json']
base_url = 'https://github.com/y0uf0ol/MS_CA_Automater/blob/main/Policy_Testing/Base%20Protection/Links.md' # Base Protection Policies

# Create a ServicePrincipalCredentials object
credentials = ClientSecretCredential(
    client_id='2acf62c4-cee1-4c55-b2fd-f10d4f734327',
    client_secret='Dda8Q~kvPNMPfWBBdnAWk6oTZR56Vi2MGVzpva5g',
    tenant_id='1376e5cb-6a36-4804-beba-0078c7b1329d'
)
# Create a Graph client
graph_client = GraphClient(credential=credentials)

# Creating base protection groups

# Collect all Base Protection Policies
print('Collecting Base Protection Policies')

#Get all policies
policies = graph_client.get(ca_url).json()

for policy in policies['value']:
    name=(policy['displayName'])
    json_object = json.dumps(policy)
    print(name)
    f=open(name+".json",'w+')
    f.write(json_object)


