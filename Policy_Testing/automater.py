import json
import requests
from msgraph.core import GraphClient
import msgraph.core
from azure.identity import ClientSecretCredential
#Variables
users_url = 'https://graph.microsoft.com/v1.0/users'
ca_url = 'https://graph.microsoft.com/beta/identity/conditionalAccess/policies'
grp_url = 'https://graph.microsoft.com/v1.0/groups'
test_ca_url = ['https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA100_BaseProtection_%20AllUsers_RegisterSecurityInfo_AllePlattformen_UntrustedLocation_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA101_BaseProtection_Admins_AlleApps_AllePlattformen_RequireMFA.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA103_BaseProtection_InternalUsers_AllApps_AllPlatforms_MFA.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA107_BaseProtection_ExternalUsers_AllApps_AllPlatforms_RequireMFA.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA200_IdentityProtection_AllUsers_AllApps_LegacyClients_AllPlatforms_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA300_DataProtection_Admins_AllApps_AllPlatform_ShortSign-inFrequency_AND_NeverPersistantBrowserSession.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA301_DataProtection_InternalUsers_AllApps_AllPlatform_ShortSign-inFrequency.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA302_DataProtection_ExternalUsers_AllApps_AllPlatform_ShortSign-inFrequency.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA500_AttackSurfaceReduction_Admins_AllApps_AllPlatforms_UntrustedLocation_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA501_AttackSurfaceReduction_InternalUsers_AllApps_AllPlatforms_UntrustedLocation_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA502_AttackSurfaceReduction_Admins_AllApps_UnknownDevicePlatforms_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA503_AttackSurfaceReduction_InternalUsers_AllApps_UnkownDevicePlatform_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA504_AttackSurfaceReduction_ExternalUsers_AllApps_UnkownDevicePlatform_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA505_AttackSurfaceReduction_ExternalUsers_NotAllowedApps_AllPlatforms_BlockAccess.json',
'https://raw.githubusercontent.com/y0uf0ol/MS_CA_Automater/main/Policy_Testing/Base%20Protection/CA506_AttackSurfaceReduction_SeviceAccounts_AllApps_AllPlatforms_UntrustedLocation_BlockAccess.json']
base_url = 'https://github.com/y0uf0ol/MS_CA_Automater/blob/main/Policy_Testing/Base%20Protection/Links.md' # Base Protection Policies

# Create a ServicePrincipalCredentials object
credentials = ClientSecretCredential(
    client_id='ff20e021-d49f-4532-ab17-47dbf72181e4',
    client_secret='tjU8Q~LidBkNN2MzZIeR6uB2TKWiTnBJhr6zAcq3',
    tenant_id='e0c0089e-139c-46e7-a82f-231cd621849e'
)
# Create a Graph client
graph_client = GraphClient(credential=credentials)

# Creating base protection groups

#graph_client.post(grp_url, json={"description": "Base Protection Group", "displayName": "Base Protection Group", "groupTypes": ["Unified"], "mailEnabled": False, "mailNickname": "BaseProtectionGroup", "securityEnabled": True})

# Collect all Base Protection Policies
print('Collecting Base Protection Policies')

#Create a new policy
print('Creating new policy')
for cap in test_ca_url:
    re = requests.get(cap).json()
    new_policy = graph_client.post(ca_url, json=re)