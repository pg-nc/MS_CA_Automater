import json
import requests
from msgraph.core import GraphClient
import msgraph.core
from azure.identity import ClientSecretCredential
#Variables
users_url = 'https://graph.microsoft.com/v1.0/users'
ca_url = 'https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies'
grp_url = 'https://graph.microsoft.com/v1.0/groups'
test_ca_url = ['https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA506_AttackSurfaceReduction_SeviceAccounts_AllApps_AllPlatforms_UntrustedLocation_BlockAccess.json','https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA502_AttackSurfaceReduction_Admins_AllApps_UnknownDevicePlatforms_BlockAccess.json']
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

graph_client.post(grp_url, json={"description": "Base Protection Group", "displayName": "Base Protection Group", "groupTypes": ["Unified"], "mailEnabled": False, "mailNickname": "BaseProtectionGroup", "securityEnabled": True})

# Collect all Base Protection Policies
print('Collecting Base Protection Policies')

#Create a new policy
print('Creating new policy')
for cap in test_ca_url:
    re = requests.get(cap).json()
    new_policy = graph_client.post(ca_url, json=re)