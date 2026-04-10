# Azure Resource Provisioning using ARM Templates

## Step-by-Step Procedure

### 1️⃣ Understand ARM Templates
- **ARM (Azure Resource Manager)** is Azure’s deployment and management service.
- ARM templates are **JSON files** that define the infrastructure and configuration for your Azure solution.
- They are **idempotent** — running the same template multiple times won’t create duplicate resources.

**Basic ARM Template Schema:**
```json
{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "",
  "apiProfile": "",
  "parameters": { },
  "variables": { },
  "functions": [ ],
  "resources": [ ],
  "outputs": { }
}
```

---

### 2️⃣ Create the Template
- Define the **resources** you want to deploy in the `resources` array.
- Example: Storage Account definition
```json
"resources": [
  {
    "type": "Microsoft.Storage/storageAccounts",
    "name": "[variables('storageAccountName')]",
    "location": "[parameters('location')]",
    "apiVersion": "2018-07-01",
    "sku": {
      "name": "[parameters('storageAccountType')]"
    },
    "kind": "StorageV2",
    "properties": {}
  }
]
```

---

### 3️⃣ Parameterize the Template
- Use **parameters** for values that change between environments (e.g., location, SKU).
- Example:
```json
"parameters": {
  "location": {
    "type": "string",
    "defaultValue": "eastus"
  },
  "storageAccountType": {
    "type": "string",
    "defaultValue": "Standard_LRS"
  }
}
```

---

### 4️⃣ Prepare a Parameters File
- Store environment-specific values in a separate `.parameters.json` file.
- Example:
```json
{
  "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "location": { "value": "eastus" },
    "storageAccountType": { "value": "Standard_LRS" }
  }
}
```

---

### 5️⃣ Deploy the Template
You can deploy using:

**Azure Portal**
1. Go to **Home** → **+ Create a resource**.
2. Search for **Template deployment (deploy using custom templates)**.
3. Paste your JSON template or upload it.
4. Provide parameter values and deploy.

**Azure CLI**
```bash
az deployment group create \
  --resource-group MyResourceGroup \
  --template-file azuredeploy.json \
  --parameters azuredeploy.parameters.json
```

**Azure PowerShell**
```powershell
New-AzResourceGroupDeployment `
  -ResourceGroupName MyResourceGroup `
  -TemplateFile azuredeploy.json `
  -TemplateParameterFile azuredeploy.parameters.json
```

---

### 6️⃣ Validate and Monitor
- Use `what-if` deployment mode to preview changes:
```bash
az deployment group what-if \
  --resource-group MyResourceGroup \
  --template-file azuredeploy.json
```
- Monitor deployment in the **Azure Portal** under the resource group’s **Deployments** tab.

---

### 7️⃣ Manage and Update
- Update the template and redeploy to modify resources.
- Delete the resource group to remove all resources in one go.

---

📖 **Reference:**
- [Infrastructure as Code with ARM Templates](https://learn.microsoft.com/dotnet/architecture/cloud-native/infrastructure-as-code#azure-resource-manager-templates)
- [Deploy ARM Templates](https://learn.microsoft.com/azure/azure-resource-manager/templates/overview)