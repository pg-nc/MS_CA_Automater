import json
import requests
from msgraph.core import GraphClient
import msgraph.core
from azure.identity import ClientSecretCredential

users_url = 'https://graph.microsoft.com/v1.0/users'
ca_url = 'https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies'
test_ca_url = ['https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/testCA.json, https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/testCA2.json, https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/testCA3.json']

# Create a ServicePrincipalCredentials object
credentials = ClientSecretCredential(
    client_id='ff20e021-d49f-4532-ab17-47dbf72181e4',
    client_secret='cNX8Q~SuxVeAD.y9gveP6IIlVX8jCY2tsDbTdbKv',
    tenant_id='e0c0089e-139c-46e7-a82f-231cd621849e'
)

# Create a Graph client
graph_client = GraphClient(credential=credentials)
#client = GraphClient(user)
# Get the list of users
#users_read = graph_client.get(users_url)
#print(users_read.json())
#Get the list of policies
#policies = graph_client.get(ca_url)
#for policy in policies.json()['value']:
  #  print(policy['displayName'])

#Create a new policy
print(test_ca_url)
for cap in test_ca_url:
    re = requests.get(cap).json()
    print(re)
    #new_policy = graph_client.post(ca_url, json=re)