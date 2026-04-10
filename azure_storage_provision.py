import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, Sku, Kind, Encryption, EncryptionServices, EncryptionService

# Acquire a credential object
credential = DefaultAzureCredential()

# Retrieve subscription ID from environment variable
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

# Define resource group and storage account details
RESOURCE_GROUP_NAME = os.environ.get("AZURE_RESOURCE_GROUP_NAME", "demoResourceGroup")
LOCATION = os.environ.get("AZURE_LOCATION", "eastus")
STORAGE_ACCOUNT_NAME = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME", "demostorageacct123")

# Create Resource Management client
resource_client = ResourceManagementClient(credential, subscription_id)

# Create or update the resource group
print(f"Creating resource group: {RESOURCE_GROUP_NAME}...")
resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME, {"location": LOCATION})

# Create Storage Management client
storage_client = StorageManagementClient(credential, subscription_id)

# Define encryption settings
encryption_services = EncryptionServices(
    blob=EncryptionService(enabled=True),
    file=EncryptionService(enabled=True)
)

# Define storage account parameters
params = StorageAccountCreateParameters(
    sku=Sku(name="Standard_LRS"),
    kind=Kind.STORAGE_V2,
    location=LOCATION,
    encryption=Encryption(services=encryption_services, key_source="Microsoft.Storage")
)

# Create the storage account
print(f"Creating storage account: {STORAGE_ACCOUNT_NAME} with encryption enabled...")
poller = storage_client.storage_accounts.begin_create(
    RESOURCE_GROUP_NAME,
    STORAGE_ACCOUNT_NAME,
    params
)
account_result = poller.result()

print(f"Provisioned storage account {account_result.name} in resource group {RESOURCE_GROUP_NAME} with encryption enabled.")