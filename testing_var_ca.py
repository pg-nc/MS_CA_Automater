import json
import requests
from msgraph.core import GraphClient
import msgraph.core
from azure.identity import ClientSecretCredential
#Variables
client_id = input('Enter your appliction ID: ')
client_secret = input('Enter your client secret: ')
tenant_id = input('Enter your tenant ID: ')
users_url = 'https://graph.microsoft.com/v1.0/users'
ca_url = 'https://graph.microsoft.com/beta/identity/conditionalAccess/policies'
grp_url = 'https://graph.microsoft.com/v1.0/groups'
test_ca_url = ['https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/testing_ca_variables.json',]
base_url = 'https://github.com/y0uf0ol/MS_CA_Automater/blob/main/Policy_Testing/Base%20Protection/Links.md' # Base Protection Policies
group_list = ['SG-CA-ServiceAccounts', 'SG-CA-InternalUsers']

# Create a ServicePrincipalCredentials object
credentials = ClientSecretCredential(
    client_id=client_id,
    client_secret=client_secret,
    tenant_id=tenant_id
)
# Create a Graph client
graph_client = GraphClient(credential=credentials)

""" # Creating base protection groups
def create_group(group_name):
    print('Creating group ' + group_name)
    grp = graph_client.post(grp_url, json={"description": group_name, "displayName": group_name, "groupTypes": [], "mailNickname": group_name, "mailEnabled": False, "securityEnabled": True})
    return grp

for each in group_list:
    create_group(each)
    #get all created groupd IDs
    get_grp = graph_client.get(grp_url).json()
    for g in get_grp['value']:
        if g['displayName'] == each:
            print('Group ' + each + ' created with ID ' + g['id']) """



# Collect all Base Protection Policies
print('Collecting Base Protection Policies')

#Create a new policy
print('Creating new policy')
for cap in test_ca_url:
    re = requests.get(cap).json()
    new_policy = graph_client.post(ca_url, json=re)
