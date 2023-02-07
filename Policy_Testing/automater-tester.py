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
    client_id='ff20e021-d49f-4532-ab17-47dbf72181e4',
    client_secret='GbV8Q~42Lw4vqx.2XBg8y8yFT8GYfLw3f7Kfkb43',
    tenant_id='e0c0089e-139c-46e7-a82f-231cd621849e'
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