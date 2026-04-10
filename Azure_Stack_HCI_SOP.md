# Azure Stack HCI - Standard Operating Procedure (SOP) for L2 Team

## 1. Overview of Azure Stack HCI
Azure Stack HCI is a hyperconverged infrastructure solution from Microsoft that enables you to run virtualized workloads on-premises with cloud integration.

### Benefits:
- Unified management control plane.
- Supports a wide range of validated hardware.
- Seamless delivery of cloud and AI workloads to the edge.
- Flexible deployment sizes (1 to 16 nodes).

**Reference:** [Hyperconverged Overview](https://learn.microsoft.com/azure/azure-local/overview/hyperconverged-overview?view=azloc-2603)

---

## 2. Cluster Deployment
Azure Stack HCI clusters can be deployed using Bicep templates.

### Example: 2-node switched configuration
- Deploy Azure VM to host a 2-node switched Azure Stack HCI cluster.
- Validate cluster configuration.
- Deploy cluster WAF aligned if required.

**Reference:** [Cluster Deployment Examples](https://raw.githubusercontent.com/Azure/bicep-registry-modules/refs/heads/main/avm/res/azure-stack-hci/cluster/README.md#usage-examples)

---

## 3. Networking
### Network Interfaces
- Deploy Azure Stack HCI network interfaces.
- Assign roles and configure API versions.

**Reference:** [Network Interface Module](https://raw.githubusercontent.com/Azure/bicep-registry-modules/refs/heads/main/avm/res/azure-stack-hci/network-interface/README.md)

### Logical Networks
- Deploy logical networks for Azure Stack HCI.
- Configure parameters and outputs.

**Reference:** [Logical Network Module](https://raw.githubusercontent.com/Azure/bicep-registry-modules/refs/heads/main/avm/res/azure-stack-hci/logical-network/README.md)

---

## 4. Azure Kubernetes Service (AKS) on Azure Stack HCI
### Capabilities:
- Deploy AKS clusters.
- Connect to Azure Arc for Kubernetes.
- Manage pods and storage.
- Implement containerized Windows workloads.
- Troubleshoot AKS on Azure Stack HCI.

**Reference:** [AKS on Azure Stack HCI Training](https://learn.microsoft.com/training/modules/manage-azure-kubernetes-service-azure-stack-hci/)

---

## 5. VM Management
Use the Azure.ResourceManager.Hci.Vm library for:
- VM lifecycle management.
- Resource allocation.
- Monitoring.
- Integration with Azure services.

**Reference:** [HCI VM Management Client Library](https://learn.microsoft.com/dotnet/api/overview/azure/resourcemanager.hci.vm-readme?view=azure-dotnet-preview)

---

## 6. Operations & Maintenance
- Monitor clusters via Azure Portal, Windows Admin Center, and PowerShell.
- Apply updates and patches regularly.
- Implement backup and disaster recovery strategies.

---

## 7. Troubleshooting
- Review logs and diagnostics.
- Address common issues (network misconfigurations, storage issues, cluster health alerts).
- Escalate unresolved issues to L3 support.

---

**End of SOP**