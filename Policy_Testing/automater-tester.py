import json
import requests
from msgraph.core import GraphClient
from azure.identity import ClientSecretCredential
#Variables
users_url = 'https://graph.microsoft.com/v1.0/users'
ca_url = 'https://graph.microsoft.com/beta/identity/conditionalAccess/policies'
grp_url = 'https://graph.microsoft.com/v1.0/groups'
test_ca_url = ['https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA504_AttackSurfaceReduction_ExternalUsers_AllApps_UnkownDevicePlatform_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA505_AttackSurfaceReduction_ExternalUsers_NotAllowedApps_AllPlatforms_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA506_AttackSurfaceReduction_SeviceAccounts_AllApps_AllPlatforms_UntrustedLocation_BlockAccess.json']
base_url = 'https://github.com/y0uf0ol/MS_CA_Automater/blob/main/Policy_Testing/Base%20Protection/Links.md' # Base Protection Policies

# Create a ServicePrincipalCredentials object
credentials = ClientSecretCredential(
    client_id=,
    client_secret=,
    tenant_id=
)
# Create a Graph client
graph_client = GraphClient(credential=credentials)

# Creating base protection groups

graph_client.post(grp_url, json={"displayName": "SG_ServiceAccounts2", "mailEnabled": False, "mailNickname": "SG_ServiceAccounts2", "securityEnabled": True, "groupTypes": []})


# Collect all Base Protection Policies
print('Collecting Base Protection Policies')

#Create a new policy
#print('Creating new policy')
#for cap in test_ca_url:
 #   re = requests.get(cap).json()
  #  new_policy = graph_client.post(ca_url, json=re)
